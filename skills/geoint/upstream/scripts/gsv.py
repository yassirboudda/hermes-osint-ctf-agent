#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["streetlevel", "numpy", "pillow"]
# ///
"""Google Street View (the main ground-level source outside China): find panoramas, read dates/history/address,
render views by compass heading, build comparison sheets. Mainland China: use baidu_pano.py.

No API key. Discovery uses Google Maps coverage tiles + the photometa call (via the maintained `streetlevel`
package); views are rendered locally from the downloaded equirectangular panorama (cached in --cache).
Official car/trekker coverage only: user-uploaded photospheres are skipped.

Examples:
  gsv.py near 35.6595,139.7005 --radius 50              # nearest panorama: id, coordinates, capture date, history, address, street names, nearby ids
  gsv.py render <pano id> --heading 90 --out v.jpg      # heading = compass bearing; --pitch + looks up; --fov horizontal
  gsv.py sheet --at 35.6595,139.7005 --headings 0,60,120,180,240,300 --out around.jpg    # look around from one point
  gsv.py sheet --ids ID1,ID2 --toward 35.6600,139.7010 --out s.jpg                      # every point faces the same target
  gsv.py sheet --points pts.json --heading 90 --date 2018 --out s2018.jpg               # one capture year only (the "© year" in a screenshot is the
                                                                                      # display year, ≥ capture year: use near's dates to pick)
  gsv.py sheet --points pts.json --along --out road.jpg                                 # look along the road at each point
  gsv.py area --bbox 35.676,139.760,35.686,139.775 --spacing 120 --out panos.json       # every covered spot in an area, no Overpass needed
  match.py rank --query photo.jpg --panos panos.json --headings 0,90,180,270 --render gsv --top 10 --sheet m.jpg  # then rank them
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _streetlevel as SL  # noqa: E402
import geo  # noqa: E402
from _net import PROXY_HELP, model_proxy_env  # noqa: E402


_LATIN_FONTS = ("/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Helvetica.ttc",
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
_WIDE_FONTS = ("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", "/System/Library/Fonts/Hiragino Sans GB.ttc",
               "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")


def _font(size: int, text: str = ""):
    """Label font: Arial for Latin/Cyrillic/Greek (it has ș ț ő ğ…); Arial Unicode for CJK, Thai and other scripts."""
    wide = any(ord(ch) >= 0x0590 for ch in text)
    for p in (_WIDE_FONTS + _LATIN_FONTS) if wide else (_LATIN_FONTS + _WIDE_FONTS):
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()


def near(lat: float, lon: float, radius: float, proxy: str | None = None) -> dict | None:
    """Nearest official panorama within radius metres, with metadata; None if there is none."""
    model_proxy_env(proxy)
    hits = SL.find_near(lat, lon, radius)
    for h in hits[:3]:
        m = SL.metadata(h["id"])
        if m:
            m["distance_m"] = round(h["dist_m"], 1)
            m["candidates_within_radius"] = len(hits)
            return m
    return None


def area(bbox: list[float], spacing: float, max_tiles: int = 400, meta: bool = False) -> dict[str, dict]:
    """Official panoramas inside a bbox (s,w,n,e) from zoom-17 coverage tiles, thinned to one per `spacing` metres.
    Output matches match.py --panos: {pano_id: {"wgs": [lat, lon], "date": "", "road": ""}}."""
    s_, w_, n_, e_ = bbox
    x0, y1 = SL.tile_xy(s_, w_)
    x1, y0 = SL.tile_xy(n_, e_)
    tiles = [(x, y) for x in range(min(x0, x1), max(x0, x1) + 1) for y in range(min(y0, y1), max(y0, y1) + 1)]
    if len(tiles) > max_tiles:
        sys.exit(f"bbox covers {len(tiles)} map tiles (limit {max_tiles}, ~300 m each): use a smaller area or raise --max-tiles")
    sv = SL.streetview()

    def fetch(xy):
        try:
            return sv.get_coverage_tile(*xy)
        except Exception:  # noqa: BLE001
            return []

    found = {}
    with ThreadPoolExecutor(12) as ex:
        for panos in ex.map(fetch, tiles):
            for pnr in panos or []:
                if SL.official(pnr.id) and s_ <= pnr.lat <= n_ and w_ <= pnr.lon <= e_:
                    found[pnr.id] = (pnr.lat, pnr.lon)
    kept: dict[str, dict] = {}
    for pid, (la, lo) in sorted(found.items(), key=lambda kv: (round(kv[1][0], 4), kv[1][1])):
        if all(SL.dist_m((la, lo), tuple(v["wgs"])) >= spacing for v in kept.values()):
            kept[pid] = {"wgs": [la, lo], "date": "", "road": ""}
    if meta and kept:
        with ThreadPoolExecutor(8) as ex:
            for pid, m in zip(list(kept), ex.map(SL.metadata, list(kept))):
                if m:
                    kept[pid].update(date=m.get("date") or "", road=(m.get("streets") or [""])[0],
                                     pano_heading=m.get("pano_heading"))
    print(f"{len(found)} official panoramas in {len(tiles)} tiles; kept {len(kept)} at ≥{spacing:g} m spacing", file=sys.stderr)
    return kept


def pick_date(res: dict, date: str) -> dict | None:
    """One capture ('2018' or '2018-07') from a near() result: this panorama or one of its historical captures."""
    for p in [{"id": res["id"], "wgs": res["wgs"], "date": res["date"]}, *res.get("history", [])]:
        if p["date"] and p["date"].startswith(date):
            return p
    return None


def render(pid: str, heading: float, pitch: float, fov: float, w: int, h: int, proxy: str | None, cache: Path,
           zoom: int = 3) -> Image.Image:
    """heading: compass bearing; positive pitch = looking up; fov: horizontal field of view in degrees."""
    model_proxy_env(proxy)
    try:
        eq, pano_heading = SL.equirect(pid, cache, zoom)
    except Exception as e:  # noqa: BLE001
        print(f"gsv render failed for {pid}: {type(e).__name__}: {str(e)[:160]}", file=sys.stderr)
        im = Image.new("RGB", (w, h), "gray")
        ImageDraw.Draw(im).text((10, 10), f"render failed: {str(e)[:60]}", fill="white")
        return im
    return SL.perspective(eq, pano_heading, heading % 360, pitch, fov, w, h)


def sheet(items: list[dict], out: Path, proxy: str | None, cache: Path, cols: int = 3, tw: int = 480, th: int = 360) -> None:
    with ThreadPoolExecutor(4) as ex:
        ims = list(ex.map(lambda it: render(it["id"], it["heading"], it.get("pitch", 0), it.get("fov", 90),
                                           640, 480, proxy, cache), items))
    rows = (len(items) + cols - 1) // cols
    S = Image.new("RGB", (cols * tw, max(1, rows) * th), "black")
    d = ImageDraw.Draw(S)
    f = _font(16)
    for i, (it, im) in enumerate(zip(items, ims)):
        x, y = (i % cols) * tw, (i // cols) * th
        S.paste(im.resize((tw, th)), (x, y))
        d.rectangle([x, y, x + tw, y + 22], fill="black")
        lab = it.get("label") or f"{i}: …{it['id'][-8:]} h{it['heading']:.0f}"
        d.text((x + 4, y + 2), lab, fill="yellow", font=_font(16, lab))
    S.save(out, quality=88)


def _neg_coords(argv: list[str]) -> list[str]:
    """argparse treats negative coordinates like -1.45,-48.5 as option names; a leading space makes them plain values."""
    return [" " + a if re.match(r"^-\d[\d.]*(,-?[\d.]+)+$", a) else a for a in argv]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--proxy", default=os.environ.get("GEO_PROXY"), help=PROXY_HELP)
    ap.add_argument("--cache", type=Path, default=Path(".geo-cache/gsv"))
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("--proxy", default=argparse.SUPPRESS, help="can go before or after the subcommand")
        sp.add_argument("--cache", type=Path, default=argparse.SUPPRESS)

    n = sub.add_parser("near")
    common(n)
    n.add_argument("latlon")
    n.add_argument("--radius", type=float, default=50)

    r = sub.add_parser("render")
    common(r)
    r.add_argument("id")
    r.add_argument("--heading", type=float, required=True)
    r.add_argument("--pitch", type=float, default=0, help="positive = looking up")
    r.add_argument("--fov", type=float, default=90, help="horizontal field of view")
    r.add_argument("--width", type=int, default=1024)
    r.add_argument("--height", type=int, default=768)
    r.add_argument("--zoom", type=int, default=3, help="panorama resolution level 1–5 (3 ≈ 4096 px wide)")
    r.add_argument("--out", type=Path, required=True)

    s = sub.add_parser("sheet")
    common(s)
    g = s.add_mutually_exclusive_group(required=True)
    g.add_argument("--ids", help="comma-separated panoids")
    g.add_argument("--at", help="lat,lon: take the nearest panorama point")
    g.add_argument("--points", type=Path, help="JSON {name:[lat,lon]}: take the nearest panorama point for each")
    h = s.add_mutually_exclusive_group(required=True)
    h.add_argument("--heading", type=float)
    h.add_argument("--headings", help="comma-separated, e.g. 0,60,120,180,240,300")
    h.add_argument("--toward", help="lat,lon: every point faces this target")
    h.add_argument("--along", action="store_true", help="face the direction the camera car was driving")
    s.add_argument("--offset", type=float, default=0)
    s.add_argument("--pitch", type=float, default=0)
    s.add_argument("--fov", type=float, default=90)
    s.add_argument("--radius", type=float, default=50)
    s.add_argument("--date", help="only this capture (2018 or 2018-07), picked from this panorama and its historical captures; "
                                  "a screenshot's © year is when it was displayed, not captured")
    s.add_argument("--limit", type=int, default=12)
    s.add_argument("--out", type=Path, required=True)

    a = sub.add_parser("area")
    common(a)
    a.add_argument("--bbox", required=True, help="south,west,north,east")
    a.add_argument("--spacing", type=float, default=100, help="keep one panorama per this many metres")
    a.add_argument("--max-tiles", type=int, default=400)
    a.add_argument("--meta", action="store_true", help="also fetch capture date, street name and car heading for each kept panorama")
    a.add_argument("--out", type=Path, required=True)

    args = ap.parse_args(_neg_coords(sys.argv[1:]))
    if args.cmd == "area":
        model_proxy_env(args.proxy)
        bb = [float(v) for v in args.bbox.split(",")]
        res = area(bb, args.spacing, args.max_tiles, args.meta)
        args.out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"-> {args.out} ({len(res)} panoramas). Next: `match.py rank --query <photo> --panos {args.out} --headings 0,90,180,270 "
              f"--render gsv --top 10 --sheet m.jpg` or `gsv.py sheet --points {args.out} --along --out s.jpg`")
        return
    if args.cmd == "near":
        lat, lon = map(float, args.latlon.split(","))
        res = near(lat, lon, args.radius, args.proxy)
        print(json.dumps({"found": True, **res} if res else
                         {"found": False, "radius_m": args.radius,
                          "message": "no official Google Street View panorama within the radius (increase --radius, check coverage, "
                                     "or run doctor.py --network)"}, ensure_ascii=False, indent=1))
    elif args.cmd == "render":
        render(args.id, args.heading, args.pitch, args.fov, args.width, args.height, args.proxy, args.cache, args.zoom).save(args.out)
        print(args.out)
    else:
        panos: dict[str, dict] = {}
        if args.ids:
            for pid in args.ids.split(","):
                m = SL.metadata(pid) or {}
                panos[pid] = {"ll": m.get("wgs"), "name": "", "date": m.get("date") or "", "pano_heading": m.get("pano_heading")}
        else:
            pts = {"at": list(map(float, args.at.split(",")))} if args.at else json.loads(args.points.read_text(encoding="utf-8"))
            for name, v in pts.items():
                if isinstance(v, dict) and "wgs" in v and SL.official(name):  # gsv.py area output: already panorama ids
                    m = SL.metadata(name) or {}
                    panos.setdefault(name, {"ll": v["wgs"], "name": (m.get("streets") or [""])[0], "date": m.get("date") or "",
                                            "pano_heading": m.get("pano_heading")})
                    continue
                la, lo = (v[0], v[1]) if isinstance(v, (list, tuple)) else (v["lat"], v["lon"])
                res = near(la, lo, args.radius, args.proxy)
                if res and args.date:
                    p = pick_date(res, args.date)
                    if not p:
                        print(f"{name}: no {args.date} capture (available: {', '.join(res['dates_seen'])})", file=sys.stderr)
                        continue
                    m = SL.metadata(p["id"]) or {}
                    panos.setdefault(p["id"], {"ll": p["wgs"], "name": name, "date": p["date"], "pano_heading": m.get("pano_heading")})
                elif res:
                    street = (res.get("streets") or [""])[0]
                    label = f"{name} [{street}]" if street and name != "at" else (street or name)
                    panos.setdefault(res["id"], {"ll": res["wgs"], "name": label, "date": res.get("date") or "",
                                                 "pano_heading": res.get("pano_heading")})
                else:
                    print(f"{name}: no panorama nearby", file=sys.stderr)
        target = tuple(map(float, args.toward.split(","))) if args.toward else None
        items = []
        for pid, meta in panos.items():
            ll = meta["ll"]
            if args.headings:
                heads = [float(x) for x in args.headings.split(",")]
            elif target:
                heads = [geo.bearing(tuple(ll), target) + args.offset] if ll else [args.offset]
            elif args.along:
                heads = [(meta.get("pano_heading") or 0) + args.offset]
            else:
                heads = [args.heading]
            for hd in heads:
                where = f"{ll[0]:.5f},{ll[1]:.5f}" if ll else f"…{pid[-8:]}"
                label = " ".join(x for x in (meta["name"][:26], where, meta["date"], f"h{hd % 360:.0f}") if x)
                items.append({"id": pid, "heading": hd % 360, "pitch": args.pitch, "fov": args.fov,
                              "label": f"{len(items)}: {label}", "point": meta["name"], "wgs": ll, "date": meta["date"]})
        if not items:
            sys.exit(f"No panorama within --radius {args.radius:g} m of any requested point: nothing rendered. "
                     "Increase --radius (e.g. 300–1000) or check coverage with `gsv.py near <lat,lon> --radius 1000`.")
        pages = [items[k:k + args.limit] for k in range(0, len(items), args.limit)]
        for pi, page in enumerate(pages):
            out = args.out if pi == 0 else args.out.with_name(f"{args.out.stem}_{pi + 1}{args.out.suffix}")
            sheet(page, out, args.proxy, args.cache)
            print(out)
        args.out.with_suffix(".index.json").write_text(json.dumps(items, indent=1), encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    main()
