#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy", "pillow", "phonenumbers>=8.13", "lingua-language-detector>=2.0"]
# ///
"""Offline checks for the newer tools. Run: uv run tests/test_tools.py
Network-free: GeoNames- and brand-index-dependent checks are skipped when those caches are absent."""
from __future__ import annotations

import json
import math
import shutil
import subprocess
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import geodata  # noqa: E402
import textgeo  # noqa: E402
import meta  # noqa: E402
import _streetlevel as SL  # noqa: E402

CACHE = Path.home() / ".cache" / "geoint"
HAVE_PLACES = any((CACHE / "geonames").glob("cities500*.pkl"))
HAVE_BRANDS = (CACHE / "nsi" / "brands.v1.pkl").exists()


def signals(*texts: str, places: bool = False, brands: bool = False) -> tuple[list[dict], list[dict]]:
    lines = [{"text": t, "conf": 1.0, "box": None, "pass": "typed", "src": "typed"} for t in texts]
    ev = textgeo.Board(None)
    textgeo.analyse_scripts(lines, ev)
    textgeo.analyse_letters(lines, ev)
    textgeo.analyse_domains(lines, ev)
    textgeo.analyse_postal(lines, ev)
    textgeo.analyse_currency(lines, ev)
    textgeo.analyse_words(lines, ev)
    if brands:
        textgeo.analyse_brands(lines, ev, None)
    textgeo.analyse_phones(lines, ev, [r["iso2"] for r in textgeo.shortlist(ev)] or ["US"])
    if places:
        textgeo.analyse_places(lines, ev, None, False, None)
    return ev.signals, textgeo.shortlist(ev)


class CountryDataTests(unittest.TestCase):
    def test_aliases_and_driving_side(self):
        self.assertEqual(geodata.country("Czech Republic")["iso2"], "CZ")
        self.assertEqual(geodata.country("UK")["iso2"], "GB")
        self.assertEqual(geodata.country("Ivory Coast")["iso2"], "CI")
        self.assertEqual(geodata.country("Azores")["iso2"], "PT")
        self.assertEqual(geodata.country("GB")["drive"], "left")
        self.assertEqual(geodata.country("CN")["drive"], "right")
        self.assertEqual(geodata.country("HK")["drive"], "left")
        self.assertEqual(geodata.country("GI")["drive"], "right")
        self.assertNotIn("CS", geodata.countries())

    def test_norm_folds_accents_not_scripts(self):
        self.assertEqual(geodata.norm("São Tomé"), "sao tome")
        self.assertEqual(geodata.norm("Москва"), "москва")


