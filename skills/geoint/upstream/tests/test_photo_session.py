"""Archive workflow checks; all sample sessions live in temporary directories."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "photo_session.py"


class PhotoArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "original photo.jpg"
        self.source.write_bytes(b"archive test fixture; copied without modification")

    def command(self, *args, success=True):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args)],
            cwd=self.root, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0 if success else 1, result.stderr)
        return json.loads(result.stdout) if success else result.stderr

    def start(self):
        return self.command("start", "--root", self.root / "archives", "--image", self.source)

    def finish(self, folder, *extra, success=True):
        return self.command(
            "finish", folder, "--country", "Slovakia", "--region", "Prešov",
            "--city", "Poprad", "--latitude", "49.1675", "--longitude", "20.0675",
            "--confidence", "medium", *extra, success=success,
        )

    def test_preserves_original_evidence_timestamp_and_final_links(self):
        first = self.start()
        folder = Path(first["folder"])
        (folder / "report.md").write_text(f"Best estimate. Original: {first['original']}\n")
        (folder / "evidence.jpg").write_bytes(b"evidence fixture")
        final = self.finish(folder)
        renamed = Path(final["folder"])
        self.assertFalse(folder.exists())
        self.assertEqual(first["started_at"], final["started_at"])
        self.assertTrue(renamed.name.endswith("__slovakia__presov__poprad"))
        self.assertEqual(Path(final["original"]).read_bytes(), self.source.read_bytes())
        self.assertEqual((renamed / "evidence.jpg").read_bytes(), b"evidence fixture")
        metadata = json.loads((renamed / "session.json").read_text())
        self.assertEqual(metadata["original"]["sha256"], hashlib.sha256(self.source.read_bytes()).hexdigest())
        self.assertEqual(metadata["result"]["coordinate_system"], "WGS84")
        report = Path(final["report"]).read_text()
        self.assertIn(str(renamed), report)
        self.assertNotIn(str(folder) + "/original/", report)
        second = self.finish(renamed)
        self.assertEqual(final["folder"], second["folder"])
        self.assertEqual(Path(second["report"]).read_text().count("<!-- geogussr-archive -->"), 1)

    def test_invalid_coordinates_and_missing_report_preserve_pending_folder(self):
        started = self.start()
        folder = Path(started["folder"])
        self.finish(folder, success=False)
        (folder / "report.md").write_text("Best estimate.\n")
        for latitude in ("nan", "91", "inf"):
            self.finish(folder, "--latitude", latitude, success=False)
        self.assertTrue(folder.exists())
        self.assertEqual(json.loads((folder / "session.json").read_text())["status"], "pending")

    def test_existing_archive_is_never_overwritten(self):
        started = self.start()
        folder = Path(started["folder"])
        (folder / "report.md").write_text("Best estimate.\n")
        collision = folder.with_name(folder.name + "__slovakia__presov__poprad")
        collision.mkdir()
        (collision / "keep.txt").write_text("Keep this earlier archive.")
        self.finish(folder, success=False)
        self.assertTrue(folder.exists())
        self.assertEqual((collision / "keep.txt").read_text(), "Keep this earlier archive.")

    def test_new_photos_have_separate_folders_and_missing_bytes_are_explicit(self):
        self.assertNotEqual(self.start()["folder"], self.start()["folder"])
        pending = self.command("start", "--root", self.root / "archives")
        self.assertIsNone(pending["original"])
        self.assertIn("not been saved", (Path(pending["folder"]) / "original" / "source.txt").read_text())
        self.command("start", "--root", self.root / "missing", "--image", self.root / "no.jpg", success=False)
        self.assertFalse((self.root / "missing").exists())

    def test_truth_scores_session_and_survives_refinish(self):
        started = self.start()
        folder = Path(started["folder"])
        (folder / "report.md").write_text("Best estimate.\n")
        self.command("truth", folder, "--latitude", "49.0", "--longitude", "20.0", success=False)  # not finished yet
        final = self.finish(folder)
        renamed = Path(final["folder"])
        scored = self.command("truth", renamed, "--latitude", "49.2", "--longitude", "20.1",
                              "--country", "Slovakia", "--region", "Prešov", "--source", "owner")
        truth = scored["truth"]
        self.assertAlmostEqual(truth["error_km"], 4.53, delta=0.3)
        self.assertTrue(truth["country_hit"])
        self.assertTrue(truth["region_hit"])
        self.assertGreater(truth["game_score_estimate"], 4980)
        report = (renamed / "report.md").read_text()
        self.assertIn("## Ground truth", report)
        # recording the truth again replaces the block; finishing again keeps it once
        self.command("truth", renamed, "--latitude", "48.15", "--longitude", "17.11", "--country", "Slovakia")
        self.finish(renamed)
        report = (renamed / "report.md").read_text()
        self.assertEqual(report.count("## Ground truth"), 1)
        self.assertIn("48.150000, 17.110000", report)
        self.assertEqual(report.count("<!-- geogussr-archive -->"), 1)
        self.assertLess(report.index("## Ground truth"), report.index("<!-- geogussr-archive -->"))

    def test_scoreboard_and_list(self):
        archives = self.root / "archives"
        for lat, conf in (("49.2", "medium"), ("10.0", "high")):
            folder = Path(self.start()["folder"])
            (folder / "report.md").write_text("Best estimate.\n")
            final = self.finish(folder, "--confidence", conf)
            self.command("truth", final["folder"], "--latitude", lat, "--longitude", "20.1", "--country", "Slovakia")
        pending = self.start()
        listed = self.command("list", "--root", archives)
        self.assertEqual(listed["count"], 3)
        self.assertEqual(self.command("list", "--root", archives, "--status", "pending")["sessions"][0]["folder"], pending["folder"])
        board = self.command("scoreboard", "--root", archives, "--write")
        self.assertEqual(board["scored_sessions"], 2)
        self.assertEqual(board["within_km"]["25"], 0.5)
        self.assertEqual(board["by_confidence"]["high"]["n"], 1)
        self.assertEqual(board["by_confidence"]["high"]["within_200km"], 0.0)
        self.assertTrue((archives / "scoreboard.md").read_text().startswith("# GeoInt scoreboard"))

    def test_report_skeleton_must_be_filled_before_finish(self):
        folder = Path(self.start()["folder"])
        skeleton = (folder / "report.md").read_text()
        self.assertIn("## Gut call (before tools)", skeleton)
        self.assertIn("Fill these report.md sections", self.finish(folder, success=False))
        filled = skeleton.replace("## Gut call (before tools)\n<!-- fill:", "## Gut call (before tools)\nSlovakia 60% (Tatras)\n<!--")
        (folder / "report.md").write_text(filled)
        self.assertIn("Answer", self.finish(folder, success=False))
        (folder / "report.md").write_text(filled.replace("## Answer\n<!-- fill:", "## Answer\nPoprad, medium\n<!--"))
        self.assertTrue(self.finish(folder)["folder"].endswith("__slovakia__presov__poprad"))

    def test_unicode_place_names_fit_filesystem_limits(self):
        pending = self.start()
        folder = Path(pending["folder"])
        (folder / "report.md").write_text("Estimated location.\n")
        final = self.finish(folder, "--country", "中国" * 40, "--region", "广东" * 40, "--city", "清远" * 40)
        self.assertLessEqual(len(Path(final["folder"]).name.encode("utf-8")), 255)
        self.assertTrue(Path(final["report"]).is_file())


if __name__ == "__main__":
    unittest.main()
