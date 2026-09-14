---
name: osintmapper
description: >-
  Control an OSINTMapper instance: login, list cases, create/update entities and links
  for CTF investigation graphs.
---

# OSINTMapper control

The agent can drive a mapper instance via HTTP API (credentials from `.env` only).

## Env
```bash
OSINTMAPPER_BASE_URL=https://****.example
OSINTMAPPER_USERNAME=****
OSINTMAPPER_PASSWORD=****
# optional after login:
OSINTMAPPER_TOKEN=****
```

## Commands
```bash
python3 tools/osintmapper_cli.py login
python3 tools/osintmapper_cli.py cases
python3 tools/osintmapper_cli.py get-case <case_id>
python3 tools/osintmapper_cli.py add-entity --case <id> --type person --label "Alice"
python3 tools/osintmapper_cli.py add-link --case <id> --from <eid> --to <eid>
```

## Practice
- Keep the graph updated as leads appear (people, domains, wallets, docs, events).
- Do not put secrets (passwords, session cookies) inside entity descriptions on shared maps.
