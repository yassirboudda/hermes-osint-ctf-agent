# LLM providers

Hermes OSINT CTF Agent supports three OpenAI-compatible backends. Pick independently for orchestrator vs sub-agents.

| Id (`ORCHESTRATOR_PROVIDER` / `SUBAGENT_PROVIDER`) | Portal / console | Inference base URL | Env key |
|----------------------------------------------------|------------------|--------------------|---------|
| `deepseek` | [platform.deepseek.com](https://platform.deepseek.com/) | `https://api.deepseek.com` | `DEEPSEEK_API_KEY` |
| `openrouter` | [openrouter.ai](https://openrouter.ai/) | `https://openrouter.ai/api/v1` | `OPENROUTER_API_KEY` |
| `nousresearch` | [portal.nousresearch.com](https://portal.nousresearch.com) | `https://inference-api.nousresearch.com/v1` | `NOUS_API_KEY` |

## Nous Research (Hermes)

1. Create an account / subscription / credits on **https://portal.nousresearch.com**
2. Generate an API key (Bearer auth — see [API docs](https://portal.nousresearch.com/api-docs))
3. Put it in `.env`:

```bash
NOUS_API_KEY=****
NOUS_BASE_URL=https://inference-api.nousresearch.com/v1
NOUS_MODEL=Hermes-4.3-36B   # or Hermes-4-70B / Hermes-4-405B

ORCHESTRATOR_PROVIDER=nousresearch
SUBAGENT_PROVIDER=nousresearch
```

Aliases accepted for the key: `NOUSRESEARCH_API_KEY`, `NOUS_PORTAL_API_KEY`.

## CLI helper

```bash
python3 tools/llm_providers.py list
python3 tools/llm_providers.py status          # never prints secrets
python3 tools/llm_providers.py resolve --role orchestrator
python3 tools/llm_providers.py resolve --provider nousresearch
python3 tools/llm_providers.py chat "hello" --provider deepseek
```

Defaults live in `config/models.yaml`.
