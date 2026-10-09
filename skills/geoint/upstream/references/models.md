# Local models: what they are good for, how to read them, when to ignore them

All models run locally (Apple MPS, CUDA or CPU); nothing about the photo leaves the machine. Weights download
once (`doctor.py --models`, ~6.2 GB). Licences allow this personal use; StreetCLIP is non-commercial.

| Tool | Model | Output | Typical time (M-series Mac, cached) |
|---|---|---|---|
| `prior.py` | StreetCLIP (geolocal/StreetCLIP, CLIP ViT-L/14-336, CC BY-NC 4.0) + GeoCLIP (MIT, CLIP ViT-L/14 + GPS gallery of 100k points) | country ranking, regions of the top countries, GeoCLIP clusters, a consistent point guess, self-assessment | ~12 s |
| `detect.py` | OWLv2 (google/owlv2-base-patch16-ensemble, Apache-2.0), open vocabulary | numbered crops of signs, plates, poles, bollards, markings, vehicles… | ~8 s |
| `calib.py` | GeoCalib (ETH CVG, ECCV 2024, Apache-2.0) | FOV, focal (px and 35 mm eq.), pitch, roll, horizon line, uncertainties | ~5 s |
| `sweep.py`, `match.py` | MegaLoc (gberton/MegaLoc, MIT; DINOv2-B + optimal-transport aggregation, 8448-d, 1.7 GB) | visual place recognition: ranks street-level views of the same place across days, years and cameras | ~50 views/s |
| `match.py` | DINOv2-small / CLIP ViT-B/32 + SIFT | generic similarity (satellite thumbnails, object references) | per batch |
| `sat_scan.py` | CLIP ViT-B/32 | ranks satellite cells by a text query/preset | per scan |
| `ocr.py` | Apple Vision (auto language) / RapidOCR | text lines with boxes and confidence | ~5 s |
| `textgeo.py` | lingua (offline language ID) + rules + libphonenumber + GeoNames + name-suggestion-index | board-ready text signals | ~3 s |

## World prior (`prior.py`)

What it is: two models that learned what places look like from millions of geotagged photos and street views.
StreetCLIP scores the image against "A Street View photo in <country>" for ~200 countries (and regions of the
leading ones); GeoCLIP scores it against 100,000 GPS points. Both run on several crops and are averaged.

Measured here (24-round Street View benchmark `bench/sv24-seed1`, model alone, no reasoning): country correct
58%, median error 274 km, within 25 km 17%, within 750 km 67%, mean game score ~3,500. On ordinary real-world
photos it nailed Lisbon and Kyoto (region included) and put Kraków's country first but the region wrong.

Where it fails, and says so: indoor scenes, museum objects, close-ups, historical or monochrome photos, generic
forest/desert/sea. `assessment.informative = false` → no board signal is written; do not ingest it by hand.
It is also fooled by look-alikes (Taiwan vs Hong Kong, Czechia vs Germany, Ecuador vs Guatemala in the
benchmark) — exactly the cases the reference sheets and text clues settle.

How to use it: as a third opinion after your gut call and the text. If it agrees, move faster; if it
disagrees, look for the reason (often a strong clue it cannot read, such as a plate format). On the board it is
status `model`: likelihood ratio ≤3, never verified, never excludes. Its point guess is a starting area, not an
answer.

## Object crops (`detect.py`)

Recall-oriented: it would rather show you a tree trunk labelled "bollard" than miss a real bollard. Use the
numbered sheet as a checklist of places to zoom; judge each crop yourself. Scores are not evidence. Tune with
`--classes "a yellow road sign,a kilometre marker"` and `--threshold`. It found the taxi, storefronts and a
blurred street-name sign in a Córdoba street view; it found nothing above threshold in a wall-heavy alley —
then scan by eye.

## Camera calibration (`calib.py`)

Validated on Street View renders with known settings: pitch +12° / FOV 70° → estimated +12.2° / 72.1°
(horizon within 3 px); pitch −8° / FOV 100° → −7.0° / 98.1°. It failed on a narrow alley close-up (FOV 45° vs
80° true) but reported a large uncertainty (vfov ±13°, focal ±600 px) — `recon.md` marks such results
UNRELIABLE. Always look at the red horizon in `calib.jpg` before feeding numbers to `pose.py`, `terrain.py` or
`geo.py`. If EXIF has a trustworthy 35 mm focal length, pass `--prior-focal-35mm` to fix it.

## OCR coverage

Apple Vision with automatic language detection keeps diacritics and Cyrillic (a fixed language list strips
them: "Długa" became "Dhuga", Ukrainian became gibberish). It reads Latin-script European languages, Turkish,
Vietnamese, Indonesian, Malay, Russian, Ukrainian, Arabic, Thai, Chinese, Japanese and Korean. It does not
read Greek, Hebrew, Georgian, Armenian, Indic scripts, Sinhala, Khmer, Lao, Burmese or Ethiopic: read those
yourself and pass them to `textgeo.py --text`. Lines read only after upscaling or tiling (`pass` up/tile) are
hypotheses: zoom in and confirm.

## Upgrades worth testing next

See the project `ROADMAP.md`: modern place-recognition (MegaLoc) and matchers (LightGlue/RoMa/MASt3R) for
`match.py`; SigLIP 2 / RemoteCLIP and ground-to-aerial models for `sat_scan.py`; Apple Look Around, Yandex,
Naver and Kakao panoramas (the `streetlevel` package supports them); species ID (BioCLIP 2 → GBIF ranges);
3D-tiles render-and-compare. Measure every upgrade with `bench.py` before trusting it.
