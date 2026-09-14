# Règles d’or OPSEC — CTF OSINT

> Incident déclencheur : ban CTFd Deep Threats pour « Fuzzing site LNN ».  
> Objectif : **ne plus jamais** se faire ban pour fingerprint / agressivité / confusion avec le navigateur quotidien.

---

## 0. Mandat OSINT (rappel)

- OSINT / archives / WHOIS / reverse image / corrélation uniquement.
- **Interdit** : bruteforce, fuzz dir/path, scans, exploits, IDOR, SE, spam de requêtes.
- Si le challenge dit « OSINT only » → **zéro** wordlist, **zéro** ffuf/gobuster/dirsearch, **zéro** boucle HEAD/GET.

---

## 1. Isoler l’identité technique (le plus important)

### 1.1 User-Agent

**Ne jamais** utiliser le User-Agent par défaut de la machine / de Chromium quotidien / de `curl` stock.

| Mauvais | Bon |
|---------|-----|
| UA Chrome Ubuntu de ta session desktop | UA **dédié CTF**, figé dans un fichier env du CTF |
| UA partagé entre boulot, perso et CTF | Un UA **par compétition**, jamais réutilisé après |
| Copier le UA d’un HAR perso | Générer un UA plausible mais **distinct** |

Exemple (à adapter à chaque CTF — **ne pas** recopier tel quel d’un CTF à l’autre) :

```bash
# /chemin/ctf-YYYY/env/opsec.env
export CTF_UA='Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'
# PAS le Chrome 152 Ubuntu de ta machine
```

Tout `curl`, script, browser-use, Playwright doit lire `$CTF_UA`.

### 1.2 APIs et clés

**Ne jamais** utiliser la même clé API / même compte que le profil quotidien (Shodan, Apify, Google, Discord bot, etc.) pour du crawl CTF.

| Mauvais | Bon |
|---------|-----|
| Clé Shodan perso | Clé / compte **jetable CTF** ou pas d’API |
| Même Apify actor + même token | Token CTF séparé ou session manuelle |
| Tokens dans le shell history global | `secrets/` chmod 600, hors git |

### 1.3 Cookies / sessions

- Cookies HAR d’un CTF = **usage unique**, puis destruction.
- Ne pas mélanger cookie Discord perso / CTFd / VPN.
- Après CTF : purge HAR + cookies (déjà la procédure de fin).

### 1.4 IP / proxy

- Si VPN CTF fourni (ex. DGA) → **uniquement** ce canal pour le réseau cible.
- Ne pas scanner depuis l’IP maison + VPN en parallèle.
- Tor = onion uniquement ; pas de fuzz via Tor.

---

## 2. Soft crawl (anti-ban)

1. **≤ 5 navigations** par piste avant pause.
2. Gaps entre sessions (dizaines de secondes minimum ; plus si 429).
3. **Une URL** à la fois sur VPN instrumenté (détection %).
4. Préférer **archives** (Wayback, archive.ph, Memento) au live scrape.
5. Pas de parallélisme agressif (`xargs -P`, boucles concurrentes).
6. Sur 403/429 → **stop**, changer d’approche (archive / autre source), ne pas retry-storm.
7. Jamais `copy_selection` / actions qui trigger la télémétrie VPN si le CTF en a une.

---

## 3. Fuzz / enum — règle absolue

```
SI le règlement dit OSINT / interdit bruteforce
ALORS fuzz = INTERDIT (même « juste robots.txt + quelques paths »)
```

- Path guessing, dir enum, wordlists = **ban** (Deep Threats / LNN).
- « Je teste juste 20 URLs » reste du fuzz si non justifié par une source OSINT.
- Paths autorisés = ceux **trouvés** (robots.txt cité, lien HTML, WHOIS doc, hint officiel) — pas inventés.

---

## 4. Surfaces à ne plus toucher (post-ban)

Pour Deep Threats / Lianhua (historique) : ne plus requêter depuis outils auto :

- `deepthreats.fr`, `lianhuanews-network.info`, `lianhua.wiki`, `institut-lianhua*`
- domaines / IP / `.ln` du scénario via curl/WebFetch/browser/fuzz

Artefacts locaux déjà téléchargés = OK pour analyse offline.  
Si l’orga ban → Discord orga / fichiers locaux uniquement.

---

## 5. Checklist avant chaque requête réseau (CTF)

- [ ] UA = `$CTF_UA` dédié (≠ desktop)
- [ ] Clé API = compte CTF ou aucune
- [ ] Pas de wordlist / fuzz
- [ ] Source OSINT justifie l’URL exacte
- [ ] Rate soft + stop sur 403/429
- [ ] Logs : quoi / pourquoi / quand (journal CTF)

---

## 6. Fin de CTF — purge

1. Archiver skills/knowledge dans ce kit.
2. Supprimer **tous** les `.har`, dumps VPN, cookies CTF, `/tmp/*` liés.
3. Retirer le skill CTF de l’agent live (garder seulement ce dossier).
4. Ne pas laisser de secrets dans le chat / git.

---

*Hackinator — leçon Deep Threats 2026 — à lire avant tout futur CTF OSINT.*
