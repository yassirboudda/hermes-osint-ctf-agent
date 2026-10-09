#!/usr/bin/env python3
"""Create, finalize and score one timestamped GeoInt archive per photograph.

  start     new archive for one photo (copies the untouched original, records its checksum)
  finish    append the chosen country/region/city to the folder name, record the result
  truth     record the real location later (from the photo's owner, a puzzle answer, a game reveal)
            and score the session: error in km, approximate world-map game score, country/region hit
  scoreboard  accuracy over every scored session: median error, hit rates at 1/25/200/750/2500 km,
            and whether "high/medium/low" confidence actually meant what it claimed
  list      sessions with their status, so an interrupted one can be resumed
"""

from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import sys
import unicodedata
from zoneinfo import ZoneInfo

SKILL_DIR = Path(__file__).resolve().parent.parent


def _local_config() -> dict:
    """Optional machine settings in <skill>/config.local.json (git-ignored): {"photos_root": …, "timezone": …}."""
    try:
        return json.loads((SKILL_DIR / "config.local.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


_CONFIG = _local_config()
# Archive root: --root, else GEOINT_PHOTOS, else config.local.json "photos_root", else ~/geoint-photos
DEFAULT_ROOT = Path(os.environ.get("GEOINT_PHOTOS") or _CONFIG.get("photos_root") or Path.home() / "geoint-photos").expanduser()
# Time zone of the archive timestamps: GEOINT_TZ, else config.local.json "timezone", else this computer's own
TIMEZONE = os.environ.get("GEOINT_TZ") or _CONFIG.get("timezone")
FOOTER = "<!-- geogussr-archive -->"
TRUTH_START = "<!-- geogussr-truth -->"
TRUTH_END = "<!-- /geogussr-truth -->"
THRESHOLDS_KM = (1, 25, 200, 750, 2500)
SCORE_SCALE_KM = 1492.7  # approximate world-map scoring: 5000 · exp(-d / 1492.7 km)


def now() -> datetime:
    return datetime.now(ZoneInfo(TIMEZONE)) if TIMEZONE else datetime.now().astimezone()


def slug(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value.strip().lower())
    normalized = "".join(c for c in normalized if not unicodedata.combining(c))
    cleaned = re.sub(r"[^\w]+", "-", normalized, flags=re.UNICODE).replace("_", "-").strip("-")
    # Limit bytes, since filesystem component limits also apply to Unicode names.
    return cleaned.encode("utf-8")[:64].decode("utf-8", errors="ignore").rstrip("-") or "unnamed"


def save_json(path: Path, data: dict) -> None:
    pending = path.with_suffix(".json.tmp")
    pending.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pending.replace(path)


def describe(folder: Path, metadata: dict) -> dict:
    return {
        "folder": str(folder),
        "started_at": metadata["started_at"],
        "completed_at": metadata.get("completed_at"),
        "timezone": TIMEZONE,
        "report": str(folder / "report.md"),
        "original": str(folder / metadata["original"]["relative_path"]) if metadata.get("original") else None,
        "status": metadata["status"],
    }


def start(args: argparse.Namespace) -> dict:
    image = args.image.expanduser().resolve(strict=True) if args.image else None
    if image and not image.is_file():
        raise ValueError("The image must be a regular file.")
    root = args.root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    while True:
        started = now()
        timestamp = started.strftime("%Y-%m-%d_%H-%M-%S-%f%z")
        folder = root / timestamp
        try:
            folder.mkdir()
            break
        except FileExistsError:
            continue
    original_dir = folder / "original"
    original_dir.mkdir()
    metadata = {
        "schema_version": 1,
        "timestamp": timestamp,
        "started_at": started.isoformat(timespec="microseconds"),
        "timezone": TIMEZONE,
        "status": "pending",
        "folder": str(folder),
        "original": None,
    }
    if image:
        target = original_dir / image.name
        shutil.copy2(image, target)
        checksum = hashlib.sha256()
        with target.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                checksum.update(chunk)
        digest = checksum.hexdigest()
        metadata["original"] = {
            "source_path": str(image),
            "relative_path": str(target.relative_to(folder)),
            "sha256": digest,
        }
    else:
        (original_dir / "source.txt").write_text(
            "The original image bytes have not been saved. Record the attachment's source here; "
            "save the actual original when accessible.\n", encoding="utf-8"
        )
    save_json(folder / "session.json", metadata)
    name = metadata["original"]["relative_path"] if metadata.get("original") else "original (not saved)"
    (folder / "report.md").write_text(REPORT_SKELETON.format(name=name), encoding="utf-8")
    return describe(folder, metadata)


REPORT_SKELETON = """# Geolocation report: {name}

## Gut call (before tools)
<!-- fill: ranked shortlist with percentages and the cues behind each; region hunch; what would change your mind -->

## Evidence
<!-- fill: decisive clues with the files that show them, commands actually run, sources with links -->

## Answer
<!-- fill: country / region / city, coordinates (WGS84; GCJ-02 too in mainland China), confidence per level, radius and what it rests on -->

## Alternatives and how to separate them
<!-- fill if any -->

## Excluded candidates and unresolved clues
<!-- fill if any -->
"""
REQUIRED_SECTIONS = ("## Gut call (before tools)\n<!-- fill:", "## Answer\n<!-- fill:")


def finish(args: argparse.Namespace) -> dict:
    if not math.isfinite(args.latitude) or not -90 <= args.latitude <= 90:
        raise ValueError("Latitude must be a finite number from -90 to 90.")
    if not math.isfinite(args.longitude) or not -180 <= args.longitude <= 180:
        raise ValueError("Longitude must be a finite number from -180 to 180.")
    if not args.country.strip() or not args.city.strip():
        raise ValueError("Country and city/nearest locality must be nonempty.")
    folder = args.folder.expanduser().resolve(strict=True)
    metadata = json.loads((folder / "session.json").read_text(encoding="utf-8"))
    report = (folder / "report.md").read_text(encoding="utf-8")
    if not report.strip():
        raise ValueError("Save a nonempty report.md before finalizing the session.")
    unfilled = [s.split("\n")[0].lstrip("# ") for s in REQUIRED_SECTIONS if s in report]
    if unfilled:
        raise ValueError(f"Fill these report.md sections before finalizing: {', '.join(unfilled)}.")
    # The timestamp is a single safe path component, never a caller-provided path.
    timestamp = metadata["timestamp"]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}-\d{6}[+-]\d{4}", timestamp):
        raise ValueError("Invalid timestamp in session.json.")
    country, region, city = args.country.strip(), args.region.strip(), args.city.strip()
    names = [slug(value) for value in (country, region, city) if value]
    destination = folder.parent / (timestamp + "__" + "__".join(names))
    if destination != folder and destination.exists():
        raise ValueError("The final archive already exists; no existing session was changed.")
    if destination != folder:
        folder.rename(destination)
    metadata.update({
        "status": "completed",
        "completed_at": now().isoformat(timespec="microseconds"),
        "folder": str(destination),
        "result": {
            "country": country,
            "region": region or None,
            "city_or_nearest_locality": city,
            "latitude": args.latitude,
            "longitude": args.longitude,
            "coordinate_system": "WGS84",
            "confidence": args.confidence,
        },
    })
    body = report.split(FOOTER, 1)[0].rstrip().replace(str(folder), str(destination))
    footer = (
        f"\n\n{FOOTER}\n\n"
        f"Analysis started: {metadata['started_at']} ({TIMEZONE})  \n"
        f"Analysis completed: {metadata['completed_at']}  \n"
        f"Archive: [{destination.name}](<{destination}>)\n"
    )
    (destination / "report.md").write_text(body + footer, encoding="utf-8")
    save_json(destination / "session.json", metadata)
    return describe(destination, metadata)


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    p1, p2 = math.radians(lat1), math.radians(lat2)
    a = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(lon2 - lon1) / 2) ** 2
    return 2 * 6371.0088 * math.asin(min(1.0, math.sqrt(a)))


