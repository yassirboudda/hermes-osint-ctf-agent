# Lookup data

`clues.py lookup` reads the JSON in this directory. Each file's `_meta` records the source URL, fetch date, and entry count; `clues.py update` refetches from `_meta.source`.

| File | Content | Source | Fetched | Entries | License |
|---|---|---|---|---|---|
| `cn_plates.json` | Province prefixes of PRC civilian motor vehicle plates | [zh.wikipedia.org/zh-cn/中华人民共和国民用机动车号牌](https://zh.wikipedia.org/zh-cn/中华人民共和国民用机动车号牌) | 2026-09-14 | 31 | Derived from Wikipedia, CC BY-SA 4.0 |
| `cn_area_codes.json` | Mainland China landline area codes | [zh.wikipedia.org/zh-cn/中国大陆固定电话号码](https://zh.wikipedia.org/zh-cn/中国大陆固定电话号码) | 2026-09-14 | 349 | Derived from Wikipedia, CC BY-SA 4.0 |
| `calling_codes.json` | Country calling codes for countries and regions | [en.wikipedia.org/wiki/List_of_telephone_country_codes](https://en.wikipedia.org/wiki/List_of_telephone_country_codes) | 2026-09-14 | 281 | Derived from Wikipedia, CC BY-SA 4.0 |
| `driving_side.json` | Driving side by country | [en.wikipedia.org/wiki/Left-_and_right-hand_traffic](https://en.wikipedia.org/wiki/Left-_and_right-hand_traffic) | 2026-09-14 | 236 | Derived from Wikipedia, CC BY-SA 4.0 |
| `territories.json` | Overseas territories and dependencies | [en.wikipedia.org/wiki/List_of_dependent_territories](https://en.wikipedia.org/wiki/List_of_dependent_territories) | 2026-09-14 | 60 | Derived from Wikipedia, CC BY-SA 4.0 |
| `cn_admin.json` | China admin division codes at three levels (province, city, county) | [modood/Administrative-divisions-of-China](https://github.com/modood/Administrative-divisions-of-China) `dist/pca-code.json` | 2026-09-14 | 3420 | WTFPL |
| `country_names.json` | Chinese–English country and region name mapping, with aliases | Hand-compiled | 2026-09-14 | 300 | MIT (with this repository) |
| `countries.json` | 250 countries/territories: ISO codes, names, capital, continent, TLD, currency, phone prefix, postal format/regex, languages, neighbours, driving side, population-weighted centre and extent | [GeoNames countryInfo.txt](https://download.geonames.org/export/dump/countryInfo.txt) + `driving_side.json` + GeoNames cities500 | 2026-10-08 | 250 | CC BY 4.0 (GeoNames) |
| `text_signals.json` | Scripts → countries, digits, telltale letters → languages, simplified/traditional/Japanese kanji forms, currency marks, vanity TLDs, regional signage words | Hand-compiled from Unicode properties and national orthographies | 2026-10-08 | ~560 entries | MIT (with this repository) |
| `streetview_coverage.json` | Countries/territories with official Google Street View road coverage, partial coverage, and notable gaps | `references/world/streetview.md` §3 (Wikipedia "Coverage of Google Street View" + launch news) | 2026-10-08 | 181 | MIT (with this repository) |

Notes:

- The five Wikipedia-sourced tables are factual data scraped and compiled from the tables in the corresponding articles. Wikipedia text is licensed under CC BY-SA 4.0; these five tables are released under the same license, with attribution to Wikipedia and its editors.
- The `letter_notes_unverified` block under the `渝` (Chongqing) entry in `cn_plates.json` (municipality plate letter zones) does not come from Wikipedia; it comes from a general-knowledge table and is unverified. `clues.py` marks it unverified in its output.
- `countries.json` is rebuilt with `geodata.py build-countries`; `driving_side.json` rows marked `curated` were corrected by hand (the scrape had marked mainland China as left-hand traffic).
- `country_names.json` is a hand-compiled mapping table; the keys of `en2zh` match the English spellings used in the other tables, and `aliases` maps short names, traditional-character names, former names, and English abbreviations to `en2zh` keys.
- This directory contains no OpenStreetMap data; `gazetteer.py` and `osm.py` query Overpass live.

Source names and quoted source notes stay in their original language. Maintained annotations (including curated driving-side notes and unverified municipality hints) are in English; the agent explains source evidence in the user's language.
