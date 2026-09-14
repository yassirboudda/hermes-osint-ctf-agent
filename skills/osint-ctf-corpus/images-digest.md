# Image digest — analyses vision (batches 2–3)

Analyses détaillées pour l’agent (ne **pas** re-OCR / ne pas renvoyer les images à DeepSeek).  
Sources images : `/tmp/hackinator-wu-imgs` (wu2-/wu3-*) — digérées ici.

> Flags / réponses d’autres CTF = **exemples de méthodo uniquement**, jamais à coller sur Deep Threats.

---

## APT Hunter
- **CyberChef** : recipe From Base64 → lettre FR, pseudo `_Tr0tsk1`.
- **WhatsMyName Web** : search `_Tr0tsk1` → Twitter only (1/590).
- **Twitter** `@_Tr0tsk1` : display Andrejew, avatar St-Basile Moscou, join Nov 2023.
- **CV Andrejew Vladlen** : email `trtsk211@gmail.com`, Tomsk ; Rubius / BI.ZONE pentester / NTR Labs ; TSU.
- **Pastebin** `pastebin.com/GShjtY3S` : « Русская рулетка », author **PBKB112**, edited, Python roulette.
- **Google Drive Shared** : folder `ВАЖНО`, `russian_roulette.py` (highlight), `kremlin.png`, `document.docx`, video Kalinka ; owners « Couldn't load user ».
- Leaderboard CTFd FR top10 all 3000 pts (Incompetent Detectives, Tacosint, Streetview Fighters…).

## HEXA OSINT CTF V3
- Stats : 466 users, 171 teams, 40 challenges CTFd, hardest « Do or do not. » (5 solves).
- Top1 Oscar Zulu 8600 ; Tacosint 2nd.
- Facebook **Fildargent** sewing → email **`azlamp19@proton.me`**.
- Instagram **`azlamp19`** / Alíz Lamp 🇭🇺 sewing ; highlights ORDERS (Dolce & Gabbana / SNK).
- Molécule 2D/3D (MolView-like) → **Ricinine** (castor / ricin context).

## GEOINT Synoslabs quizzes
- Indoor café → Ralph Lauren + Caffè Nero + exit EU → Designer Outlet York (Street View Oct 2021 annotated).
- Wen Cheng 4 Berlin : Maps metadata Schönhauser Allee / Sredzkistraße ; enseigne 文成手工扯面 ; conduits rouges + hublot bleu.
- Lost restaurant MondayQuiz (Julia) : enseigne chinoise + Falafel/Schawarma voisin + exit EU → Berlin Wen Cheng ; prix Wolt ≈ 18,50 €.

## Cody Bernardy challenges
- Copenhagen Falkoner Allé 31 / Bolia / Hostrupsvej — Street View Jul 2022 + **See more dates** (chrono). Annotations sol (tram tracks / paving).
- Waterman Pier / Edmonds–Kingston Ferry (Jun 2022, contributor Gabriel).
- Vidéo stade : **Lumen Field** Seattle, CONCACAF Champions League, Sounders green, sponsors Scotiabank/Qatar Airways/Subway → chronolocation match ; section/row/seat (ex. Section 230 Row J).
- Cody #7 Art Alley Lynchburg VA + **SunCalc** (ombre / heure).
- Cody #10 : SSID **HulaBula** (pas le hotspot « Thors Hammer ») → **Wigle.net** → Copenhagen → manhole + peinture jaune → Street View exact.
- Cody #12 drone sunset → Google Lens → Carpinteria CA / Linden–Sandyland.

## Mirai / Legacy
- UI **Plex** Sign In (reconnaissance service).
- Terminal `root@raspberrypi` `mount` → `/dev/sdb` on `/media/usbstick` **ext4 ro,noexec** (forensics USB).

---

## Gralhix OSINT Exercises (Synoslabs) — vision + findings

