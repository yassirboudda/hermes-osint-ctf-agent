#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["streetlevel", "numpy", "pillow"]
# ///
"""Benchmarks: measure whether a change to the skill actually helps.

  bench.py make-streetview --n 40 --out bench/sv40 [--seed 1] [--countries PT,ES,…]
        GeoGuessr-style test set: random towns (one random covered country per round), the nearest official
        Street View panorama, a random heading → images/0001.jpg … and truth.json (kept apart from the images).
  bench.py score preds.json --truth bench/sv40/truth.json
        preds: {"0001": {"lat": …, "lon": …, "country": "PT"}, …} (or a CSV id,lat,lon[,country]).
  bench.py prior bench/sv40 --out preds_prior.json
        run prior.py on every image and keep the best GeoCLIP cluster as the guess (a model-only baseline).
  bench.py sessions [--root photos/]
        same metrics over finished archive sessions that have a recorded truth (photo_session.py truth).

Metrics: median and mean error (km), share within 1 / 25 / 200 / 750 / 2500 km, country accuracy, and the
approximate world-map game score 5000·exp(−d/1492.7 km). Use the same seed to compare versions fairly.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import random
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _streetlevel as SL  # noqa: E402
import geodata  # noqa: E402

HERE = Path(__file__).resolve().parent
THRESHOLDS = (1, 25, 200, 750, 2500)
# Countries with broad official Street View coverage; rounds are drawn uniformly from this list unless --countries
DEFAULT_POOL = ("US,CA,MX,GT,CR,PA,CO,EC,PE,BO,CL,AR,UY,BR,PR,DO,GB,IE,FR,ES,PT,IT,DE,AT,CH,NL,BE,LU,DK,NO,SE,FI,"
                "IS,EE,LV,LT,PL,CZ,SK,HU,SI,HR,RS,ME,AL,MK,BG,RO,GR,TR,UA,RU,IL,JO,AE,QA,JP,KR,TW,HK,TH,KH,LA,MY,SG,"
                "ID,PH,IN,BD,LK,MN,KZ,KG,AU,NZ,ZA,BW,LS,SZ,NA,KE,UG,RW,GH,NG,SN,TN").split(",")


def score_km(d: float) -> int:
    return int(round(5000 * math.exp(-d / 1492.7)))


def metrics(pairs: list[dict]) -> dict:
    errs = sorted(p["error_km"] for p in pairs)
    n = len(errs)
    if not n:
        return {"n": 0}
    med = errs[n // 2] if n % 2 else (errs[n // 2 - 1] + errs[n // 2]) / 2
    cc = [p for p in pairs if p.get("country_true") and p.get("country_pred")]
    return {"n": n, "median_km": round(med, 1), "mean_km": round(sum(errs) / n, 1),
            "within": {f"{k}km": round(sum(e <= k for e in errs) / n, 3) for k in THRESHOLDS},
            "country_accuracy": round(sum(p["country_true"] == p["country_pred"] for p in cc) / len(cc), 3) if cc else None,
            "mean_game_score": round(sum(score_km(e) for e in errs) / n)}


def load_preds(path: Path) -> dict:
    if path.suffix.lower() == ".csv":
        out = {}
        with path.open(encoding="utf-8") as f:
            for row in csv.DictReader(f):
                out[row["id"]] = {"lat": float(row["lat"]), "lon": float(row["lon"]), "country": row.get("country") or None}
        return out
    return json.loads(path.read_text(encoding="utf-8"))


def cmd_make(args) -> None:
    out = Path(args.out)
    (out / "images").mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    pool = [c.strip().upper() for c in (args.countries.split(",") if args.countries else DEFAULT_POOL)]
    truth, made, tries = {}, 0, 0
    cache = Path(args.cache)
    while made < args.n and tries < args.n * 8:
        tries += 1
        cc = rng.choice(pool)
        towns = geodata.sample(cc, 1, seed=rng.randrange(1 << 30), alpha=0.35, min_pop=0)
        if not towns:
            continue
        t = towns[0]
        # wander off the town centre a little so rounds are not always on the main square
        lat = t["lat"] + rng.uniform(-0.03, 0.03)
        lon = t["lon"] + rng.uniform(-0.03, 0.03) / max(math.cos(math.radians(t["lat"])), 0.2)
        hits = SL.find_near(lat, lon, args.radius, max_ring=3)
        if not hits:
            continue
        m = SL.metadata(hits[0]["id"])
        if not m:
            continue
        heading = rng.uniform(0, 360)
        try:
            eq, ph = SL.equirect(m["id"], cache, 3)
        except Exception:  # noqa: BLE001
            continue
        made += 1
        rid = f"{made:04d}"
        SL.perspective(eq, ph, heading, 0, args.fov, 1280, 800).save(out / "images" / f"{rid}.jpg", quality=90)
        truth[rid] = {"lat": round(m["wgs"][0], 6), "lon": round(m["wgs"][1], 6), "country": m.get("country_code") or cc,
                      "pano": m["id"], "date": m["date"], "heading": round(heading, 1), "town": t["name"], "admin1": t["admin1"]}
        print(f"{rid} {truth[rid]['country']} {t['name']}, {t['admin1']} ({m['date']})", flush=True)
    (out / "truth.json").write_text(json.dumps(truth, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "README.md").write_text(
        f"# Street View benchmark ({made} rounds, seed {args.seed})\n\nImages are in images/. truth.json holds the answers: "
        "do not show it to the solver. Score predictions with `bench.py score preds.json --truth truth.json`.\n", encoding="utf-8")
    print(f"-> {out} ({made} images; truth in truth.json — keep it away from the solver)")


def cmd_score(args) -> None:
    truth = json.loads(Path(args.truth).read_text(encoding="utf-8"))
    preds = load_preds(Path(args.preds))
    pairs = []
    for rid, t in truth.items():
        p = preds.get(rid)
        if not p:
            continue
        d = float(geodata.haversine_km(t["lat"], t["lon"], p["lat"], p["lon"]))
        pairs.append({"id": rid, "error_km": round(d, 2), "country_true": t.get("country"),
                      "country_pred": (p.get("country") or geodata.reverse_country(p["lat"], p["lon"])) or None})
    m = metrics(pairs)
    m["missing"] = sorted(set(truth) - set(preds))
    print(json.dumps(m, indent=1))
    if args.out:
        Path(args.out).write_text(json.dumps({"metrics": m, "rounds": pairs}, indent=1), encoding="utf-8")


def consistent_guess(d: dict) -> dict | None:
    """Best guess from a prior.json that is internally consistent: the top combined country, and inside it the
    heaviest GeoCLIP cluster (else its most probable gallery point, else the country's centre)."""
    comb = d.get("combined") or []
    gc = d.get("geoclip") or {}
    if not comb:
        cl = gc.get("clusters") or []
        return {"lat": cl[0]["lat"], "lon": cl[0]["lon"], "country": (cl[0].get("near") or {}).get("country")} if cl else None
    cc = comb[0]["iso2"]
    for c in gc.get("clusters") or []:
        if (c.get("near") or {}).get("country") == cc:
            return {"lat": c["lat"], "lon": c["lon"], "country": cc}
    for la, lo, _p in gc.get("points") or []:
        if geodata.reverse_country(la, lo) == cc:
            return {"lat": la, "lon": lo, "country": cc}
    c = geodata.countries().get(cc, {})
    return {"lat": c["center"][0], "lon": c["center"][1], "country": cc} if c.get("center") else None


def cmd_prior(args) -> None:
    root = Path(args.bench)
    imgs = sorted((root / "images").glob("*.jpg"))
    preds, preds_gc = {}, {}
    for im in imgs:
        od = root / "prior_runs" / im.stem
        if not (args.reuse and (od / "prior.json").exists()):
            r = subprocess.run(["uv", "run", "-q", str(HERE / "prior.py"), str(im), "--out-dir", str(od)], capture_output=True, text=True)
            if r.returncode:
                print(f"{im.stem}: prior failed {r.stderr[-200:]}")
                continue
        d = json.loads((od / "prior.json").read_text(encoding="utf-8"))
        g = consistent_guess(d)
        if g:
            preds[im.stem] = g
        cl = (d.get("geoclip") or {}).get("clusters") or []
        if cl:
            preds_gc[im.stem] = {"lat": cl[0]["lat"], "lon": cl[0]["lon"], "country": (cl[0].get("near") or {}).get("country")}
        print(f"{im.stem}: {preds.get(im.stem)}", flush=True)
    Path(args.out).write_text(json.dumps(preds, indent=1), encoding="utf-8")
    gc_out = Path(args.out).with_name(Path(args.out).stem + "_geoclip_only.json")
    gc_out.write_text(json.dumps(preds_gc, indent=1), encoding="utf-8")
    print(f"-> {args.out} (top combined country + its best GeoCLIP cluster) and {gc_out} (GeoCLIP top cluster only); "
          f"score with: bench.py score {args.out} --truth {root / 'truth.json'}")


def cmd_sessions(args) -> None:
    if args.root is None:
        from photo_session import DEFAULT_ROOT
        args.root = DEFAULT_ROOT
    root = Path(args.root)
    pairs = []
    for f in sorted(root.glob("*/session.json")):
        m = json.loads(f.read_text(encoding="utf-8"))
        t, r = m.get("truth"), m.get("result")
        if t and r:
            pairs.append({"id": f.parent.name, "error_km": t["error_km"], "country_true": t.get("country"), "country_pred": r.get("country")})
    print(json.dumps(metrics(pairs), indent=1))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    mk = sub.add_parser("make-streetview")
    mk.add_argument("--n", type=int, default=40)
    mk.add_argument("--out", required=True)
    mk.add_argument("--seed", type=int, default=1)
    mk.add_argument("--countries", help="comma list of ISO2 codes (default: a pool of covered countries)")
    mk.add_argument("--radius", type=float, default=900)
    mk.add_argument("--fov", type=float, default=90)
    mk.add_argument("--cache", default=str(Path.home() / ".cache" / "geoint" / "bench-panos"))
    sc = sub.add_parser("score")
    sc.add_argument("preds")
    sc.add_argument("--truth", required=True)
    sc.add_argument("--out")
    pr = sub.add_parser("prior")
    pr.add_argument("bench")
    pr.add_argument("--out", default="preds_prior.json")
    pr.add_argument("--reuse", action="store_true", help="reuse prior_runs/*/prior.json instead of rerunning the models")
    se = sub.add_parser("sessions")
    se.add_argument("--root", default=None, help="archive root (default: the same as photo_session.py)")
    args = ap.parse_args()
    {"make-streetview": cmd_make, "score": cmd_score, "prior": cmd_prior, "sessions": cmd_sessions}[args.cmd](args)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    main()
