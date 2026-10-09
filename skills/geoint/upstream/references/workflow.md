# Default workflow: one archive per photo, autonomy, answer format

These defaults apply whenever this skill runs, from any project folder.
A project can choose another archive root explicitly (`--root`).

## Start: one timestamped archive per photograph

```bash
python3 <skill>/scripts/photo_session.py start --image "/absolute/path/to/photo.jpg"
```

- Default root: `$GEOINT_PHOTOS`, else `photos_root` in this skill's `config.local.json`, else `~/geoint-photos/`.
  The folder name is the exact analysis start time to microseconds with its UTC offset (time zone: `$GEOINT_TZ`,
  else `timezone` in `config.local.json`, else this computer's) — the analysis time, not the capture time.
- One session per photograph, even when several arrive together; never mix photos on one candidate board.
- The untouched original is copied to `original/` with its SHA-256. If the attachment bytes cannot be read,
  omit `--image`, describe the source in `original/source.txt`, and say that the original was not saved.
  Never substitute a different image.
- `cd` into the session folder and run every tool from there, with absolute script paths and the saved
  original, so crops, OCR, boards, caches and evidence all stay with that photo. Use session-relative paths
  inside boards and evidence specs (they must survive the rename). Finish background commands before renaming.
- Interrupted? `photo_session.py list --status pending` shows sessions to resume; never start over silently.

## Autonomy

- Work end to end without asking the user anything. Reverse image search (uploading the photo and crops to
  Yandex, Baidu, Google Lens, Bing, TinEye), web search, maps, OpenStreetMap, GeoNames and Street View lookups
  are all pre-approved for every photo analysed with this skill.
- Ambiguity is resolved by judgment, not by questions: choose the most reasonable reading, record the
  assumption in `report.md`, continue. A blocked service (CAPTCHA, rate limit) is skipped and noted.
- Keep secrets (API keys, tokens) out of saved files, command lines and shell history.

## report.md

`start` creates a skeleton (gut call, evidence, answer, alternatives, exclusions); `finish` refuses while the
gut call or answer section is still a placeholder. Write it as you go, in the user's language, keeping source text verbatim with a translation. It contains:
the gut call (written before tools), observations, decisive clues with the files that show them, commands
actually run, sources with links, the chosen location and coordinates (WGS84; GCJ-02 too for mainland China),
confidence per level and the radius it is based on, alternatives with the test that would separate them,
excluded candidates and why, and clues not yet explained.

## Finish

```bash
python3 <skill>/scripts/photo_session.py finish "/absolute/session/path" --country "Country" \
  --region "Region" --city "City or nearest locality" --latitude 49.1675 --longitude 20.0675 --confidence medium
```

Use the real values (those are only syntax). The folder becomes
`YYYY-MM-DD_HH-mm-ss-microseconds±HHMM__country__region__city`; `session.json` records the completion time and
result; `report.md` gets the final path and timestamps appended. Use the printed paths from then on.

## Answer format

Lead with exactly:

**Country: … | Region: … | City / nearest locality: …**

**Coordinates: 38°34'14.4"N 7°54'30.1"W (38.570667, -7.908361)**

Then: one confidence/accuracy line (what level is settled, what radius, what it rests on — an unverified
estimate is called an estimate); the decisive clues in a few bullets; the evidence image when there is one;
and last, the exact analysis timestamp with clickable absolute links to the renamed folder and its `report.md`.

## Learning from results

When the true location becomes known (the user says so, a puzzle answer, a game reveal):

```bash
python3 <skill>/scripts/photo_session.py truth "<final folder>" --latitude … --longitude … --country "…" --source "…"
python3 <skill>/scripts/photo_session.py scoreboard --write        # photos/scoreboard.md: accuracy and calibration
```

Then add whatever decided or misled the case to `references/world/` (format in `world/README.md`), tagged
`case:<folder timestamp>`. The scoreboard shows whether "high" confidence really means high.