### Exercise 001 — Kiffa (Mauritanie)
- Photo tweet AR (matin) ; soleil à gauche → route vers sud, bord sud de **Kiffa**.
- Google Earth annoté : pin **« maison de L'hote kiffa moritania »** ; coords UI ≈ `16°36'31.19"N 11°23'52.60"W` ; imagery Maxar 2/9/2018 ; élévation ~120 m.
- Annotations : végétation (violet), compound (vert), arbres près guest house (bleu), bâtiment isolé (rouge).
- Croiser satellite alternatif (`satellites.pro`) + Google Earth POV.
- **Exemple flag méthodo :** `16.609407,-11.397771,19`

### Exercise 002 — Melbourne
- Gare **Flinders Street** ; tours brunes + docks + arbres.
- Structure haute : **FOCUS Apartments – 166 m**.
- Street View Feb 2023 pour confirmer quai.

### Exercise 003 — Ankara
- Briefing visite Farmaajo / Erdoğan avril 2017 → **Presidential Complex** Beştepe.
- Reverse image peut donner **faux positif** — prioriser contexte news + Maps.
- Coords approx. `39.931126, 32.799617`.

### Exercise 004 — Chuuk / Micronésie
- Resort île ; Google Earth chaîne Bahamas ≠ (piège) → **Oan Resort, Wonip, Chuuk**.
- Coords `7.363080, 151.755930` ; orientation **NW**.

### Exercise 005 — San Diego Zoo (polar cam)
- Screenshot webcam : 2 ours polaires, rochers artificiels, pin, baies rouges ; icône pop-out player.
- Pivot Google `polar bears zoo webcam` → sandiegozoo.org/cams/polar-cam ; logo coin = même cam.
- Autre angle cam : landmark **California Tower** (Balboa Park) en fond → confirme San Diego Zoo.
- Street View / Maps « Polar Bear Plunge » pour coords lit.
- Température via date/heure screenshot + météo historique (~16 °C).
- **Exemple :** a) San Diego Zoo b) ~16 °C c) `32.734453, -117.154573`

### Exercise 006 — Fake news / TinEye
- Tweet journaliste recycle une image → **TinEye** tri crawl_date ASC.
- Premier hit russe (Bagdad bombing) + Wikipedia DK Irakkrieg ; Flickr mort (Wayback vide).
- Photographe crédité **Eli J. Medellin** → conclusion **Fake news!**
- Règle : ne pas cliquer aveuglément sur sponsor TinEye.

### Exercise 007 — Lisbonne Tutankhamon
- Vue surélevée (vitrage) : sculpture fer **Homem-Sol** (Jorge Vieira) + bannière **TUTANKHAMON** + Lime scooters → Parque das Nações / Rossio dos Olivais.
- Street View Oct 2022 sans poster → **See more dates** → **2019** + site `https://tutankamon.pt/`.
- Coords ex. `38.767704, -9.096135`.

### Exercise 008 — Shen Yun / Norfolk
- Journal + Google Lens (traduction + match exact) → **Shen Yun Performing Arts**.
- Date **7 jan 2023** ; venue **Chrysler Hall, Norfolk, Virginia**.
- Enum tickets shenyun.com si besoin.

### Exercise 009 — Tirana bike / Visit Tirana
- Tweet Visit Tirana → IG photographe `four_s34sons` / Eriseld Myrto ; post `instagram.com/p/CouwRhAjsQ6/`.
- Userscript GitHub **Instagram-explicit-date** (LBreda) pour date exacte.
- Sunset Tirana (timeanddate) + orientation ouest ; **CyclOSM** pistes vélo.
- Street View **46 Kavaja St / Rruga e Kavajës** (juin 2016) : gratte-ciel verre, trottoir motif noir/blanc.
- **Exemple :** ~16:48 ; coords `41.326933, 19.807273`.

### Exercise 010 — Voodoo Benin
- Costumes **zangbeto** → festival vodoun Ouidah.
- CNN crédite photographe ; LinkedIn auteur ; Twitter `@dkitwood` advanced search `since:/until:` → était à **Cotonou** avant Ouidah.
- **Exemple :** a) Annual voodoo festival Benin b) 1ère+dernière photos = Dan Kitwood c) Cotonou.

---

## Hacktoria (Synoslabs) — vision

### Florida Snow
- Satellite annoté côte (jetée + X rouge, structure immergée rectangulaire, hangar bateaux, toits tuiles, vignes).
- Briefing : Espagne/France → **Cambados / Aldea O Facho** (Galice).
- Answer slug : `spain-cambados-aldea-o-facho`.

### The Cartel Connection
- MarineTraffic AIS Colombie (trafic nord) ; Street View pauvre → Barranquilla / Bocas de Ceniza.
- SV UI : **1111 Cl. 106, Atlántico**, août 2019 ; POI **Trencitos Artesanales Bocas de Ceniza** ; cargo bleu ; rails « trencito ».
- Answer : `calle-106-riomar-barranquilla-atlantico-colombia` (photo SV, pas forcément timestamp contrat).