class TextSignalTests(unittest.TestCase):
    def top(self, *texts, **kw):
        _, short = signals(*texts, **kw)
        return short[0]["iso2"] if short else None

    def test_scripts(self):
        self.assertEqual(self.top("ถนนสุขุมวิท ซอย 11"), "TH")
        self.assertEqual(self.top("東京駅 丸の内北口"), "JP")
        self.assertEqual(self.top("서울특별시 종로구"), "KR")
        self.assertIn(self.top("台北市忠孝東路四段"), ("TW", "HK"))

    def test_unique_letters_confirm_language_and_explain_shared_ones(self):
        sigs, short = signals("Zażółć gęślą jaźń, ul. Długa 5")
        self.assertEqual(short[0]["iso2"], "PL")
        pl = [s for s in sigs if s.get("language") == "pl"]
        self.assertTrue(pl and pl[0]["lr"]["PL"] == 10.0)
        self.assertFalse(any(s.get("language") == "lt" for s in sigs))

    def test_phone_domain_currency_words(self):
        self.assertEqual(self.top("+351 21 342 0000"), "PT")
        self.assertEqual(self.top("www.example.co.uk"), "GB")
        self.assertEqual(self.top("Fiyat 25 ₺"), "TR")
        self.assertEqual(self.top("Borracharia do Zé"), "BR")
        self.assertEqual(self.top("Talho Central"), "PT")

    def test_phone_digits_are_not_postal_codes(self):
        sigs, _ = signals("+351 21 342 0000")
        self.assertFalse([s for s in sigs if s["kind"] == "postal"])

    def test_watermarks_are_ignored(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "ocr.json"
            p.write_text(json.dumps({"items": [{"text": "© 2026 Google", "conf": 1.0}, {"text": "Rua Augusta", "conf": 1.0}]}))
            lines = textgeo.load_lines(Namespace(ocr=str(p), text=None, file=None, min_conf=0.4))
            self.assertEqual([ln["text"] for ln in lines], ["Rua Augusta"])

    @unittest.skipUnless(HAVE_BRANDS, "brand index not cached")
    def test_brand(self):
        self.assertEqual(self.top("Żabka", brands=True), "PL")
        _, short = signals("Biedronka", brands=True)
        self.assertEqual({r["iso2"] for r in short[:2]}, {"PL", "SK"})  # operates in both: a tie is the right answer

    @unittest.skipUnless((CACHE / "geonames" / "admin1CodesASCII.txt").exists(), "admin1 names not cached")
    def test_region_names_tolerate_admin_words(self):
        names = lambda cc, q: [geodata.admin1_name(cc, c) for c in geodata.admin1_codes(cc, q)]  # noqa: E731
        self.assertEqual(names("PL", "Pomeranian Voivodeship"), ["Pomerania"])
        self.assertEqual(names("RU", "Moscow Oblast"), ["Moscow Oblast"])
        self.assertIn("Munster", geodata.admin1_names("IE"))

    @unittest.skipUnless(HAVE_PLACES, "GeoNames not cached")
    def test_places_primary_names_first(self):
        rows = geodata.search("Augusta")
        self.assertEqual(rows[0]["match"], "name")
        self.assertEqual(geodata.reverse(38.57, -7.91)[0]["country"], "PT")


class MetaTests(unittest.TestCase):
    def test_offset_countries_are_dst_aware(self):
        from datetime import datetime
        summer = meta.countries_for_offset(60, datetime(2024, 7, 12, 10))
        winter = meta.countries_for_offset(60, datetime(2024, 1, 12, 10))
        self.assertIn("PT", summer)   # WEST in summer
        self.assertIn("GB", summer)   # BST
        self.assertNotIn("PT", winter)
        self.assertIn("FR", winter)   # CET in winter
        self.assertNotIn("FR", summer)

    @unittest.skipUnless(shutil.which("exiftool"), "exiftool missing")
    def test_offset_from_gps_time_and_thumbnail_crop(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "PXL_20240712_101530123.jpg"
            Image.new("RGB", (400, 300), (90, 140, 90)).save(f)
            Image.new("RGB", (160, 90)).save(Path(d) / "t.jpg")
            subprocess.run(["exiftool", "-q", "-overwrite_original", "-DateTimeOriginal=2024:07:12 10:15:30",
                            "-GPSDateStamp=2024:07:12", "-GPSTimeStamp=09:15:30", "-GPSLatitude=38.71", "-GPSLatitudeRef=N",
                            "-GPSLongitude=9.13", "-GPSLongitudeRef=W", f"-ThumbnailImage<={Path(d) / 't.jpg'}", str(f)], check=True)
            raw = meta.exiftool(f)
            dg = meta.digest(f, raw)
            self.assertAlmostEqual(dg["gps"]["lon"], -9.13, places=2)
            self.assertEqual(dg["time"]["utc_offset"], "+01:00")
            self.assertIn("PT", dg["time"]["countries_with_this_offset_on_that_date"])
            prev = meta.extract_previews(f, Path(d), dg["image"]["size"])
            self.assertTrue(any("cropped" in p.get("note", "") for p in prev))


class BoardTests(unittest.TestCase):
    def run_board(self, d: Path, *args):
        return subprocess.run([sys.executable, str(ROOT / "scripts" / "board.py"), *args], cwd=d, capture_output=True, text=True)

    def test_ingest_caps_model_and_model_cannot_exclude(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            self.run_board(d, "init", "--photo", "x.jpg")
            sig = {"tool": "prior.py", "signals": [{"kind": "model", "status": "model", "level": "country", "clue": "model says PT",
                                                    "p": {"PT": 0.9, "ES": 0.05}, "n_classes": 200}]}
            (d / "prior.json").write_text(json.dumps(sig))
            r = self.run_board(d, "ingest", "prior.json")
            self.assertEqual(r.returncode, 0, r.stderr)
            b = json.loads((d / "board.json").read_text())
            pt = [e for e in b["evidence"] if e["candidate"] == "Portugal"]
            self.assertEqual(pt[0]["lr"], 3.0)          # 0.9 × 200 capped at 3
            self.assertEqual(b["candidates"]["Portugal"]["iso2"], "PT")
            again = self.run_board(d, "ingest", "prior.json")
            self.assertIn("Ingested 0 signals", again.stdout)
            r = self.run_board(d, "exclude", "Spain", "--clue", "K1", "--computed", "prior.json")
            self.assertNotEqual(r.returncode, 0)
            r = self.run_board(d, "check")
            self.assertIn("no read/computed evidence", r.stdout)


    def test_retract_report_json_and_status_cap(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            self.run_board(d, "init", "--photo", "x.jpg")
            r = self.run_board(d, "apply", "--kind", "driving-side", "--value", "left", "--status", "observed")
            self.assertEqual(r.returncode, 0, r.stderr)
            b = json.loads((d / "board.json").read_text())
            self.assertEqual(b["clues"]["K1"]["status"], "observed")
            self.assertTrue(all(e["lr"] <= 5.0 for e in b["evidence"]))
            r = self.run_board(d, "retract", "K1", "--why", "it was a mirrored image")
            self.assertEqual(r.returncode, 0, r.stderr)
            b = json.loads((d / "board.json").read_text())
            self.assertTrue(all(e["lr"] == 1.0 for e in b["evidence"] if e["clue"] == "K1"))
            r = self.run_board(d, "report")
            json.loads(r.stdout)  # stdout must be valid JSON (reminders go to stderr)

    def test_streetview_coverage_prior(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            self.run_board(d, "init", "--photo", "x.jpg")
            r = self.run_board(d, "apply", "--kind", "coverage", "--value", "streetview")
            self.assertEqual(r.returncode, 0, r.stderr)
            b = json.loads((d / "board.json").read_text())
            iso = {v.get("iso2") for v in b["candidates"].values()}
            self.assertIn("KE", iso)          # official coverage
            self.assertNotIn("MA", iso)       # Morocco: no official road coverage
            self.assertTrue(all(v.get("iso2") for v in b["candidates"].values()))

    @unittest.skipUnless(HAVE_PLACES and shutil.which("uv"), "GeoNames or uv missing")
    def test_children_of_a_country_are_offline_regions(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            self.run_board(d, "init", "--photo", "x.jpg")
            r = self.run_board(d, "children", "Ghana")
            self.assertEqual(r.returncode, 0, r.stderr)
            b = json.loads((d / "board.json").read_text())
            regions = {k: v for k, v in b["candidates"].items() if v["level"] == "admin1"}
            self.assertIn("Greater Accra", regions)
            self.assertTrue(regions["Greater Accra"]["center"])


class StreetViewProjectionTests(unittest.TestCase):
    def test_heading_maps_to_the_right_part_of_the_panorama(self):
        W, H = 720, 360
        eq = np.zeros((H, W, 3), dtype=np.uint8)
        pano_heading = 40.0
        # paint a red column at compass bearing 130° = pano_heading + 90° → x = W * (90/360 + 0.5)
        x = int(W * (90 / 360 + 0.5))
        eq[:, x - 3:x + 4] = (255, 0, 0)
        im = np.asarray(SL.perspective(eq, pano_heading, 130.0, 0, 60, 101, 61))
        self.assertGreater(im[30, 50, 0], 200)
        self.assertLess(np.asarray(SL.perspective(eq, pano_heading, 40.0, 0, 60, 101, 61))[30, 50, 0], 50)

    def test_tile_math(self):
        self.assertEqual(SL.tile_xy(40.7580, -73.9855), (38598, 49258))


class BenchTests(unittest.TestCase):
    def test_metrics(self):
        import importlib
        bench = importlib.import_module("bench")
        m = bench.metrics([{"error_km": 0.5, "country_true": "PT", "country_pred": "PT"},
                           {"error_km": 300, "country_true": "PT", "country_pred": "ES"}])
        self.assertEqual(m["within"]["1km"], 0.5)
        self.assertEqual(m["within"]["750km"], 1.0)
        self.assertEqual(m["country_accuracy"], 0.5)
        self.assertEqual(bench.score_km(0), 5000)


if __name__ == "__main__":
    unittest.main(verbosity=1)
