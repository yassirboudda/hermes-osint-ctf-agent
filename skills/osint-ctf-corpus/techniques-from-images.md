# Techniques & outils — digest vision + write-ups

Corpus pré-analysé pour Hackinator (économie tokens). Sources : APT Hunter, HEXA OSINT CTF V3, Synoslabs GEOINT quizzes, Cody Bernardy challenges, Gralhix OSINT exercises 001–010, Hacktoria, Mirai/Legacy WUs, Oscar Zulu (texte), NeutrOSINT, **Deep Threats write-up officiel**.

> Flags d’autres CTF = exemples de méthodo uniquement — **jamais** à coller sur Deep Threats.  
> **Règle tokens :** lire `images-digest.md` + ce fichier — **ne jamais** demander à DeepSeek d’analyser les PNG/JPG bruts.

---

## Catalogue d’outils (observés / cités)

### Décodage / forensics data
| Outil | Usage CTF |
|-------|-----------|
| **CyberChef** | Base64 / encodings ; recipe « From Base64 », Auto Bake ; pivot handle dans plaintext |
| hashes.com / CyberChef Magic | Identifier le type d’encodage avant decode |
| ExifTool / FotoForensics | Métadonnées image |
| `mount` / live Linux RO | Clé USB forensics (`ro,noexec`) — chemins `/media/...` |

### Username / SOCMINT
| Outil | Usage |
|-------|--------|
| **WhatsMyName Web** | Enum username multi-sites (ex. `_Tr0tsk1` → Twitter) |
| Sherlock / Maigret | Complément username |
| Twitter/X, Instagram, Facebook Pages | Bios, highlights, emails, logos → reverse image |
| LinkedIn | Emploi / historique / posts → Pastebin / GitHub ; **past experience** souvent = flag |
| Mastodon + Wayback | Pseudo X → Mastodon → snapshot profil ancien révèle identité |
| Reddit / Rosint | Parcours univ, mentor, docs partagés |
| ProtonMail (`@proton.me`) | Pivot privacy-mail fréquent |
| Google Docs (share UI) | Email auteur visible dans dialogue de partage (sans envoyer) |

### Archives / web history
| Outil | Usage |
|-------|--------|
| Wayback | Snapshots site / team pages / paste edits |
| archive.ph / Memento / urlscan | Voir `archival-hunt.md` |
| Google Street View **« See more dates »** | Chronolocation — objets disparus entre captures |
| Pastebin history / edited pastes | Versions antérieures du code |

### GEOINT
| Outil / signal | Usage |
|----------------|--------|
| Google Maps / Street View / Earth | Magasins, adresses, Pegman, contributeurs photo |
| Overpass / OSM | Requêtes POI |
| Google Lens / Yandex / Bing | Reverse image |
| Signage multilingual | Traduire enseignes (ex. chinois 文成手工扯面) |
| Co-visibilité magasins | Ralph Lauren + Caffè Nero ; Bolia + Falkoner Allé |
| Sponsors stade / LED boards | Lumen Field + CONCACAF + Scotiabank → date match |
| SunCalc / ombres | Estimation heure (quand présent dans WU) |
| Ferry / maritime | Edmonds–Kingston, Waterman Pier |
| Mapillary | Complément Street View |

### Code / GitHub / fichiers
| Méthode | Usage |
|---------|--------|
| **GitHub commit history / diffs** | Flag dans ancien commit (Stella Launch Solutions / k4menev) |
| PR titles / merge messages | Voir skill `github-osint` |
| Google Drive « Shared with me » | Fichiers thématiques ; owner « Couldn't load user » → pivot share link |
| Comments in source | Liens Drive / C2 / target_website |

