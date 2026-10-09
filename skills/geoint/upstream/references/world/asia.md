# Asia clues: East, Southeast, South and Central Asia

Scope: Japan, Korea, Taiwan, Hong Kong, Macau, Mongolia, Southeast Asia, South Asia (India to state level) and Central Asia. Mainland China has its own file (`china.md`, pointer below); Russia is in `europe.md` (Siberia note near the end).
Plate formats and paint colours were checked 2026-10 where a source is named. Old plates and old paint stay on the road for years, so every "changed in year X" fact is also a dating clue.

## Quick table

| Country (ISO2) | Drive | Plates, quick look | Road paint (centre / edge) | Script / language | Other strong tells |
|---|---|---|---|---|---|
| Japan (JP) | L | kanji area + 3 digits over kana + 4 digits; white (private), yellow (kei), green (commercial) | white, yellow = no overtaking / white | kanji + hiragana + katakana | inverted-triangle 止まれ stop sign; mirrors on orange poles |
| South Korea (KR) | R | white 123가 4567; yellow commercial with region name; light-blue EV | yellow / white | Hangul | big block numbers on apartment towers; yellow kerb lines |
| Taiwan (TW) | R | white ABC-1234, no place name | yellow / white; red and yellow kerb lines | Traditional Chinese | scooter waiting boxes; betel-nut kiosks |
| Hong Kong (HK) | L | white front, yellow rear, AB 1234 | white (UK style); yellow kerb = no stopping | Traditional Chinese + English | red/green/blue taxis; trams, double-deckers |
| Macau (MO) | L | black, white characters, AB-12-34 | (unverified) | Traditional Chinese + Portuguese | blue-white tiled street signs |
| Mongolia (MN) | R | white 1234 УБА, Soyombo + MNG | white, often faded (single source) | Cyrillic with Ө Ү | gers; treeless steppe; many RHD cars |
| China (CN) | R | blue / yellow / green, 粤B·12345 | yellow / white | Simplified Chinese | see `china.md` |
| Thailand (TH) | L | white, Thai letters + digits, province in Thai below; yellow for hire | mostly yellow / white | Thai | red-white and yellow-white kerbs; songthaews |
| Cambodia (KH) | R | white, blue characters, province in Khmer + English, 2A-1234 | (unverified) | Khmer | red laterite; sugar palms in paddies; US$ prices |
| Laos (LA) | R | yellow-orange, black, Lao province name on top (single source) | (unverified) | Lao | karst and Mekong valleys; sparse signage |
| Vietnam (VN) | R | white 29A-123.45, province code first; yellow commercial | yellow (older white) / white | Vietnamese diacritics | tube houses; motorbike swarms; red flags |
| Malaysia (MY) | L | black, white characters, state letter first | white / white; yellow kerb lines | Malay, Chinese, Tamil, Jawi | oil palm; black-white kerbs |
| Singapore (SG) | L | S + 2 letters + digits + check letter; red = off-peak car | white; yellow kerb lines | English, Chinese, Malay, Tamil | numbered HDB blocks; no overhead wires |
| Indonesia (ID) | L | B 1234 ABC + validity date; black → white since 2022 | white; yellow on national roads | Indonesian (Latin) | "Jl.", "Gg."; regional roof styles |
| Philippines (PH) | R | white ABC 1234; green on white (old); yellow for hire | white, yellow = no overtaking | English, Filipino, Cebuano | jeepneys, tricycles, concrete highways |
| Myanmar (MM) | R | black (private), red (hire); YGN/MDY codes | (unverified) | Burmese | RHD cars driving on the right; stupas |
| Brunei (BN) | L | black, white characters (B…, K…) | (unverified) | Malay in Jawi above Latin | gold-domed mosques |
| Timor-Leste (TL) | L | (unverified) | (unverified) | Tetum + Portuguese | US$ prices; Tetum "k" spellings |
| India (IN) | L | MH 12 AB 1234; colour by class | white, solid yellow = no overtaking | Hindi, English + state scripts | milestones with coloured tops; auto-rickshaws |
| Bangladesh (BD) | L | Bengali script and numerals, "ঢাকা মেট্রো" | (unverified) | Bengali | green CNG three-wheelers; cycle rickshaws |
| Sri Lanka (LK) | L | WP CAB-1234, white front, yellow rear | white (single source) | Sinhala + Tamil + English | trilingual signs; tuk-tuks |
| Nepal (NP) | L | red with white Devanagari (older private); embossed Latin (2020+) | (unverified) | Devanagari (Nepali) | Himalaya; prayer flags |
| Bhutan (BT) | L | BP-1-A1234, white on red | (unverified) | Dzongkha + English | mandated traditional architecture |
| Pakistan (PK) | L | by province: Punjab white, Sindh yellow (single source) | (unverified) | Urdu (Nastaliq) + English | decorated trucks |
| Maldives (MV) | L | (unverified) | n/a | Thaana (right-to-left) | coral islands |
| Kazakhstan (KZ) | R | 123 ABC 01, region code at right | white (unverified) | Kazakh Cyrillic Ә Ғ Қ Ң Ө Ұ Ү Һ І + Russian | flat steppe; birch groves in the north |
| Kyrgyzstan (KG) | R | 01 123 ABC, region code at left | white (unverified) | Kyrgyz Cyrillic Ң Ө Ү + Russian | mountains in most views |
| Uzbekistan (UZ) | R | 01 A 123 BC, region code at left | (unverified) | Uzbek Latin oʻ gʻ, Cyrillic ў қ | white Chevrolets |
| Tajikistan (TJ) | R | 1234 AB 01, region code at right | (unverified) | Tajik Cyrillic Ҷ Ӯ Ӣ | high mountains |
| Turkmenistan (TM) | R | AB 1234 AG, region letters last | (unverified) | Turkmen Latin ň ý ž ä | white marble Ashgabat; desert |

## Region-wide patterns

### Driving side
- Left: JP, HK, MO, TH, MY, SG, ID, BN, TL, IN, BD, LK, NP, BT, PK, MV. Right: KR, TW, CN, MN, KH, LA, VN, PH, MM, KZ, KG, UZ, TJ, TM, RU. Check with `clues.py lookup driving-side left`.
- Thailand flips side at its borders with Myanmar, Laos and Cambodia (all right-hand; Malaysia keeps left); so do HK and Macau against the mainland.
- Steering wheel and traffic side disagree in Myanmar (right-hand traffic, mostly right-hand-drive Japanese imports) and, less uniformly, in Mongolia and the Russian Far East. A right-hand-drive car keeping right narrows Asia to these.

### Scripts (decisive when legible; run `textgeo.py --text "<string>"`)

| Script | How it looks | Where |
|---|---|---|
| Kana | curvy hiragana (の は る) and angular katakana (ア ン ト) mixed with kanji | Japan |
| Hangul | syllable blocks with circles ㅇ and boxes ㅁ | South Korea (also Yanbian in China) |
| Simplified Hanzi | 门 东 车 广 区 发 龙 | mainland China, Singapore, newer Malaysian Chinese signs |
| Traditional Hanzi | 門 東 車 廣 區 發 龍; 臺 often for 台 | Taiwan, Hong Kong, Macau, old overseas-Chinese shopfronts |
| Thai | small loops at letter starts, tall vowel marks above and below, no word spaces | Thailand |
| Lao | a rounder, simpler-looking Thai: fewer loops, serifs and tall strokes | Laos |
| Khmer | consonants stacked below others, small hooks on top | Cambodia |
| Burmese | chains of circles and arcs | Myanmar |
| Devanagari | flat headline bar | Hindi belt, Maharashtra (with ळ), Nepal |
| Bengali-Assamese | headline with triangular hooks; Assamese adds ৰ ৱ | Bangladesh, West Bengal, Tripura, Assam |
| Gurmukhi / Gujarati / Odia | headline with squarer letters / no headline / umbrella-like arches | Punjab / Gujarat / Odisha |
| Telugu / Kannada | round letters with a small tick on top / similar with flatter hooked heads | Andhra Pradesh, Telangana / Karnataka |
| Tamil / Malayalam | angular loops, no headline / very round, wide looped letters | Tamil Nadu, north and east Sri Lanka, SG, MY / Kerala |
| Sinhala | very round, curly, no headline | Sri Lanka |
| Tibetan | headline, dot ་ between syllables | Bhutan (Dzongkha), Ladakh, Sikkim, Tibet |
| Thaana | right-to-left, vowel strokes above and below | Maldives |
| Perso-Arabic | Urdu in slanted Nastaliq; Jawi (Malay) adds چ ڠ ڤ ڽ | Pakistan, Indian Urdu areas; Brunei, Kelantan, Terengganu, Thai deep south, Aceh |
| Cyrillic extras | Ә Ғ Қ Ң Ө Ұ Ү Һ І (KZ); Ң Ө Ү (KG); Ө Ү (MN); Ў Қ Ғ Ҳ (UZ); Ҷ Ӯ Ӣ (TJ) | Central Asia, Mongolia |
| Latin with diacritics | ư ơ đ + tone marks (VN); ň ý ž ä ş (TM); oʻ gʻ (UZ) | as listed |

