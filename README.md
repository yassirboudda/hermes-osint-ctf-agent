<p align="center">
  <img src="static/hermes-osint-icon.png" alt="Hermes OSINT CTF Agent" width="128" height="128" />
</p>

<h1 align="center">Hermes OSINT CTF Agent</h1>

<p align="center">
  Open-source <b>OSINT CTF agent template</b> — pluggable LLM providers (DeepSeek · OpenRouter · Nous Hermes).<br/>
  Soft crawl · archives · username pivots · CTFd / OSINTMapper hooks.<br/>
  LLM providers: <b>DeepSeek</b> · <b>OpenRouter</b> · <b>Nous Research (Hermes)</b>.
</p>

<p align="center">
  <a href="https://github.com/yassirboudda/hermes-osint-ctf-agent/stargazers"><img src="https://img.shields.io/github/stars/yassirboudda/hermes-osint-ctf-agent?style=for-the-badge&logo=github&color=2dd4bf&labelColor=0b1220" alt="Stars" /></a>
  <a href="https://github.com/yassirboudda/hermes-osint-ctf-agent/blob/main/LICENSE"><img src="https://img.shields.io/github/license/yassirboudda/hermes-osint-ctf-agent?style=for-the-badge&color=f59e0b&labelColor=0b1220" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/OSINT-only-0ea5e9?style=for-the-badge&labelColor=0b1220" alt="OSINT only" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0b1220" alt="Python" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/DeepSeek-provider-4f46e5?style=flat-square&labelColor=111827" alt="DeepSeek" />
  <img src="https://img.shields.io/badge/OpenRouter-provider-10b981?style=flat-square&labelColor=111827" alt="OpenRouter" />
  <a href="https://portal.nousresearch.com"><img src="https://img.shields.io/badge/Nous%20Research-Hermes%20API-f43f5e?style=flat-square&labelColor=111827" alt="Nous Research" /></a>
  <a href="https://www.rosint.dev/"><img src="https://img.shields.io/badge/Rosint-Reddit%20archives-ff4500?style=flat-square&labelColor=111827" alt="Rosint" /></a>
  <a href="https://instantusername.com/"><img src="https://img.shields.io/badge/InstantUsername-pivots-06b6d4?style=flat-square&labelColor=111827" alt="Instant Username" /></a>
  <a href="https://github.com/soxoj/maigret"><img src="https://img.shields.io/badge/Maigret-5900%2B%20sites-e11d48?style=flat-square&labelColor=111827&logo=github" alt="Maigret" /></a>
  <img src="https://img.shields.io/badge/OSINT%20Industries-when%20keyed-8b5cf6?style=flat-square&labelColor=111827" alt="OSINT Industries" />
</p>

---

> **This repository contains NO live secrets.**  
> Every API key, cookie, refresh token, and password is a placeholder (`****`).  
> Copy `.env.example` → `.env` and fill with **your own** credentials.

## What you get

| Area | Capability |
|------|------------|
| Skills & corpus | OSINT CTF methodology, write-up digests, challenge patterns |
| Username pivots | **Instant Username**, **Maigret** (soxoj), Sherlock/WMN-compatible flows |
| Reddit archives | **Rosint-style** Arctic Shift + PullPush (`tools/rosint_reddit.py`) |
| Enrichment | **OSINT Industries** when API key is set (skipped if absent) |
| Platform hooks | CTFd, OSINTMapper, captcha solvers, Browser-Use / Apify |
| OPSEC | Dedicated UA, no fuzz / bruteforce / SE — see `opsec/` |

## Username priority

```text
Instant Username  →  Maigret  →  Rosint Reddit  →  OSINT Industries (if keyed)
```

One-shot:

```bash
python3 tools/username_osint.py pivot some_handle
```

## Models

Pick **any** of these OpenAI-compatible providers for orchestrator and/or sub-agents:

