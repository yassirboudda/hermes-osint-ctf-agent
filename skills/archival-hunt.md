# Archival Hunt SOP (flags historiques)

Quand une mission implique une URL / domaine / page disparue : **ne jamais s’arrêter à Wayback seul**. Enchaîner systématiquement les archives ci-dessous via **browser-use** (DOM + view-source).

## Checklist obligatoire

### 1. Wayback Machine — `https://web.archive.org/web/*/[TARGET_URL]`
- Ouvrir le calendrier de snapshots ; inspecter **plusieurs dates**.
- Pour chaque snapshot utile : texte rendu **et** source HTML (commentaires, scripts inline, meta).
- Snapshots de `/robots.txt`, `/sitemap.xml`, chemins cachés.
- Attendre le rendu DOM complet avant extraction (pages lentes CDX).

### 2. Archive.today — `https://archive.ph/[TARGET_URL]` (aussi archive.is / archive.vn)
- Chercher snapshots manuels.
- Si CAPTCHA : noter le blocage, passer à l’outil suivant (CapSolver seulement si nécessaire et autorisé).

### 3. Memento Time Travel — `http://timetravel.mementoweb.org/`
- Rechercher l’URL cible ; explorer archives nationales / WebCite / autres mementos.

### 4. URLScan.io — `https://urlscan.io/`
- Query : `domain:[TARGET_DOMAIN]` ou URL exacte.
- Onglet **HTTP** (headers cachés), **DOM** (chaînes `CTF{…}`, `flag{…}`, `FLAG{…}`).

## Règles d’exécution
- Toujours lire le **code source**, pas seulement le texte rendu.
- Prioriser aussi : historiques `/robots.txt`, `/sitemap.xml`, fuites `.git/` (passif, pas de scan agressif).
- Si snapshot lent : attendre le DOM (browser-use wait) avant extract.
- Dès qu’une chaîne matche un format flag : **reporter immédiatement** avec timestamp + source archive exacte (URL snapshot).
- Ne **jamais** submit CTFd sans OK team Discord.

## Outils complémentaires
- `curl` / API CDX Wayback pour lister timestamps rapidement, puis browser-use pour le contenu.
- GitHub OSINT (skill `github-osint`) si l’URL pointe vers un repo / org / gist.
