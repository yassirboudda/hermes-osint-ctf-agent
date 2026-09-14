#!/usr/bin/env python3
"""OSINT Industries client — API key auth (https://api.osint.industries/misc/docs)."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# Reuse quota guard
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from osint_industries_guard import consume, remaining  # noqa: E402


def api_key() -> str:
    k = os.environ.get("OSINT_INDUSTRIES_API_KEY", "")
    if not k or "****" in k:
        raise SystemExit("Set OSINT_INDUSTRIES_API_KEY in .env (API key, not cookies)")
    return k


def base() -> str:
    return os.environ.get("OSINT_INDUSTRIES_BASE_URL", "https://api.osint.industries").rstrip("/")


def get(path: str, params: dict | None = None) -> dict:
    from urllib.parse import urlencode

    url = f"{base()}{path}"
    if params:
        url += "?" + urlencode(params)
    req = Request(
        url,
        headers={
            "Authorization": f"Bearer {api_key()}",
            "Accept": "application/json",
            "User-Agent": os.environ.get("CTF_UA", "HermesOsintCtfAgent/1.0"),
        },
    )
    try:
        with urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except HTTPError as e:
        raise SystemExit(f"HTTP {e.code}: {e.read()[:500]!r}") from e
    except URLError as e:
        raise SystemExit(f"URL error: {e}") from e


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("quota")
    q = sub.add_parser("lookup")
    q.add_argument("query")
    q.add_argument("--type", default="email", help="Depends on API — see official docs")
    ns = p.parse_args()
    if ns.cmd == "quota":
        print(json.dumps({"remaining": remaining()}, indent=2))
        return
    consume(ns.query)
    # Endpoint path is illustrative — adjust to current OSINT Industries OpenAPI
    print(json.dumps(get("/v1/search", {"q": ns.query, "type": ns.type}), indent=2))


if __name__ == "__main__":
    main()
