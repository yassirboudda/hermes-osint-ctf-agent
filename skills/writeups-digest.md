# Write-ups digest (techniques + image OCR) — offline corpus

**Purpose:** pré-digérer les write-ups OSINT pour que DeepSeek n’ait pas à re-fetcher/re-OCR les pages.  
Corpus brut : `skills/osint-ctf/corpus/` (APT Hunter full, Oscar Zulu pages, Tacosint, Synoslabs GEOINT/HEXA/Cody).

**Lire d’abord :** `corpus/techniques-from-images.md` + `corpus/images-digest.md` (vision déjà faite — **ne pas** re-analyser les images avec DeepSeek).

> Les flags d’**autres** CTF sont des **exemples de méthodo**, jamais à coller sur Deep Threats.

---

## Batch 3 — Gralhix + Hacktoria + outils (pré-digéré)

Corpus : `wu2-osint-exercise-*`, `wu3-osint-exercise-*`, `wu*-hacktoria-*`, `wu3-neutrosint*`, `wu3-exemple-concret-de-geoint.md`, Cody restants.

| Série | Patterns clés (détail vision dans images-digest) |
|-------|--------------------------------------------------|
| OSINT Ex. 001–010 | Satellite/Earth annoté ; webcam zoo + landmark ; TinEye fake news ; Street View dates (Tutankhamon) ; Lens + Shen Yun ; IG date script + CyclOSM Tirana ; Twitter advanced search Benin |
| Hacktoria | Satellite côte Galice ; AIS + SV Bocas de Ceniza ; téléphone taxi → Maldives Addu ; park Berkeley/SF |
| Cody #7–12 / #10 | SunCalc ; Lumen Field seats ; Wigle SSID ; Lens Carpinteria |
| NeutrOSINT | Proton existence + MX custom domains |
| GEOINT sans Lens | Serrant / Inter-Kando — observations d’abord |

## Batch 4 — Tacosint + Oscar Zulu + Gralhix 011–032

| Source | Fichiers | Patterns |
|--------|----------|----------|
| HEXA V2 | `wu4-write-up-hexa-ctf-v2.md` | Overpass spatial, Lens, EXIF GPS, FlightAware, Wigle |
| AEGE 2022 | `wu4-write-up-hunt-aege-2022.md` | holehe→Strava/Flickr, Maltego graphe, FB/Twitter pivots |
| Appel forêt 2026 | `wu4-write-up-l-appel-de-la-foret-2026.md` | mesure objet/échelle, WhatsMyName, SOCMINT |
| OZ Medileak / Disparues / Indo / IE / Rhino / ML3 | `oz4-*.md`, `oz4-wu-medileak-2-pdf.md` | FB+SV, Overpass, FlightAware, Wayback, EXIF→Behance, PeakFinder |
| Gralhix 011–032 | `wu4-gralhix-exercise-*.md` | briefings + covers (cam port, sat thermique, etc.) |

## Batch 5–6 — Gralhix walkthroughs + techniques

| Source | Fichiers | Patterns |
|--------|----------|----------|
| Hacktoria WT 01–14 | `wu5-walkthrough-hacktoria-*` | Yandex-first, TinEye, SV dates, Photopea |
| Cake indoor / filetype / AFG maps / SS IDP / Wagner / eagle / Balakliya | `wu5-*` | branding indoor, dorks, reference maps, FB movement, traffic Maps |
| TweetDeck / Lists / geoblock / Earth-only / UA GEOINT | `wu6-*` | colonnes TweetDeck, lists X, Wayback geoblock, Earth Pro, SV Cyrillic |

---

## Archival Hunt (rappel obligatoire)
Wayback → archive.ph → Memento → urlscan (HTTP+DOM) + view-source. Voir `archival-hunt.md`.

---

## APT Hunter CTF (Synoslabs) — playbook condensé

Source: https://synoslabs.com/blog/apt-hunter-ctf-writeup/  
Équipe Incompetent Detectives (MBAY, Kortez, Bouddah, KrowZ) — 3000 pts.

