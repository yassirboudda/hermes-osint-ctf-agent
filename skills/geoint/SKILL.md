---
name: geoint
description: >-
  Photo / Street View / GeoGuessr geolocation for OSINT CTFs. Vendors
  marouane53/GeoInt (method, references, scripts, clue tables). Use for
  “where was this taken?”, chronolocation, Overpass geometry, sun/shadow,
  OCR→country, panorama matching. Hermes OPSEC overlays apply.
---

# GeoInt (Hermes) — photo geolocation

Upstream skill: [marouane53/GeoInt](https://github.com/marouane53/GeoInt) (MIT), vendored at
`skills/geoint/upstream/`.

`${GEOINT_HOME}` = absolute path to `skills/geoint/upstream` (or `$GEOINT_HOME` from `.env`).

## Hermes OPSEC overlays (mandatory)

GeoInt’s upstream skill is aggressive (autonomous reverse-image / Street View sweeps). In **this**
repo, CTF rules win:

1. Soft crawl only — dedicated `$CTF_UA` / `$GEOINT_UA` (never desktop Chrome UA).
2. No fuzz, no wordlists, no exploit, no social engineering.
3. Prefer offline corpus + digests before expensive vision / local model downloads (~6 GB).
4. Correlate ≥2 independent sources before proposing a location as a CTF flag.
5. Never submit CTFd flags without human/team OK.
6. Stop on 403/429; note blocked services in the session `report.md`.

Launcher (sets `GEOINT_HOME`, injects UA, runs upstream scripts):

```bash
python3 tools/geoint_cli.py doctor
python3 tools/geoint_cli.py clues lookup driving-side left
python3 tools/geoint_cli.py sun pos --at 48.8566,2.3522 --time 2024-06-21T12:00 --tz Europe/Paris
python3 tools/geoint_cli.py session start --image /abs/path/photo.jpg
```

## When to load

- Challenge image / video frame / Street View screenshot with unknown place
- Chronolocation (shadows, sun, season)
- “Exact spot” OSINT after a handle/org pivot yields a photo
- Nation-fiction GEOINT (still use Overpass / sun / OCR tables where applicable)

## Method (summary — full text in upstream)

1. **Gut call first** (write ranked shortlist + %) before tools — see `upstream/SKILL.md` Step 1
   and `upstream/references/observe.md`.
2. **Archive per photo**: `photo_session.py start` → work inside that folder → `finish`.
3. **Quick vs deep**: game/SV screenshots = quick; CTF “exact spot” = deep funnel.
4. **Recon**: `recon.py` → meta / EXIF / OCR / textgeo / detect / calib / prior (models optional).
5. **Prove**: reverse image (Yandex/Baidu/Lens/Bing/TinEye), web search in local languages,
   Overpass (`osm.py`), sun geometry (`sun.py`), panoramas (`pano.py` / `sweep.py`), board
   (`board.py`).
6. **Answer format**: Country | Region | City + WGS84 coords + confidence/radius + decisive clues.
   For CTF flags, also cite ≥2 sources.

Read once per session: `upstream/references/workflow.md`.

## Key playbooks (upstream/references)

| File | Topic |
|------|--------|
| `observe.md` | Image-reading checklist (edges, plates, roads, sky) |
| `country-funnel.md` | Coarse→fine country exclusion |
| `search.md` | Reverse image + web search tactics |
| `streetlevel.md` | Panorama providers beyond Google SV |
| `sky.md` / `geometry.md` | Sun, shadows, bearings, FoV |
| `aerial.md` / `corridors.md` | Satellite + linear OSM features |
| `verify.md` | What counts as proof vs estimate |
| `world/*.md` | Regional clue library |

## Offline clue tables (upstream/data)

`clues.py lookup` — plates, calling codes, driving side, territories, admin divisions,
`text_signals.json`, `countries.json`, Street View coverage. No network for lookups.

```bash
python3 tools/geoint_cli.py clues list
python3 tools/geoint_cli.py clues lookup calling-code +33
python3 tools/geoint_cli.py clues lookup driving-side --country France
```

## Heavy / optional pieces

- Local models (StreetCLIP, GeoCLIP, OWLv2, MegaLoc, …): `doctor.py --models` (~6.2 GB). Skip in
  constrained cages; gut + OCR + Overpass + sun + reverse image often suffice for CTF.
- Requires: Python 3.10+, `curl`; `exiftool` / `ffmpeg` recommended; [uv](https://docs.astral.sh/uv/)
  for script PEP 723 deps (`uv run …`).

## Update upstream

See `UPSTREAM.md`. Do not strip the MIT / data licence notices in `upstream/LICENSE` and
`upstream/data/README.md`.
