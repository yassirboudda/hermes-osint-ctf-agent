---
name: username-search
description: >-
  Instant Username–style multi-platform account discovery + orchestrated pivot
  with Rosint Reddit and optional OSINT Industries.
---

# Username search (Instant Username first)

## Priority order (mandatory)
1. **Instant Username–style** — `tools/instant_username.py`  
   UI: https://instantusername.com/?q=<username>  
   Automation uses **WhatsMyName** (same purpose; Instant Username has no public self-serve API).
2. **Rosint Reddit archives** — `tools/rosint_reddit.py` when Reddit is in scope or found.
3. **OSINT Industries** — `tools/osint_industries_client.py` **whenever** `OSINT_INDUSTRIES_API_KEY` is set.  
   If the key is missing / `****`, **skip Industries** and continue with free tools. Do not invent paid results.

One-shot pivot:
```bash
python3 tools/username_osint.py pivot wuan_xijiang
python3 tools/username_osint.py status
```

## Instant Username CLI
```bash
python3 tools/instant_username.py search wuan_xijiang --limit 60
python3 tools/instant_username.py ui-url wuan_xijiang
python3 tools/instant_username.py refresh-wmn
```

Optional self-hosted / proxied Instant Username API:
```bash
# .env
INSTANTUSERNAME_API_BASE=https://your-ius-api.example
```

## Rules
- Expand handle variants (case, `_`/`-`, leetspeak) **sparingly** — no wordlist spam.
- Cap sites via `--limit` / `INSTANTUSERNAME_MAX_SITES` (default 80).
- Correlate ≥2 sources before proposing a flag.
- Still use Sherlock / Maigret / WhatsMyName Web in browser if CLI is blocked.

## Complements (do not replace)
- Holehe / GHunt / Epieos for **emails**
- OSINT Industries for deep paid enrichment **when keyed**
- `skills/github-osint` for GitHub archaeology after a hit