### Plate colour systems
- Black plate, white characters: Malaysia, Brunei, Macau, Myanmar (private), older Indonesian private plates.
- Yellow: commercial or for-hire in TH, VN (since 2020), KR, ID, IN, PH, BT (taxi), MO (characters only); rear plates in HK and LK; private plates in Sindh (PK).
- Red: private plates in Nepal (older) and Bhutan; off-peak cars in Singapore; brand-new unregistered cars in Thailand.
- Green: EVs in India and Bangladesh (with white text), new-energy cars in China; for-hire plates in Bangladesh; EV stripe on Malaysian plates since 2024.
- Region read from the plate: Thai province (bottom line), Vietnamese province code, Malaysian state letter, Indonesian region prefix, Indian state code, Philippine first letter, Sri Lankan province code, Kazakh/Kyrgyz/Uzbek/Tajik region number, Mongolian aimag letters, Myanmar region code, Korean commercial region name, Japanese area name.

### Road paint
- Yellow centre line separating opposing traffic: KR, TW, CN, VN (QCVN 41 standard, 2019 edition and later; older white lines remain), TH (mostly), ID on national roads only (2018 transport-ministry rule; elsewhere white).
- White centre lines, yellow only where overtaking is banned: JP, IN, PH.
- White, UK or post-Soviet heritage: HK, SG, MY (dashed white on rural two-lane roads), LK and MN (single source), KZ/KG/UZ (unverified). Russia has allowed yellow centre lines since 2018 but they are rare.
- Unverified: KH, LA, MM, BD, NP, PK; many rural roads there are unpainted.
- Kerbs: TW red line = no stopping, yellow = no parking; KR yellow kerb lines; TH red-white = no stopping, yellow-white = brief stops only, black-white = visibility; HK, SG, MY yellow kerb lines = parking restrictions; black-white and black-yellow painted kerbs are common in MY, ID, TH and IN (general knowledge, weak).

### Poles, wires, street furniture
- Japan: concrete poles with many neat cables, numbered pole plates and pole ads, yellow-black striped guy-wire guards, convex mirrors on orange poles at blind corners.
- Sagging bundles of telecom cable on concrete poles: TH, VN, PH, KH, IN (weak; also Latin America). Few or no overhead wires: Singapore, central Hong Kong, Korean and Chinese new towns.

### Vegetation and climate bands (weak without a month)
- Wet tropics (coconut, banana, bamboo, rice): mainland Southeast Asia lowlands, PH, ID, MY, south India, Sri Lanka, Bangladesh.
- Oil palm in grid plantations (stubby cut-frond trunks): MY, ID (Sumatra, Kalimantan), south Thailand. Rubber rows (slim grey trunks, tapping cups): MY, south and east TH, east KH, southeast VN, Sumatra, Kerala, Sri Lanka wet zone.
- Sugar/palmyra palms (single tall trunk, round fan crown) standing in rice fields: Cambodia, central and northeast Thailand, Myanmar dry zone, Tamil Nadu, Jaffna, Nusa Tenggara (lontar).
- Teak and dry deciduous forest (bare in the dry season): north TH, MM, LA, central India, east-central Java.
- Highland pines in the tropics: Luzon Cordillera, Đà Lạt, Himalayan foothills.
- Temperate deciduous forest and rice: JP, KR. Steppe: MN, north and central KZ. Desert: TM, UZ, south KZ, Sindh, Balochistan, Rajasthan. High mountains: KG, TJ, Himalaya.

### Two-wheelers and small public transport
- Motorbike density very high: VN, TW, ID, TH, KH, LA, MM, PH, IN; low: JP, KR, SG, HK, Central Asia, MN.
- Signature vehicles: jeepney and motorbike-with-sidecar tricycle (PH); songthaew pickup taxis (TH, LA); remorque, a motorbike towing a carriage (KH); green CNG three-wheelers and cycle rickshaws (BD); auto-rickshaws (IN, LK, PK); angkot minivans, becak, Jakarta bajaj (ID).

## Japan (JP)

Quick facts
- Drive left (Okinawa drove on the right until 1978).
- Plates: two lines. Top: area name in kanji (a Land Transport office or a "local" name such as 湘南, 富士山) + 3-digit class. Bottom: one hiragana + up to 4 digits (・1-23). White/green = private; yellow/black = kei (≤660 cc); green/white = commercial; black/yellow = commercial kei. Event and local artwork plates since 2017. Rental cars use わ or れ; US-forces personnel cars carry Latin letters (Y, E, A).
- Road paint: white centre line may be crossed to overtake; yellow centre line (always solid) = no crossing to overtake; white edge lines.
- Signs: stop = red inverted triangle 止まれ (English STOP added on signs since 2017); guide signs blue on ordinary roads, green on expressways; national routes on blue inverted shields (国道), prefectural routes on blue hexagons.
- Phone +81: 03 Tokyo, 045 Yokohama, 052 Nagoya, 06 Osaka, 075 Kyoto, 078 Kobe, 082 Hiroshima, 092 Fukuoka, 011 Sapporo, 022 Sendai, 098 Naha; mobiles 070/080/090.
- Postal 〒123-4567 (7 digits). TLD .jp.

### Kana in any text
- Look for: hiragana or katakana mixed with kanji on signs, shop names, vending machines, road paint (とまれ)
- Points to: Japan
- Strength: strong (official writing system)
- Counterexamples: Japanese restaurants and tourist signs abroad (Guam, Hawaii, Taipei, Seoul, Bangkok); Japanese brand logos; one stray character can be a Chinese stroke that resembles katakana
- Verify: `textgeo.py --text "<string>"`; require kana on more than one sign
- Source: general knowledge

### Japanese plate layout and colours
- Look for: two-line plate with kanji area name and a single hiragana; yellow plates on small boxy kei cars and trucks
- Points to: Japan; the area name points to one transport-office area (usually part of one prefecture)
- Strength: strong for country; medium for prefecture (cars travel, rentals roam)
- Counterexamples: exported Japanese used cars (Russian Far East, Mongolia, Pacific islands) keep kei shapes and Japanese stickers but not the plates
- Verify: web search "<area name>ナンバー"; `refsheet.py countries JP,KR --n 6`
- Source: general knowledge

### Inverted-triangle stop sign
- Look for: red downward-pointing triangle reading 止まれ, often with STOP; とまれ painted on the road before it
- Points to: Japan
- Strength: strong (national sign standard)
- Counterexamples: Korea and Taiwan use octagons, so none nearby; themed parks and gardens abroad
- Verify: `refsheet.py countries JP,KR,TW --n 6`
- Source: general knowledge

### Snow-country street kit
- Look for: vertical traffic lights; red-white arrows hanging over the road edge; snow poles; snow sheds; rust-orange streaks from snow-melting water nozzles in the road centre
- Points to: Hokkaido and Aomori (vertical lights standard); the Sea of Japan side of Tohoku and Hokuriku (Akita, Yamagata, Niigata, Toyama, Ishikawa, Fukui)
- Strength: medium
- Counterexamples: isolated vertical lights elsewhere; arrows on mountain passes in central Honshu; Pacific-side Tohoku (Miyagi) mostly horizontal lights
- Verify: `refsheet.py regions JP:Hokkaido,JP:Niigata,JP:Aichi`; `gsv.py near` on candidate towns
- Source: kuruma-news.jp/post/555653 and trafficnews.jp/post/611467 checked 2026-10 (vertical lights); arrows and nozzles general knowledge

### Regions inside Japan
- Plate area names: 札幌 函館 旭川 室蘭 釧路 帯広 北見 = Hokkaido; 品川 練馬 足立 多摩 八王子 = Tokyo; 横浜 川崎 相模 湘南 = Kanagawa; 大阪 なにわ 和泉 堺 = Osaka; 沖縄 = Okinawa. Look up others by web search.
- Postal first digit: 0 Hokkaido, Aomori, Iwate, Akita; 1 and 20x Tokyo; 2 Kanagawa, Chiba; 3 Ibaraki, Tochigi, Saitama, Gunma, Nagano; 4 Yamanashi, Shizuoka, Aichi; 5 Gifu, Mie, Shiga, Osaka; 6 Kyoto, Nara, Wakayama, Hyogo, Tottori, Shimane; 7 Okayama, Hiroshima, Yamaguchi, Shikoku; 8 Kyushu; 9 Okinawa (90x), Hokuriku, Niigata, Fukushima, Miyagi, Yamagata.
- Hokkaido: wide straight roads, big fields and dairy pasture, birch and larch, houses with flat or shallow metal roofs and outdoor kerosene tanks, few clay-tile roofs.
- Tohoku and Hokuriku snow belt: steep metal roofs, snow sheds, vertical lights; flat rice plains around Niigata.
- Kanto, Tokai, Kansai: continuous low-rise suburbs; grey or black glazed tile roofs mixed with modern siding; tea fields in Shizuoka.
- San'in (Shimane, Tottori): red-brown glazed roof tiles dominate villages (general knowledge).
- Kyushu and Shikoku: warmer flora (camphor, roadside palms in Miyazaki), volcanic landscapes, citrus terraces.
- Okinawa: flat-roofed concrete houses with rooftop water tanks, shisa lion figures, red-tile traditional roofs, sugarcane, base fences, Y-plates; area code 098, postcodes 90x.
- Yamaguchi: yellow-painted guardrails (unverified, weak).

