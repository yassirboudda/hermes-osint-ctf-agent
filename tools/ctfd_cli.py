#!/usr/bin/env python3
"""CTFd CLI — list/show challenges via session cookie; submit gated."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

ROOT = Path(__file__).resolve().parents[1]
SECRETS = Path(os.environ.get("HERMES_SECRETS", ROOT / "secrets"))


def load_session() -> Dict[str, Any]:
    if os.environ.get("CTFD_SESSION") and os.environ.get("CTFD_BASE_URL"):
        return {
            "base_url": os.environ["CTFD_BASE_URL"].rstrip("/"),
            "cookies": {"session": os.environ["CTFD_SESSION"]},
        }
    session_path = Path(os.environ.get("CTFD_SESSION_FILE", SECRETS / "ctfd_session.json"))
    if session_path.is_file():
        return json.loads(session_path.read_text(encoding="utf-8"))
    raise SystemExit(
        "Missing CTFd session. Set CTFD_BASE_URL + CTFD_SESSION in .env "
        "or create secrets/ctfd_session.json (see secrets/README.md)."
    )


def api(path: str, method: str = "GET", body: Optional[dict] = None) -> Any:
    sess = load_session()
    base = sess.get("base_url") or os.environ.get("CTFD_BASE_URL")
    if not base:
        raise SystemExit("CTFD_BASE_URL missing")
    cookie = "; ".join(f"{k}={v}" for k, v in (sess.get("cookies") or {}).items())
    ua = os.environ.get("CTF_UA", "HermesOsintCtfAgent/1.0")
    data = None if body is None else json.dumps(body).encode()
    req = Request(
        urljoin(base.rstrip("/") + "/", path.lstrip("/")),
        data=data,
        method=method,
        headers={
            "Cookie": cookie,
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": ua,
        },
    )
    try:
        with urlopen(req, timeout=45) as r:
            return json.loads(r.read().decode())
    except HTTPError as e:
        raise SystemExit(f"HTTP {e.code}: {e.read()[:400]!r}") from e
    except URLError as e:
        raise SystemExit(f"URL error: {e}") from e


def cmd_list(_: argparse.Namespace) -> None:
    data = api("/api/v1/challenges")
    print(json.dumps(data.get("data") or data, indent=2, ensure_ascii=False))


def cmd_show(ns: argparse.Namespace) -> None:
    data = api(f"/api/v1/challenges/{ns.id}")
    print(json.dumps(data, indent=2, ensure_ascii=False))


def cmd_submit(ns: argparse.Namespace) -> None:
    if not ns.i_have_team_approval:
        raise SystemExit(
            "Refusing submit: pass --i-have-team-approval after human/team OK."
        )
    csrf = os.environ.get("CTFD_NONCE") or ""
    body = {"challenge_id": ns.id, "submission": ns.flag}
    # Some CTFd setups need CSRF header — set CTFD_NONCE if required
    data = api("/api/v1/challenges/attempt", method="POST", body=body)
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main() -> None:
    p = argparse.ArgumentParser(description="CTFd OSINT helper (secrets from .env)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    sp = sub.add_parser("show")
    sp.add_argument("id", type=int)
    su = sub.add_parser("submit")
    su.add_argument("id", type=int)
    su.add_argument("flag")
    su.add_argument("--i-have-team-approval", action="store_true")
    ns = p.parse_args()
    {"list": cmd_list, "show": cmd_show, "submit": cmd_submit}[ns.cmd](ns)


if __name__ == "__main__":
    main()
