#!/usr/bin/env python3
"""Username OSINT orchestrator — prioritize free tools, keep OSINT Industries.

Priority (handles / Reddit):
  1. Instant Username–style multi-site search (`instant_username.py`)
  2. Maigret (`maigret_cli.py`) — tags, permutations, deep site DB
  3. Rosint-style Reddit archive (`rosint_reddit.py`)
  4. OSINT Industries — only when OSINT_INDUSTRIES_API_KEY is set (still used;
     never skip it when available). If the key is missing/placeholder, skip
     Industries and rely on free tools above.

Correlate ≥2 sources before proposing flags.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import instant_username as iu  # noqa: E402
import maigret_cli as mg  # noqa: E402
import rosint_reddit as rr  # noqa: E402


def industries_configured() -> bool:
    k = os.environ.get("OSINT_INDUSTRIES_API_KEY", "")
    return bool(k) and "****" not in k


def try_industries(query: str, qtype: str = "username") -> dict:
    """Call OSINT Industries if configured; never invent results."""
    if not industries_configured():
        return {
            "skipped": True,
            "reason": "OSINT_INDUSTRIES_API_KEY not set — using free tools only",
        }
    try:
        from osint_industries_guard import consume, remaining
        from osint_industries_client import get
    except ImportError as e:
        return {"skipped": True, "reason": f"import error: {e}"}

    try:
        consume(query, quiet=True)
    except SystemExit as e:
        return {"skipped": True, "reason": str(e), "remaining": 0}

    try:
        data = get("/v1/search", {"q": query, "type": qtype})
        return {
            "skipped": False,
            "remaining": remaining(),
            "data": data,
        }
    except SystemExit as e:
        return {"skipped": True, "reason": str(e), "remaining": remaining()}


def pivot(
    username: str,
    *,
    site_limit: int = 60,
    reddit_limit: int = 50,
    maigret_top: int = 80,
    maigret_tags: list[str] | None = None,
    skip_maigret: bool = False,
) -> dict:
    user = iu.normalize_username(username) or rr.normalize_username(username)
    if not user:
        raise SystemExit("Empty username")

    accounts = iu.search_username(user, limit=site_limit, only_taken=True)

    maigret_view: dict
    if skip_maigret:
        maigret_view = {"skipped": True, "reason": "--skip-maigret"}
    else:
        try:
            maigret_view = mg.search(
                user,
                engine="auto",
                top=maigret_top,
                tags=maigret_tags,
            )
            # keep orchestrator payload lean
            maigret_view = {
                "engine": maigret_view.get("engine"),
                "checked": maigret_view.get("checked"),
                "claimed_count": maigret_view.get("claimed_count"),
                "accounts": (maigret_view.get("accounts") or [])[:25],
                "note": maigret_view.get("note"),
                "fallback_reason": maigret_view.get("fallback_reason"),
            }
        except SystemExit as e:
            maigret_view = {"skipped": True, "reason": str(e)}

    reddit = rr.fetch_user(user, limit=reddit_limit)
    reddit_view = {
        "username": reddit["username"],
        "rosint_ui": reddit["rosint_ui"],
        "sources": reddit["sources"],
        "summary": reddit["summary"],
        "posts_preview": reddit["posts"][:15],
        "comments_preview": reddit["comments"][:15],
    }
    industries = try_industries(user, "username")

    return {
        "tool": "username_osint",
        "username": user,
        "priority": [
            "instant_username (WhatsMyName / InstantUsername UI)",
            "maigret (soxoj/maigret subset or full)",
            "rosint_reddit (Arctic Shift + PullPush)",
            "osint_industries (when API key present)",
        ],
        "instantusername": {
            "ui": accounts["instantusername_ui"],
            "taken_count": accounts["taken_count"],
            "accounts": accounts["accounts"],
            "checked": accounts["checked"],
        },
        "maigret": maigret_view,
        "rosint": reddit_view,
        "osint_industries": industries,
        "correlation_hint": (
            "Require ≥2 independent sources before proposing a flag. "
            "Rosint archives ≠ live Reddit; Instant Username / Maigret prove presence only."
        ),
    }


def main() -> None:
    p = argparse.ArgumentParser(description="Prioritized username OSINT pivot")
    sub = p.add_subparsers(dest="cmd", required=True)

    piv = sub.add_parser(
        "pivot",
        help="InstantUsername + Maigret + Rosint (+ Industries if keyed)",
    )
    piv.add_argument("username")
    piv.add_argument("--site-limit", type=int, default=60)
    piv.add_argument("--reddit-limit", type=int, default=50)
    piv.add_argument("--maigret-top", type=int, default=80)
    piv.add_argument(
        "--maigret-tags",
        default="",
        help="Comma-separated Maigret tags (coding,social,…)",
    )
    piv.add_argument("--skip-maigret", action="store_true")

    sub.add_parser("status").set_defaults(cmd="status")

    ns = p.parse_args()
    if ns.cmd == "status":
        print(
            json.dumps(
                {
                    "osint_industries_configured": industries_configured(),
                    "instantusername_ui": iu.IUS_UI,
                    "rosint_ui": "https://www.rosint.dev/",
                    "maigret_installed": mg.maigret_installed(),
                    "maigret_subset": str(mg.SUBSET_PATH),
                    "wmn_cache": str(iu.WMN_CACHE),
                },
                indent=2,
            )
        )
        return

    tags = [t for t in ns.maigret_tags.split(",") if t.strip()] or None
    print(
        json.dumps(
            pivot(
                ns.username,
                site_limit=ns.site_limit,
                reddit_limit=ns.reddit_limit,
                maigret_top=ns.maigret_top,
                maigret_tags=tags,
                skip_maigret=ns.skip_maigret,
            ),
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
