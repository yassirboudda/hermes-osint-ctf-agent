#!/usr/bin/env python3
"""Maigret-powered username search for Hermes OSINT CTF.

Primary: use the installed `maigret` package (https://github.com/soxoj/maigret)
when available — 5900+ sites, tags, parsing, recursive IDs.

Fallback: curated offline subset in `data/maigret_subset.json` (top Alexa-ranked
sites without auth headers; NSFW/dating excluded) for soft-crawl CTF use.

OPSEC: dedicated $CTF_UA, hard site caps, no fuzz/bruteforce.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import sys
from itertools import permutations
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

ROOT = Path(__file__).resolve().parents[1]
SUBSET_PATH = Path(
    os.environ.get(
        "MAIGRET_SUBSET_PATH",
        str(ROOT / "data" / "maigret_subset.json"),
    )
)
UA = os.environ.get("CTF_UA", "HermesOsintCtfAgent/1.0")
TIMEOUT = int(os.environ.get("MAIGRET_TIMEOUT", "12"))
WORKERS = int(os.environ.get("MAIGRET_WORKERS", "16"))
DEFAULT_TOP = int(os.environ.get("MAIGRET_TOP", "100"))
MAX_TOP = int(os.environ.get("MAIGRET_MAX_TOP", "250"))
DEFAULT_EXCLUDE_TAGS = [
    t.strip()
    for t in os.environ.get("MAIGRET_EXCLUDE_TAGS", "nsfw,dating").split(",")
    if t.strip()
]


def normalize_username(raw: str) -> str:
    s = (raw or "").strip()
    s = re.sub(r"^@", "", s)
    s = re.sub(r"[/?#].*$", "", s).strip()
    return s


def maigret_installed() -> bool:
    try:
        import maigret  # noqa: F401

        return True
    except ImportError:
        return False


# ─── username permutations (Maigret-style, capped) ───────────────────────────


def permute_parts(parts: list[str], *, method: str = "strict", limit: int = 40) -> list[str]:
    """Generate username variants from name parts (inspired by maigret.permutator)."""
    clean = [re.sub(r"[^A-Za-z0-9]", "", p.lower()) for p in parts if p and p.strip()]
    clean = [c for c in clean if c]
    if not clean:
        return []
    seps = ["", "_", "-", "."] if method == "all" else ["", "_", "-"]
    out: list[str] = []
    seen: set[str] = set()
    for i in range(1, len(clean) + 1):
        for subset in permutations(clean, i):
            if i == 1:
                cand = subset[0]
                if cand not in seen:
                    seen.add(cand)
                    out.append(cand)
                continue
            for sep in seps:
                cand = sep.join(subset)
                if cand not in seen:
                    seen.add(cand)
                    out.append(cand)
                if len(out) >= limit:
                    return out
    return out[:limit]


# ─── offline subset checker ─────────────────────────────────────────────────


def load_subset() -> dict[str, Any]:
    if not SUBSET_PATH.is_file():
        raise SystemExit(f"Missing Maigret subset: {SUBSET_PATH}")
    return json.loads(SUBSET_PATH.read_text(encoding="utf-8"))


def _filter_sites(
    sites: dict[str, dict],
    *,
    top: int,
    tags: list[str] | None,
    exclude_tags: list[str] | None,
    names: list[str] | None,
) -> dict[str, dict]:
    tag_need = {t.lower() for t in (tags or [])}
    tag_ex = {t.lower() for t in (exclude_tags or [])}
    name_need = {n.lower() for n in (names or [])}
    rows = []
    for name, s in sites.items():
        stags = [t.lower() for t in (s.get("tags") or [])]
        if tag_ex and any(t in tag_ex for t in stags):
            continue
        if tag_need and not any(t in tag_need for t in stags):
            continue
        if name_need and name.lower() not in name_need:
            continue
        rank = s.get("alexaRank") or 10**6
        rows.append((rank, name, s))
    rows.sort()
    return {name: s for _, name, s in rows[:top]}


def _check_site(name: str, site: dict, username: str) -> dict[str, Any]:
    regex = site.get("regexCheck")
    if regex and not re.fullmatch(regex, username):
        return {
            "site": name,
            "status": "invalid_username",
            "exists": False,
            "url": (site.get("url") or "").replace("{username}", username),
            "tags": site.get("tags") or [],
            "alexaRank": site.get("alexaRank"),
        }

    url = (site.get("urlProbe") or site.get("url") or "").replace("{username}", username)
    result: dict[str, Any] = {
        "site": name,
        "url": (site.get("url") or url).replace("{username}", username),
        "probe": url,
        "tags": site.get("tags") or [],
        "alexaRank": site.get("alexaRank"),
        "checkType": site.get("checkType"),
        "exists": None,
        "status": "unknown",
        "http_code": None,
        "error": None,
    }
    if not url:
        result["error"] = "no_url"
        result["status"] = "error"
        return result

    headers = {"User-Agent": UA, "Accept": "*/*"}
    req = Request(url, headers=headers, method="GET")
    try:
        with urlopen(req, timeout=TIMEOUT) as r:
            body = r.read(250_000).decode("utf-8", errors="replace")
            code = r.status
            final = r.geturl()
    except HTTPError as e:
        code = e.code
        try:
            body = e.read(250_000).decode("utf-8", errors="replace")
        except Exception:
            body = ""
        final = url
    except (URLError, TimeoutError, OSError) as e:
        result["error"] = type(e).__name__
        result["status"] = "error"
        return result

    result["http_code"] = code
    if code in (401, 403, 429, 503):
        result["status"] = "blocked"
        result["error"] = f"http_{code}"
        return result

    check = site.get("checkType") or "status_code"
    presence = site.get("presenseStrs") or []
    absence = site.get("absenceStrs") or []

    exists = False
    if check == "status_code":
        exists = 200 <= code < 300
    elif check == "response_url":
        # claimed URLs usually stay on profile path; unclaimed often redirect away
        exists = username.lower() in (final or "").lower() and code < 400
    else:  # message
        if presence and any(p in body for p in presence):
            exists = True
        if absence and any(a in body for a in absence):
            exists = False
        elif not presence and 200 <= code < 300:
            exists = True

    result["exists"] = exists
    result["status"] = "claimed" if exists else "available"
    return result


def search_subset(
    username: str,
    *,
    top: int = DEFAULT_TOP,
    tags: list[str] | None = None,
    exclude_tags: list[str] | None = None,
    names: list[str] | None = None,
    workers: int = WORKERS,
) -> dict[str, Any]:
    username = normalize_username(username)
    if not username:
        raise SystemExit("Empty username")
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,64}", username):
        raise SystemExit(f"Refusing suspicious username shape: {username!r}")

    top = max(1, min(top, MAX_TOP))
    data = load_subset()
    sites = _filter_sites(
        data.get("sites") or {},
        top=top,
        tags=tags,
        exclude_tags=exclude_tags if exclude_tags is not None else DEFAULT_EXCLUDE_TAGS,
        names=names,
    )

    results: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as ex:
        futs = [ex.submit(_check_site, n, s, username) for n, s in sites.items()]
        for f in concurrent.futures.as_completed(futs):
            results.append(f.result())

    results.sort(key=lambda r: (r.get("alexaRank") or 10**6, r.get("site") or ""))
    claimed = [r for r in results if r.get("exists") is True]
    return {
        "tool": "maigret_cli",
        "engine": "subset",
        "inspired_by": "https://github.com/soxoj/maigret",
        "username": username,
        "subset_path": str(SUBSET_PATH),
        "subset_count": data.get("count"),
        "checked": len(results),
        "claimed_count": len(claimed),
        "accounts": claimed,
        "tags_filter": tags or [],
        "exclude_tags": exclude_tags if exclude_tags is not None else DEFAULT_EXCLUDE_TAGS,
        "note": (
            "Offline curated subset. Install `pip install maigret` and re-run with "
            "--engine full for 5900+ sites + socid parsing."
        ),
    }


# ─── full Maigret package ───────────────────────────────────────────────────


def search_full(
    username: str,
    *,
    top: int = DEFAULT_TOP,
    tags: list[str] | None = None,
    exclude_tags: list[str] | None = None,
    timeout: int = 30,
) -> dict[str, Any]:
    username = normalize_username(username)
    if not username:
        raise SystemExit("Empty username")
    top = max(1, min(top, MAX_TOP))

    import asyncio
    import logging

    from maigret.checking import maigret as maigret_search
    from maigret.sites import MaigretDatabase

    db = MaigretDatabase()
    # Prefer package resources; auto-update left to Maigret defaults when online
    try:
        import maigret as mg

        res = Path(mg.__file__).resolve().parent / "resources" / "data.json"
        db.load_from_path(str(res))
    except Exception:
        db.load_from_path(str(SUBSET_PATH))  # unlikely shape mismatch — last resort

    site_dict = db.ranked_sites_dict(
        top=top,
        tags=tags or [],
        excluded_tags=exclude_tags if exclude_tags is not None else DEFAULT_EXCLUDE_TAGS,
    )

    logger = logging.getLogger("hermes.maigret")
    logger.setLevel(logging.WARNING)

    results = asyncio.run(
        maigret_search(
            username=username,
            site_dict=site_dict,
            logger=logger,
            timeout=timeout,
            is_parsing_enabled=True,
        )
    )

    accounts = []
    for site_name, item in results.items():
        status = item.get("status")
        found = False
        try:
            found = bool(status and status.is_found())
        except Exception:
            found = False
        if not found:
            continue
        accounts.append(
            {
                "site": site_name,
                "url": item.get("url_user"),
                "http_status": item.get("http_status"),
                "rank": item.get("rank"),
                "ids_data": item.get("ids_data") or {},
                "tags": list(getattr(item.get("site"), "tags", []) or [])
                if item.get("site")
                else [],
            }
        )

    return {
        "tool": "maigret_cli",
        "engine": "full",
        "inspired_by": "https://github.com/soxoj/maigret",
        "username": username,
        "checked": len(results),
        "claimed_count": len(accounts),
        "accounts": accounts,
        "tags_filter": tags or [],
        "exclude_tags": exclude_tags if exclude_tags is not None else DEFAULT_EXCLUDE_TAGS,
        "note": "Full Maigret engine with socid_extractor parsing when available.",
    }


def search(
    username: str,
    *,
    engine: str = "auto",
    top: int = DEFAULT_TOP,
    tags: list[str] | None = None,
    exclude_tags: list[str] | None = None,
    workers: int = WORKERS,
) -> dict[str, Any]:
    use_full = engine == "full" or (engine == "auto" and maigret_installed())
    if engine == "full" and not maigret_installed():
        raise SystemExit("maigret package not installed — pip install maigret")
    if use_full:
        try:
            return search_full(
                username, top=top, tags=tags, exclude_tags=exclude_tags
            )
        except Exception as e:
            if engine == "full":
                raise
            # degrade to subset
            out = search_subset(
                username,
                top=top,
                tags=tags,
                exclude_tags=exclude_tags,
                workers=workers,
            )
            out["fallback_reason"] = f"full engine failed: {type(e).__name__}: {e}"
            return out
    return search_subset(
        username, top=top, tags=tags, exclude_tags=exclude_tags, workers=workers
    )


def tags_stats() -> dict[str, Any]:
    data = load_subset()
    return {
        "engine_available": maigret_installed(),
        "subset_count": data.get("count"),
        "tags_freq": data.get("tags_freq") or {},
        "source": data.get("source"),
    }


def main() -> None:
    p = argparse.ArgumentParser(description="Maigret-style username search (Hermes)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="Search sites for username")
    s.add_argument("username")
    s.add_argument("--top", type=int, default=DEFAULT_TOP, help=f"Max sites (cap {MAX_TOP})")
    s.add_argument("--tags", default="", help="Comma-separated tags (coding,social,…)")
    s.add_argument(
        "--exclude-tags",
        default=",".join(DEFAULT_EXCLUDE_TAGS),
        help="Comma-separated tags to exclude",
    )
    s.add_argument(
        "--engine",
        choices=("auto", "subset", "full"),
        default="auto",
        help="auto=full Maigret if installed else subset",
    )
    s.add_argument("--workers", type=int, default=WORKERS)

    perm = sub.add_parser("permute", help="Generate username variants from name parts")
    perm.add_argument("parts", nargs="+", help="e.g. john doe")
    perm.add_argument("--method", choices=("strict", "all"), default="strict")
    perm.add_argument("--limit", type=int, default=40)
    perm.add_argument(
        "--search-each",
        action="store_true",
        help="Also run subset search on each variant (soft-capped)",
    )
    perm.add_argument("--top", type=int, default=40)

    sub.add_parser("stats")
    sub.add_parser("status")

    ns = p.parse_args()
    if ns.cmd == "status":
        print(
            json.dumps(
                {
                    "maigret_installed": maigret_installed(),
                    "subset_path": str(SUBSET_PATH),
                    "subset_exists": SUBSET_PATH.is_file(),
                    "default_top": DEFAULT_TOP,
                    "max_top": MAX_TOP,
                    "exclude_tags": DEFAULT_EXCLUDE_TAGS,
                    "docs": "https://maigret.readthedocs.io/",
                },
                indent=2,
            )
        )
        return
    if ns.cmd == "stats":
        print(json.dumps(tags_stats(), indent=2))
        return
    if ns.cmd == "permute":
        variants = permute_parts(ns.parts, method=ns.method, limit=ns.limit)
        out: dict[str, Any] = {
            "tool": "maigret_cli",
            "cmd": "permute",
            "parts": ns.parts,
            "variants": variants,
            "count": len(variants),
        }
        if ns.search_each:
            hits = []
            for v in variants[: min(8, len(variants))]:  # hard soft-crawl cap
                r = search_subset(v, top=min(ns.top, 60))
                if r["claimed_count"]:
                    hits.append(
                        {
                            "username": v,
                            "claimed_count": r["claimed_count"],
                            "accounts": r["accounts"][:10],
                        }
                    )
            out["searches"] = hits
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return

    tags = [t for t in ns.tags.split(",") if t.strip()] or None
    excl = [t for t in ns.exclude_tags.split(",") if t.strip()]
    print(
        json.dumps(
            search(
                ns.username,
                engine=ns.engine,
                top=ns.top,
                tags=tags,
                exclude_tags=excl,
                workers=ns.workers,
            ),
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