## South Korea (KR)

Quick facts
- Drive right.
- Plates: white with black characters, one line: digits + Hangul syllable + 4 digits; class number has 3 digits since September 2019 (123가 4567); blue holographic band on the left since July 2020. Region names left private plates in 2004 but remain on yellow commercial plates (서울, 경기…; single source). EV and hydrogen cars: light blue since 9 June 2017. Rental cars 하/허/호; taxis and buses 바/사/아/자; delivery 배; high-value corporate cars light green since 2024.
- Road paint: yellow centre line (solid = no crossing, dashed = overtaking allowed); white between same-direction lanes; kerbs: yellow dashed = no parking, double yellow = no stopping, red = hydrant.
- Phone +82: 02 Seoul, 031 Gyeonggi, 032 Incheon, 033 Gangwon, 041 Chungnam, 042 Daejeon, 043 Chungbuk, 044 Sejong, 051 Busan, 052 Ulsan, 053 Daegu, 054 Gyeongbuk, 055 Gyeongnam, 061 Jeonnam, 062 Gwangju, 063 Jeonbuk, 064 Jeju; mobiles 010.
- Postal: 5 digits since 2015 (6 digits 123-456 before). TLD .kr.
- Regions: Jeju has black basalt stone walls, tangerine orchards and 064; Gangwon is mountainous with pine forest; the southwest (Jeolla) has the widest rice plains.

### Numbered apartment towers
- Look for: rows of identical high-rise blocks with a large building number (101, 102…) and a builder brand painted high on the gable end
- Points to: South Korea
- Strength: medium
- Counterexamples: Chinese estates also number blocks (smaller, e.g. 3栋); Singapore HDB blocks show numbers too; North Korean blocks lack brands
- Verify: `refsheet.py countries KR,CN --n 6`
- Source: general knowledge

### Korean plates
- Look for: Hangul syllable in the middle of a white plate; yellow plates with a region name on taxis and buses; light-blue EV plates
- Points to: South Korea; the region name on commercial plates gives the province or metropolitan city
- Strength: strong for country (national format); medium for region
- Counterexamples: commercial vehicles cross province lines; a two-digit class number means a pre-2019 registration, not another country
- Verify: `refsheet.py countries KR,JP --n 6`
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_South_Korea checked 2026-10; EV date: sidae.com 2017 report checked 2026-10

## Taiwan (TW)

Quick facts
- Drive right; very dense scooter traffic.
- Plates: white with black characters, 7-character ABC-1234 since 17 December 2012 (digit 4 avoided); older AB-1234 / 1234-AB; no place of issue printed since 2007; EV plates have green bands top and bottom with 電動車; rental cars start with R; business vehicles (taxis, trucks) use their own series and reportedly red characters (unverified).
- Road paint: yellow centre lines (dashed = may cross, double solid = no crossing); white lane and edge lines; red kerb line = no stopping, yellow kerb line = no parking.
- Script: Traditional Chinese; romanisation mixes Hanyu Pinyin with older spellings (Taichung, Kaohsiung, Hsinchu).
- Phone +886: 02 Taipei, New Taipei, Keelung; 03 Taoyuan, Hsinchu, Yilan, Hualien; 037 Miaoli; 04 Taichung, Changhua; 049 Nantou; 05 Chiayi, Yunlin; 06 Tainan, Penghu; 07 Kaohsiung; 08 Pingtung; 089 Taitung; 082 Kinmen; 0836 Matsu; mobiles 09.
- Postal: 3+3 digits since 2020 (3+2 before). TLD .tw.
- Regions: dense west-coast plain; steep east coast (Hualien, Taitung) where mountains meet the sea; tropical south (Pingtung betel and coconut palms); Kinmen and Matsu with Fujian-style stone houses.

### Scooter waiting boxes
- Look for: white painted boxes with a scooter symbol ahead of the stop line, and smaller two-stage left-turn boxes at the side of junctions
- Points to: Taiwan
- Strength: medium
- Counterexamples: some mainland Chinese cities paint non-motor waiting areas; Vietnamese junctions are crowded with bikes but rarely boxed
- Verify: `refsheet.py countries TW,VN --n 6`
- Source: general knowledge

### Red and yellow kerb lines with yellow centre lines
- Look for: continuous red or yellow lines along the road edge; yellow double centre lines; Traditional characters on signs
- Points to: Taiwan
- Strength: medium (Korea uses yellow kerb lines too)
- Counterexamples: Korea (Hangul); Hong Kong yellow kerb lines with left-hand traffic
- Verify: `refsheet.py countries TW,KR,HK --n 6`
- Source: general knowledge

## Hong Kong (HK)

Quick facts
- Drive left (opposite to the mainland).
- Plates: UK style, white front and yellow rear, black characters, two letters + up to 4 digits (AB 1234) or personalised; cross-boundary cars also carry a black Guangdong 粤Z plate ending in 港.
- Road paint: UK style white lines; yellow kerb lines = no stopping (double = at any time); zig-zags at zebra crossings; LOOK RIGHT / 望右 painted at crossings.
- Signs: bilingual Traditional Chinese and English. Taxis: red (urban), green (New Territories), blue (Lantau).
- Phone +852, 8 digits, no area codes. No postcodes. TLD .hk.

### Bilingual Traditional Chinese and English with left-hand traffic
- Look for: Traditional characters next to English on road signs; UK-style markings; white front and yellow rear plates
- Points to: Hong Kong
- Strength: strong (combination fixed by local standards)
- Counterexamples: Macau (Portuguese instead of English on street signs, black plates); Shenzhen side of the boundary (Simplified, right-hand traffic)
- Verify: `refsheet.py countries HK,MO --n 6`
- Source: en.wikipedia.org/wiki/Road_surface_marking checked 2026-10 (markings); rest general knowledge

## Macau (MO)

Quick facts
- Drive left.
- Plates: white characters on black, two letters + 2 + 2 digits (MA-12-34 style; after the M-letter series came A-series prefixes, AB in use by 2023); commercial vehicles have yellow characters on black; cross-boundary cars carry an extra 粤Z…澳 plate.
- Languages: Traditional Chinese and Portuguese: Rua, Avenida, Travessa, Estrada, Calçada, Largo.
- Phone +853, 8 digits (landlines 28…, mobiles 6…). No postcodes. TLD .mo.

### Portuguese and Chinese tiled street signs
- Look for: blue-and-white ceramic tile name plaques with a Portuguese name above or beside Chinese; wavy black-white stone pavement
- Points to: Macau
- Strength: strong
- Counterexamples: Portuguese-themed districts or hotels elsewhere; Portugal itself has tiles but no Chinese text
- Verify: `refsheet.py countries MO,HK --n 6`
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_Macau checked 2026-10 (plates); signs general knowledge

## Mongolia (MN)

Quick facts
- Drive right; many right-hand-drive Japanese used cars (general knowledge).
- Plates: black on white, 4 digits + 3 Cyrillic letters (1234 УБА); the first two letters give the aimag or city (УБ, УН, УА, УЕ, УК = Ulaanbaatar; АР Arkhangai; ДО Dornod; ХО Khovd; УВ Uvs; ЗА Zavkhan); red Soyombo and oval MNG since 2001.
- Road paint: white, often faded or missing (single source).
- Script: Cyrillic with Ө ө and Ү ү (no Ң); traditional vertical Mongolian script on some official signs.
- Phone +976 (8 digits). Postal 5 digits. TLD .mn.

### Ger districts and treeless steppe
- Look for: white felt gers inside wooden-fenced plots, small houses with bright green, red or blue metal roofs, bare rolling steppe without trees
- Points to: Mongolia (Ulaanbaatar outskirts and aimag centres)
- Strength: medium
- Counterexamples: Inner Mongolia, China (Chinese plates, Hanzi with vertical Mongolian script); yurts in Kazakhstan and Kyrgyzstan (Kazakh or Kyrgyz letters, different plates); Buryatia and Tuva in Russia
- Verify: `refsheet.py countries MN,KZ,KG --n 6`
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_Mongolia checked 2026-10 (plates); landscape general knowledge

## Mainland China (CN): pointer

- Depth is in `china.md` (plates by province, area codes, phenology, Baidu sampling with `baidu_pano.py sample`).
- Against neighbours: right-hand traffic (HK, MO left); Simplified characters (TW, HK, MO Traditional); plates with one Hanzi province abbreviation + letter on blue (small), yellow (large) or green (new-energy); yellow centre lines; Google Street View is scarce inside the mainland.
- Border zones that look foreign: Yanbian (Hangul above Hanzi, Chinese plates) is not Korea; Inner Mongolia (vertical Mongolian + Hanzi) is not Mongolia; Xinjiang (Uyghur Arabic script); Tibet (Tibetan + Hanzi); Yunnan and Guangxi near Vietnam, Laos, Myanmar.

