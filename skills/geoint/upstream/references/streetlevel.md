# Street-level imagery anywhere: find it, sweep it, verify across years

Used in SKILL.md Steps 5–7 whenever a town (or a short list of towns) is in play and you need the street.
Google Street View is one source among many. Where it is missing — much of Africa, the Middle East, Central
Asia, parts of South Asia, every place before 2007 — the answer usually sits in a source you have to go and
find: a national or local panorama site, a crowd-sourced platform, an old capture, a satellite archive.

## Why this file exists (measured, not assumed)

A 1990s film print of a residential street, no text, no landmark. The agent's gut named the best-known
town of the region, reverse search found nothing, the country has no Google coverage, and it stopped at a
city-level guess. The photo was taken in the region's *largest* town, which a local website covers with
2013–2015 panoramas — a source the agent never looked for. What it took, and what the tools now do:

| Step the agent skipped | Measured effect once done |
|---|---|
| List every big town of the region (`geodata.py towns`), not just the gut town | the right town was #1 of its region by population; the gut town #2 |
| Look for local street-level sites (a web search in the local languages finds it) | the only street-level imagery of those towns; 2013–14, the closest in time to the photo |
| Sweep **every** panorama of the candidate towns instead of a sample | the agent's 15 % sample never contained the right panorama |
| Rank with a place-recognition model (MegaLoc) instead of generic DINOv2 | true panorama ranked **1st of 2,703** in its town (DINOv2: 479th); **1st of 9,203** across three cities, with all 50 of the top 50 in the right town |
| Read the cluster of top hits | 7–17 of the top 20 fell within 500 m of the answer |
| Verify on structure, not inlier counts | SIFT, LoFTR and DISK+LightGlue all gave 8–35 "inliers" for the truth and for 30 look-alikes alike: across decades they are noise |

Downloading one town's panoramas took 80 s (2,703 small previews); indexing ~7 min on a laptop GPU.
Cheap compared with the hour the agent spent on generic reverse searches.

## 1. The ladder: what covers this place?

Run it for each candidate town (or the gut-call point) before saying "no street level here":

1. **Probe everything scriptable at once**: `pano.py coverage <lat,lon> --radius 500` — Google (official),
   Apple Look Around, Bing Streetside, Yandex, Naver, Kakao, Mapy, Já.is, KartaView, Panoramax (+ Mapillary
   with `MAPILLARY_TOKEN`). Seconds per provider; prints counts, nearest panorama and dates. These are only
   the sources everyone knows; step 2 is not optional.
2. **Find the local and historical sources** (the step that decided the case above). Search the web in
   the country's languages, for the town and for the country:
   - English: `"<town>" street view 360`, `"<country>" street level panoramas`, `virtual tour streets <town>`
   - French: `vue des rues 360 <ville>`, `panoramas rues <pays>`, `visite virtuelle <ville> rues`
   - Spanish/Portuguese: `vista de calle 360 <ciudad>`, `fotos 360 ruas <cidade>`
   - Arabic: `صور 360 شوارع <المدينة>`, `جولة افتراضية شوارع`; Persian: `نمای خیابان <شهر>`;
     Russian: `панорамы улиц <город>`; Turkish: `sokak görünümü <şehir>`
   - also: the national mapping agency, the city's open-data portal, telecom/real-estate "360" projects,
     universities, tourism boards, old "street view" startups (often dead sites with live image servers).
   Anything found becomes a manifest (§3) and is swept like the big providers. (The site that decided the
   case above was carte.ma, 2013–2015 panoramas of Moroccan cities — an example of what to look for, not a
   place to go by default: every country has its own, and you have to find them.)