| Provider | Key (`.env`) | Base URL | Typical models |
|----------|--------------|----------|----------------|
| **DeepSeek** | `DEEPSEEK_API_KEY` | `https://api.deepseek.com` | `deepseek-chat`, `deepseek-reasoner` |
| **OpenRouter** | `OPENROUTER_API_KEY` | `https://openrouter.ai/api/v1` | Any OpenRouter slug |
| **Nous Research (Hermes)** | `NOUS_API_KEY` from [portal.nousresearch.com](https://portal.nousresearch.com) | `https://inference-api.nousresearch.com/v1` | `Hermes-4.3-36B`, `Hermes-4-70B`, `Hermes-4-405B` |

```bash
# .env — examples
ORCHESTRATOR_PROVIDER=deepseek          # or openrouter | nousresearch
SUBAGENT_PROVIDER=openrouter            # or nousresearch | deepseek

# All-Nous Hermes stack:
# ORCHESTRATOR_PROVIDER=nousresearch
# SUBAGENT_PROVIDER=nousresearch
# NOUS_API_KEY=sk-...
# NOUS_MODEL=Hermes-4-70B

python3 tools/llm_providers.py status
python3 tools/llm_providers.py resolve --role orchestrator
# python3 tools/llm_providers.py chat "ping" --provider nousresearch
```

Configure defaults in `config/models.yaml`. Portal API docs: https://portal.nousresearch.com/api-docs

## Quick start

```bash
git clone https://github.com/yassirboudda/hermes-osint-ctf-agent.git
cd hermes-osint-ctf-agent
cp .env.example .env
# edit .env — replace **** with YOUR keys only

python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# optional full Maigret engine (5900+ sites):
# pip install -r requirements-maigret.txt

# Examples (read-only by default)
python3 tools/ctfd_cli.py list          # needs CTFD_* in .env
python3 tools/osintmapper_cli.py status # needs OSINTMAPPER_* in .env

# Username / Reddit (no paid key required)
python3 tools/username_osint.py pivot some_handle
python3 tools/rosint_reddit.py user some_handle          # like https://www.rosint.dev/?u=…
python3 tools/instant_username.py search some_handle     # like https://instantusername.com/?q=…
python3 tools/maigret_cli.py search some_handle --top 80 # Maigret subset or full engine
python3 tools/maigret_cli.py permute john doe --limit 20
# OSINT Industries still used when OSINT_INDUSTRIES_API_KEY is set
```

Wire this folder as the skill/knowledge root of your Hermes / Cursor / custom agent runtime.

## Tool widgets

<p align="center">
  <a href="https://www.rosint.dev/?u=Wuan_Xijiang"><img src="https://img.shields.io/badge/Open-Rosint%20demo-ff4500?style=for-the-badge&logo=reddit&logoColor=white" alt="Rosint demo" /></a>
  <a href="https://instantusername.com/?q=wuan_xijiang"><img src="https://img.shields.io/badge/Open-InstantUsername%20demo-06b6d4?style=for-the-badge" alt="InstantUsername demo" /></a>
  <a href="https://github.com/soxoj/maigret"><img src="https://img.shields.io/badge/Upstream-Maigret-e11d48?style=for-the-badge&logo=github" alt="Maigret" /></a>
</p>

```bash
# Maigret skill helpers
python3 tools/maigret_cli.py status
python3 tools/maigret_cli.py stats
python3 tools/maigret_cli.py search soxoj --tags coding,social --top 100
```

Bundled curated site DB: [`data/maigret_subset.json`](data/maigret_subset.json) (~200 top sites, MIT attribution to [soxoj/maigret](https://github.com/soxoj/maigret)).

## Required third parties (bring your own keys)

See `.env.example` for the full list. Typical stack:

- **LLM providers** (pick any mix) — DeepSeek, OpenRouter, and/or **Nous Research Hermes** (`NOUS_API_KEY` from [portal.nousresearch.com](https://portal.nousresearch.com); see `docs/PROVIDERS.md`)
- **OSINT Industries** — API key ([docs](https://api.osint.industries/misc/docs)); used when set, skipped when absent
- **Rosint / Instant Username / Maigret** — no keys for free path; optional `pip install maigret` for full engine
- **Mailbox** — dedicated CTF mailbox (+ OAuth refresh if Gmail)
- **Captcha** — CapSolver and/or 2Captcha
- **Browser automation** — Browser-Use pool and/or Apify actors
- **Shodan** (passive only), optional GitHub PAT for commit archaeology
- **OSINTMapper** — self-hosted or team instance (agent can create/update entities via API)
- **CTFd** — session cookie after *your* registration (list/show challenges; submit gated)

## Hard rules (read before any CTF)

1. **OSINT only** unless the rules explicitly allow more.  
2. **No fuzzing, no wordlists, no exploits, no bruteforce** — this got accounts banned.  
3. Use a **dedicated User-Agent** and **CTF-only API keys** — never your daily desktop fingerprint.  
4. See `opsec/REGLES-DOR-OPSEC.md`.

## Skills map

| Skill | Path |
|-------|------|
| OSINT CTF core | `skills/osint-ctf/` |
| Username search | `skills/username-search/` |
| Maigret | `skills/maigret/` |
| Rosint Reddit | `skills/rosint-reddit/` |
| GitHub OSINT | `skills/github-osint/` |
| CTFd / Mapper / Captcha | `skills/ctfd/`, `skills/osintmapper/`, `skills/captcha-browser/` |

## Disclaimer

For educational / authorized CTF use. Authors are not responsible for misuse.  
Do not attack real infrastructure. Respect each event’s rules and local law.

Maigret subset data © [soxoj/maigret](https://github.com/soxoj/maigret) contributors (MIT).

## License

MIT — see `LICENSE`.
