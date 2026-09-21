#!/usr/bin/env python3
"""Instant Username–style multi-platform account discovery.

Primary UX mirror: https://instantusername.com/?q=<username>
Automation path: WhatsMyName dataset (WebBreacher) — same job as Instant Username
(find where a handle exists), because the live Instant Username API is Cloudflare-
gated and has no public self-serve key.

Optional: set INSTANTUSERNAME_API_BASE if you run / proxy their check API.

Passive only — dedicated $CTF_UA, bounded concurrency, no fuzz.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

UA = os.environ.get("CTF_UA", "HermesOsintCtfAgent/1.0")
WMN_URL = os.environ.get(
    "WHATSMyNAME_DATA_URL",
    "https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json",
)
WMN_CACHE = Path(
    os.environ.get(
        "WHATSMyNAME_CACHE",
        str(Path(__file__).resolve().parents[1] / "cache" / "wmn-data.json"),
    )
)
IUS_API = os.environ.get("INSTANTUSERNAME_API_BASE", "").rstrip("/")
IUS_UI = "https://instantusername.com"
TIMEOUT = int(os.environ.get("INSTANTUSERNAME_TIMEOUT", "12"))
WORKERS = int(os.environ.get("INSTANTUSERNAME_WORKERS", "12"))
# Soft crawl: hard cap sites checked per run (never unbounded)
MAX_SITES = int(os.environ.get("INSTANTUSERNAME_MAX_SITES", "80"))

# High-signal platforms first (Instant Username–style priority set)
PRIORITY_NAMES = [
    "Reddit",
    "GitHub (User)",
    "GitHub (Gists)",
    "GitLab",
    "X",
    "Instagram",
    "TikTok",
    "YouTube",
    "Twitch",
    "Discord",
    "Steam",
    "LinkedIn",
    "Facebook",
    "Pinterest",
    "Tumblr",
    "Medium",
    "HackerNews",
    "Keybase",
    "Telegram",
    "Snapchat",
    "Flickr",
    "Behance",
    "DeviantArt",
    "Spotify",
    "SoundCloud",
    "Pastebin",
    "About.me",
    "Linktree",
]


def normalize_username(raw: str) -> str:
    s = (raw or "").strip()
    s = re.sub(r"^@", "", s)
    s = re.sub(r"[/?#].*$", "", s).strip()
    return s


def instantusername_ui(username: str) -> str:
    return f"{IUS_UI}/?q={quote(username)}"


def _headers() -> dict[str, str]:
    return {"User-Agent": UA, "Accept": "*/*"}


def load_wmn(force: bool = False) -> dict[str, Any]:
    if not force and WMN_CACHE.is_file():
        age = time.time() - WMN_CACHE.stat().st_mtime
        if age < 7 * 86400:
            return json.loads(WMN_CACHE.read_text(encoding="utf-8"))
    req = Request(WMN_URL, headers=_headers())
    with urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode())
    WMN_CACHE.parent.mkdir(parents=True, exist_ok=True)
    WMN_CACHE.write_text(json.dumps(data), encoding="utf-8")
    return data


def _priority_key(name: str) -> tuple[int, str]:
    try:
        return (PRIORITY_NAMES.index(name), name.lower())
    except ValueError:
        # fuzzy contains
        lower = name.lower()
        for i, p in enumerate(PRIORITY_NAMES):
            if p.lower() in lower or lower in p.lower():
                return (i, name.lower())
        return (10_000, name.lower())


def select_sites(
    sites: list[dict],
    *,
    categories: list[str] | None,
    names: list[str] | None,
    limit: int,
    include_nsfw: bool,
) -> list[dict]:
    out = []
    name_needles = [n.lower() for n in (names or [])]
    cat_set = {c.lower() for c in (categories or [])}
    for s in sites:
        cat = (s.get("cat") or "").lower()
        if not include_nsfw and "nsfw" in cat:
            continue
        sname = (s.get("name") or "").lower()
        if name_needles and not any(n == sname or n in sname for n in name_needles):
            continue
        if cat_set and cat not in cat_set:
            continue
        out.append(s)
    out.sort(key=lambda s: _priority_key(s.get("name") or ""))
    return out[:limit]


def _check_site(site: dict, username: str) -> dict[str, Any]:
    name = site.get("name") or "?"
    uri = (site.get("uri_check") or "").replace("{account}", quote(username, safe=""))
    result: dict[str, Any] = {
        "service": name,
        "category": site.get("cat"),
        "url": uri,
        "available": None,
        "exists": None,
        "status": None,
        "error": None,
        "protection": site.get("protection") or [],
    }
    if not uri:
        result["error"] = "no uri_check"
        return result
    req = Request(uri, headers=_headers(), method="GET")
    try:
        with urlopen(req, timeout=TIMEOUT) as r:
            body = r.read(200_000).decode("utf-8", errors="replace")
            code = r.status
    except HTTPError as e:
        code = e.code
        try:
            body = e.read(200_000).decode("utf-8", errors="replace")
        except Exception:
            body = ""
    except (URLError, TimeoutError, OSError) as e:
        result["error"] = type(e).__name__
        result["status"] = "error"
        return result

    result["http_code"] = code
    e_code = site.get("e_code")
    m_code = site.get("m_code")
    e_string = site.get("e_string") or ""
    m_string = site.get("m_string") or ""

    # Soft crawl: treat blocks / challenges as unknown, not "available"
    if code in (401, 403, 429, 503):
        result["exists"] = None
        result["available"] = None
        result["status"] = "blocked"
        result["error"] = f"http_{code}"
        return result

    exists = False
    matched = False
    if e_code is not None and code == e_code:
        if not e_string or e_string in body:
            exists = True
            matched = True
    if m_code is not None and code == m_code and (not m_string or m_string in body):
        exists = False
        matched = True
    elif m_string and m_string in body and e_string and e_string not in body:
        exists = False
        matched = True

    if not matched and e_code is not None and code != e_code and code != m_code:
        result["exists"] = None
        result["available"] = None
        result["status"] = "unknown"
        result["error"] = f"unexpected_http_{code}"
        return result

    result["exists"] = exists
    result["available"] = not exists
    result["status"] = "taken" if exists else "available"
    # Prefer pretty profile URL when provided
    pretty = (site.get("uri_pretty") or "").replace("{account}", quote(username, safe=""))
    if pretty and exists:
        result["url"] = pretty
    return result


def check_via_ius_api(username: str, service: str) -> dict[str, Any] | None:
    """Optional Instant Username API (self-hosted / proxied)."""
    if not IUS_API:
        return None
    url = f"{IUS_API}/check/{quote(service)}/{quote(username)}"
    req = Request(url, headers={**_headers(), "Accept": "application/json"})
    try:
        with urlopen(req, timeout=TIMEOUT) as r:
            return json.loads(r.read().decode())
    except Exception:
        return None


def search_username(
    raw: str,
    *,
    limit: int = MAX_SITES,
    categories: list[str] | None = None,
    names: list[str] | None = None,
    include_nsfw: bool = False,
    only_taken: bool = True,
    workers: int = WORKERS,
) -> dict[str, Any]:
    username = normalize_username(raw)
    if not username:
        raise SystemExit("Empty username")
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,64}", username):
        raise SystemExit(f"Refusing suspicious username shape: {username!r}")

    data = load_wmn()
    sites = select_sites(
        data.get("sites") or [],
        categories=categories,
        names=names,
        limit=limit,
        include_nsfw=include_nsfw,
    )

    results: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as ex:
        futs = [ex.submit(_check_site, s, username) for s in sites]
        for f in concurrent.futures.as_completed(futs):
            results.append(f.result())

    results.sort(key=lambda r: (_priority_key(r.get("service") or ""), r.get("service") or ""))
    taken = [r for r in results if r.get("exists") is True]
    available = [r for r in results if r.get("available") is True]
    blocked = [r for r in results if r.get("status") in ("blocked", "unknown", "error")]

    out = {
        "tool": "instant_username",
        "inspired_by": IUS_UI,
        "username": username,
        "instantusername_ui": instantusername_ui(username),
        "dataset": "WhatsMyName (WebBreacher)",
        "dataset_url": WMN_URL,
        "checked": len(results),
        "taken_count": len(taken),
        "available_count": len(available),
        "blocked_or_unknown_count": len(blocked),
        "accounts": taken if only_taken else results,
        "note": (
            "Automated checks use WhatsMyName rules (Instant Username has no public API). "
            "Open instantusername_ui in a browser for the live site UI."
        ),
    }
    if not only_taken:
        out["available"] = available
        out["blocked_or_unknown"] = blocked
    return out


def list_priority_sites() -> list[str]:
    data = load_wmn()
    names = sorted({s.get("name") for s in data.get("sites") or [] if s.get("name")})
    ordered = [n for n, _ in sorted(((n, _priority_key(n)) for n in names), key=lambda x: x[1])]
    return ordered[:60]


def main() -> None:
    p = argparse.ArgumentParser(
        description="Instant Username–style multi-site username search (WhatsMyName)"
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="Find platforms where username appears taken")
    s.add_argument("username")
    s.add_argument("--limit", type=int, default=MAX_SITES)
    s.add_argument("--workers", type=int, default=WORKERS)
    s.add_argument("--category", action="append", default=[], help="WMN category filter")
    s.add_argument("--site", action="append", default=[], help="Exact WMN site name")
    s.add_argument("--include-nsfw", action="store_true")
    s.add_argument(
        "--all",
        action="store_true",
        help="Include available + error rows (default: taken only)",
    )

    sub.add_parser("ui-url").add_argument("username")
    sub.add_parser("priority-sites")
    sub.add_parser("refresh-wmn")

    ns = p.parse_args()
    if ns.cmd == "ui-url":
        print(instantusername_ui(normalize_username(ns.username)))
        return
    if ns.cmd == "priority-sites":
        print(json.dumps(list_priority_sites(), indent=2))
        return
    if ns.cmd == "refresh-wmn":
        load_wmn(force=True)
        print(json.dumps({"cached": str(WMN_CACHE), "ok": True}, indent=2))
        return

    print(
        json.dumps(
            search_username(
                ns.username,
                limit=ns.limit,
                categories=ns.category or None,
                names=ns.site or None,
                include_nsfw=ns.include_nsfw,
                only_taken=not ns.all,
                workers=ns.workers,
            ),
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
