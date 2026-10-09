"""Street-level imagery helpers shared by gsv.py and refsheet.py.

Google retired the GeoPhotoService.SingleImageSearch endpoint (it now answers "decommissioned") and the
streetviewpixels thumbnail endpoint refuses anonymous callers (403). Discovery therefore uses Google Maps
coverage tiles (every official panorama inside a zoom-17 map tile) plus the photometa metadata call, both
through the maintained `streetlevel` package; views are rendered locally from the equirectangular panorama.
"""
from __future__ import annotations

import json
import math
import sys
import types
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
from PIL import Image

_SV = None
USER_UPLOAD_PREFIXES = ("CIHM", "CIAB", "CAoS", "AF1Q")


def streetview():
    """streetlevel.streetview, importable even without pyexiv2's native library (only used to write EXIF)."""
    global _SV
    if _SV is not None:
        return _SV
    try:
        import pyexiv2  # noqa: F401
    except Exception:  # noqa: BLE001 - missing dylib raises OSError, not ImportError
        stub = types.ModuleType("pyexiv2")

        class _Unavailable:
            def __init__(self, *a, **k):
                raise RuntimeError("pyexiv2 is unavailable; streetlevel's EXIF writing is disabled")

        stub.ImageData = stub.Image = _Unavailable
        sys.modules["pyexiv2"] = stub
    from streetlevel import streetview as sv
    _SV = sv
    return sv


def tile_xy(lat: float, lon: float, z: int = 17) -> tuple[int, int]:
    n = 2 ** z
    x = int((lon + 180.0) / 360.0 * n)
    y = int((1.0 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2.0 * n)
    return x, y


def dist_m(a: tuple[float, float], b: tuple[float, float]) -> float:
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(b[1] - a[1]) / 2) ** 2
    return 2 * 6371008.8 * math.asin(min(1.0, math.sqrt(h)))


def official(pid: str) -> bool:
    return len(pid) == 22 and not pid.startswith(USER_UPLOAD_PREFIXES)


def find_near(lat: float, lon: float, radius: float = 50.0, max_ring: int = 5, workers: int = 8) -> list[dict]:
    """Official panoramas within radius metres, nearest first: [{id, lat, lon, dist_m}].
    Searches z17 coverage tiles (~300 m wide at the equator) in rings around the point."""
    sv = streetview()
    x0, y0 = tile_xy(lat, lon)
    tile_m = 40075016.686 * max(math.cos(math.radians(lat)), 0.05) / 2 ** 17
    rings = min(max_ring, max(1, math.ceil(radius / tile_m)))
    seen: dict[str, dict] = {}

    def fetch(xy):
        try:
            return sv.get_coverage_tile(*xy)
        except Exception:  # noqa: BLE001
            return []

    for ring in range(0, rings + 1):
        xys = [(x0 + dx, y0 + dy) for dx in range(-ring, ring + 1) for dy in range(-ring, ring + 1)
               if max(abs(dx), abs(dy)) == ring]
        with ThreadPoolExecutor(workers) as ex:
            for panos in ex.map(fetch, xys):
                for p in panos or []:
                    if official(p.id) and p.id not in seen:
                        seen[p.id] = {"id": p.id, "lat": p.lat, "lon": p.lon, "dist_m": dist_m((lat, lon), (p.lat, p.lon))}
        inside = [v for v in seen.values() if v["dist_m"] <= radius]
        # stop once we have a hit and the next ring can only be farther away than the best hit
        if inside and min(v["dist_m"] for v in inside) < (ring + 0.5) * tile_m:
            break
    return sorted((v for v in seen.values() if v["dist_m"] <= radius), key=lambda v: v["dist_m"])


