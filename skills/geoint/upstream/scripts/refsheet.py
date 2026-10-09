#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["streetlevel", "numpy", "pillow"]
# ///
"""Reference sheets: what do roads actually look like in each candidate country or region?

Samples real towns (GeoNames, weighted by population), finds the nearest official Google Street View panorama
in each, and renders one row of views per candidate, side by side. Use it to settle "A or B?" questions about
bollards, utility poles, road paint, curbs, guardrails, signs, plates, vegetation, soil and architecture by
comparing against current imagery instead of memory.

  refsheet.py countries PT,ES,IT --n 6 --out ref.jpg
  refsheet.py regions "ES:Andalusia,ES:Galicia,PT:Faro" --n 6 --out ref_regions.jpg
  refsheet.py countries KE,UG,TZ --n 8 --side right --rural --out ref.jpg    # look at the roadside, small towns only
  refsheet.py countries US --n 6 --pitch -10 --fov 70                      # tilt down for road paint and curbs

Each cell is labelled with the town, region, capture date and heading; ref.index.json keeps the panorama ids
and coordinates. Rows with empty cells mean no coverage near the sampled towns (itself a clue for game-style
images). Mainland China has no Google coverage: use `baidu_pano.py sample`. This sends only coordinates to
Google, never your photo.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _streetlevel as SL  # noqa: E402
import geodata  # noqa: E402
from _net import PROXY_HELP, model_proxy_env  # noqa: E402
from gsv import _font  # noqa: E402

SIDE_OFFSET = {"ahead": 0.0, "right": 90.0, "behind": 180.0, "left": 270.0}


def candidates(spec: str, mode: str) -> list[dict]:
    """countries: 'PT,ES' → [{label, cc, admin1}]; regions: 'ES:Andalusia,PT:Faro'."""
    out = []
    for part in [x.strip() for x in spec.split(",") if x.strip()]:
        if mode == "regions":
            if ":" not in part:
                sys.exit(f"Region must be CC:Region, got '{part}'")
            cc, reg = part.split(":", 1)
            c = geodata.country(cc)
            if not c:
                sys.exit(f"Unknown country {cc}")
            if not geodata.admin1_codes(c["iso2"], reg):
                sys.exit(f"No region matching '{reg}' in {c['name']}. First-level regions: "
                         + ", ".join(geodata.admin1_names(c["iso2"])))
            out.append({"label": f"{reg} ({c['iso2']})", "cc": c["iso2"], "admin1": reg})
        else:
            c = geodata.country(part)
            if not c:
                sys.exit(f"Unknown country {part}")
            out.append({"label": c["name"], "cc": c["iso2"], "admin1": None})
    return out


def one_cell(cand: dict, town: dict, args) -> dict | None:
    hits = SL.find_near(town["lat"], town["lon"], args.radius, max_ring=args.max_ring)
    for h in hits[:2]:
        m = SL.metadata(h["id"])
        if not m:
            continue
        if args.max_age and m["date"] and int(m["date"][:4]) < args.max_age:
            continue
        heading = (m["pano_heading"] + SIDE_OFFSET[args.side] + random.uniform(-args.jitter, args.jitter)) % 360
        try:
            eq, ph = SL.equirect(m["id"], args.cache, args.zoom)
            im = SL.perspective(eq, ph, heading, args.pitch, args.fov, args.tile_w, args.tile_h)
        except Exception:  # noqa: BLE001
            continue
        return {"image": im, "id": m["id"], "wgs": m["wgs"], "date": m["date"], "heading": round(heading),
                "town": town["name"], "admin1": town["admin1"], "country": cand["cc"], "address": m["address"]}
    return None


def sample_towns(cand: dict, args) -> list[dict]:
    rng_seed = None if args.seed is None else args.seed + hash(cand["label"]) % 1000
    min_pop = 0 if args.rural else args.min_pop
    try:
        towns = geodata.sample(cand["cc"], args.n * 3, cand["admin1"], alpha=0.25 if args.rural else 0.5,
                               seed=rng_seed, min_pop=min_pop)
    except ValueError as e:
        print(e, file=sys.stderr)
        return []
    return sorted(towns, key=lambda t: t["population"]) if args.rural else towns


def build_rows(cands: list[dict], args) -> list[tuple[dict, list[dict]]]:
    """All candidates' towns go through one worker pool; each finished view is reported as it arrives."""
    from concurrent.futures import as_completed
    jobs = [(i, c, t) for i, c in enumerate(cands) for t in sample_towns(c, args)]
    cells: dict[int, list[dict]] = {i: [] for i in range(len(cands))}
    with ThreadPoolExecutor(args.workers) as ex:
        futs = {ex.submit(one_cell, c, t, args): (i, c, t) for i, c, t in jobs}
        for fu in as_completed(futs):
            i, c, t = futs[fu]
            try:
                res = fu.result()
            except Exception:  # noqa: BLE001
                res = None
            if res and len(cells[i]) < args.n and all(SL.dist_m(tuple(res["wgs"]), tuple(x["wgs"])) > 2000 for x in cells[i]):
                cells[i].append(res)
                print(f"  {c['label']}: {len(cells[i])}/{args.n} ({res['town']}, {res['date']})", flush=True)
    return [(c, cells[i]) for i, c in enumerate(cands)]