## Thailand (TH)

Quick facts
- Drive left.
- Plates: white; character colour by class: black (private car ≤7 seats), blue (private van), green (private pickup); taxis and other for-hire vehicles yellow; red plates = new car awaiting registration. Top line: Thai consonants (a leading digit added when a series runs out, e.g. 1กข 1234, Bangkok since 2012) + up to 4 digits; bottom line: province name in Thai. Motorcycle plates: three rows, province in the middle.
- Road paint: centre lines mostly yellow (dashed, solid or double); white lane and edge lines (Thai sources disagree on whether white dashed centre lines also count as normal). Kerbs: red-white, yellow-white, black-white.
- Signs: blue guide signs with Thai and English; highway numbers whose first digit gives the region (see below).
- Phone +66: 02 Bangkok metro; 053 Chiang Mai; 054 Lampang; 038 Chonburi, Rayong; 044 Nakhon Ratchasima; 043 Khon Kaen; 042 Udon Thani; 045 Ubon; 076 Phuket; 077 Surat Thani; 074 Songkhla, Hat Yai; 073 Pattani, Yala, Narathiwat; mobiles 06/08/09.
- Postal: 5 digits, first two = province. TLD .th.

### Province name on Thai plates
- Look for: the bottom line of a car plate (middle row on motorbikes) in Thai script
- Points to: province of registration
- Strength: strong for registration (national format); medium for location (Bangkok cars everywhere)
- Counterexamples: Bangkok-registered rentals and company cars; tourist areas; red new-car plates have no useful province
- Verify: `textgeo.py --text "<province name>"`; plates on several local motorbikes agree
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_Thailand checked 2026-10

### Thai kerb paint
- Look for: kerb stones painted in red-white or yellow-white stripes (also black-white), with yellow centre lines and left-hand traffic
- Points to: Thailand
- Strength: medium
- Counterexamples: Malaysia and Indonesia paint black-white and yellow-black kerbs; Cambodia and Laos borrow Thai styles near the border
- Verify: `refsheet.py countries TH,MY,ID --n 6`
- Source: ktc.co.th, autospinn.com, chobrod.com articles on kerb colours checked 2026-10

### Regions inside Thailand
- Highway numbers: 1 north, 2 northeast, 3 east, 4 south from Bangkok; 2- to 4-digit routes start with their region digit (1x north, 2x northeast, 3x central and east, 4x south) (general knowledge).
- Postcode first digit: 1 Bangkok and central plain; 2 east; 3 lower northeast (Korat, Buriram, Surin, Ubon); 4 upper northeast (Khon Kaen, Udon, Loei, Nong Khai); 5 upper north (Chiang Mai, Chiang Rai, Nan); 6 lower north (Phitsanulok, Sukhothai, Tak); 7 west (Kanchanaburi, Ratchaburi, Prachuap); 8 upper south (Phuket 83, Surat Thani 84); 9 lower south (Songkhla 90, Pattani 94, Yala 95, Narathiwat 96).
- North: forested mountains, teak and dry deciduous forest, steep layered Lanna temple roofs, cooler air; area codes 05x.
- Northeast (Isan): flat to rolling plateau, rice, cassava and sugarcane, sugar palms; people speak Lao but write Thai; codes 04x.
- Central: very flat rice plain with canals, Bangkok sprawl, elevated expressways; 02, 03x.
- East: industrial Chonburi and Rayong; durian and rambutan orchards around Chanthaburi.
- South: rubber and oil palm, limestone karst (Krabi, Phang Nga), more mosques southward; the deep south (Pattani, Yala, Narathiwat) has Jawi beside Thai, army checkpoints and code 073.

## Cambodia (KH)

Quick facts
- Drive right; many left-hand-drive American-spec imports (general knowledge).
- Plates (since 2004): province name in Khmer above and English below (PHNOM PENH, SIEM REAP); number like 2A-1234 where the first digit is the class (1 motorcycle, 2 private car up to 7 seats: white with blue characters, 3 larger vehicles: blue with white); police red; NGO light blue.
- Script: Khmer; English common on shop signs; prices often in US dollars beside riel.
- Phone +855: 023 Phnom Penh; mobiles 01x, 06x-09x. TLD .kh.
- Landscape: flat central plain, red laterite roads and shoulders, wooden stilt houses, sugar palms in rice fields, remorques.

### Khmer plus English province plates
- Look for: Khmer script above an English province name on a white plate with blue characters
- Points to: Cambodia; the province name gives the registering province
- Strength: strong for country (national format); medium for province
- Counterexamples: Phnom Penh plates travel the whole country; Thai plates look similar in layout but carry Thai script only
- Verify: `refsheet.py countries KH,TH,LA --n 6`
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_Cambodia checked 2026-10

## Laos (LA)

Quick facts
- Drive right.
- Plates (since 2001): province name in Lao on the top line; two Lao letters (first = vehicle type) + 4 digits; private plates black on yellow-orange, other colours by owner type (single source); EV mark from 2024 (single source).
- Script: Lao. Phone +856: 021 Vientiane; mobiles 020. TLD .la.
- Landscape: mountainous north with limestone karst, slash-and-burn fields and hill villages; Mekong lowlands (Vientiane, Savannakhet, Pakse); Bolaven Plateau coffee in the south. Road paint (unverified).

### Lao script
- Look for: rounder, simpler letters than Thai, fewer loops and tall strokes
- Points to: Laos
- Strength: strong when several words are legible (official script)
- Counterexamples: northeast Thailand speaks Lao but writes Thai; Thai text at the Friendship Bridges
- Verify: `textgeo.py --text "<string>"`
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_Laos checked 2026-10 (plates); script general knowledge

## Vietnam (VN)

Quick facts
- Drive right; motorbikes dominate.
- Plates: two-digit province code + series letter + number (cars 29A-123.45; motorbikes two lines, 59-X1 / 123.45); white (private), yellow with black (commercial transport, from 1 August 2020), blue (government), red (military).
- Road paint: yellow lines separate opposing traffic and white lines separate same-direction lanes (QCVN 41; 2019 edition, replaced by QCVN 41:2024 from 2025); older white centre lines remain.
- Script: Vietnamese Latin with ư ơ ă â ê ô đ and tone marks.
- Phone +84: since 2017 024 Hà Nội, 028 TP HCM, 0236 Đà Nẵng, 0225 Hải Phòng, 0292 Cần Thơ; mobiles 03/05/07/08/09.
- Postal: 5 digits since 2018. TLD .vn.
- Dating: on 1 July 2025 the 63 provinces were merged into 34 (Resolution 202/2025/QH15); old plates keep their codes and signs show old or new names.

### Vietnamese diacritics
- Look for: ư, ơ, đ and stacked tone marks (ế, ữ, ạ) on any sign
- Points to: Vietnam
- Strength: strong (official orthography)
- Counterexamples: Vietnamese shops abroad (Cambodia, Laos, diaspora); stylised logos without marks
- Verify: `textgeo.py --text "<string>"`
- Source: general knowledge

### Tube houses
- Look for: very narrow (3-5 m), tall (3-6 storeys) row houses with decorated fronts and bare side walls, often in mismatched heights
- Points to: Vietnam
- Strength: medium
- Counterexamples: Cambodian and Thai shophouses are wider and lower in uniform rows; Indonesian ruko
- Verify: `refsheet.py countries VN,KH,TH --n 6`
- Source: general knowledge

### Regions inside Vietnam
- Plate codes (pre-2025 provinces; check a table): 29-33 and 40 Hà Nội; 41 and 50-59 TP HCM; 43 Đà Nẵng; 15-16 Hải Phòng; 65 Cần Thơ; 14 Quảng Ninh; 36 Thanh Hóa; 37 Nghệ An; 75 Huế; 79 Khánh Hòa; 49 Lâm Đồng; 47 Đắk Lắk; 60 Đồng Nai; 61 Bình Dương; 72 Bà Rịa-Vũng Tàu. Roughly 11-38, 88-90 and 97-99 north; 43, 47-49, 73-82, 85-86, 92 centre and highlands; 41, 50-72, 83-84, 93-95 south.
- North: Red River Delta rice and dense villages; misty, cooler winters; northern mountains with terraces, karst and minority stilt houses.
- Centre: narrow coastal plain under the Annamite range; sandy coast dotted with ornate family tombs.
- Central Highlands: red basalt soil, coffee and pepper; pine around Đà Lạt.
- South: Mekong Delta canals, coconut palms, water hyacinth, very flat; TP HCM sprawl.

## Malaysia (MY)

