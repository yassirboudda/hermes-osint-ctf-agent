---
name: username-search
description: >-
  Instant Username–style multi-platform account discovery + Maigret + Rosint
  Reddit + optional OSINT Industries orchestrated pivot.
---

# Username search (Instant Username → Maigret → Rosint)

## Priority order (mandatory)
1. **Instant Username–style** — `tools/instant_username.py`  
   UI: https://instantusername.com/?q=<username>  
   Automation uses **WhatsMyName** (Instant Username has no public self-serve API).
2. **Maigret** — `tools/maigret_cli.py` ([soxoj/maigret](https://github.com/soxoj/maigret))  
   Tags, permutations, curated subset or full 5900+ site engine. See `skills/maigret/`.
3. **Rosint Reddit archives** — `tools/rosint_reddit.py` when Reddit is in scope or found.
4. **OSINT Industries** — `tools/osint_industries_client.py` **whenever** `OSINT_INDUSTRIES_API_KEY` is set.  
   If the key is missing / `****`, **skip Industries** and continue with free tools. Do not invent paid results.

One-shot pivot:
```bash
python3 tools/username_osint.py pivot wuan_xijiang
python3 tools/username_osint.py pivot wuan_xijiang --maigret-tags coding,social
python3 tools/username_osint.py status
```

## Instant Username CLI
```bash
python3 tools/instant_username.py search wuan_xijiang --limit 60
python3 tools/instant_username.py ui-url wuan_xijiang
python3 tools/instant_username.py refresh-wmn
```

## Maigret CLI (quick)
```bash
python3 tools/maigret_cli.py search wuan_xijiang --top 80
python3 tools/maigret_cli.py permute wuan xijiang --limit 25
# optional: pip install -r requirements-maigret.txt
python3 tools/maigret_cli.py search wuan_xijiang --engine full --top 200
```

Optional self-hosted / proxied Instant Username API:
```bash
# .env
INSTANTUSERNAME_API_BASE=https://your-ius-api.example
```

## Rules
- Expand handle variants **sparingly** (prefer `maigret_cli.py permute`) — no wordlist spam.
- Cap sites via `--limit` / `--top` / env caps.
- Correlate ≥2 sources before proposing a flag.

## Complements (do not replace)
- Holehe / GHunt / Epieos for **emails**
- OSINT Industries for deep paid enrichment **when keyed**
- `skills/github-osint` for GitHub archaeology after a hit