### Where’s Klumgongyn
- Pivot téléphone **My Taxi** `6882122` / `3882122` → Facebook groupe Maldives.
- SV oct 2020 : Addu City / Hithadhoo, **Addu High School**, Nooraanee Magu × Kashinee Magu ; panneau TAXI MY TAXI ; tour telecom rouge/blanc.
- Answer : `maldives-elhe-didi-magu`.

### The Killer Clown
- Victim near Northwest Berkeley → parks SF Bay ; Street View match **Cedar Rose Park / Ohlone Greenway**.
- Password/answer : `cedar-rose-park-ohlone-greenway`.

---

## Autres captures digérées
- **Exemple GEOINT Alain Godon** : méthodo sans reverse image → Château de Serrant + festival Inter-Kando printemps 2024.
- **NeutrOSINT** (Kr0wZ) : check email Proton existant + MX custom domain (`dig`/`nslookup`) ; remplace ProtOSINT mort.
- **Link preview hacking** article Synoslabs : digéré texte (`wu3-hacker-la-previsualisation-des-liens.md`) — techniques OG/meta, pas images prioritaires.

---

## Batch 4 — Tacosint + Oscar Zulu + Gralhix 011–032

### HEXA OSINT CTF V2 (Tacosint GitHub)
- Vision **Overpass Turbo** : query `religion/building` ∩ `leisure=pitch` dans `around:500` (ex. Terengganu / Chendering MY) — pattern « mosquée près d’un terrain ».
- Patterns texte : Google Lens → Street View intersections ; **EXIF GPS** (ex. Chania) ; WhatsMyName ; Wigle ; holehe ; FlightAware ; Maltego ; Overpass multi-tags.
- Fichier : `wu4-write-up-hexa-ctf-v2.md` (+ images `wu4-write-up-hexa-ctf-v2-*`).

### Hunt AEGE 2022 (Tacosint)
- Vision **Maltego** : graphe relations (Telegram `anarchistedetaregion`, FB/Twitter/IG/LinkedIn/Strava/Flickr, emails, couples, Wikipedia RO).
- Playbook : email CV → **holehe** → Strava/Flickr ; FB handle = partie email ; Twitter `hunt{compte}` ; pivots couple/amis → groupe Telegram.
- Fichier : `wu4-write-up-hunt-aege-2022.md`.

### L’appel de la forêt 2026 (Tacosint)
- Vision : mesure douille annotée (L=2,80 cm, base 0,81, col 0,63) + règle 1″=2,54 → calibre type **5.7×28 mm** (méthodo mesure photo + scale).
- Patterns : WhatsMyName, Sherlock, FB/IG massifs, Overpass, Street View, Proton.
- Fichier : `wu4-write-up-l-appel-de-la-foret-2026.md`.

### Oscar Zulu (texte re-fetch `oz4-*`)
- **Medileak** : FB profil → adresse + Street View ; stage/parcelle cadastre ; archive site clinique (expérience cachée) ; robots.txt `/FTP` ; Overpass pharmacy∩restaurant ; FlightAware vol ACA871 ; WhatsMyName → Calendly ; Proton Drive backup mails.
- **Disparues** : LinkedIn ; **Wayback** posts supprimés ; EXIF → Behance (pas IG/FB/Flickr) ; Overpass `ruins=yes` ; mails pattern org ; Copains d’avant.
- **Indopacifique** : Overpass lieux de culte ; PeakFinder sommets ; Instagram géotag cricket ; Wayback imagery navire/IMO ; Flight/avion festival ; J-Alert audio ; Yandex/Lens.
- **Intelligence éco / Rhino / Medileak 3 finale** : digérés texte (`oz4-wu-*`, `oz4-medileak-3-finale.md`).
- **Medileak 2 PDF** (`oz4-wu-medileak-2-pdf.md`) : suite Raoul / clinique — legacy flags, Wayback, pivots WU Medileak 1.

---

## Batch 5 — Gralhix Hacktoria walkthroughs + techniques (vision + texte)