Quick facts
- Drive left.
- Plates: white characters on black, front and rear; first letter = state. Taxis: H prefix, black on white. Newly registered EVs since September 2024: white plate with a green stripe.
- Road paint: dashed white centre line on rural two-lane roads (JKR standard); yellow kerb lines = parking limits; yellow transverse bars before junctions and toll plazas.
- Signs: Malay in Latin script (Jalan, Lorong, Kampung, Awas, Ikut Kiri, Simpang, Keluar); blue guide signs on ordinary roads, green on tolled expressways (E routes).
- Languages: Malay; Chinese (mixed simplified and traditional), Tamil; Jawi on official signs, prominent in Kelantan and Terengganu.
- Phone +60: 03 Klang Valley; 04 Penang, Kedah, Perlis; 05 Perak; 06 Melaka, Negeri Sembilan; 07 Johor; 09 Pahang, Terengganu, Kelantan; 082-086 Sarawak; 087-089 Sabah, Labuan; mobiles 01x.
- Postal 5 digits. TLD .my.

### State letter on black plates
- Look for: the first letter(s) of a black plate
- Points to: R Perlis; K Kedah (KV Langkawi); P Penang; A Perak; B Selangor; W and V Kuala Lumpur; F Putrajaya; N Negeri Sembilan; M Melaka; J Johor; C Pahang; T Terengganu; D Kelantan; L Labuan; S + letter Sabah (SA, SY, SJ Kota Kinabalu; SS, SM Sandakan; ST, SW Tawau; SD, SP Lahad Datu; SK Kudat; SB Beaufort; SU Keningau); Q + letter Sarawak (QA, QK Kuching; QB Sri Aman; QC Samarahan; QS, QE Sibu; QT, QD Bintulu; QM Miri; QL Limbang; QP Kapit; QR Sarikei)
- Strength: strong for registration (national format); medium for location
- Counterexamples: Klang Valley (B, W, V) cars everywhere; Singapore plates are also black with white characters but start with S and end in a check letter; Brunei plates are black too
- Verify: `textgeo.py --text "<plate>"`; agreement across several local cars
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_Malaysia checked 2026-10

### Jawi on official signs
- Look for: Arabic-script Malay under or above the Latin text on road and government signs
- Points to: Kelantan and Terengganu most strongly; also Brunei and other Malaysian states more lightly
- Strength: medium
- Counterexamples: Brunei puts Jawi above Latin everywhere; mosques and religious schools anywhere in the Malay world
- Verify: `refsheet.py regions MY:Kelantan,MY:Selangor`
- Source: general knowledge

### Regions inside Malaysia
- Postcode first two digits: 01-02 Perlis; 05-09 Kedah; 10-14 Penang; 15-18 Kelantan; 20-24 Terengganu; 25-28 Pahang; 30-36 Perak; 40-48 Selangor; 50-60 Kuala Lumpur; 62 Putrajaya; 70-73 Negeri Sembilan; 75-78 Melaka; 79-86 Johor; 87 Labuan; 88-91 Sabah; 93-98 Sarawak.
- West coast (Selangor, KL, Perak, Penang): dense highways and condos; limestone karst around Ipoh; flat rice paddies with limestone hills in Kedah and Perlis.
- East coast (Kelantan, Terengganu, Pahang): Malay-only signage, Jawi, wooden kampung houses, casuarina beaches.
- South (Johor, Melaka, Negeri Sembilan): oil palm; curved buffalo-horn roofs of Minangkabau style in Negeri Sembilan.
- Borneo (Sabah, Sarawak): hillier, wetter, longhouses, more churches, 08x area codes, S and Q plates.

## Singapore (SG)

Quick facts
- Drive left.
- Plates: black with white characters, or white front and yellow rear; S + 2 letters + 1-4 digits + a check letter (SBA 1234 A); taxis SH…; older E series; red plates with white characters = off-peak cars.
- Road paint: white lines; yellow kerb lines (double = no parking at any time); zig-zags before crossings.
- Languages: English, Chinese (simplified), Malay, Tamil; street names include Jalan and Lorong.
- Phone +65, 8 digits (6 landline; 8, 9 mobile). Postal 6 digits, first two = sector. TLD .sg.

### Singapore plate and estate pattern
- Look for: S-series plate ending in a single check letter; HDB slab blocks with a large block number; covered walkways, manicured verges, no overhead wires
- Points to: Singapore
- Strength: strong for the plate (national format); medium for the estate look
- Counterexamples: Singapore cars in Johor Bahru; Malaysian condos and Hong Kong estates look similar from afar
- Verify: `refsheet.py countries SG,MY --n 6`
- Source: general knowledge

## Indonesia (ID)

Quick facts
- Drive left; motorbikes everywhere.
- Plates: region letter(s) + up to 4 digits + up to 3 letters (B 1234 ABC), validity month.year printed below; private plates white with black characters from June 2022 (phased in at new registration and 5-year renewal), black with white before; yellow = public transport, red = government.
- Road paint: white in general; yellow markings identify national roads (2018 transport-ministry rule); repainting is gradual.
- Language: Indonesian in Latin script (Jl. = Jalan, Gg. = Gang, Desa, Kelurahan, Kecamatan, Kabupaten, Toko, Warung, Dijual, Dilarang, Hati-hati); regional scripts on street-name signs: Javanese in Yogyakarta and Surakarta, Balinese in Bali, Sundanese in parts of West Java, Arabic script in Aceh.
- Phone +62: 021 Jakarta; 022 Bandung; 024 Semarang; 0271 Solo; 0274 Yogyakarta; 031 Surabaya; 0341 Malang; 0361 Bali; 061 Medan; 0711 Palembang; 0751 Padang; 0411 Makassar; 0431 Manado; 0561 Pontianak; 0542 Balikpapan; 0967 Jayapura; mobiles 08xx.
- Postal 5 digits. TLD .id.

### Region prefix on Indonesian plates
- Look for: the letters before the number
- Points to: B Jakarta and its satellites; D Bandung; F Bogor, Sukabumi, Cianjur; E Cirebon; T Karawang, Purwakarta, Subang; Z Garut, Tasikmalaya, Ciamis; A Banten; G Pekalongan, Tegal; H Semarang; K Pati, Kudus; R Banyumas; AA Magelang area; AB Yogyakarta; AD Surakarta; L Surabaya; W Sidoarjo, Gresik; N Malang; P Jember, Banyuwangi; AG Kediri; AE Madiun; S Bojonegoro, Lamongan; M Madura; DK Bali; DR Lombok; EA Sumbawa; DH Timor; EB Flores; ED Sumba; BL Aceh; BK, BB North Sumatra; BA West Sumatra; BM Riau; BP Riau Islands; BH Jambi; BG South Sumatra; BN Bangka-Belitung; BD Bengkulu; BE Lampung; KB West, KH Central, KT East, KU North Kalimantan; DA South Kalimantan; DB North Sulawesi; DM Gorontalo; DN Central Sulawesi; DT Southeast Sulawesi; DD South Sulawesi; DC West Sulawesi; DE Maluku; DG North Maluku; PA Papua; PB West Papua
- Strength: strong for registration (national format); medium for location
- Counterexamples: B cars on every Java road; old black and new white plates coexist until about 2027
- Verify: `textgeo.py --text "<plate>"`; local motorbikes and angkot agree
- Source: general knowledge (prefixes); white plates: oto.detik.com 2022 reports on Perpol 7/2021 checked 2026-10

### Regional roof styles
- Look for: buffalo-horn upswept gables (Minangkabau); boat-shaped saddle roofs (Toraja); split stone gates, shrine compounds and offerings (Bali); tall pointed Batak roofs; Javanese joglo roofs with a raised centre
- Points to: West Sumatra; South Sulawesi highlands; Bali; North Sumatra; Central Java and Yogyakarta
- Strength: medium
- Counterexamples: Padang restaurants copy Minangkabau roofs across Indonesia and Malaysia; Negeri Sembilan (MY) uses similar roofs; Bali-style resorts exist elsewhere
- Verify: `refsheet.py regions "ID:West Sumatra,ID:Bali,ID:South Sulawesi"`
- Source: general knowledge

### Regions inside Indonesia
- Postcode first digit: 1 Greater Jakarta (with Tangerang, Bogor, Bekasi); 2 northern Sumatra (Aceh, North and West Sumatra, Riau); 3 southern Sumatra (South Sumatra, Bangka, Lampung, Jambi, Bengkulu); 4 rest of West Java and Banten; 5 Central Java and Yogyakarta; 6 East Java; 7 Kalimantan; 8 Bali and Nusa Tenggara; 9 Sulawesi, Maluku, Papua.
- Java: densest; rice terraces under volcanoes; teak in east-central Java; Javanese script signs in Yogyakarta and Solo.
- Bali: Hindu shrines in every compound, split gates, offerings on pavements, tall bamboo penjor poles around the Galungan holidays.
- Sumatra: oil palm and rubber, Minangkabau roofs (West), Batak houses and churches (North), Arabic-script signs and large mosques (Aceh).
- Kalimantan: wide brown rivers, peat swamp, wooden stilt houses, coal-hauling roads.
- Sulawesi: mountainous; Toraja roofs; Christian north (Manado), Muslim south (Makassar).
- Nusa Tenggara: dry savanna, lontar palms, churches in Flores and Timor. Maluku and Papua: churches, steep forested terrain, few roads.

## Philippines (PH)

