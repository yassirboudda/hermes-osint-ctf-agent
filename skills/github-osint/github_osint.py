#!/usr/bin/env python3
"""GitHub OSINT helper — read-only, uses GITHUB_TOKEN from .env."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional

API = "https://api.github.com"
FLAG_RE = re.compile(r"(?i)(CTF\{[^}]+\}|FLAG\{[^}]+\}|flag\{[^}]+\}|[A-Za-z0-9_-]{0,20}\{[^}]{6,}\})")


def token() -> str:
    t = (os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or "").strip()
    if t and "****" not in t:
        return t
    path = os.environ.get("GITHUB_PAT_FILE", "")
    if path and os.path.isfile(path):
        return open(path, encoding="utf-8").read().strip()
    return ""


def api(path: str, params: Optional[dict] = None) -> Any:
    url = path if path.startswith("http") else f"{API}{path}"
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": os.environ.get("CTF_UA", "HermesOsintCtfAgent/1.0"),
        "X-GitHub-Api-Version": "2022-11-28",
    }
    tok = token()
    if tok:
        headers["Authorization"] = f"Bearer {tok}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read()[:500]
        raise SystemExit(f"GitHub HTTP {e.code}: {body!r}") from e


def scan_text(label: str, text: str) -> None:
    if not text:
        return
    for m in FLAG_RE.finditer(text):
        print(f"[FLAG?] {label}: {m.group(0)}")


def cmd_user(ns: argparse.Namespace) -> None:
    u = api(f"/users/{ns.login}")
    print(json.dumps({k: u.get(k) for k in ("login", "name", "company", "blog", "location", "email", "bio", "twitter_username", "created_at", "public_repos")}, indent=2))
    repos = api(f"/users/{ns.login}/repos", {"per_page": 100, "sort": "updated"})
    for r in repos:
        print(f"REPO {r.get('full_name')} fork={r.get('fork')} desc={r.get('description')}")
        scan_text(r.get("full_name"), (r.get("description") or "") + " " + (r.get("homepage") or ""))


def cmd_repo(ns: argparse.Namespace) -> None:
    owner, name = ns.repo.split("/", 1)
    r = api(f"/repos/{owner}/{name}")
    print(json.dumps({k: r.get(k) for k in ("full_name", "description", "homepage", "default_branch", "created_at", "pushed_at", "archived")}, indent=2))
    scan_text("desc", r.get("description") or "")


def cmd_commits(ns: argparse.Namespace) -> None:
    owner, name = ns.repo.split("/", 1)
    params: Dict[str, Any] = {"per_page": ns.limit}
    if ns.sha:
        params["sha"] = ns.sha
    commits = api(f"/repos/{owner}/{name}/commits", params)
    for c in commits:
        msg = (c.get("commit") or {}).get("message") or ""
        sha = c.get("sha", "")[:12]
        author = ((c.get("commit") or {}).get("author") or {}).get("name")
        print(f"{sha} | {author} | {msg.splitlines()[0][:120]}")
        scan_text(sha, msg)
        if ns.grep and ns.grep.lower() not in msg.lower():
            continue
        if ns.grep:
            print(f"  MATCH grep={ns.grep!r}")


def cmd_prs(ns: argparse.Namespace) -> None:
    owner, name = ns.repo.split("/", 1)
    prs = api(f"/repos/{owner}/{name}/pulls", {"state": "all", "per_page": ns.limit})
    for p in prs:
        title = p.get("title") or ""
        body = p.get("body") or ""
        print(f"PR#{p.get('number')} [{p.get('state')}] {title} merge={p.get('merged_at')}")
        scan_text(f"PR#{p.get('number')} title", title)
        scan_text(f"PR#{p.get('number')} body", body)


def cmd_search(ns: argparse.Namespace) -> None:
    data = api("/search/commits", {"q": ns.query, "per_page": min(ns.limit, 50)})
    # commits search needs special accept — retry with header via raw if empty
    items = data.get("items") or []
    if not items:
        # fallback code search
        data = api("/search/code", {"q": ns.query, "per_page": min(ns.limit, 30)})
        items = data.get("items") or []
        for it in items:
            print(f"CODE {it.get('repository',{}).get('full_name')} {it.get('path')} {it.get('html_url')}")
        return
    for it in items:
        msg = (it.get("commit") or {}).get("message") or ""
        repo = (it.get("repository") or {}).get("full_name")
        print(f"COMMIT {repo} {msg.splitlines()[0][:120]}")
        scan_text(repo or "commit", msg)


def main() -> None:
    p = argparse.ArgumentParser(description="Hackinator GitHub OSINT")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("user"); s.add_argument("login"); s.set_defaults(func=cmd_user)
    s = sub.add_parser("repo"); s.add_argument("repo"); s.set_defaults(func=cmd_repo)
    s = sub.add_parser("commits"); s.add_argument("repo"); s.add_argument("--sha"); s.add_argument("--grep"); s.add_argument("--limit", type=int, default=50); s.set_defaults(func=cmd_commits)
    s = sub.add_parser("prs"); s.add_argument("repo"); s.add_argument("--limit", type=int, default=50); s.set_defaults(func=cmd_prs)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--limit", type=int, default=30); s.set_defaults(func=cmd_search)
    ns = p.parse_args()
    if not token():
        print("WARN: no GITHUB_TOKEN — unauthenticated (low rate limits)", file=sys.stderr)
    ns.func(ns)


if __name__ == "__main__":
    main()
