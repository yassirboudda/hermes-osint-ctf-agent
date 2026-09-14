#!/usr/bin/env python3
"""OSINTMapper API helper — login, cases, entities, links (credentials from .env)."""
from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any, Dict, Optional
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def base() -> str:
    b = os.environ.get("OSINTMAPPER_BASE_URL", "").rstrip("/")
    if not b or "****" in b:
        raise SystemExit("Set OSINTMAPPER_BASE_URL in .env")
    return b


def ua() -> str:
    return os.environ.get("CTF_UA", "HermesOsintCtfAgent/1.0")


def request(
    path: str,
    method: str = "GET",
    body: Optional[dict] = None,
    token: Optional[str] = None,
) -> Any:
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": ua(),
    }
    tok = token or os.environ.get("OSINTMAPPER_TOKEN")
    if tok and "****" not in tok:
        headers["Authorization"] = f"Bearer {tok}"
    data = None if body is None else json.dumps(body).encode()
    req = Request(f"{base()}{path}", data=data, method=method, headers=headers)
    try:
        with urlopen(req, timeout=45) as r:
            raw = r.read().decode()
            return json.loads(raw) if raw else {}
    except HTTPError as e:
        raise SystemExit(f"HTTP {e.code}: {e.read()[:400]!r}") from e
    except URLError as e:
        raise SystemExit(f"URL error: {e}") from e


def cmd_login(_: argparse.Namespace) -> None:
    user = os.environ.get("OSINTMAPPER_USERNAME", "")
    pw = os.environ.get("OSINTMAPPER_PASSWORD", "")
    if not user or "****" in user:
        raise SystemExit("Set OSINTMAPPER_USERNAME / OSINTMAPPER_PASSWORD")
    data = request(
        "/api/auth/login",
        method="POST",
        body={"username": user, "password": pw},
    )
    token = data.get("token")
    print(json.dumps({"ok": bool(token), "token": "****" if token else None, "user": data.get("user")}, indent=2))
    if token:
        print("\n# export for this shell:", file=sys.stderr)
        print(f"export OSINTMAPPER_TOKEN={token}", file=sys.stderr)


def cmd_cases(_: argparse.Namespace) -> None:
    print(json.dumps(request("/api/cases"), indent=2, ensure_ascii=False))


def cmd_get_case(ns: argparse.Namespace) -> None:
    print(json.dumps(request(f"/api/cases/{ns.case_id}"), indent=2, ensure_ascii=False))


def cmd_add_entity(ns: argparse.Namespace) -> None:
    # Shape depends on mapper version — adjust fields as needed
    body = {
        "type": ns.type,
        "label": ns.label,
        "description": ns.description or "",
    }
    print(
        json.dumps(
            request(f"/api/cases/{ns.case}/entities", method="POST", body=body),
            indent=2,
            ensure_ascii=False,
        )
    )


def cmd_add_link(ns: argparse.Namespace) -> None:
    body = {"from": ns.from_id, "to": ns.to_id, "type": ns.link_type or "related"}
    print(
        json.dumps(
            request(f"/api/cases/{ns.case}/links", method="POST", body=body),
            indent=2,
            ensure_ascii=False,
        )
    )


def cmd_status(_: argparse.Namespace) -> None:
    print(
        json.dumps(
            {
                "base": base(),
                "has_token": bool(os.environ.get("OSINTMAPPER_TOKEN"))
                and "****" not in (os.environ.get("OSINTMAPPER_TOKEN") or ""),
            },
            indent=2,
        )
    )


def main() -> None:
    p = argparse.ArgumentParser(description="OSINTMapper control (secrets from .env)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    sub.add_parser("login")
    sub.add_parser("cases")
    g = sub.add_parser("get-case")
    g.add_argument("case_id")
    ae = sub.add_parser("add-entity")
    ae.add_argument("--case", required=True)
    ae.add_argument("--type", required=True)
    ae.add_argument("--label", required=True)
    ae.add_argument("--description", default="")
    al = sub.add_parser("add-link")
    al.add_argument("--case", required=True)
    al.add_argument("--from", dest="from_id", required=True)
    al.add_argument("--to", dest="to_id", required=True)
    al.add_argument("--link-type", default="related")
    ns = p.parse_args()
    {
        "status": cmd_status,
        "login": cmd_login,
        "cases": cmd_cases,
        "get-case": cmd_get_case,
        "add-entity": cmd_add_entity,
        "add-link": cmd_add_link,
    }[ns.cmd](ns)


if __name__ == "__main__":
    main()