### Image OCR / captures digérées
- **Logo APT HUNTER** : crâne + circuits + drapeau CTF sur le A.
- **Dashboard score** : 87.23% solves / 12.77% fails ; score final 3000 ; catégories FR (*Le point d’entrée*, *L’escalade d’un hacker*, *Un projet ambitieux*, etc.).
- **Page Welcome CTF** (texte FR) : interdiction scans/red team ; pas de partage de flags ; accents comptent ; **5 tentatives/flag** ; support Discord `#aide-ctf` ; validation welcome = `lu et accepté`.

### Chaîne méthodo → résultat (patterns réutilisables)

| Pattern | Méthode | Exemple de finding |
|--------|---------|-------------------|
| Pseudo encodé | Base64 / CyberChef / hashes.com | `_Tr0tsk1` |
| Pseudo → identité | WhatsMyName → Twitter → CV tweet | Andrejew Vladlen |
| Emploi | LinkedIn + CV + Google | Rubius |
| Code dev | LinkedIn activité → Pastebin | Pastebin / `russian_roulette.py` |
| Identité crypto/handle | Pivot comptes | K4menev, etc. |
| **GitHub archaeology** | Historique commits / diffs (pas seulement HEAD) | **Stella Launch Solutions** (nom entreprise dans un commit antérieur, repo https://github.com/k4menev/) |
| Site entreprise | Live + Wayback équipe | Matilda Beck (R&D) ; membre disparu via Wayback |
| Backdoor / page cachée | robots.txt + urlscan / screenshots | URL construite pour être cachée |
| GEOINT / screens | landmarks, EXIF, reverse image | challenges ondes / conversations |

### Règle d’or GitHub (APT Hunter)
> Code live peut être **sanitized**. Toujours ouvrir **commits / PR / merges** ; le flag était dans le **diff d’un ancien commit** (`target_website` remplacé → nom réel Stella Launch Solutions).

---

## Oscar Zulu write-ups (index)
https://oscarzulu.org/write-ups/ — séries : Medileak 1/2/3, Indopacifique, Intelligence économique, Challenges du Rhino, CtF disparue(s).  
Fichiers texte pré-fetch : `corpus/oz-*.md`.

Thèmes récurrents : GEOINT FR, archives web, SOCMINT passif, corrélation multi-sources.

---

## Tacosint (GitHub)
Repos `corpus/tacosint-repos.md` — outils/scripts OSINT à réutiliser en cage.

---

## Recurring playbooks (général)

### Username / alias
**Prioritize** Instant Username–style (`tools/instant_username.py` / [instantusername.com](https://instantusername.com/)) → Rosint Reddit archives (`tools/rosint_reddit.py` / [rosint.dev](https://www.rosint.dev/)) → Sherlock/Maigret/WhatsMyName → reverse image bio pics → emails liés.  
One-shot: `python3 tools/username_osint.py pivot <handle>`.

### Email
Holehe → GHunt/Epieos → OSINT Industries **when keyed** (quota 4–5). If no Industries key, stay on free tools above.

### Image / geolocation
EXIF → Yandex/Bing/Lens → landmarks → OSM/Overpass → GeoSpy hypothèses.

### Domain / org
crt.sh, SecurityTrails, Wayback **+** archive.ph **+** Memento **+** urlscan.

### GitHub / code history
`github-osint` + PAT : commits, PR titles/bodies, merges, gists, Events, `git log -S 'CTF{'`, clone en cage.

### Social / SOCMINT
Comptes jetables + captcha solvers si règles CTF OK ; Gmail dédié ; **jamais SE**.

---

## Anti-patterns
- Submit flags tôt / guessing brûle les tentatives.
- S’arrêter à Wayback seul.
- Lire seulement le tree GitHub live.
- Brûler OSINT Industries.
- Shodan/SpiderFoot agressifs (Deep Threats = passif).
