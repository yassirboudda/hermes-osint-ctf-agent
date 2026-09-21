#!/usr/bin/env python3
"""Rosint-style Reddit archive OSINT — Arctic Shift + PullPush (deleted/private history).

Mirrors https://www.rosint.dev/ (https://github.com/zuxu4n/RedditOsint):
dual-source fetch, merge + dedupe by id, posts + comments.

No API key. Soft crawl only — dedicated $CTF_UA, no fuzz/bruteforce.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import sys
from datetime import datetime, timezone
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

ARCTIC = os.environ.get(
    "ROSINT_ARCTIC_BASE", "https://arctic-shift.photon-reddit.com"
).rstrip("/")
PULLPUSH = os.environ.get("ROSINT_PULLPUSH_BASE", "https://api.pullpush.io").rstrip("/")
DEFAULT_LIMIT = int(os.environ.get("ROSINT_LIMIT", "100"))
TIMEOUT = int(os.environ.get("ROSINT_TIMEOUT", "45"))
UA = os.environ.get("CTF_UA", "HermesOsintCtfAgent/1.0")

_URL_STRIP = re.compile(r"^https?://(www\.|old\.|new\.)?reddit\.com", re.I)


def normalize_username(raw: str) -> str:
    s = (raw or "").strip()
    s = _URL_STRIP.sub("", s)
    s = re.sub(r"^/+", "", s)
    s = re.sub(r"^(u|user)/", "", s, flags=re.I)
    s = re.sub(r"^@", "", s)
    s = re.sub(r"[/?#].*$", "", s).strip()
    return s


def _ua_headers() -> dict[str, str]:
    return {"Accept": "application/json", "User-Agent": UA}


def _get_json(url: str) -> tuple[bool, list[dict]]:
    req = Request(url, headers=_ua_headers())
    try:
        with urlopen(req, timeout=TIMEOUT) as r:
            payload = json.loads(r.read().decode())
        data = payload.get("data", []) if isinstance(payload, dict) else []
        if not isinstance(data, list):
            data = []
        return True, [x for x in data if isinstance(x, dict)]
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, OSError):
        return False, []


def _build_qs(
    username: str,
    *,
    limit: int,
    before: str | None = None,
    after: str | None = None,
    subreddit: str | None = None,
) -> str:
    parts = [
        ("limit", str(limit)),
        ("sort", "desc"),
        ("author", username),
    ]
    if subreddit:
        parts.append(("subreddit", subreddit))
    if before:
        parts.append(("before", before))
    if after:
        parts.append(("after", after))
    return urlencode(parts)


def _urls(
    username: str,
    kind: str,
    *,
    limit: int,
    before: str | None = None,
    after: str | None = None,
    subreddit: str | None = None,
    keywords: str | None = None,
) -> tuple[str, str]:
    qs = _build_qs(
        username, limit=limit, before=before, after=after, subreddit=subreddit
    )
    arctic_qs, pullpush_qs = qs, qs
    if keywords:
        from urllib.parse import quote

        kw = quote(keywords, safe="")
        if kind == "posts":
            arctic_qs += f"&query={kw}"
        else:
            arctic_qs += f"&body={kw}"
        pullpush_qs += f"&q={kw}"
    if kind == "posts":
        return (
            f"{ARCTIC}/api/posts/search?{arctic_qs}",
            f"{PULLPUSH}/reddit/search/submission/?test&{pullpush_qs}",
        )
    return (
        f"{ARCTIC}/api/comments/search?{arctic_qs}",
        f"{PULLPUSH}/reddit/search/comment/?test&{pullpush_qs}",
    )


def merge_dedupe(*lists: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for lst in lists:
        for item in lst:
            iid = str(item.get("id") or "")
            if not iid or iid in seen:
                continue
            seen.add(iid)
            out.append(item)
    out.sort(key=lambda x: int(x.get("created_utc") or 0), reverse=True)
    return out


def fetch_kind(
    username: str,
    kind: str,
    *,
    limit: int = DEFAULT_LIMIT,
    before: str | None = None,
    after: str | None = None,
    subreddit: str | None = None,
    keywords: str | None = None,
) -> dict[str, Any]:
    arctic_url, pullpush_url = _urls(
        username,
        kind,
        limit=limit,
        before=before,
        after=after,
        subreddit=subreddit,
        keywords=keywords,
    )
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        fa = ex.submit(_get_json, arctic_url)
        fp = ex.submit(_get_json, pullpush_url)
        a_ok, a_data = fa.result()
        p_ok, p_data = fp.result()
    sources = []
    if a_ok and a_data:
        sources.append("Arctic Shift")
    if p_ok and p_data:
        sources.append("PullPush")
    return {
        "kind": kind,
        "sources": sources,
        "arctic_ok": a_ok,
        "pullpush_ok": p_ok,
        "items": merge_dedupe(a_data, p_data),
        "urls": {"arctic": arctic_url, "pullpush": pullpush_url},
        "rosint_ui": f"https://www.rosint.dev/?u={username}",
    }


def status_of(item: dict, kind: str) -> dict[str, bool]:
    text = item.get("selftext") if kind == "posts" else item.get("body")
    return {
        "removed": text == "[removed]"
        or (kind == "posts" and bool(item.get("removed_by_category"))),
        "deleted": text == "[deleted]" or item.get("author") == "[deleted]",
    }


def summarize(posts: list[dict], comments: list[dict]) -> dict[str, Any]:
    subs: dict[str, int] = {}
    removed = deleted = nsfw = karma = 0
    earliest = latest = 0

    def walk(items: list[dict], kind: str) -> None:
        nonlocal removed, deleted, nsfw, karma, earliest, latest
        for it in items:
            sub = it.get("subreddit")
            if sub:
                subs[sub] = subs.get(sub, 0) + 1
            st = status_of(it, kind)
            if st["removed"]:
                removed += 1
            if st["deleted"]:
                deleted += 1
            if kind == "posts" and it.get("over_18"):
                nsfw += 1
            karma += int(it.get("score") or 0)
            t = int(it.get("created_utc") or 0)
            if t:
                if not earliest or t < earliest:
                    earliest = t
                if t > latest:
                    latest = t

    walk(posts, "posts")
    walk(comments, "comments")
    top_subs = sorted(subs.items(), key=lambda x: -x[1])[:20]
    return {
        "post_count": len(posts),
        "comment_count": len(comments),
        "removed": removed,
        "deleted": deleted,
        "nsfw_posts": nsfw,
        "karma_sample": karma,
        "earliest_utc": earliest or None,
        "latest_utc": latest or None,
        "earliest_iso": _iso(earliest),
        "latest_iso": _iso(latest),
        "top_subreddits": [{"name": n, "count": c} for n, c in top_subs],
    }


def _iso(utc: int) -> str | None:
    if not utc:
        return None
    return datetime.fromtimestamp(utc, tz=timezone.utc).isoformat()


def compact_item(item: dict, kind: str) -> dict[str, Any]:
    st = status_of(item, kind)
    base = {
        "id": item.get("id"),
        "subreddit": item.get("subreddit"),
        "score": item.get("score"),
        "created_utc": item.get("created_utc"),
        "created_iso": _iso(int(item.get("created_utc") or 0)),
        "permalink": (
            f"https://www.reddit.com{item['permalink']}"
            if item.get("permalink") and not str(item["permalink"]).startswith("http")
            else item.get("permalink")
        ),
        "removed": st["removed"],
        "deleted": st["deleted"],
    }
    if kind == "posts":
        base.update(
            {
                "title": item.get("title"),
                "selftext": (item.get("selftext") or "")[:500],
                "num_comments": item.get("num_comments"),
                "over_18": bool(item.get("over_18")),
                "url": item.get("url"),
            }
        )
    else:
        base.update(
            {
                "body": (item.get("body") or "")[:800],
                "link_id": item.get("link_id"),
                "parent_id": item.get("parent_id"),
            }
        )
    return base


def fetch_user(
    raw: str,
    *,
    limit: int = DEFAULT_LIMIT,
    include_raw: bool = False,
) -> dict[str, Any]:
    user = normalize_username(raw)
    if not user:
        raise SystemExit("Empty username after normalization")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        fp = ex.submit(fetch_kind, user, "posts", limit=limit)
        fc = ex.submit(fetch_kind, user, "comments", limit=limit)
        posts_pack = fp.result()
        comments_pack = fc.result()
    posts, comments = posts_pack["items"], comments_pack["items"]
    sources = sorted(
        set(posts_pack["sources"] + comments_pack["sources"]),
        key=lambda s: (s != "Arctic Shift", s),
    )
    out: dict[str, Any] = {
        "tool": "rosint_reddit",
        "inspired_by": "https://www.rosint.dev/",
        "username": user,
        "rosint_ui": f"https://www.rosint.dev/?u={user}",
        "sources": sources,
        "arctic_ok": posts_pack["arctic_ok"] or comments_pack["arctic_ok"],
        "pullpush_ok": posts_pack["pullpush_ok"] or comments_pack["pullpush_ok"],
        "summary": summarize(posts, comments),
        "posts": [compact_item(p, "posts") for p in posts],
        "comments": [compact_item(c, "comments") for c in comments],
    }
    if include_raw:
        out["raw_posts"] = posts
        out["raw_comments"] = comments
    return out


def main() -> None:
    p = argparse.ArgumentParser(
        description="Rosint-style Reddit archive lookup (Arctic Shift + PullPush)"
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    u = sub.add_parser("user", help="Full history summary for a Reddit username")
    u.add_argument("username")
    u.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    u.add_argument("--raw", action="store_true", help="Include raw archive objects")
    u.add_argument(
        "--max-items",
        type=int,
        default=50,
        help="Cap posts/comments in JSON output (0 = all)",
    )

    posts = sub.add_parser("posts", help="Posts only")
    posts.add_argument("username")
    posts.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    posts.add_argument("--subreddit")
    posts.add_argument("--keywords")
    posts.add_argument("--before")
    posts.add_argument("--after")

    comments = sub.add_parser("comments", help="Comments only")
    comments.add_argument("username")
    comments.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    comments.add_argument("--subreddit")
    comments.add_argument("--keywords")
    comments.add_argument("--before")
    comments.add_argument("--after")

    sub.add_parser("normalize").add_argument("username")

    ns = p.parse_args()
    if ns.cmd == "normalize":
        print(normalize_username(ns.username))
        return
    if ns.cmd == "user":
        data = fetch_user(ns.username, limit=ns.limit, include_raw=ns.raw)
        if ns.max_items and ns.max_items > 0:
            data["posts"] = data["posts"][: ns.max_items]
            data["comments"] = data["comments"][: ns.max_items]
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    kind = "posts" if ns.cmd == "posts" else "comments"
    pack = fetch_kind(
        normalize_username(ns.username),
        kind,
        limit=ns.limit,
        before=getattr(ns, "before", None),
        after=getattr(ns, "after", None),
        subreddit=getattr(ns, "subreddit", None),
        keywords=getattr(ns, "keywords", None),
    )
    pack["items"] = [compact_item(i, kind) for i in pack["items"]]
    pack["username"] = normalize_username(ns.username)
    print(json.dumps(pack, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
