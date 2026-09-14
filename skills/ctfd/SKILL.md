---
name: ctfd-osint
description: >-
  Read-only CTFd helpers via session cookie (list/show challenges).
  Submit is hard-blocked without explicit approval flag.
---

# CTFd integration (session cookie)

## Purpose
During a CTF, the agent can **list** and **inspect** challenges using *your* CTFd session
(after you registered / logged in). Useful for inventory, point values, categories, and
descriptions — without manually clicking every challenge.

## Secrets
```bash
# .env
CTFD_BASE_URL=https://****.example
CTFD_SESSION=****
```

Or `secrets/ctfd_session.json` (gitignored).

## Commands
```bash
python3 tools/ctfd_cli.py list
python3 tools/ctfd_cli.py show <challenge_id>
# blocked unless you pass the approval flag:
python3 tools/ctfd_cli.py submit <id> <flag> --i-have-team-approval
```

## Rules
- Never commit real session cookies.
- Wrong flags / hints often cost points — human OK required for submit.
- Respect the event rules; this is for **authorized participation**, not bypassing access controls of third parties.