def metadata(pid: str) -> dict | None:
    sv = streetview()
    try:
        p = sv.find_panorama_by_id(pid)
    except Exception:  # noqa: BLE001
        return None
    if p is None:
        return None
    ym = lambda d: f"{d.year}-{int(d.month):02d}" if d and getattr(d, "month", None) else (str(d.year) if d else None)  # noqa: E731
    hist = []
    for h in p.historical or []:
        if official(h.id):
            hist.append({"id": h.id, "wgs": [h.lat, h.lon], "date": ym(h.date)})
    addr = " / ".join(str(getattr(a, "value", a)) for a in (p.address or []))
    streets = [str(getattr(s.name, "value", s.name)) for s in (p.street_names or [])]
    return {"id": p.id, "wgs": [p.lat, p.lon], "pano_heading": round(math.degrees(p.heading or 0) % 360, 1),
            "date": ym(p.date), "country_code": p.country_code, "address": addr, "streets": streets,
            "elevation_m": p.elevation, "source": p.source, "copyright": p.copyright_message,
            "history": sorted(hist, key=lambda h: h["date"] or "", reverse=True),
            "dates_seen": sorted({d for d in [ym(p.date), *(h["date"] for h in hist)] if d}),
            "neighbors": [{"id": n.id, "wgs": [n.lat, n.lon]} for n in (p.neighbors or [])][:40]}


def equirect(pid: str, cache: Path, zoom: int = 3) -> tuple[np.ndarray, float]:
    """Equirectangular panorama as an array plus the car heading (degrees) at the image centre; cached."""
    cache.mkdir(parents=True, exist_ok=True)
    img_p, meta_p = cache / f"{pid}_z{zoom}.jpg", cache / f"{pid}_z{zoom}.json"
    if img_p.exists() and meta_p.exists():
        return np.asarray(Image.open(img_p).convert("RGB")), json.loads(meta_p.read_text())["heading"]
    sv = streetview()
    p = sv.find_panorama_by_id(pid)
    if p is None:
        raise RuntimeError(f"panorama {pid} not found")
    im = sv.get_panorama(p, zoom=zoom).convert("RGB")
    im.save(img_p, quality=90)
    heading = math.degrees(p.heading or 0.0) % 360
    meta_p.write_text(json.dumps({"heading": heading}))
    return np.asarray(im), heading


def perspective(eq: np.ndarray, pano_heading: float, yaw: float, pitch: float = 0.0, hfov: float = 90.0,
                w: int = 1024, h: int = 768) -> Image.Image:
    """Pinhole view from an equirectangular panorama. yaw: compass bearing; pitch: + looks up; hfov in degrees."""
    H, W = eq.shape[:2]
    f = (w / 2) / math.tan(math.radians(hfov) / 2)
    u, v = np.meshgrid(np.arange(w) - (w - 1) / 2, np.arange(h) - (h - 1) / 2)
    x, y, z = u, -v, np.full_like(u, f, dtype=float)
    cp, sp = math.cos(math.radians(pitch)), math.sin(math.radians(pitch))
    y2, z2 = y * cp + z * sp, -y * sp + z * cp
    lon = np.arctan2(x, z2)                       # right of the view direction = positive
    lat = np.arctan2(y2, np.hypot(x, z2))
    az = np.radians(yaw - pano_heading) + lon     # relative to the panorama centre (car heading)
    px = ((az / (2 * math.pi) + 0.5) % 1.0) * W - 0.5
    py = (0.5 - lat / math.pi) * H - 0.5
    x0 = np.floor(px).astype(int)
    y0 = np.clip(np.floor(py).astype(int), 0, H - 1)
    y1 = np.clip(y0 + 1, 0, H - 1)
    fx, fy = (px - np.floor(px))[..., None], np.clip(py - np.floor(py), 0, 1)[..., None]
    x0w, x1w = x0 % W, (x0 + 1) % W
    out = (eq[y0, x0w] * (1 - fx) * (1 - fy) + eq[y0, x1w] * fx * (1 - fy)
           + eq[y1, x0w] * (1 - fx) * fy + eq[y1, x1w] * fx * fy)
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