def _same(a: str | None, b: str | None) -> bool | None:
    if not a or not b:
        return None
    return slug(a) == slug(b)


def _check_coords(lat: float, lon: float) -> None:
    if not math.isfinite(lat) or not -90 <= lat <= 90:
        raise ValueError("Latitude must be a finite number from -90 to 90.")
    if not math.isfinite(lon) or not -180 <= lon <= 180:
        raise ValueError("Longitude must be a finite number from -180 to 180.")


def truth(args: argparse.Namespace) -> dict:
    _check_coords(args.latitude, args.longitude)
    folder = args.folder.expanduser().resolve(strict=True)
    metadata = json.loads((folder / "session.json").read_text(encoding="utf-8"))
    result = metadata.get("result")
    if not result:
        raise ValueError("Finish the session first (photo_session.py finish), then record the truth.")
    distance = haversine_km(result["latitude"], result["longitude"], args.latitude, args.longitude)
    record = {
        "latitude": args.latitude, "longitude": args.longitude,
        "country": args.country or None, "region": args.region or None, "city": args.city or None,
        "source": args.source or None, "recorded_at": now().isoformat(timespec="microseconds"),
        "error_km": round(distance, 3),
        "game_score_estimate": int(round(5000 * math.exp(-distance / SCORE_SCALE_KM))),
        "country_hit": _same(result.get("country"), args.country),
        "region_hit": _same(result.get("region"), args.region),
    }
    metadata["truth"] = record
    save_json(folder / "session.json", metadata)
    report_path = folder / "report.md"
    report = report_path.read_text(encoding="utf-8") if report_path.exists() else ""
    if TRUTH_START in report:
        before, rest = report.split(TRUTH_START, 1)
        report = before.rstrip() + rest.split(TRUTH_END, 1)[-1]
    hit = lambda v: "unknown" if v is None else ("yes" if v else "no")  # noqa: E731
    block = (
        f"\n\n{TRUTH_START}\n\n## Ground truth\n\n"
        f"Actual location: {args.latitude:.6f}, {args.longitude:.6f}"
        + (f" ({', '.join(x for x in (args.city, args.region, args.country) if x)})" if (args.city or args.region or args.country) else "")
        + (f"; source: {args.source}" if args.source else "") + "  \n"
        f"Error: {distance:.2f} km; approximate world-map game score {record['game_score_estimate']}; "
        f"country hit: {hit(record['country_hit'])}; region hit: {hit(record['region_hit'])}; "
        f"stated confidence: {result.get('confidence')}.\n\n{TRUTH_END}\n"
    )
    if FOOTER in report:
        body, footer = report.split(FOOTER, 1)
        report = body.rstrip() + block + "\n" + FOOTER + footer
    else:
        report = report.rstrip() + block
    report_path.write_text(report, encoding="utf-8")
    return {**describe(folder, metadata), "truth": record}