3. **The browser, for what scripts cannot reach** (pre-approved; use the owner's Chrome when available):
   - Google Maps: drag the Street View pegman — blue dots/lines are coverage, small blue circles are
     **user photo spheres** (often the only Google imagery in uncovered countries; not reachable by
     script any more). Also the place's **photos** tab for shops, schools, mosques, hotels nearby.
   - Mapillary (`mapillary.com/app/?lat=…&lng=…&z=16`) and KartaView web maps; Apple Maps Look Around.
   - YouTube: `walking tour <town> 4K`, `<town> driving`, `<town> 360` — frame-grab and compare.
4. **Maps and satellite reasoning** (works everywhere, even with no ground imagery):
   - **City fabric**: `geodata.py towns <CC> --admin1 "<region>" --json > towns.json` then
     `tiles.py sheet --points towns.json --zoom 15 --size 640 --out fabric.jpg` — every candidate town at the
     same scale. Read street grid regularity, street width, block size, river/oasis/sea, relief; keep the
     towns whose fabric can produce what the photo shows (a long straight 20 m street, a planned grid, an
     old medina, a hillside).
   - **Labels**: `--source google-hybrid` (satellite + street names) or `google-map` / `esri-street`.
   - **Then and now**: `tiles.py wayback <lat,lon> --out wb.jpg` shows every archived look of a place
     since 2014 (Esri Wayback); `--source s2:<year>` gives yearly Sentinel-2 mosaics (10 m) from 2018; older
     than that, search national aerial-photo archives (many countries have them online).
   - `osm.py` for geometry questions (street orientation from the sun, junction angles, widths).
5. **Still nothing**: news and blog photos, Wikimedia Commons geosearch, real-estate and school photos,
   old postcards (`delcampe`, Flickr groups) — see `verify.md` §4.

Prefer imagery **closest in time to the photo**: for an old print, the oldest street-level capture you can
get (a 2013 local archive beats 2024 coverage) plus Wayback; for a recent phone photo, the newest.

## 2. Providers you can script

| Provider | Where | Notes |
|---|---|---|
| `google` | worldwide where covered | official imagery only through coverage tiles; history and dates via `gsv.py near` |
| `apple` | US, Canada, Japan, Australia, NZ, much of Europe (cities) | HEIC faces (needs `pillow-heif`); tops/bottoms not rendered |
| `bing` | US, parts of Europe | Microsoft and TomTom captures, mostly 2009–2022 |
| `yandex` | Russia, Belarus, Kazakhstan, Turkey, Serbia, others | nearest-panorama lookups; grid sampling for areas |
| `naver`, `kakao` | South Korea | Kakao keeps captures back to ~2009 |
| `mapy` | Czechia, Slovakia, neighbouring countries | panoramas are stored north-centred |
| `ja` | Iceland | blocks bursts (HTTP 403): keep `--spacing` large |
| `kartaview` | patchy worldwide | dashcam photos (one direction), 2015–2020 mostly |
| `panoramax` | France first, growing (CC-BY-SA) | the meta-catalogue is sometimes down; the main instances are queried too |
| `mapillary` | worldwide, patchy | needs a free `MAPILLARY_TOKEN`; otherwise use the web app |
| `baidu_pano.py` | mainland China | separate script (GCJ-02 coordinates) |
| a manifest | anything else | §3 |

`pano.py coverage` answers "who covers this?"; `pano.py list --provider X --near lat,lon --radius m --out
town.jsonl` writes the manifest a sweep needs. Point-lookup providers (Yandex, Naver, Kakao, Mapy, Já) are
sampled on a grid (`--spacing`), throttled; Já.is in particular blocks bursts.

## 3. Any other source: write a manifest

A manifest is JSON Lines, one panorama per line (full format in `scripts/_pano.py`):

```json
{"provider": "mysite", "id": "001234", "lat": 34.03412, "lon": -5.00051, "heading": 87.0, "date": "2014-09-12",
 "link": "https://…", "low": {"kind": "cube-strip", "url": "https://…/preview.jpg", "order": "lfrbud"},
 "high": {"kind": "cube", "faces": {"f": "https://…/f.jpg", "r": "…", "b": "…", "l": "…", "u": "…", "d": "…"}}}
```

Kinds: `equirect` (`url`, optional `center` = bearing of the middle column), `cube` (faces seen from inside,
`f` along `heading`, `r` = heading + 90°), `cube-strip` (all faces in one image), `photo` (one ordinary
photo looking along `heading`, with `hfov`). "low" is what a sweep downloads; "high" is for sheets.

How to get there from a viewer website (most panorama sites are built the same way):
- Open the site in the browser, open one panorama, and read its **network requests** (or the page's JS):
  you are looking for (1) a **scene index** (a JSON listing every panorama with lat/lon, heading, date, links
  to neighbours) and (2) the **image URL pattern**.
- Common patterns: krpano / Pannellum multires `…/l3_f_1_1.jpg` or `%l/%s/%y_%x.jpg` (faces `f b l r u d`);
  Marzipano `…/tiles/<scene>/<z>/<face>/<y>/<x>.jpg`; a `preview.jpg` strip of all six faces; plain
  equirectangular `…/pano.jpg`. Low-resolution "fallback" or "mobile" faces are ideal for sweeps.
- A heading field (or `northOffset`) gives the compass bearing of the front face; check one panorama with
  `pano.py render … --bearing <toward a landmark>` before sweeping (the landmark must be centred).
- Write the manifest with a few lines of Python, then `sweep.py index --manifest it.jsonl`. Worked example of
  the pattern: a site's catalogue JSON listed its cities and their asset folders, each city's JSON listed
  every scene with lat/lon, heading and date, and each scene folder held `preview.jpg` (a six-face strip,
  256 px) and `mobile_<f|b|l|r|u|d>.jpg` (1024 px faces): low = the strip, high = the faces.
- Be polite: one index download per town, cached in `~/.cache/geoint/panos`; no hammering.

## 4. Sweep: rank a whole town (or several)

```bash
pano.py list --provider <provider> --near <town lat,lon> --radius 6000 --out town.jsonl   # or your own manifest
sweep.py index --manifest town.jsonl                     # ~1 min download + ~3 min per 1,000 panoramas; cached
sweep.py rank --index town --query original/<photo> --out-dir sweep           # several towns: --index a b c
sweep.py view --index town --id <provider:id> --query original/<photo> --out sweep/view.jpg
```

- Index **every** panorama of each candidate town. Sampling is the failure mode: a 15 % sample cannot
  contain the answer 85 % of the time, and the ranking cannot find what was never indexed.
- Several towns in one `rank` is a town test: the share of each town in the top 50 is evidence (in the
  case above, 50/50 for the right town against two big decoy cities).
- `rank` fuses the whole photo with its left and right parts (robust to people in the middle) and adds an
  **area score** (support from neighbouring panoramas within 120 m). Read `clusters.json`: a tight group of
  top hits is a far stronger signal than a lone high score.
- Masks: `--mask x0,y0,x1,y1` paints out a big foreground object. Usually unnecessary (people barely hurt
  MegaLoc); try it when a person or car covers most of the frame.
- Look at `top.jpg` and `top_area.jpg` yourself: each panorama is rendered at its best direction.
- Views are rendered at 65° every 45°; the photo's own field of view does not need to match.
- Not the right town after a full sweep? The next town on the list, not a denser sample of the same one.

## 5. Verify across years (old photos, old imagery)

The photo and the reference can be decades apart. Things that survive: street axes and widths, junction
angles, block and plot divisions, the position of building corners, the rhythm of openings on old
façades, slab/corbel/balcony patterns of the original structure, terrain and skyline, minarets, water
towers, big trees that were already big. Things that change: added storeys, render and paint, shop
fronts, signs, shutters, young trees (grow or vanish), new buildings on empty lots, paving.

- Reproduce the view: `sweep.py view` searches direction, field of view and pitch and writes a
  side-by-side; then compare the structures one by one, writing which match, which changed plausibly
  (a floor added, a lot built on) and which contradict.
- The camera of an old photo is rarely at the panorama: expect offsets of 5–30 m; neighbouring panoramas
  (`pano.py sheet --manifest … --near <lat,lon> --radius 40 --toward <target>`) show the same corner from
  other points.
- Do not use local-feature inlier counts (`match.py --refine sift`) to accept or reject across decades;
  they are noise there (measured above). Use them only for same-era imagery.
- A sweep winner that also heads a cluster, whose reproduced view matches ≥3 invariant structures, with no
  contradiction, is a street-level answer (medium; high with a second independent constraint such as the
  sun, a sight line, or the owner's confirmation). Write the changes you accepted in the report.

## 6. When the answer becomes known

Record it (`photo_session.py truth …`) and, if a provider or source was decisive, add it to this file and
to the matching `references/world/*.md` country notes, so the next agent looks there first.