Quick facts
- Drive right (switched 1946).
- Plates: 2014+ series ABC 1234: black on white (private), black on yellow (for hire), red on white (government), blue on white (diplomatic), green on white (EV and hybrid, 2023); older private plates green on white (Rizal Monument background 2002-2014). First letter = region of registration: N, P, Q, T, U, X Metro Manila; C, R, W Central Luzon; D, O Calabarzon; V Mimaropa; A, I Ilocos; B Cagayan Valley; Y Cordillera; E Bicol; F Western Visayas; G Central Visayas; H Eastern Visayas; J Zamboanga; K Northern Mindanao; L Davao; M Soccsksargen; Z Caraga (single source).
- Road paint: mostly white; yellow for no-overtaking lines and box junctions (single source); many national highways are concrete slabs.
- Languages: English, Filipino (Bawal = forbidden, Mag-ingat = be careful, Barangay, sari-sari store, Tindahan), Cebuano in Visayas and Mindanao, Ilocano in the north.
- Phone +63: 02 Metro Manila; 032 Cebu; 033 Iloilo; 034 Bacolod; 074 Baguio; 082 Davao; 088 Cagayan de Oro; mobiles 09xx.
- Postal 4 digits. TLD .ph.

### Jeepneys, tricycles and barangay arches
- Look for: long chromed jeepneys with painted names; motorbikes with a covered sidecar; concrete arches reading "Welcome to Barangay …"; basketball hoops beside the road
- Points to: Philippines
- Strength: strong (jeepneys and barangay signs exist only here)
- Counterexamples: modern minibus PUVs are replacing jeepneys; Indonesian and Thai sidecar motorbikes look different and drive left
- Verify: `refsheet.py countries PH,ID --n 6`
- Source: general knowledge

### Region letter on Philippine plates
- Look for: the first letter of a car or motorcycle plate
- Points to: region of registration (list in quick facts)
- Strength: medium (registration, not location)
- Counterexamples: Metro Manila cars everywhere on Luzon; the 2014 design printed the region at the bottom instead of using the letter for cars
- Verify: `textgeo.py --text "<plate>"`
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_Philippines checked 2026-10 (single source)

### Regions inside the Philippines
- Northern Luzon: Cordillera with pine forest, steep rice terraces, cool Baguio (074, Y plates); dry Ilocos coast with Spanish-era stone churches (A, I).
- Central Luzon and Calabarzon: wide rice plains, Pampanga lahar fields, coconut belts in Quezon, Taal.
- Bicol: Mayon volcano, coconut and abaca (E).
- Visayas: sugarcane on Negros (034), hilly Cebu (032, G), Waray in Leyte and Samar (H).
- Mindanao: banana and pineapple plantations (Davao 082, Bukidnon); Muslim areas of Bangsamoro and Sulu with mosques and Arabic script.

## Myanmar (MM)

Quick facts
- Drive right, but most cars are right-hand-drive Japanese imports (general knowledge).
- Plates: black with white (private), red with white (hire and commercial); region code + township number in Latin since September 2013 (YGN Yangon, MDY Mandalay, SHN Shan); older plates in Burmese script and numerals (single source).
- Script: Burmese, numerals ၀-၉. Phone +95: 01 Yangon, 02 Mandalay, 067 Nay Pyi Taw; mobiles 09. TLD .mm.
- Landscape: golden stupas, monasteries, central dry zone with toddy palms, men in longyi.

### Right-hand-drive cars keeping right with Burmese text
- Look for: steering wheels on the right in right-hand traffic; round Burmese letters
- Points to: Myanmar
- Strength: strong when both are seen
- Counterexamples: Mongolia and the Russian Far East also mix RHD cars with right-hand traffic (Cyrillic text there)
- Verify: `refsheet.py countries MM,TH --n 6`
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_Myanmar checked 2026-10 (plates); RHD share general knowledge

## Brunei (BN)

Quick facts
- Drive left. Plates: white on black, letters + up to 4 digits (B… Brunei-Muara and K… Kuala Belait historically; BAA… series since 2009); taxis and buses green (single source).
- Script: official signs put Jawi above Latin Malay (the quickest test against Sabah and Sarawak). Phone +673, 7 digits. Postcodes 2 letters + 4 digits (BS8811; first letter B Brunei-Muara, K Belait, T Tutong, P Temburong). TLD .bn.

## Timor-Leste (TL)

Quick facts
- Drive left (since 1976). Currency US dollar. Languages Tetum and Portuguese (Tetum spells with k: Repúblika Demokrátika, Ministériu), Indonesian widely understood.
- Phone +670 (mobiles 7xxx xxxx). TLD .tl. Plates and paint (unverified). Landscape: steep dry hills, savanna and eucalyptus, Catholic churches; Indonesian West Timor next door has DH plates and Indonesian signage.

## India (IN)

Quick facts
- Drive left.
- Plates: state code + 2-digit district (RTO) number + series + 4 digits (MH 12 AB 1234). White/black private; yellow/black commercial; green/white private EV, green/yellow commercial EV; black/yellow self-drive rental; BH series (21 BH 1234 AA, since 2021) not tied to a state; high-security plates with chromium hologram and IND.
- State codes: AN, AP, AR, AS, BR, CG, CH, DD, DL, GA, GJ, HP, HR, JH, JK, KA, KL, LA (Ladakh), LD, MH, ML, MN, MP, MZ, NL, OD (Odisha, formerly OR), PB, PY, RJ, SK, TN, TR, TG (Telangana since March 2024; TS before), UK (Uttarakhand, formerly UA), UP, WB.
- Road paint: white lines; continuous yellow centre line = no overtaking (IRC:35); kerbs often black-yellow or black-white.
- Milestones: white stones with a coloured top: yellow = national highway, green = state highway, blue, black or white = district or city road, orange (some say red) = rural road; destination and km in local script and English.
- Phone +91: 011 Delhi, 022 Mumbai, 033 Kolkata, 044 Chennai, 080 Bengaluru, 040 Hyderabad, 020 Pune, 079 Ahmedabad, 0141 Jaipur, 0522 Lucknow; mobiles 10 digits starting 6-9.
- PIN: 6 digits; first digit 1 Delhi, Haryana, Punjab, HP, J&K, Ladakh, Chandigarh; 2 UP, Uttarakhand; 3 Rajasthan, Gujarat; 4 Maharashtra, Goa, MP, Chhattisgarh; 5 AP, Telangana, Karnataka; 6 Tamil Nadu, Kerala, Puducherry; 7 West Bengal, Odisha, Northeast, Sikkim, Andaman; 8 Bihar, Jharkhand; 9 army post. TLD .in.

### State code on Indian plates
- Look for: the two letters at the start of the plate
- Points to: state or union territory of registration (list above)
- Strength: strong for registration (central rules); medium for location (interstate trucks, tourist taxis, BH plates)
- Counterexamples: national-permit trucks; Delhi and Haryana cars around the capital region; TS and TG both valid in Telangana
- Verify: `textgeo.py --text "<plate>"`; agreement across two-wheelers and autos
- Source: general knowledge; Telangana change: deccanchronicle.com and thenewsminute.com March 2024 reports checked 2026-10

### Milestone top colour
- Look for: a roadside stone with a coloured cap and place names
- Points to: road class (yellow national, green state highway); the script on it gives the state
- Strength: medium
- Counterexamples: faded or repainted stones; some states paint other colours
- Verify: `osm.py near` for the road ref (NH/SH number) at the candidate point
- Source: udayavani.com and orissapost.com explainers checked 2026-10

### State script on official signs
- Look for: the non-English, non-Hindi script on government signs, milestones and bus boards
- Points to: Gurmukhi Punjab; Gujarati Gujarat; Devanagari with ळ Maharashtra or Goa; Bengali West Bengal and Tripura; Assamese (ৰ ৱ) Assam; Odia Odisha; Telugu AP and Telangana; Kannada Karnataka; Tamil Tamil Nadu and Puducherry; Malayalam Kerala; Urdu J&K (and Urdu areas elsewhere); Tibetan Ladakh, Sikkim (partly)
- Strength: strong on official signs; medium on shop signs
- Counterexamples: border districts; migrant shopkeepers; Hindi on central-government signs everywhere; Delhi signs carry Hindi, English, Punjabi and Urdu
- Verify: `textgeo.py --text "<string>"`
- Source: general knowledge

### Regions inside India
- Northwest: Punjab (Gurmukhi, PB) flat wheat and rice fields, gurdwaras; Haryana (HR) flat farmland and brick kilns; Delhi (DL) four-language signs.
- Himalaya: Himachal (HP) slate and tin roofs, deodar and apple orchards; Uttarakhand (UK) pine ridges and temples; J&K (JK) chinar trees, sloping tin roofs, Urdu; Ladakh (LA) cold desert, stupas; Sikkim (SK) Nepali signs, prayer flags.
- Gangetic plain: UP (UP), Bihar (BR): flat, brick kilns with tall chimneys, mustard fields in winter; Jharkhand (JH) plateau forests.
- West: Rajasthan (RJ) desert scrub, khejri trees, sandstone and forts; Gujarat (GJ) flat, good roads, Gujarati script; Maharashtra (MH) black basalt soils, Marathi; Goa (GA) Portuguese-style houses and churches.
- South: Karnataka (KA); AP and Telangana (AP, TG) with granite boulder hills on the Deccan; Tamil Nadu (TN) temple towers, palmyra palms; Kerala (KL) coconut palms, red laterite, steep tiled roofs, continuous roadside settlement; Puducherry (PY) French street names.
- East and northeast: West Bengal (WB) flat paddies and ponds, Kolkata yellow taxis; Odisha (OD); Assam (AS) tea gardens and bamboo houses; Meghalaya, Mizoram, Nagaland (ML, MZ, NL) hill towns with churches and Latin-script local languages; Manipur (MN) Meitei Mayek script.