def _sessions(root: Path) -> list[tuple[Path, dict]]:
    out = []
    if not root.exists():
        return out
    for d in sorted(root.iterdir()):
        f = d / "session.json"
        if d.is_dir() and f.exists():
            try:
                out.append((d, json.loads(f.read_text(encoding="utf-8"))))
            except (OSError, json.JSONDecodeError):
                continue
    return out


def _pct(v: float | None) -> str:
    return "–" if v is None else f"{v:.0%}"


def _median(values: list[float]) -> float | None:
    if not values:
        return None
    v = sorted(values)
    n = len(v)
    return v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2


def scoreboard(args: argparse.Namespace) -> dict:
    root = args.root.expanduser().resolve()
    rows = []
    for folder, m in _sessions(root):
        t, r = m.get("truth"), m.get("result")
        if t and r:
            rows.append({"folder": folder.name, "started_at": m.get("started_at"), "chosen": r.get("city_or_nearest_locality"),
                         "country": r.get("country"), "confidence": r.get("confidence"), "error_km": t["error_km"],
                         "score": t.get("game_score_estimate"), "country_hit": t.get("country_hit")})
    errors = [x["error_km"] for x in rows]
    summary = {"root": str(root), "scored_sessions": len(rows),
               "median_error_km": _median(errors),
               "mean_game_score": round(sum(x["score"] or 0 for x in rows) / len(rows)) if rows else None,
               "within_km": {str(k): round(sum(e <= k for e in errors) / len(errors), 3) if errors else None for k in THRESHOLDS_KM},
               "country_hit_rate": (round(sum(1 for x in rows if x["country_hit"]) / len([x for x in rows if x["country_hit"] is not None]), 3)
                                    if any(x["country_hit"] is not None for x in rows) else None)}
    calib = {}
    for tier in ("high", "medium", "low"):
        e = [x["error_km"] for x in rows if x["confidence"] == tier]
        calib[tier] = {"n": len(e), "median_error_km": _median(e),
                       "within_25km": round(sum(v <= 25 for v in e) / len(e), 3) if e else None,
                       "within_200km": round(sum(v <= 200 for v in e) / len(e), 3) if e else None}
    summary["by_confidence"] = calib
    summary["sessions"] = rows
    if args.write:
        lines = ["# GeoInt scoreboard", "", f"Scored sessions: {len(rows)}. Median error: "
                 f"{summary['median_error_km'] if summary['median_error_km'] is not None else '–'} km. "
                 f"Mean approximate game score: {summary['mean_game_score'] if summary['mean_game_score'] is not None else '–'}.", "",
                 "| Within | " + " | ".join(f"{k} km" for k in THRESHOLDS_KM) + " |", "|---|" + "---|" * len(THRESHOLDS_KM),
                 "| share | " + " | ".join(_pct(summary["within_km"][str(k)]) for k in THRESHOLDS_KM) + " |",
                 "", "## Calibration", "", "| Stated confidence | n | median error km | within 25 km | within 200 km |", "|---|---|---|---|---|"]
        for tier, c in calib.items():
            med = "–" if c["median_error_km"] is None else f"{c['median_error_km']:.1f}"
            lines.append(f"| {tier} | {c['n']} | {med} | {_pct(c['within_25km'])} | {_pct(c['within_200km'])} |")
        lines += ["", "## Sessions", "", "| Session | Chosen | Confidence | Error km | Score |", "|---|---|---|---|---|"]
        for x in sorted(rows, key=lambda x: x["started_at"] or ""):
            lines.append(f"| {x['folder']} | {x['chosen']}, {x['country']} | {x['confidence']} | {x['error_km']:.1f} | {x['score']} |")
        (root / "scoreboard.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        save_json(root / "scoreboard.json", summary)
        summary["written"] = str(root / "scoreboard.md")
    return summary


def list_sessions(args: argparse.Namespace) -> dict:
    root = args.root.expanduser().resolve()
    rows = []
    for folder, m in _sessions(root):
        if args.status and m.get("status") != args.status:
            continue
        r, t = m.get("result") or {}, m.get("truth") or {}
        rows.append({"folder": str(folder), "status": m.get("status"), "started_at": m.get("started_at"),
                     "result": f"{r.get('city_or_nearest_locality')}, {r.get('country')} ({r.get('confidence')})" if r else None,
                     "error_km": t.get("error_km")})
    return {"root": str(root), "count": len(rows), "sessions": rows}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest="command", required=True)
    create = subparsers.add_parser("start", help="Create a new archive and copy the original image.")
    create.add_argument("--image", type=Path, help="Optional source image to copy unchanged.")
    create.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Archive root (default: GEOINT_PHOTOS, config.local.json, or ~/geoint-photos).")
    create.set_defaults(handler=start)
    complete = subparsers.add_parser("finish", help="Append the location to a session with a saved report.")
    complete.add_argument("folder", type=Path)
    complete.add_argument("--country", required=True)
    complete.add_argument("--region", default="")
    complete.add_argument("--city", required=True, help="City or nearest named locality.")
    complete.add_argument("--latitude", required=True, type=float)
    complete.add_argument("--longitude", required=True, type=float)
    complete.add_argument("--confidence", required=True, choices=("high", "medium", "low"))
    complete.set_defaults(handler=finish)
    scored = subparsers.add_parser("truth", help="Record the real location of a finished session and score it.")
    scored.add_argument("folder", type=Path)
    scored.add_argument("--latitude", required=True, type=float)
    scored.add_argument("--longitude", required=True, type=float)
    scored.add_argument("--country", default="")
    scored.add_argument("--region", default="")
    scored.add_argument("--city", default="")
    scored.add_argument("--source", default="", help="Where the truth comes from (owner, puzzle answer, game reveal…).")
    scored.set_defaults(handler=truth)
    board = subparsers.add_parser("scoreboard", help="Accuracy and calibration over all scored sessions.")
    board.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    board.add_argument("--write", action="store_true", help="Also write scoreboard.md and scoreboard.json in the root.")
    board.set_defaults(handler=scoreboard)
    listing = subparsers.add_parser("list", help="List sessions (resume pending ones).")
    listing.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    listing.add_argument("--status", choices=("pending", "completed"))
    listing.set_defaults(handler=list_sessions)
    args = parser.parse_args()
    try:
        output = args.handler(args)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
