# GeoInt

An agent skill for finding where any photo, screenshot, video frame or Street View image was taken — the
instincts of a strong GeoGuessr player plus the discipline of an OSINT investigation. The agent leads with its own
expert read of the scene (a written gut call), then proves, sharpens or overturns it with web research and local
tools, down to street or camera level when the evidence allows. Every photo gets its own timestamped archive with
a report, evidence images and a scoreboard once the true location is known.

`SKILL.md` is the method; `references/` holds the playbooks and the worldwide clue library; `scripts/` holds the
tools.

## Install

```bash
git clone https://github.com/marouane53/GeoInt.git ~/.agents/skills/geoint   # Codex and other agents
ln -s ~/.agents/skills/geoint ~/.claude/skills/geoint                         # Claude Code
uv run ~/.agents/skills/geoint/scripts/doctor.py --network                        # check the setup
uv run ~/.agents/skills/geoint/scripts/doctor.py --models                         # optional: pre-download local models (~6.2 GB)
```

Requirements: Python 3.10+, [uv](https://docs.astral.sh/uv/), `curl`; `exiftool` and `ffmpeg` recommended. Each
script declares its own dependencies and runs with `uv run`. Per-photo archives go to `~/geoint-photos` with
timestamps in this computer's time zone; set `GEOINT_PHOTOS` / `GEOINT_TZ`, or put
`{"photos_root": "…", "timezone": "…"}` in a `config.local.json` next to `SKILL.md` (git-ignored), to change that.

## What's inside

| Area | Tools |
|---|---|
| Archive and scoring | `photo_session.py` (start / finish / truth / scoreboard / list), `bench.py` |
| One-command local first pass | `recon.py` → `meta.py`, `intake.py`, `ocr.py`, `textgeo.py`, `detect.py`, `calib.py`, `prior.py` |
| Text → place | `textgeo.py` (scripts, telltale letters, language, phone numbers, domains, postal codes, currency, regional words, ~50k brands, GeoNames places), `geodata.py`, `clues.py` |
| Reasoning ledger | `board.py` — candidates, clues, likelihood ratios capped by evidence type, exclusion rules, rank / next / check / report |
| Street level | `pano.py` (every provider plus your own manifests: coverage, list, render, sheet), `sweep.py` (rank every panorama of whole towns with MegaLoc), `gsv.py`, `refsheet.py` (real Street View rows per candidate country or region), `match.py`, `baidu_pano.py` |
| Maps and geometry | `osm.py`, `poi.py`, `gazetteer.py`, `tiles.py`, `sat_scan.py`, `terrain.py`, `sun.py`, `geo.py`, `pose.py`, `evidence.py` |
| Local models | StreetCLIP + GeoCLIP world prior (`prior.py`), OWLv2 object crops (`detect.py`), GeoCalib camera calibration (`calib.py`), MegaLoc place recognition (`sweep.py`, `match.py`), DINOv2/CLIP matching |

The skill works end to end without asking questions: reverse image search, web search, maps and Street View
lookups run automatically as part of the flow.

## Tests

```bash
uv run tests/test_tools.py && uv run tests/test_runtime.py && python3 -m unittest tests/test_photo_session.py
```

## Licences and data

Code: MIT (see `LICENSE`, which keeps the notice for reused portions). Data: GeoNames (CC BY 4.0), Wikipedia-derived
tables (CC BY-SA 4.0), OpenStreetMap name-suggestion-index (downloaded at runtime); details in `data/README.md`
and `references/data-sources.md`. Model weights are downloaded from their publishers under their own licences
(StreetCLIP is non-commercial); see `references/models.md`.