## Bangladesh (BD)

Quick facts
- Drive left. Plates: Bengali script and Bengali numerals; line 1 city or district (ঢাকা মেট্রো = Dhaka Metro) + class letter; line 2 series + 4-digit number; private white with black (digital plates since 2012; older private white on black); commercial green with black; EV green with white.
- Script: Bengali almost everywhere, little English outside cities. Phone +880: 02 Dhaka, 031 Chattogram; mobiles 01x. Postal 4 digits (1000 Dhaka). TLD .bd.
- Landscape: flat delta, ponds, brick kilns, jute and rice; tea gardens in Sylhet; hills in the Chattogram Hill Tracts. Vehicles: green CNG three-wheelers, decorated cycle rickshaws, battered buses.

### Bengali-script plates
- Look for: a plate written entirely in Bengali, including the digits
- Points to: Bangladesh
- Strength: strong (national format; West Bengal plates use Latin WB codes)
- Counterexamples: Bangladeshi vehicles near Indian border crossings
- Verify: `refsheet.py countries BD,IN --n 6`
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_Bangladesh checked 2026-10

## Sri Lanka (LK)

Quick facts
- Drive left. Plates (since 2000): province code (WP Western, CP Central, SP Southern, NW North Western, NC North Central, NP Northern, EP Eastern, UP Uva, SG Sabaragamuwa) + 2-3 letters + 4 digits (WP CAB-1234); front white, rear yellow. Older plates have digits with the Sinhala ශ්‍රී between them.
- Road paint white (single source). Signs trilingual: Sinhala, Tamil, English.
- Phone +94: 011 Colombo, 081 Kandy, 091 Galle, 021 Jaffna, 026 Trincomalee, 065 Batticaloa, 052 Nuwara Eliya; mobiles 07x. Postal 5 digits. TLD .lk.
- Regions: coconut-lined wet southwest; tea estates and cool hill country (Nuwara Eliya); dry zone with tanks and paddies (Anuradhapura); Tamil north and east (Hindu kovils, palmyra palms, Tamil-first signs).

### Sinhala script
- Look for: very round, curly letters without a headline
- Points to: Sri Lanka
- Strength: strong (official script found nowhere else)
- Counterexamples: Sri Lankan shops abroad
- Verify: `textgeo.py --text "<string>"`
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_Sri_Lanka checked 2026-10 (plates); script general knowledge

## Nepal (NP)

Quick facts
- Drive left. Plates: older Devanagari plates (zone letter + number + class letter + 4 digits; बा = Bagmati, the Kathmandu valley): red with white = private, black with white = public, white with red = government, green = tourism. Since July 2020: embossed Latin plates with province name, flag and NEP (single source).
- Script: Devanagari (Nepali); Nepal-specific words: गाउँपालिका (rural municipality), वडा नं. (ward no.), प्रदेश (province).
- Phone +977: 01 Kathmandu valley; mobiles 98x/97x. Postal 5 digits. TLD .np.
- Landscape: flat Terai in the south (rice, sal forest, Indian-looking towns), terraced middle hills with brick and tin-roof houses, high Himalaya; prayer flags, stupas, pagoda temples.

### Red Devanagari plates
- Look for: red plate with white Devanagari characters on cars and motorbikes
- Points to: Nepal
- Strength: strong (national format; Indian plates are Latin)
- Counterexamples: Nepali vehicles in Indian border towns; Bhutanese private plates are also red but Latin (BP)
- Verify: `refsheet.py countries NP,IN --n 6`
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_Nepal checked 2026-10

## Bhutan (BT)

Quick facts
- Drive left. Plates BP-1-A1234: BP private (white on red), BT taxi (black on yellow), BG government (yellow on red), RBP police (white on blue); the digit is the region (1 west incl. Thimphu, Paro; 2 Chukha, Samtse; 3 central; 4 Samdrup Jongkhar, Pemagatshel; 5 east).
- Script: Dzongkha (Tibetan script) with English. Phone +975. TLD .bt.
- Architecture: law requires traditional design: whitewashed walls, timber upper floors, richly painted window frames, low-pitched roofs; dzongs, chortens, prayer-flag poles. Thimphu is known for having no traffic lights (weak, could change).

## Pakistan (PK)

Quick facts
- Drive left. Plates by province (single source): Punjab white with "PUNJAB" on top; Sindh yellow with black embossed characters and "Sindh"; Khyber Pakhtunkhwa and Balochistan white with the province name; Islamabad white with a dark-blue left strip; Gilgit-Baltistan black with white; AJK white with a chinar leaf.
- Scripts: Urdu in Nastaliq with English; Sindhi Arabic script with extra dotted letters in Sindh; Pashto (ټ ډ ړ ښ ږ) in Khyber Pakhtunkhwa and north Balochistan.
- Phone +92: 021 Karachi, 042 Lahore, 051 Islamabad/Rawalpindi, 091 Peshawar, 081 Quetta, 061 Multan, 041 Faisalabad; mobiles 03xx. Postal 5 digits. TLD .pk.
- Landscape: irrigated Indus plains, Thar and Balochistan deserts, Karakoram and Himalaya in the north; heavily decorated trucks and buses.

### Nastaliq Urdu
- Look for: slanting, hanging Perso-Arabic script with English beside it
- Points to: Pakistan
- Strength: medium
- Counterexamples: Urdu signs in Indian cities (Hyderabad, Lucknow, Delhi, J&K); Afghanistan uses straighter Naskh-style Pashto and Dari
- Verify: `textgeo.py --text "<string>"`
- Source: general knowledge

## Maldives (MV)

Quick facts
- Drive left; few roads outside Malé, Hulhumalé and Addu. Script: Thaana (Dhivehi), right-to-left, unique to the Maldives; English widely. Phone +960, 7 digits. TLD .mv.
- Landscape: flat coral islands, white sand, coconut palms; Malé packed with mid-rise buildings and scooters.

## Kazakhstan (KZ)

Quick facts
- Drive right.
- Plates (since August 2012): black on white, 3 digits + 3 Latin letters + 2-digit region code boxed at the right, flag and KZ at the left. Pre-2012 plates start with a region letter (A Almaty city, Z Astana, B Almaty region…).
- Road paint: white, post-Soviet style (unverified).
- Script: Kazakh Cyrillic with Ә Ғ Қ Ң Ө Ұ Ү Һ І beside Russian; a Latin Kazakh alphabet is being phased in (completion date unverified).
- Phone +7 (shared with Russia; Kazakh numbers start +7 6 or +7 7): 7172 Astana, 727 Almaty, 7252 Shymkent, 7212 Karaganda; mobiles 70x, 747, 77x.
- Postal: 6-digit legacy codes (010000 Astana, 050000 Almaty). TLD .kz.

### Kazakh plate region code
- Look for: the boxed two-digit number at the right end of the plate
- Points to: 01 Astana; 02 Almaty city; 03 Akmola; 04 Aktobe; 05 Almaty region; 06 Atyrau; 07 West Kazakhstan; 08 Zhambyl; 09 Karaganda; 10 Kostanay; 11 Kyzylorda; 12 Mangystau; 13 Turkistan; 14 Pavlodar; 15 North Kazakhstan; 16 East Kazakhstan; 17 Shymkent; 18 Abai; 19 Jetisu; 20 Ulytau
- Strength: strong for registration (national format); medium for location
- Counterexamples: Astana and Almaty cars everywhere; codes 18-20 belong to regions created in 2022, so older cars there carry 05, 09 or 16
- Verify: `refsheet.py regions "KZ:Almaty,KZ:Aqmola"`
- Source: en.wikipedia.org/wiki/Vehicle_registration_plates_of_Kazakhstan checked 2026-10

### Kazakh-only letters
- Look for: Ұ, Ә, І or Һ on signs (Қ, Ғ, Ң, Ө, Ү are shared with neighbours)
- Points to: Kazakhstan
- Strength: strong (official orthography)
- Counterexamples: Kazakh-speaking areas of Xinjiang (China, Arabic script there), western Mongolia (Bayan-Ölgii) and Russian border regions
- Verify: `textgeo.py --text "<string>"`
- Source: general knowledge

### Regions inside Kazakhstan
- North (Astana, Kostanay, Petropavl, Pavlodar): flat grain steppe, birch groves, cold-climate Soviet towns, more Russian signage.
- Centre (Karaganda, Ulytau): dry steppe and mining towns.
- South (Almaty, Taldykorgan, Shymkent, Turkistan, Taraz): Tian Shan snow peaks behind the city, irrigated orchards, poplar rows, adobe houses; more Uzbek in Turkistan region.
- West (Atyrau, Aktau, Aktobe, Oral): treeless desert, oil infrastructure, camels.
- East (Oskemen, Semey): Altai foothills, conifer forest.

