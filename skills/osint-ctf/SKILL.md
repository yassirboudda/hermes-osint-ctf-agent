---
name: osint-ctf
description: >-
  OSINT CTF methodology, tools, OPSEC, and challenge-solving patterns.
  Use for Capture The Flag OSINT events (archives, SOCMINT, GEOINT, stego, CTFd, mapping).
---

# OSINT CTF — Supercharged skill

## Methodology checklist
1. Scope the challenge text: names, handles, emails, domains, photos, coords, timestamps, flag format.
2. Passive only: public web, archives, WHOIS/crt.sh, reverse image, EXIF, social footprinting.
3. Correlate ≥2 independent sources before proposing a flag.
4. Log timeline in a local journal (not committed with secrets).
5. Never submit flags without human/team OK. Never SE / scan / bruteforce / exploit / fuzz.

## Models
- Orchestrator / sub-agents: **DeepSeek**, **OpenRouter**, or **Nous Research (Hermes)** — set in `.env`
- Helper: `python3 tools/llm_providers.py status` · docs: `../docs/PROVIDERS.md`

## Delegation
Hard OSINT / long context / vision → sub-agent provider (often OpenRouter multimodal or Hermes-4-405B); orchestrator stays on the chosen primary provider.

## Companion files
- `../skills/archival-hunt.md` — multi-archive SOP
- `../skills/writeups-digest.md` — technique digest
- `../skills/osint-ctf-corpus/` — offline write-up corpus
- `../knowledge/` — patterns learned in live CTFs (sanitized)
- `../opsec/REGLES-DOR-OPSEC.md` — mandatory before network I/O
- `../tools/` — CTFd, OSINTMapper, OSINT Industries, Rosint Reddit, Instant Username, Maigret, LLM providers helpers
- `../docs/PROVIDERS.md` — DeepSeek / OpenRouter / Nous Research setup
- `../skills/rosint-reddit/` — deleted/old Reddit history (Arctic Shift + PullPush)
- `../skills/username-search/` — Instant Username–first pivots; Industries when keyed
- `../skills/maigret/` — Maigret username OSINT (subset + optional full engine)

## Soft crawl / anti-ban
- Dedicated `$CTF_UA` ≠ desktop UA
- Dedicated API keys ≠ personal daily keys
- ≤5 navigations per lead; stop on 403/429
- Prefer archives over live scrape
- **Forbidden:** fuzz, wordlists, path guessing, exploits

## Tooling (bring your own keys)
See root `.env.example` and `docs/TOOLS.md`.
