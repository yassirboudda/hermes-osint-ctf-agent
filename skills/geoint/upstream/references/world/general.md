# Discriminators that work everywhere

Scope: clues that split the world before you know the region. Country-specific detail lives in the regional
files. Entry format and rules: `README.md`. Items marked "(verify)" are worth a quick web check or a
`refsheet.py` comparison before you lean on them.

## Quick table

| Clue | First split it gives | Tool |
|---|---|---|
| Driving side | ~70 left-hand vs ~170 right-hand territories | `board.py apply --kind driving-side --value left` |
| Script and diacritics | language → a few countries | `textgeo.py` |
| Plate shape/colour | continent → country group | regional files, `refsheet.py` |
| Centre-line colour | the Americas (yellow) vs most of the rest (white) | regional files |
| Warning-sign shape | yellow diamonds vs red-bordered triangles | regional files |
| Sun / shadows / dishes | hemisphere and latitude band | `sun.py`, `sky.md` |
| Biome and soil | climate zone | your eye, satellite |
| Street View car/camera | covered countries, generation | `streetview.md` |

## Sun, shadows, satellite dishes

### Where the sun is at midday
- Look for: the sun's side of the sky, the direction of shadows of vertical objects, which facades are lit around midday.
- Points to: north of the Tropic of Cancer the noon sun is due south; south of the Tropic of Capricorn it is due north; between the tropics it can be either side depending on the date.
- Strength: strong for the hemisphere once you know the camera heading and that it is near midday; medium otherwise.
- Counterexamples: morning/evening sun is far east/west, not south/north; a mirrored image flips everything; reflections from glass towers mimic sunlight.
- Verify: `sun.py locate/facing/compass` with whatever time information exists (EXIF, shop hours, shadows); `sky.md`.
- Source: general knowledge (solar geometry).

### Satellite TV dishes
- Look for: the direction and the elevation of household dishes on many buildings.
- Points to: dishes aim at geostationary satellites over the equator, so they face roughly south in the northern hemisphere and roughly north in the southern; they tilt up steeply near the equator and lie lower toward the poles. A whole street aiming the same way gives the equator's direction.
- Strength: medium (strong for the hemisphere when many dishes agree).
- Counterexamples: dishes aimed at different satellites differ by tens of degrees in azimuth; offset-feed dishes look more upright than their real elevation angle.
- Verify: `sun.py dish` (`sky.md` §5).
- Source: general knowledge (orbital geometry).

## Traffic and roads

### Driving side
- Look for: which side moving traffic keeps to, the side parked cars face, the steering-wheel side of vehicles, which side of the road signs stand on, bus doors.
- Points to: left-hand traffic in the UK, Ireland, Malta, Cyprus, Japan, India, Pakistan, Bangladesh, Sri Lanka, Nepal, Bhutan, Thailand, Malaysia, Singapore, Indonesia, Brunei, Timor-Leste, Hong Kong, Macau, Australia, New Zealand, most of southern and eastern Africa (South Africa, Lesotho, Eswatini, Botswana, Namibia, Zimbabwe, Zambia, Malawi, Mozambique, Tanzania, Kenya, Uganda), Mauritius, Seychelles, Suriname, Guyana and many Caribbean islands; right-hand traffic almost everywhere else.
- Strength: strong (one clue removes a large part of the world).
- Counterexamples: mirrored images (check text); imported left-hand-drive cars in some LHT countries and vice versa; one-way streets; Gibraltar drives on the right while the UK drives on the left; mainland China drives on the right while Hong Kong and Macau drive on the left.
- Verify: `clues.py lookup driving-side left`, then `board.py apply --kind driving-side --value left`.
- Source: data/driving_side.json (Wikipedia, curated).

### Centre and edge line colours
- Look for: the colour of the line separating opposite directions, and of edge lines.
- Points to: yellow centre lines are standard in the United States, Canada and Mexico and widespread in Latin America; most of Europe, Africa, the Middle East and Oceania use white. Notable non-American yellow uses: Norway and Finland (lines separating opposite traffic), South Korea (centre lines), Japan (yellow centre lines mark no-overtaking sections), New Zealand (yellow no-overtaking lines), yellow edge lines in South Africa and Ireland.
- Strength: medium (strong in combination with plates/signs).
- Counterexamples: temporary roadworks lines are yellow in several European countries; some Latin American roads use white centre lines (see `americas.md`); faded paint changes apparent colour; parking-restriction kerb lines are not centre lines.
- Verify: `refsheet.py countries <A,B> --pitch -12` to see current paint; web search "<country> road markings".
- Source: general knowledge (verify per country).

