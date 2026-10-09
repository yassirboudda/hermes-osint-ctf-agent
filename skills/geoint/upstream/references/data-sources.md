# Scripts, data sources and coordinate systems

## Script overview (`scripts/`)

| Script | What it does |
|---|--- |
| `doctor.py` | Environment checks, browser launch, optional endpoint probes; English fixes and JSON output |
| `exif.py` | GPS, capture time, equivalent focal length, camera heading |
| `imgprep.py` | zoom (enlarge to read text) / edges (four edges, four corners) / variants (image-search variants) / grid (split into tiles) / `piers` (brightness profile along a given row to find pixel columns of evenly spaced structures; outputs a check image) |
| `revimg.py` | Baidu image search + Yandex reverse image search; `--query` Chinese keyword search (Bing China, Baidu/Sogou Images) |
| `geo.py` | Coordinate conversion, bearing and distance, camera geometry (`range --hfov a:b` distance range), `line` alignment line, `intersect` sight-line intersection, `frame` computes the frame and occlusion before excluding, `spacing` pixel columns of evenly spaced structures × known polyline → solve for camera position (optionally scored jointly with the skyline) |
| `poi.py` | Place names, residential compound names, housing development names, shop names → candidate coordinates (360 Maps + OSM Nominatim + Baidu suggestions); lists every same-name point nationwide |
| `sun.py` | Sun position, shadow-length ratio, `locate` location band, `when` time, `street` street orientation, `facing` heading from lit faces, `dish` satellite dish |
| `osm.py` | Overpass: find / near (co-occurrence) / crossings (line-to-point) / route (route corridor) / intersect (crossings of two kinds of lines; bends are only labeled, `--rank-near` ranks) / street-scan (street-view geometry template) / geom (export geometry) |
| `tiles.py` | Satellite/map tile mosaic (Google satellite / hybrid / map, Esri imagery / street, Bing aerial, Esri Wayback releases since 2014, EOX Sentinel-2 by year), `mark` plots points + overlays GeoJSON lines + field-of-view wedge, `sheet` numbered thumbnails of candidate points (town-fabric comparisons), `wayback` every archived look of a point |
| `baidu_pano.py` | Baidu panoramas: near / info / scan / render / sheet (`--headings` to look around from one point, `--road` `--spread`) / sample (street view sampling of candidate cities) |
| `gsv.py` | Google Street View (outside China): near / render / sheet, no key, official coverage only |
| `pano.py` | Street-level imagery from every scriptable provider in one manifest format (Google, Apple Look Around, Bing Streetside, Yandex, Naver, Kakao, Mapy, Já.is, KartaView, Panoramax, Mapillary with a token) plus manifests you write for sources you find: coverage / list / render / sheet — see `streetlevel.md` |
| `sweep.py` | Index every panorama of one or more towns (MegaLoc descriptors, cached) and rank them for a photo; clusters of top hits; `view` reproduces the photo's view |
| `pose.py` | Solve camera position from multiple points: lat/lon, height, heading, pitch, roll, field of view + error radius + per-point check; `check` scores discrete candidate camera positions; `project` projects map points back onto the photo |
| `terrain.py` | Elevation: view (synthesized mountain view; `--overlay` overlays the skyline on the photo, `--roll`) / profile (skyline) / elev / `ridge` reads ridgeline pixel points from the photo / `scan` filters a whole region along infrastructure lines for "flat nearby + mountain present" points and clusters them / `fit` batch skyline scoring of candidate camera positions (optional infrastructure-distance constraint; outputs overlays of the top N) |
| `evidence.py` | Evidence image: satellite image + camera-position wedge + comparison panels |
| `intake.py` | Metadata, edge crops, variants, OCR and Baidu/Yandex reverse image search on the original and variants in one command (recon.py runs it; `--no-rev` skips the reverse search); outputs intake.md (tiered vote count, possible place names) |
| `ocr.py` | Reads text in the photo (Apple Vision, falls back to RapidOCR): full image + zoomed + tiles, merged; text read only after zooming is marked in `pass` |
| `clues.py` | Lookup tables: license plate prefixes, landline area codes, country calling codes, driving side, overseas territories, admin hierarchy; tables are in `data/`, `update` re-fetches them |
| `board.py` | Candidate board: candidates, clues, evidence likelihood ratios, exclusions (require a computed file), ranking, scan cost, next step, pre-conclusion check, generates result.json fields |
| `gazetteer.py` | Admin-division gazetteer: lists all subdivisions (with bbox), built-up area extents, scan pages |
| `sat_scan.py` | CLIP zero-shot scoring and ranking of satellite grid cells/candidate points (sports fields, factory buildings, silos, dams…), top-N thumbnails + heatmap |
| `match.py` | Ranks the photo against candidate ground-level images: MegaLoc (default) / DINOv2 / CLIP global similarity + SIFT inlier re-ranking (same-era imagery only); candidates can be rendered on the fly from panorama ids |
| `geo.py bearings` | Camera position → bearing, angular width and distance of each outline in a GeoJSON; use with `sun.py compass` to compute the bearing first, then identify the structure |
| `recon.py` | The local first pass in one command: meta + intake (no reverse search) + textgeo + detect + calib + prior → recon.md |
| `meta.py` | exiftool-based metadata: GPS (EXIF/XMP/video/DJI), UTC offset → countries on that date, filename/platform hints, embedded previews, provenance/AI flags |
| `textgeo.py` | Text → scripts, distinctive letters, language (lingua), phones (libphonenumber), domains, postal formats, currency, regional words, brands (name-suggestion-index), place names (GeoNames) |
| `geodata.py` | Country facts (`data/countries.json`), GeoNames places: search, reverse geocode, population-weighted sampling, the biggest towns of a region or radius (`towns`), national gazetteers |
| `prior.py` | StreetCLIP + GeoCLIP world prior on several crops, region ranking, consistent point guess, self-assessment |
| `detect.py` | OWLv2 open-vocabulary detection → numbered crops of signs, plates, poles, bollards, markings, vehicles |
| `calib.py` | GeoCalib: FOV, focal, pitch, roll, horizon line with uncertainties |
| `refsheet.py` | Street View sample rows per candidate country/region (side by side) |
| `bench.py` | Street View test sets with hidden truth, model-only baseline, scoring of predictions and sessions |
| `photo_session.py` | Per-photo archive: start, finish, truth (scoring), scoreboard, list |

