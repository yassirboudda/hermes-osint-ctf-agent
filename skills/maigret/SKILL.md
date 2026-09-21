---
name: maigret
description: >-
  Maigret username OSINT — multi-site account discovery, tags, permutations,
  and optional full engine (soxoj/maigret). Use for handle pivots in CTFs.
---

# Maigret username OSINT

Upstream: [soxoj/maigret](https://github.com/soxoj/maigret) (MIT) — 5,900+ sites, tags, recursive IDs, socid parsing.

Hermes wraps it with **soft-crawl** defaults (site caps, NSFW/dating excluded, `$CTF_UA`).

## When to use
- Challenge gives a **username / nickname / alias**
- Need cross-platform account map before email enrichment
- Want tag-filtered sweeps (`coding`, `social`, `gaming`, `us`, …)
- Name parts → username variants (`john` + `doe` → `johndoe`, `john_doe`, …)

## Priority in the agent stack
1. Instant Username–style (`tools/instant_username.py`)
2. **Maigret** (`tools/maigret_cli.py`) — deeper site DB + tags/permute
3. Rosint Reddit archives (`tools/rosint_reddit.py`)
4. OSINT Industries when `OSINT_INDUSTRIES_API_KEY` is set

```bash
python3 tools/username_osint.py pivot some_handle
```

## CLI
```bash
# status / tag stats
python3 tools/maigret_cli.py status
python3 tools/maigret_cli.py stats

# soft default: top 100 sites (subset or full if pip-installed)
python3 tools/maigret_cli.py search soxoj --top 80
python3 tools/maigret_cli.py search soxoj --tags coding,social --top 120

# force engines
python3 tools/maigret_cli.py search soxoj --engine subset
python3 tools/maigret_cli.py search soxoj --engine full   # needs: pip install maigret

# permutations (Maigret-style)
python3 tools/maigret_cli.py permute john doe --limit 30
python3 tools/maigret_cli.py permute john doe --search-each --top 40
```

## Full engine (optional)
```bash
pip install maigret
# or: pip install -r requirements-maigret.txt
```
Full engine enables socid profile parsing (`ids_data`) and the live 5900+ site DB.

## Data
- Bundled curated subset: `data/maigret_subset.json` (~200 top Alexa sites, no auth headers, nsfw/dating stripped)
- Attribution: Maigret / soxoj (MIT)

## OPSEC
- Never run unbounded `-a` / thousands of sites in a CTF cage
- Cap with `--top` / `MAIGRET_MAX_TOP`
- Exclude noisy tags via `MAIGRET_EXCLUDE_TAGS`
- Dedicated `$CTF_UA` only

## SOWEL mapping (from Maigret)
- SOTL-2.2 Search for accounts on other platforms
- SOTL-6.1 / 6.2 Login / nickname reuse