### Kerb lines for parking rules
- Look for: single or double yellow lines along the kerb; painted kerbs (yellow, red-white, black-white).
- Points to: double yellow kerb lines are the UK/Irish parking restriction; painted kerbs are common in Spain (yellow), Latin America, South Africa, Southeast Asia, Israel and Australia, each with its own colours.
- Strength: weak to medium.
- Counterexamples: kerb paint conventions repeat across many countries.
- Verify: regional files; `refsheet.py … --pitch -15`.
- Source: general knowledge.

### Warning signs and stop signs
- Look for: the shape and background of warning signs; the word on the octagonal stop sign.
- Points to: yellow diamond warning signs (the US-style family) in the Americas, Australia, New Zealand, Ireland, Japan, Thailand, Malaysia, Indonesia and some others; red-bordered triangles (Vienna-convention family) across Europe, most of Asia, Africa and the Middle East, with a yellow background in Sweden, Finland, Norway, Iceland, Poland and Greece (verify for others). Stop-sign word: STOP in most countries; PARE in Brazil and much of South America and the Spanish Caribbean; ALTO in Mexico and Central America; ARRÊT in Quebec; 止まれ on an inverted red triangle in Japan; 정지 in Korea; หยุด in Thailand; قف in Arab countries; ایست in Iran.
- Strength: strong for the family, medium for the country.
- Counterexamples: imported or old signs; bilingual stop signs; Ireland's yellow diamonds vs the UK's triangles is a key UK/IE split.
- Verify: regional files; web search "<country> warning signs".
- Source: general knowledge (verify country lists).

## Plates

### Plate shape and the EU band
- Look for: the plate's proportions and colours, even when the characters are unreadable.
- Points to: long narrow plates → Europe (a blue band with stars and a country code on the left → an EU member, plus Norway-style national bands); about 2:1 plates → North America, also much of Latin America and Asia; small near-square plates with Japanese script → Japan; white plates with a blue top band → Mercosur format (Argentina, Brazil, Uruguay, Paraguay).
- Strength: medium (strong with colours).
- Counterexamples: square plates on some European cars and most motorbikes; foreign cars near borders and on freight corridors; overexposure whitens colours.
- Verify: regional files; zoom the crop from `detect.py`.
- Source: general knowledge.

### Plate colours
- Look for: background colours front and rear.
- Points to: yellow front and rear → the Netherlands, Luxembourg, Israel, Colombia (private cars), (verify others); white front + yellow rear → United Kingdom, Cyprus, Kenya; black plates with white characters → Malaysia (and older plates in several Asian countries); Japanese kei cars → yellow; India → white private, yellow commercial, green electric.
- Strength: medium to strong.
- Counterexamples: commercial, diplomatic, temporary and old-format plates differ from private ones; formats change (Indonesia moved from black to white plates from 2022).
- Verify: web search "<country> license plate colours", regional files.
- Source: general knowledge (verify).