## Coordinate systems (must be kept apart in China)

| Code | Name | Who uses it |
|---|---|---|
| wgs | WGS84 | GPS, photo EXIF, Google satellite imagery, OpenStreetMap, elevation tiles |
| gcj | GCJ-02 | Amap (Gaode), Tencent, 360 Maps, Google's China road maps, **Google Earth's Chinese label layer in China** |
| bd | BD-09 | Baidu Maps lat/lon |
| bdmc | Baidu Mercator | `@x,y` in Baidu Maps URLs, the Baidu panorama API |

In China the same point differs by several hundred meters between WGS84 and GCJ-02. Conversion: `scripts/geo.py convert --from X --to Y a b`.
- Amap links use gcj: `https://uri.amap.com/marker?position=<lon>,<lat>`; Google links use wgs.
- **Google Earth in China: the imagery is WGS84, the Chinese place-name labels are GCJ-02, and the two are offset by several hundred meters** (v005: a dock's Chinese label landed on the river surface). Place points and read coordinates from the imagery.
- For coordinates read from Chinese map apps or websites, confirm the coordinate system before using them.

## Satellite imagery

| Source | Notes |
|---|---|
| Google satellite tiles | `mt1.google.com/vt/lyrs=s`, WGS84, sharp in China. `tiles.py` default |
| Esri World Imagery | Backup; older in some parts of China; has the Wayback historical archive |
| Google Earth desktop | Historical imagery timeline, tilted 3D (manual use); 3D models in China are old, newly built supertall buildings are often missing |

- The same place at different zoom levels may be imagery from different years and different tilt angles.
- Zoom 17 is about 1.1 m/pixel, for areas; zoom 19 is about 0.28 m/pixel, for single buildings; zoom 7–9 as the base map for `sun.py locate --mosaic`.

## Street view and ground-level imagery

### Baidu panoramas (main source in China)

The endpoints are all at `https://mapsv0.bdimg.com/`, need no key, and must be accessed directly:

| Purpose | Parameters |
|---|---|
| Nearest panorama to a point | `?qt=qsdata&x=<bdmc x>&y=<bdmc y>` |
| Panorama info (date, location, all points along the road, historical versions) | `?qt=sdata&sid=<panoid>` |
| Render a perspective view by heading | `?qt=pr3d&panoid=<id>&heading=<compass angle>&pitch=<pitch>&fovy=<vertical FOV>&width=<≤1024>&height=<>` |

- heading is a compass bearing, 0 = due north, clockwise; a width over 1024 returns 404.
- Covers urban arterial roads and many roads inside industrial zones; almost nothing inside residential compounds. Captures are mostly from 2017–2019, so new buildings aren't visible.
- Place search on map.baidu.com triggers a captcha; don't try to get around it; use `poi.py` for place names.

### Other

| Source | Use | Known issues |
|---|---|---|
| Google Street View | Street view outside China, with historical dates; `gsv.py`, `refsheet.py` | Almost none in China. The old `GeoPhotoService.SingleImageSearch` endpoint answers "decommissioned" and the `streetviewpixels` thumbnail endpoint returns 403 to anonymous callers (checked 2026-10); discovery now uses Maps coverage tiles (`photometa/ac/v1`, zoom 17) and `photometa/v1` metadata via the `streetlevel` package, and views are rendered locally from the equirectangular panorama. User-uploaded photospheres are skipped |
| Apple Look Around, Yandex, Naver, Kakao, Bing Streetside, Mapy.cz, Ja.is | Other street-level providers (better than Google in Korea, parts of Russia/Turkey/Czechia/Iceland, many US/European cities for Apple) | Not wired into scripts yet; the `streetlevel` package supports them (see the project ROADMAP) |
| Mapillary, KartaView | Crowdsourced street view, rural roads outside China | Almost none in China |
| Tencent Street View | Backup in China | API not yet investigated |
| Map POI photos, hotel/scenic-area photos online, tourist photos | Compare skylines and building shapes when there's no street view | Shooting angle can't be controlled |

## Search

| Source | Good at | How to use |
|---|---|---|
| Baidu image search | Chinese web pages, Weibo, Baijiahao, e-commerce, scenic areas; gives "图中可能是…" ("the image may show…") | `revimg.py` |
| Yandex Images | Buildings, street view, foreign content; gives tags and source sites | `revimg.py` |
| Google Lens | Recognizing "what this is" (species, car models, statues, attractions), often stronger than Baidu and Yandex | Requests from a server's egress IP get challenged for verification; when you have a browser-control tool, use it in the user's browser; the AI Overview will confidently report a place name based on similar images |
| Bing China, Baidu Images, Sogou Images | Chinese-keyword web and image search | `revimg.py --query`; Baidu web search pops up a verification challenge, not used |
| Douyin, Xiaohongshu, Weibo | Influencer check-in spots, scenic areas' official accounts, same-city content | Web search or user assistance |
| Development photo albums on real-estate sites (Anjuke, Fang.com, Loupan.com, etc.) | New housing developments, commercial complexes; albums include signboards | Web search the development name |
| Travel review sites (Tripadvisor, Ctrip) | User photos of statues, parks, attractions | Web search |
| Stock photo libraries (VCG, Getty, Alamy) | Captions carry exact place names and dates | Web search |
| Local government and local media websites | Check the names and sizes of scenic areas, towers, statues | Web search |

## Place name → coordinates (China)

| Source | Notes |
|---|---|
| 360 Maps search `restapi.map.so.com/newapi` | No key; good coverage of residential compounds, housing developments, shops and organizations, with address and district; coordinates are GCJ-02 (`poi.py` already converts to WGS84); without a city it returns a list of cities nationwide that have same-name results |
| OpenStreetMap Nominatim | Named residential compounds, parks, roads; WGS84 |
| Baidu Maps search suggestions `map.baidu.com/su` | No key; only "city + district + name", no coordinates |
| Baidu Maps place search, Tencent and Amap APIs | Baidu needs a captcha, Tencent and Amap need keys; not used |

## Place name → coordinates (outside China)

- `poi.py "<address or place name>" --sources osm --country <two-letter country code>` (Nominatim, WGS84). When a street address isn't found, drop the house number and search only the street + district name.

## Ground photos (when there's no street view)

| Source | Notes |
|---|---|
| Images from news, encyclopedias, company websites, blogs | First find a name for the facility (OSM name, nearby place name + the local-language word for the facility type), then search; rural factory buildings and abandoned facilities often have only this kind of ground photo |
| Wikimedia Commons search by coordinates | `commons.wikimedia.org/w/api.php?action=query&list=geosearch&gscoord=<lat>|<lon>&gsradius=10000&gsnamespace=6&format=json`, no key; remote areas often have only a few |
| Mapillary | Wide crowd-sourced coverage; `pano.py --provider mapillary` with a free client token (`MAPILLARY_TOKEN`), otherwise the web app in the browser |
| KartaView, Panoramax | `pano.py --provider kartaview|panoramax`, no key; patchy (Panoramax strongest in France) |
| Local and historical panorama sites | Found by web search in the local languages (`streetlevel.md` §1), turned into a manifest and swept. One example of the kind of site to look for: carte.ma (Morocco, 2013–2015 city panoramas) |

## Thematic maps and structured data

| Source | Use | Known issues |
|---|---|---|
| OpenStreetMap Overpass | Feature co-occurrence, line-to-point, route corridors, line crossings, street-view templates, points along a road, large buildings | `osm.py`; public servers are often busy or rate-limited (the script retries on mirrors; a result with a remark gets a warning that it may be incomplete); **ranges of hundreds of kilometers with a name regex (`[~"name"~...]`) often time out**; drop the regex or query by sub-area; in Chinese counties and townships, buildings and parking are basically empty, and rivers often have only centerlines |
| OpenRailwayMap (openrailwaymap.org) | Railway class, single/double track, electrification, stations | Viewed manually on the web; same data as OSM |
| OpenInfraMap (openinframap.org) | Power lines and voltage, substations | Viewed manually on the web; voltage may be untagged |
| AWS Terrain Tiles (Terrarium) | Global elevation, about 30 m | `terrain.py`; details smaller than a hundred meters are unreliable |
| City open data | Street trees (species, trunk diameter at breast height, location), etc. | Many foreign cities, few Chinese ones |

## Offline reference data (downloaded once into ~/.cache/geoint)

| Source | Use | Licence |
|---|---|---|
| GeoNames `countryInfo.txt` (bundled as `data/countries.json`) | names, ISO codes, TLDs, phone prefixes, postal formats, languages, neighbours | CC BY 4.0 |
| GeoNames `admin1CodesASCII.txt`, `cities500.zip`, `<CC>.zip` | region names; 236k populated places with alternate names; full national gazetteers on demand | CC BY 4.0 |
| OpenStreetMap name-suggestion-index (`nsi.min.json` via jsDelivr) | ~50k brands and the countries/regions where they operate | BSD-3 / data ODbL-compatible |
| libphonenumber (`phonenumbers`) | phone number → country, region/city for many landlines, carrier | Apache-2.0 |
| lingua | offline language identification for short text | Apache-2.0 |
| Hugging Face / GitHub model weights | StreetCLIP, CLIP ViT-L/14 (GeoCLIP), OWLv2, GeoCalib, DINOv2, CLIP B/32 | see `models.md` |

## Time and weather

| Source | Use |
|---|---|
| `sun.py` (NOAA algorithm, within ≤0.02° of NREL SPA) | Sun position; replaces SunCalc |
| Historical daily weather (temperature, sun/rain) | Check "frozen", "sunny"; with a date, exclude overcast or rainy areas |
| Historical weather-satellite cloud imagery | Exclude large cloud areas on that day (clearly effective only with typhoons and fronts) |
| Flightradar24, FlightAware | Flight history by registration; the paid tier can download KML/CSV tracks |
