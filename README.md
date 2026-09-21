# Hermes OSINT CTF Agent (public template)

Open-source **OSINT CTF agent template** used during events such as Deep Threats (DGA).  
Designed to run with **DeepSeek** as the orchestrator and **OpenRouter** sub-agents for heavy OSINT / vision / code tasks.

> **This repository contains NO live secrets.**  
> Every API key, cookie, refresh token, and password is a placeholder (`****`).  
> Copy `.env.example` → `.env` and fill with **your own** credentials.

## What you get

- Skills & knowledge for OSINT CTF methodology (archives, SOCMINT, GEOINT, stego, mail headers, on-chain testnets, legal docs in fictional nations, etc.)
- Tooling stubs: CTFd session client, OSINTMapper API control, OSINT Industries (API key), **Rosint-style Reddit archives**, **Instant Username–style** multi-site search, captcha solvers, Apify / Browser-Use hooks
- Hard **OPSEC** rules (dedicated UA, no fuzz, soft crawl) — learned the hard way
- Corpus of public OSINT write-up digests for technique recall

## Models

| Role | Provider | Model |
|------|----------|--------|
| Main agent (orchestrator) | DeepSeek | DeepSeek V4 / V4.1 (or current flagship) |
| Sub-agents | OpenRouter | **Any** model the DeepSeek orchestrator selects (Kimi, Claude, GPT, Gemini, Grok, …) |

Configure in `config/models.yaml` and `.env`.

## Quick start

```bash
git clone https://github.com/yassirboudda/hermes-osint-ctf-agent.git
cd hermes-osint-ctf-agent
cp .env.example .env
# edit .env — replace **** with YOUR keys only

python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Examples (read-only by default)
python3 tools/ctfd_cli.py list          # needs CTFD_* in .env
python3 tools/osintmapper_cli.py status # needs OSINTMAPPER_* in .env

# Username / Reddit (no paid key required)
python3 tools/username_osint.py pivot some_handle
python3 tools/rosint_reddit.py user some_handle          # like https://www.rosint.dev/?u=…
python3 tools/instant_username.py search some_handle     # like https://instantusername.com/?q=…
# OSINT Industries still used when OSINT_INDUSTRIES_API_KEY is set
```

Wire this folder as the skill/knowledge root of your Hermes / Cursor / custom agent runtime.

## Required third parties (bring your own keys)

See `.env.example` for the full list. Typical stack:

- **OSINT Industries** — API key ([docs](https://api.osint.industries/misc/docs))
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

## Disclaimer

For educational / authorized CTF use. Authors are not responsible for misuse.  
Do not attack real infrastructure. Respect each event’s rules and local law.

## License

MIT — see `LICENSE`.