### Plate background and graphics in countries that issue plates by state/province
- Look for: when the characters can't be read: the plate's overall background colour, colour bands, central graphic (state or provincial flag), border colour.
- Points to: state/province level (US, Mexico, Canada, Brazil's old format, Australia, etc.).
- Strength: medium (filter to a few states against a chart of state plate designs; narrows by an order of magnitude in one step).
- Counterexamples: out-of-state vehicles crossing state lines (especially common on freight corridors and in border cities); old and new formats coexist, and reference charts go out of date; overexposure in strong light renders light-coloured graphics as white.
- Verify: web search a current plate chart for the candidate states.
- Source: v002 v009

## Text, brands and buses

### Official bilingual or multilingual signs
- Look for: two languages with the same content on one official traffic sign or street-name sign.
- Points to: an officially multilingual admin area, not "near a country that speaks that language" (e.g., German–Italian bilingual signs in Italy → South Tyrol; Swedish–Finnish → coastal Finland; Welsh–English → Wales; Catalan/Basque/Galician–Spanish → those Spanish regions; Tifinagh–Arabic–French → Morocco).
- Strength: strong.
- Counterexamples: bilingual private shop signs don't count; foreign-language signs added for tourists don't count.
- Verify: `textgeo.py --text`, web search the place names.
- Source: v001, general knowledge

### Sub-brands and business lines of chain brands
- Look for: small marks on the sign besides the parent brand (truck tyre retreading, commercial-vehicle service, etc.).
- Points to: sub-brands have far fewer stores, so listing all their stores gives a candidate point list; also suggests a freight corridor or an industrial outskirt.
- Strength: weak alone; medium together with a store search.
- Counterexamples: store data on maps is incomplete; store locators can be several km off.
- Verify: `textgeo.py` (where the brand operates), opening press releases, `osm.py along` + street-level sampling (`search.md`).
- Source: v002

### Ads for regional consumer goods
- Look for: drink, snack, telecom and bank brand ads on vehicles, kiosks and walls.
- Points to: the country or region where the brand mainly sells (telecom operators and banks are usually national).
- Strength: weak for consumer goods, medium for telecoms/banks.
- Counterexamples: multinational brands, imported brands, cross-border advertising.
- Verify: `textgeo.py` brand lookup, web search.
- Source: v007

### Bus operator abbreviation + route number
- Look for: the operator name and route number at the top of the bus front and rear.
- Points to: city; route number → `osm.py route` gives the corridor to search along.
- Strength: strong to the city; with a route map, to one line.
- Counterexamples: second-hand imported buses keep their original livery and text; route numbers change.
- Verify: web search "<operator> <route>", `osm.py route`.
- Source: v007

### Numbered road shields
- Look for: route numbers in shields or panels (US Interstate red-white-blue shields, European E-road green panels, national road-number formats).
- Points to: one specific road; add an exit number, kilometre marker or skyline landmark to fix the segment and direction.
- Strength: strong (to one road).
- Counterexamples: the same number exists in several states/countries; the sign can be tiny and easy to miss.
- Verify: `osm.py route --ref <number>`; web search.
- Source: v010-4

## Nature

### Eucalyptus
- Look for: tall smooth-barked trees with peeling bark and sparse grey-green crowns, often in plantations.
- Points to: native to Australia, but planted on a large scale in Portugal, Galicia (Spain), Brazil, Uruguay, Argentina, Chile, South Africa, Ethiopia, Kenya, India, southern China and California.
- Strength: weak (it widens rather than narrows outside Australia).
- Counterexamples: everywhere listed above.
- Verify: combine with soil, roads, plates.
- Source: general knowledge.

### Red laterite soil
- Look for: deep red/orange bare soil on verges, tracks and building sites.
- Points to: tropical and subtropical weathered soils: much of sub-Saharan Africa, Brazil and Paraguay, parts of India and Southeast Asia, northern and inland Australia.
- Strength: weak to medium.
- Counterexamples: red soils also occur in the Mediterranean (terra rossa) and in the US South.
- Verify: satellite colour of fields around candidates (`tiles.py fetch --zoom 13`).
- Source: general knowledge.

### Biome signatures
- Look for: birch and spruce (boreal: Nordics, Baltics, Russia, Canada); cork and olive groves (Mediterranean); rice paddies (monsoon Asia, but also Italy's Po valley, Arkansas/California, southern Brazil); cacti and agave (Mexico, the US Southwest, Andes, dry Brazil, also planted in the Mediterranean); acacia savanna (East/Southern Africa, also parts of Australia); dense bamboo (East/Southeast Asia).
- Points to: climate zone, then the candidates within it.
- Strength: weak alone; strong for excluding whole climates.
- Counterexamples: planted ornamentals (palms on Mediterranean promenades, eucalyptus everywhere); altitude changes vegetation within one country.
- Verify: phenology must be paired with the month; satellite land cover around candidates.
- Source: general knowledge.

## Infrastructure

### Uniform streetlight and pole designs within an area
- Look for: streetlight pole colour, lamp head shape, pole material (wood, concrete, steel), cross-arms, insulators, transformer placement.
- Points to: utilities and municipalities procure uniform designs; neighbours often differ.
- Strength: weak for finding, medium for separating two candidates.
- Counterexamples: one manufacturer sells to many places; old and new designs coexist.
- Verify: `refsheet.py countries <A,B> --side right` or `regions …`.
- Source: v001 v009

### Arched cross-arms on the French distribution grid (inherited standards)
- Look for: a cross-arm arching upward on top of a concrete or metal pole, three conductors hanging from suspension insulators; identical poles lined up into the distance.
- Points to: the French grid system: metropolitan France and the overseas departments that keep its standards; some former colonies have similar pole types. In general, a recognised national standard points to the home country + territories that keep its standards + some former colonies.
- Strength: medium.
- Counterexamples: neighbouring countries' border areas; former colonies that changed pole types; small distant arms look arched when they are not — zoom.
- Verify: `refsheet.py countries FR,<candidate>`; `clues.py lookup territories France`.
- Source: v013

### Stobie poles
- Look for: utility poles made of two steel I-beams with concrete filling between them.
- Points to: South Australia (Adelaide area), where they are standard; rarer elsewhere in Australia.
- Strength: strong for South Australia.
- Counterexamples: few; similar-looking concrete poles exist elsewhere.
- Verify: `refsheet.py regions "AU:South Australia,AU:Victoria"`.
- Source: general knowledge.

## Case-derived country entries (from earlier puzzles)

These came from specific solved cases; the regional files have the full country picture.

### Roof colour: red terracotta vs grey pitched roofs (northern Italy)
- Look for: the colour of roofs across an area in distant views or satellite imagery.
- Points to: Italian-speaking areas are mostly red terracotta; many grey or dark pitched roofs → the German-speaking cultural area (Austria, Germany, South Tyrol).
- Strength: weak (meaningful only as a statistic over a whole area).
- Counterexamples: new apartment blocks often use flat or grey metal roofs.
- Verify: satellite mosaics of candidate towns.
- Source: v001

### Arch form: round or pointed
- Look for: whether door and window arches are round or pointed; biforate windows.
- Points to: round → Romanesque or Renaissance; pointed → Gothic. A city with few medieval remains but an "intact medieval courtyard" → think replicas (exhibition pavilions, mock-historic streets, film sets).
- Strength: weak (narrows building type and search terms).
- Counterexamples: replicas are common.
- Verify: web search with style words only after checking the form.
- Source: v004

### British Columbia, Canada plates and Vancouver residential streets
- Look for: blue characters on white with a small provincial flag in the middle; residential streets with dark green streetlight poles and curved arms, grass strips between sidewalk and roadway.
- Points to: British Columbia; Metro Vancouver residential areas.
- Strength: strong for the plate (format and flag both visible); weak for the street style.
- Counterexamples: out-of-province cars; the US Northwest looks similar.
- Verify: `refsheet.py regions "CA:British Columbia,US:Washington"`.
- Source: v009

### Mexico: plate background by state; tall tubular steel transmission poles
- Look for: the rear plate's background colour and graphic placement; gray single tubular steel poles with three tiers of curved cross-arms along roads.
- Points to: state level for the plate (near-white plates were Mexico City and Nuevo León in the reference chart used); a high-voltage corridor for the poles (check which roads such lines follow).
- Strength: medium (single source) for plates; weak for poles.
- Counterexamples: other states' vehicles, federal plates, design changes, overexposure.
- Verify: a current Mexican state plate chart; OpenInfraMap.
- Source: v002

### Japan: railway company names, telephone area codes, sign authorities, four-track crossings
- Look for: company names on level-crossing signs; TEL numbers (the first digit after 0 runs north→south: 01 Hokkaido … 09 Kyushu/Okinawa); "〇〇警察署 / 〇〇土木事務所 / 〇〇区役所" at the bottom of signs; four parallel tracks at a level crossing.
- Points to: operating area / city / ward; a quadruple-track section of a trunk line.
- Strength: medium.
- Counterexamples: company boundaries; non-geographic numbers (0120, 0570, 050, 080, 090); station throats also show four tracks.
- Verify: `textgeo.py --text "<number>"`; `osm.py crossings --kind level_crossing`.
- Source: v003

### Myanmar plates
- Look for: a Latin-letter region code on the plate (e.g., YGN) plus a number.
- Points to: Myanmar; YGN = Yangon Region.
- Strength: medium (single source).
- Counterexamples: vehicles from other regions; old plates in Burmese script.
- Verify: web search the code.
- Source: v007