## Kyrgyzstan (KG)

Quick facts
- Drive right; a share of right-hand-drive Japanese imports (weak).
- Plates (region codes since July 2016): black on white, 2-digit region code at the left with flag and KG under it, then 3 digits + 3 letters (01 123 ABC). Codes: 01 Bishkek, 02 Osh city, 03 Batken, 04 Jalal-Abad, 05 Naryn, 06 Osh region, 07 Talas, 08 Chüy, 09 Issyk-Kul. 1994-2016 plates start with a region letter (B Bishkek, O Osh, I Issyk-Kul, C or S Chüy, D Jalal-Abad, N Naryn, T Talas).
- Script: Kyrgyz Cyrillic with Ң Ө Ү (no Ә Ғ Қ Ұ Һ І); Russian widely used. Phone +996: 312 Bishkek, 3222 Osh. Postal 6 digits (720000 Bishkek). TLD .kg.
- Landscape: mountains in nearly every frame, summer yurts on high pastures, Issyk-Kul; the Fergana side (Osh, Jalal-Abad) has orchards and Uzbek-language signs.

## Uzbekistan (UZ)

Quick facts
- Drive right. Plates: black on white, 2-digit region code at the left with flag and UZ, then 01 A 123 BC (an alternative 01 123 ABC series also exists). Codes: 01 Tashkent city, 10 Tashkent region, 20 Sirdaryo, 25 Jizzakh, 30 Samarkand, 40 Fergana, 50 Namangan, 60 Andijan, 70 Kashkadarya, 75 Surkhandarya, 80 Bukhara, 85 Navoiy, 90 Khorezm, 95 Karakalpakstan.
- Script: Uzbek Latin (oʻ, gʻ, sh, ch) official; Cyrillic Uzbek (ў, қ, ғ, ҳ) on older signs; Russian in Tashkent; Karakalpak in the northwest.
- Cars: overwhelmingly locally built Chevrolet/Daewoo models (Cobalt, Nexia, Spark, Damas, Lacetti), very often white (general knowledge).
- Phone +998: 71 Tashkent; mobiles 9x. Postal 6 digits (100000 Tashkent). TLD .uz.

## Tajikistan (TJ)

Quick facts
- Drive right. Plates (since 2009-2010): 4 digits + 2 Latin letters + 2-digit region code at the right, flag and TJ at the left: 01 and 05 Dushanbe, 02 and 06 Sughd, 03 Khatlon, 04 Gorno-Badakhshan, 07 and 08 Districts of Republican Subordination.
- Script: Tajik Cyrillic with Ғ Ӣ Қ Ӯ Ҳ Ҷ; Persian street words (кӯчаи = street of, хиёбони = avenue of). Phone +992: 37 Dushanbe. Postal 6 digits (734000). TLD .tj.
- Landscape: high mountains (Pamirs), narrow river valleys with poplars.

## Turkmenistan (TM)

Quick facts
- Drive right. Plates: 2 letters + 4 digits + 2-letter region code (AB 1234 AG), flag and TM at the left; AG = Ashgabat (AH Ahal, BN Balkan, DZ Daşoguz, LB Lebap, MR Mary are likely but unverified).
- Script: Turkmen Latin with Ä Ç Ž Ň Ö Ş Ü Ý; Russian on older signs. Phone +993: 12 Ashgabat. Postal 6 digits (744000). TLD .tm.
- Ashgabat: white marble towers, gold domes, very wide empty boulevards, mostly white or light cars (unverified, fragile). Elsewhere: Karakum desert and irrigated oases.

## Russia, Asian part (short note; details in `europe.md`)

- Right-hand traffic; plates А 123 ВС with a region number at the right (24 Krasnoyarsk, 25 and 125 Primorsky, 27 Khabarovsk, 38 Irkutsk, 54 Novosibirsk, 55 Omsk, 03 Buryatia, 14 Yakutia, 41 Kamchatka, 65 Sakhalin, 75 Zabaykalsky).
- The Far East (Primorsky, Khabarovsk, Sakhalin, Amur, Kamchatka) has a very high share of right-hand-drive Japanese used cars.
- Buryatia and Tuva add Ө Ү (and Һ or Ң) to Cyrillic and have Mongolian-looking steppe and Buddhist temples; Russian plates and Russian-first signs separate them from Mongolia.

## Commonly confused

### Thailand / Cambodia / Laos
- Decisive: driving side (Thailand left; Cambodia and Laos right), then script (Thai loops and tall marks; Lao rounder and simpler; Khmer stacked letters).
- Plates: Thai province name on the bottom line; Cambodian Khmer + English province with blue characters; Lao province name on top of a yellow-orange plate.
- Support: Thai red-white kerbs and yellow centre lines; Cambodian US-dollar prices and red laterite; sparse signs in rural Laos.
- Trap: Isan speaks Lao but writes Thai; the Friendship Bridges change sides mid-span.

### Malaysia / Indonesia
- Plates: Malaysia black with a state letter, no date; Indonesia region letters + number + suffix letters with a month.year line, white plates since 2022.
- Vocabulary: MY Polis, Teksi, Bas, Kereta, Hospital, Universiti, Kedai; ID Polisi, Taksi, Bus, Mobil, Rumah Sakit, Universitas, Toko, Warung, Gang.
- Phone +60 (mobiles 01x) vs +62 (mobiles 08xx); yellow lines on Indonesian national roads.
- Borneo: Sabah S and Sarawak Q plates vs Kalimantan KB, KH, KT, KU, DA.

### Indonesia / Philippines
- Decisive: driving side (Indonesia left, Philippines right).
- Language: Tagalog ng, mga, sa, Barangay, Bawal vs Indonesian Jalan, Desa, Dilarang.
- Vehicles: jeepneys and sidecar tricycles vs angkot, becak and ojek; plates ABC 1234 vs B 1234 ABC.

### Singapore / Malaysia (Johor)
- Plates: Singapore S-series with a check letter, red off-peak plates; Johor black J plates. Each country's cars are common across the causeway.
- Singapore: 8-digit phones, 6-digit postcodes, numbered HDB blocks, almost no overhead wires; Johor: 07 area code, postcodes 79-86, more motorbikes, rougher verges.
- Trap: Singapore street names also use Jalan and Lorong.

### Japan / South Korea / Taiwan
- Decisive: script (kana, Hangul, Traditional Hanzi without kana).
- Driving side: Japan left; Korea and Taiwan right. Centre line: Japan white (yellow only where overtaking is banned); Korea and Taiwan yellow.
- Ground clues: Taiwan scooter boxes and red or yellow kerb lines; Korea big numbers on apartment blocks; Japan orange mirror poles and the inverted stop triangle.

### Hong Kong / Macau / mainland China
- Decisive: driving side (HK and Macau left, mainland right) and characters (Traditional vs Simplified).
- Plates: HK white front, yellow rear; Macau white on black; mainland blue, yellow or green with a province Hanzi. Cross-boundary cars carry two plates and appear on both sides.
- Macau: Portuguese street words and tiled name plaques.

### India / Bangladesh / Sri Lanka / Nepal
- Plates: India Latin state code; Bangladesh all-Bengali with Bengali digits; Sri Lanka province code with a yellow rear plate; Nepal red Devanagari (older) or embossed province plates.
- Bengali appears in both West Bengal and Bangladesh: West Bengal adds English and Hindi, Latin WB plates, 7xxxxx PIN codes and +91; Bangladesh is almost all Bengali.
- Sinhala exists only in Sri Lanka. Nepali vs Hindi: Nepal-only words (गाउँपालिका), red plates, +977. Bhutan: Dzongkha, painted wooden windows, BP plates.

### Kazakhstan / Kyrgyzstan / Mongolia / Russia
- Letters: Ұ Ә І Һ → Kazakhstan; Ң Ө Ү without Ә Қ Ұ → Kyrgyzstan; Ө Ү without Ң → Mongolia (or Buryatia); only standard Russian letters → Russia, or Russian-language signs anywhere in Central Asia.
- Plates: KZ 3 digits + 3 letters + code at the right; KG code at the left + 3 digits + 3 letters; MN 4 digits + 3 Cyrillic letters; RU letter, 3 digits, 2 letters + region number.
- Landscape: Mongolia treeless steppe and gers; Kyrgyzstan mountains in almost every frame; Kazakhstan flat steppe and grain. Phone: +7 6/7xx Kazakhstan, +7 3/4/8/9xx Russia, +996, +976.

### Vietnam / Cambodia
- Decisive: script (Vietnamese Latin with ư ơ đ and tone marks vs Khmer).
- Plates: Vietnamese province code first, yellow commercial plates; Cambodian Khmer + English province.
- Houses: narrow tall tube houses vs lower uniform shophouses and wooden stilt houses; Vietnamese red flags and red banners with yellow letters.