### Niche OSINT
| Domaine | Outils |
|---------|--------|
| Chimie / molécules | MolView / JSME / PubChem / ChemSpider (ex. Ricinine → Ricin context) |
| Flight / vessel | FlightAware, AIS / MarineTraffic (corpus OZ Indopacifique) |
| Satellite | EOS / Copernicus mentions |
| Media server UI | Reconnaître Plex (ports typiques) en screenshot |
| **TinEye** | Première apparition image (tri crawl_date) — fake news / recycled pics |
| **Wigle.net** | SSID Wi‑Fi filmé → carte densités → zone ville |
| Zoo / webcam live | Logo cam + landmark fond (ex. California Tower) + météo historique |
| CyclOSM / OSM bike | Pistes cyclables quand Street View insuffisant |
| Instagram date userscript | `LBreda/Instagram-explicit-date` pour date exacte post |
| Twitter advanced search | `from:user since:YYYY-MM-DD until:YYYY-MM-DD` |
| NeutrOSINT / MX Proton | Existence Proton + domaines custom via MX `protonmail` |
| satellites.pro / Google Earth | POV + dates imagery alternatives à Maps |
| **Overpass Turbo** | Requêtes spatiales multi-tags (`around:`, bbox) |
| **Maltego** (passif) | Graphe personnes / comptes / emails |
| **PeakFinder** | Confirmer sommets depuis coords camp / photo |
| **FlightAware** | Pivot numéro de vol → destination |
| web-check / robots.txt | Dossiers cachés type `/FTP` |
| Behance | Pivot photographe quand IG/FB/Flickr vides |
| Copains d’avant | École / identité réelle FR |
| **TweetDeck** | Colonnes / decks monitoring `from:` + filtres |
| **Twitter/X Lists** | Lists créées par / contenant un profil |
| **Photopea / GIMP** | Levels, invert, stretch pour OCR panneaux |
| **Google Maps Traffic** | Restreindre zone géoloc convoy / route |
| **ffmpeg** (frames) | Extraire frames vidéo Twitter / YouTube |
| **Reference / humanitarian maps** | Villages non labellisés Google |
| **Earth Pro historique** | Quand imagery web insuffisante |

---

## Playbooks issus des images analysées

### 1) Lettre encodée → identité
1. Reconnaître Base64 (`==`, charset).
2. CyberChef **From Base64** → lire FR/EN.
3. Extraire pseudo (`_Tr0tsk1`).
4. WhatsMyName / Sherlock → Twitter.
5. Avatar + tweets → CV / LinkedIn → email (`trtsk211@gmail.com`) → employeurs (Rubius, BI.ZONE).
6. LinkedIn activité → Pastebin (`PBKB112`) → script → Google Drive (`russian_roulette.py`, dossier `ВАЖНО`).

### 2) Brand / page business → email → IG
1. Facebook Page (Fildargent) → email Proton.
2. Même handle Instagram (`azlamp19`) + bio + highlights (ordres, marques).
3. Reverse logo ; croiser sewing / fashion keywords.

### 3) GEOINT indoor / outlet
1. Brands visibles depuis l’intérieur (Ralph Lauren, Caffè Nero).
2. Confirmer mall (Designer Outlet York) + date Street View.
3. Annoter logos / piliers / vitrines pour match.
4. Pour resto : enseigne native + couleur infra (conduits rouges) + Maps metadata (Wen Cheng 4, Berlin Schönhauser Allee).

### 4) Chronolocation Street View
1. Fixer adresse (ex. 31 Falkoner Allé, Copenhagen / Bolia).
2. **See more dates** pour trouver l’époque où l’objet-flag était présent.
3. Croiser POI voisins (Forno a Legna, Hostrupsvej).

### 5) Event / stade depuis vidéo
1. Lire LED : « WELCOME TO LUMEN FIELD », tournoi (CONCACAF Champions League).
2. Couleurs fans + sponsors (Qatar Airways, Subway) → date match.
3. Confirmer équipe domicile (Sounders).

### 6) Chimie screenshot
1. Reproduire / identifier structure (MolView).
2. PubChem → nom (Ricinine) → contexte OSINT (castor / ricin) — **passif uniquement**.

### 7) GitHub sanitize
1. Ne pas faire confiance au tree live.
2. Commits → diffs (`target_website` → vrai nom entreprise).
3. Wayback page équipe pour membres disparus.

### 8) Webcam / zoo
1. Reconnaître UI cam (logo, pop-out).
2. Query `species + zoo + webcam`.
3. Landmark arrière-plan (tour, skyline) pour confirmer.
4. Attendre rotation cam ou Street View enclosure ; météo pour température.

### 9) Image recyclée / fake news
1. TinEye trié par date croissante (pas Google Lens seul).
2. Traduire articles non-EN ; croiser Wikipedia / agences.
3. Crédit photographe ≠ contexte tweet → fake.