def compose(rows: list[tuple[dict, list[dict]]], args) -> Image.Image:
    lab_w = 170
    W = lab_w + args.n * args.tile_w
    H = max(1, len(rows)) * (args.tile_h + 4)
    S = Image.new("RGB", (W, H), (12, 12, 12))
    d = ImageDraw.Draw(S)
    fs = _font(13)
    for r, (cand, cells) in enumerate(rows):
        y = r * (args.tile_h + 4)
        d.text((8, y + 8), cand["label"], fill="yellow", font=_font(18, cand["label"]))
        d.text((8, y + 32), f"{len(cells)}/{args.n} found", fill=(180, 180, 180), font=fs)
        for i, c in enumerate(cells):
            x = lab_w + i * args.tile_w
            S.paste(c["image"], (x, y))
            d.rectangle([x, y, x + args.tile_w, y + 18], fill=(0, 0, 0))
            lab = f"{c['town'][:16]}, {c['admin1'][:14]} {c['date'] or ''} h{c['heading']}"
            d.text((x + 3, y + 2), lab, fill="yellow", font=_font(13, lab))
    return S


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["countries", "regions"])
    ap.add_argument("spec", help="countries: PT,ES,IT (names or ISO2); regions: ES:Andalusia,PT:Faro")
    ap.add_argument("--n", type=int, default=6, help="views per row")
    ap.add_argument("--side", choices=list(SIDE_OFFSET), default="ahead", help="look along the road, or at one roadside")
    ap.add_argument("--pitch", type=float, default=0)
    ap.add_argument("--fov", type=float, default=90)
    ap.add_argument("--jitter", type=float, default=0, help="random ± degrees added to the heading")
    ap.add_argument("--rural", action="store_true", help="prefer small places (village roads, not city centres)")
    ap.add_argument("--min-pop", type=int, default=1000)
    ap.add_argument("--radius", type=float, default=600, help="search radius around each sampled town, metres")
    ap.add_argument("--max-ring", type=int, default=3)
    ap.add_argument("--max-age", type=int, help="skip captures older than this year")
    ap.add_argument("--zoom", type=int, default=2, help="panorama resolution (2 ≈ 2048 px wide; enough for sheets)")
    ap.add_argument("--tile-w", type=int, default=400)
    ap.add_argument("--tile-h", type=int, default=300)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--cache", type=Path, default=Path(".geo-cache/gsv"))
    ap.add_argument("--out", type=Path, default=Path("refsheet.jpg"))
    ap.add_argument("--proxy", default=os.environ.get("GEO_PROXY"), help=PROXY_HELP)
    args = ap.parse_args()
    model_proxy_env(args.proxy)
    if args.seed is not None:
        random.seed(args.seed)
    cands = candidates(args.spec, args.mode)
    if any(c["cc"] == "CN" for c in cands):
        print("Mainland China has no Google Street View: use baidu_pano.py sample", file=sys.stderr)
    print(f"Sampling {len(cands)} candidates × {args.n} views (towns tried in parallel) …", flush=True)
    rows = build_rows(cands, args)
    for cand, cells in rows:
        print(f"{cand['label']}: {len(cells)}/{args.n} views")
    S = compose(rows, args)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    S.save(args.out, quality=88)
    index = [{"candidate": cand["label"], "country": cand["cc"], "admin1": cand["admin1"],
              "cells": [{k: v for k, v in c.items() if k != "image"} for c in cells]} for cand, cells in rows]
    args.out.with_suffix(".index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"-> {args.out} (+ {args.out.with_suffix('.index.json').name}). Compare fixed features (bollards, poles, road paint, "
          "curbs, guardrails, sign backs, plates); one sheet is a sample, not a census.")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    main()