### Hacktoria geolocation walkthroughs (Sofia / Gralhix)
| # | Finding méthodo | Outils vision / texte |
|---|-----------------|------------------------|
| 01 | Île **Lauttasaari** (Helsinki) ; coords ≈ `60.1574, 24.8858` | Zoom marina, Street View |
| 02 | École **Het Perron** → ville via Maps ; reverse image faible | GIMP OCR enseigne, Yandex |
| 06 | Buste → TinEye/TripAdvisor Evora-like ; confirmer SV parking | TinEye, Yandex, Street View |
| 08 | Mosquée Turquie → **Ankara** `39.9529, 32.8013` | Yandex « Image appears to contain », Google Images `turkey sidewalk`, watermark Google 2020 |
| 10 | Café Jazz Espagne ; téléphone balcon **914295526** ; SV dates café | Bing/Google/Yandex, Street View timeline |
| 11 | Téléphérique Lisbonne ; venue + coords `38.7459, -9.1718` | Yandex focus câble ; zoo/parc satellite annoté (bassin blanc) |
| 12 | **Granada** `37.1832, -3.6064` ; limite 20 km/h urbaine ES | Street View abris bus, speed limit law May 2021 |
| 13 | **Adelaide** ; Photopea invert/levels pour panneau | Photopea, skyline+hills |
| 14 | Bus rouge Moyen-Orient → **Manama** | Wikipedia countries + image search bus |

### Techniques articles (Gralhix)
- **Indoor cake (NZ)** : branding Māori **E Tū Whānau** / `etuwhanau.org.nz` + FB page venue (**Tawa/Kauri** rooms) → plans panneaux 1–6 → coords table ; vision buffet + feuille carpet.
- **filetype:** dorking Google/Yandex/Bing → coords, drift buoys, docs internes.
- **Afghanistan reference maps** : cartes humanitaires / OSM labels locaux > Google seul ; Earth Pro historique ; ex. `35.012852, 69.597979`.
- **South Sudan IDPs** : tracker mouvements **Facebook** user (Kajo Keji / Equatoria) avant géoloc photos.
- **Wagner excavators** : TweetDeck similar videos + **Google Maps traffic** → Lipetsk oblast `53.069132, 39.873101`.
- **Bald eagle nest NASA** : tweet NASA → landmarks → `28.547877, -80.658811` + vérif.
- **Balakliya** : Google Lens sur texte tweet + police station Maps (UKR).
- **Small OSINT investigation** : EyesOnRussia / CIR map → railwebcams → vérifier coords avant conclure.
- **OSINT4FUN.eu** : index ressources / advent (hub).

---

## Batch 6 — Gralhix techniques + conflict geolocation (wu6)

### SOCMINT / accès contenu
- **Geoblock sans VPN** : Wayback / archives + `site:` pour URL directe (ex. Econodata BR) ; vision urbex (graffiti **NICOLAS**) = exemple contenu restreint / local.
- **TweetDeck monitoring** : decks + colonnes `from:user`, filtres ; dashboard multi-colonnes indépendantes.
- **Public Twitter Lists** : lists créées par compte ; lists contenant un profil ; vision UI Lists `@AusSpaceAgency` (négatif = pas de lists).
- **Geotagged tweets** : méthodes recherche tweets géolocalisés (fichier `wu6-how-to-find-geotagged-tweets-on-twitter.md`).
- **Twitter video geoloc** : frames via **ffmpeg** ou outil online → Yandex/Lens → Street View (attention date capture SV vs vidéo).

### GEOINT / sat
- **1 outil = Google Earth Pro** : village **Desnyanka** (Chernihiv, Maxar 2022) — dirt road / fence / forest edge ; web Earth limité.
- **Satellite change detection** : comparer dates imagery (fichier satellite changes).
- **Mariupol Chechen** : côte Sud ; SV juin 2021 toilette **ТУАЛЕТ** / **МКП ЗЕЛБУД** / lettre **М** ; annotations lignes/arbres/voitures.
- **Zoo UA damage** : site Ecopark + carte interne zoo → Street View.
- **Jets Vasylkiv** : lire ville dans vidéo ; scrub frames ; coords `50.21156, 30.317412` → EyesOnRussia.
- **Illustration author / 2 types of people** : SOCMINT attribution (fichiers wu6 correspondants).

> Contexte conflict zones = méthodo passive only ; pas de flags Deep Threats.

### Gralhix exercises 011–032 (briefings + covers)
- Types : ID personnes ; anomalies thermiques sat ; bio Twitter + phase Lune ; séisme magnitude/coords ; doc CIA déclassifié ; avion mil + lieu ; calendriers non-grégoriens ; coronation route ; transcript téléphone ; tablette choco+map ; **cam port Yanoto** (vision : overlay `Yanoto Fishing Port` + timestamp JST + véhicule surligné — feed live + géoloc véhicule) ; wallpaper YouTube frame ; groupes armés ; citations bâtiment ; zip train+photos ; Lima flags ; photographe movements ; train UK ; camps réfugiés ; girafe conservation ; aéroport TV.
- Pas de solutions officielles sur Gralhix — briefings + images challenge pour training patterns. Fichiers `wu4-gralhix-exercise-0XX.md`.