### 10) SSID filmé (Cody #10)
1. Ignorer hotspot perso (5G / nom perso).
2. SSID unique → Wigle → villes candidates → Street View détails sol (bouche d’égout, peinture).

### 11) Hacktoria « contract » GEOINT
1. Lire hints (pays, police, heure) mais **vérifier** si photo = Street View daté (peut diverger du briefing).
2. AIS / MarineTraffic pour ports ; couverture SV faible = filtre fort.
3. Pivot téléphone / enseigne locale → FB groups → ville puis SV limité.

### 12) Chronolocation événement culturel
1. Bannière expo / LED stade / journal.
2. Street View **See more dates** pour poster présent/absent.
3. Site officiel expo / billets pour date + venue.

### 13) Overpass spatial (HEXA V2 / Medileak / Indopacifique)
1. Encoder 2–3 tags observés (ex. `religion` + `leisure=pitch`, `pharmacy` near `restaurant`, `place_of_worship` + radar).
2. `around:` / bbox pour intersection spatiale.
3. Confirmer candidats en Street View.

### 14) Graphe relations (AEGE / Maltego)
1. Email → holehe (Strava, Flickr, …).
2. Même local-part → FB/Twitter.
3. Couple / amis / Telegram / Wikipedia edits → cartographie Maltego (passif).

### 15) Mesure objet sur photo (forêt 2026)
1. Inclure une échelle (règle) dans le cadre.
2. Annoter longueurs (mm) → tables calibre / dimensions objet.
3. Croiser reverse image si branding visible.

### 16) Webcam port / cam sécurité (Gralhix #022)
1. Lire overlay nom + timestamp cam.
2. Chercher feed live homonyme.
3. Landmark industriel + véhicule pour géoloc / chrono entre captures.

### 17) Hacktoria / Yandex-first GEOINT
1. Sauver image → zoom exhaustif (enseignes, filigrane Google SV).
2. Yandex reverse avant Google/Bing (souvent meilleur hors-Ouest).
3. TinEye si objet unique (statue, café disparu).
4. Street View **timeline** pour éléments temporaires.
5. Photopea/GIMP : levels / invert pour panneau illisible.

### 18) Indoor branding → coords
1. Logos / langue / domaine (.nz, Māori…).
2. FB page lieu + salles nommées.
3. Compter panneaux / murs pour position table/objet.
4. Maps indoor / pin exact.

### 19) Traffic Maps + TweetDeck
1. Mot-clés vidéo → TweetDeck colonnes similar.
2. Région approximative → Google Maps **traffic** pour goulot.
3. Confirmer landmark unique.

### 20) Earth Pro seul / sat Maxar
1. Earth Pro historique si web insuffisant.
2. Lire copyright sat (Maxar année) + pin toponyme.
3. Pattern route/forêt/jardins pour match village.

### 21) Geoblock / archives
1. Wayback + autres archives avant VPN.
2. `site:domain keyword` pour URL profonde.
3. Ne pas se fier au paywall live.

### 22) Twitter Lists / monitoring
1. Lists créées par handle ; lists *contenant* le handle.
2. TweetDeck : decks, `from:`, filtres.
3. Négatif utile (pas de lists) = aussi une donnée.

---

## Checklist challenge « je ne sais pas par où commencer »

1. Lister **tous** les strings : emails, handles, domaines, coords, marques, langues.
2. Encoder ? → CyberChef.
3. Username ? → WhatsMyName + réseaux.
4. Photo lieu ? → reverse image + Street View + enseignes.
5. URL morte ? → archival-hunt complet.
6. Repo/code ? → github-osint + commits.
7. Document/CV ? → pivots emploi/écoles/emails.
8. Corréler ≥2 sources avant de proposer un flag.
9. Logger timeline dans `memories/ctf-journal.md`.
10. **Jamais submit** sans OK team Discord.

---

## Fichiers corpus associés
- Digests vision : `images-digest.md` (ce playbook complète)
- `apt-hunter-full.md`, `wu-hexa-*`, `wu*-cody*`, `wu*-osint-exercise-*`, `wu*-hacktoria-*`, `wu*-geoint*`, `wu3-neutrosint*`, `wu3-exemple-concret*`, `oz-wu-*.md`
- Images brutes : hors prompt DeepSeek ; résultats vision déjà dans `images-digest.md`.
