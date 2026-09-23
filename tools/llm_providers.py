#!/usr/bin/env python3
"""Resolve LLM providers: DeepSeek | OpenRouter | Nous Research (Hermes).

Keys come from .env (never print them). Nous Portal keys are created at
https://portal.nousresearch.com and called against the OpenAI-compatible
endpoint https://inference-api.nousresearch.com/v1
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
MODELS_YAML = ROOT / "config" / "models.yaml"

PROVIDER_ALIASES = {
    "deepseek": "deepseek",
    "ds": "deepseek",
    "openrouter": "openrouter",
    "or": "openrouter",
    "nous": "nousresearch",
    "nousresearch": "nousresearch",
    "nous-research": "nousresearch",
    "nous_portal": "nousresearch",
    "portal": "nousresearch",
    "hermes": "nousresearch",
}

# Builtin fallbacks if models.yaml missing / incomplete
BUILTINS: dict[str, dict[str, Any]] = {
    "deepseek": {
        "label": "DeepSeek",
        "api_key_envs": ["DEEPSEEK_API_KEY"],
        "base_url_env": "DEEPSEEK_BASE_URL",
        "default_base_url": "https://api.deepseek.com",
        "default_model": "deepseek-chat",
        "model_envs": ["DEEPSEEK_MODEL", "ORCHESTRATOR_MODEL"],
    },
    "openrouter": {
        "label": "OpenRouter",
        "api_key_envs": ["OPENROUTER_API_KEY"],
        "base_url_env": "OPENROUTER_BASE_URL",
        "default_base_url": "https://openrouter.ai/api/v1",
        "default_model": "openrouter/auto",
        "model_envs": ["OPENROUTER_DEFAULT_MODEL", "SUBAGENT_MODEL"],
    },
    "nousresearch": {
        "label": "Nous Research (Hermes)",
        "api_key_envs": [
            "NOUS_API_KEY",
            "NOUSRESEARCH_API_KEY",
            "NOUS_PORTAL_API_KEY",
        ],
        "base_url_env": "NOUS_BASE_URL",
        "default_base_url": "https://inference-api.nousresearch.com/v1",
        "default_model": "Hermes-4.3-36B",
        "model_envs": ["NOUS_MODEL", "ORCHESTRATOR_MODEL", "SUBAGENT_MODEL"],
        "portal": "https://portal.nousresearch.com",
        "api_docs": "https://portal.nousresearch.com/api-docs",
    },
}


def _load_yaml() -> dict[str, Any]:
    if not MODELS_YAML.is_file() or yaml is None:
        return {}
    return yaml.safe_load(MODELS_YAML.read_text(encoding="utf-8")) or {}


def normalize_provider(name: str | None) -> str:
    key = (name or "").strip().lower().replace(" ", "")
    if key not in PROVIDER_ALIASES:
        raise SystemExit(
            f"Unknown provider {name!r}. Choose: deepseek | openrouter | nousresearch"
        )
    return PROVIDER_ALIASES[key]


def _key_configured(value: str | None) -> bool:
    if not value:
        return False
    v = value.strip()
    return bool(v) and "****" not in v


def _first_env(names: list[str]) -> str:
    for n in names:
        v = os.environ.get(n, "")
        if _key_configured(v):
            return v.strip()
    return ""


def provider_spec(provider: str) -> dict[str, Any]:
    provider = normalize_provider(provider)
    cfg = _load_yaml().get("providers", {}).get(provider, {}) or {}
    base = dict(BUILTINS[provider])
    # Merge yaml overlays
    if cfg.get("api_key_env"):
        base["api_key_envs"] = [cfg["api_key_env"]] + [
            e for e in base["api_key_envs"] if e != cfg["api_key_env"]
        ]
    if cfg.get("base_url_env"):
        base["base_url_env"] = cfg["base_url_env"]
    if cfg.get("default_base_url"):
        base["default_base_url"] = cfg["default_base_url"]
    if cfg.get("default_model"):
        base["default_model"] = cfg["default_model"]
    if cfg.get("default_model_env"):
        envs = list(base.get("model_envs") or [])
        base["model_envs"] = [cfg["default_model_env"]] + [
            e for e in envs if e != cfg["default_model_env"]
        ]
    if cfg.get("label"):
        base["label"] = cfg["label"]
    if cfg.get("portal"):
        base["portal"] = cfg["portal"]
    if cfg.get("api_docs"):
        base["api_docs"] = cfg["api_docs"]
    if cfg.get("models"):
        base["models"] = cfg["models"]
    if cfg.get("reasoning_system_prompt"):
        base["reasoning_system_prompt"] = cfg["reasoning_system_prompt"]
    base["id"] = provider
    return base


def resolve(
    provider: str | None = None,
    *,
    role: str | None = None,
    model: str | None = None,
) -> dict[str, Any]:
    """Resolve provider config for a role (orchestrator|subagent) or explicit name."""
    yml = _load_yaml()
    if provider:
        pid = normalize_provider(provider)
    elif role == "orchestrator":
        pid = normalize_provider(
            os.environ.get("ORCHESTRATOR_PROVIDER")
            or os.environ.get("LLM_PROVIDER")
            or (yml.get("orchestrator") or {}).get("provider")
            or "deepseek"
        )
    elif role in ("subagent", "subagents"):
        pid = normalize_provider(
            os.environ.get("SUBAGENT_PROVIDER")
            or os.environ.get("SUBAGENTS_PROVIDER")
            or (yml.get("subagents") or {}).get("provider")
            or "openrouter"
        )
    else:
        pid = normalize_provider(
            os.environ.get("LLM_PROVIDER")
            or os.environ.get("ORCHESTRATOR_PROVIDER")
            or "deepseek"
        )

    spec = provider_spec(pid)
    api_key = _first_env(list(spec["api_key_envs"]))
    base_url = (
        os.environ.get(spec["base_url_env"], "") or spec["default_base_url"]
    ).rstrip("/")
    # Ensure OpenAI-style /v1 for DeepSeek if user set host without path
    if pid == "deepseek" and not base_url.endswith("/v1"):
        # DeepSeek accepts both https://api.deepseek.com and .../v1
        pass

    resolved_model = model or ""
    if not resolved_model:
        if role == "orchestrator":
            resolved_model = os.environ.get("ORCHESTRATOR_MODEL", "")
        elif role in ("subagent", "subagents"):
            resolved_model = os.environ.get("SUBAGENT_MODEL", "")
    if not resolved_model:
        for env_name in spec.get("model_envs") or []:
            v = os.environ.get(env_name, "")
            if v and "****" not in v:
                resolved_model = v
                break
    if not resolved_model:
        if role == "orchestrator":
            resolved_model = (yml.get("orchestrator") or {}).get("model") or ""
        elif role in ("subagent", "subagents"):
            dm = (yml.get("subagents") or {}).get("default_model") or ""
            if isinstance(dm, str) and dm.startswith("${"):
                dm = ""
            resolved_model = dm
    if not resolved_model:
        resolved_model = spec["default_model"]

    return {
        "provider": pid,
        "label": spec["label"],
        "base_url": base_url,
        "model": resolved_model,
        "api_key_configured": bool(api_key),
        "api_key_envs": spec["api_key_envs"],
        "portal": spec.get("portal"),
        "api_docs": spec.get("api_docs"),
        "models": spec.get("models") or [],
        "openai_compatible": True,
        # Never return the raw key in status dumps — only for internal chat()
        "_api_key": api_key,
    }


def status() -> dict[str, Any]:
    out: dict[str, Any] = {"providers": {}, "roles": {}}
    for pid in ("deepseek", "openrouter", "nousresearch"):
        r = resolve(pid)
        out["providers"][pid] = {
            k: v for k, v in r.items() if not k.startswith("_")
        }
    out["roles"]["orchestrator"] = {
        k: v
        for k, v in resolve(role="orchestrator").items()
        if not k.startswith("_")
    }
    out["roles"]["subagents"] = {
        k: v
        for k, v in resolve(role="subagent").items()
        if not k.startswith("_")
    }
    out["env_hints"] = {
        "choose_orchestrator": "ORCHESTRATOR_PROVIDER=deepseek|openrouter|nousresearch",
        "choose_subagents": "SUBAGENT_PROVIDER=openrouter|nousresearch|deepseek",
        "global_alias": "LLM_PROVIDER=… (fallback for orchestrator)",
        "nous_key": "NOUS_API_KEY from https://portal.nousresearch.com",
        "nous_base": "NOUS_BASE_URL=https://inference-api.nousresearch.com/v1",
    }
    return out


def chat_completion(
    messages: list[dict[str, str]],
    *,
    provider: str | None = None,
    role: str | None = None,
    model: str | None = None,
    temperature: float = 0.2,
    max_tokens: int = 1024,
    timeout: int = 90,
) -> dict[str, Any]:
    """Minimal OpenAI-compatible chat.completions call (no streaming)."""
    cfg = resolve(provider, role=role, model=model)
    if not cfg["_api_key"]:
        envs = ", ".join(cfg["api_key_envs"])
        raise SystemExit(
            f"No API key for provider={cfg['provider']}. Set one of: {envs}"
        )
    url = f"{cfg['base_url'].rstrip('/')}/chat/completions"
    # DeepSeek default host often needs /v1
    if cfg["provider"] == "deepseek" and "/chat/completions" in url:
        if not cfg["base_url"].rstrip("/").endswith("/v1"):
            url = f"{cfg['base_url'].rstrip('/')}/v1/chat/completions"

    body = json.dumps(
        {
            "model": cfg["model"],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
    ).encode()
    headers = {
        "Authorization": f"Bearer {cfg['_api_key']}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": os.environ.get("CTF_UA", "HermesOsintCtfAgent/1.0"),
    }
    if cfg["provider"] == "openrouter":
        headers.setdefault("HTTP-Referer", "https://github.com/yassirboudda/hermes-osint-ctf-agent")
        headers.setdefault("X-Title", "Hermes OSINT CTF Agent")

    req = Request(url, data=body, headers=headers, method="POST")
    try:
        with urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode())
    except HTTPError as e:
        err = e.read()[:500]
        raise SystemExit(f"HTTP {e.code} from {cfg['provider']}: {err!r}") from e
    except URLError as e:
        raise SystemExit(f"URL error ({cfg['provider']}): {e}") from e

    choice = (data.get("choices") or [{}])[0]
    msg = choice.get("message") or {}
    return {
        "provider": cfg["provider"],
        "model": cfg["model"],
        "base_url": cfg["base_url"],
        "content": msg.get("content"),
        "reasoning_content": msg.get("reasoning_content"),
        "usage": data.get("usage"),
        "id": data.get("id"),
    }


def main() -> None:
    p = argparse.ArgumentParser(
        description="LLM provider helper (DeepSeek / OpenRouter / Nous Research)"
    )
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="Show configured providers (keys redacted)")
    sub.add_parser("list", help="List provider ids")

    r = sub.add_parser("resolve", help="Resolve active config for a role/provider")
    r.add_argument("--provider", default="")
    r.add_argument("--role", choices=("", "orchestrator", "subagent"), default="")
    r.add_argument("--model", default="")

    c = sub.add_parser("chat", help="One-shot chat.completions smoke test")
    c.add_argument("prompt")
    c.add_argument("--provider", default="")
    c.add_argument("--role", choices=("", "orchestrator", "subagent"), default="")
    c.add_argument("--model", default="")
    c.add_argument("--system", default="You are a concise OSINT CTF assistant.")
    c.add_argument("--max-tokens", type=int, default=256)

    ns = p.parse_args()
    if ns.cmd == "list":
        print(json.dumps(["deepseek", "openrouter", "nousresearch"], indent=2))
        return
    if ns.cmd == "status":
        print(json.dumps(status(), indent=2))
        return
    if ns.cmd == "resolve":
        cfg = resolve(
            ns.provider or None,
            role=ns.role or None,
            model=ns.model or None,
        )
        print(json.dumps({k: v for k, v in cfg.items() if not k.startswith("_")}, indent=2))
        return

    # chat
    messages = [
        {"role": "system", "content": ns.system},
        {"role": "user", "content": ns.prompt},
    ]
    print(
        json.dumps(
            chat_completion(
                messages,
                provider=ns.provider or None,
                role=ns.role or None,
                model=ns.model or None,
                max_tokens=ns.max_tokens,
            ),
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
