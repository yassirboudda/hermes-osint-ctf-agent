---
name: rosint-reddit
description: >-
  Rosint-style Reddit archive OSINT: deleted posts, removed comments, private
  profiles via Arctic Shift + PullPush. Use when a Reddit username appears.
---

# Rosint Reddit archive

Mirror of [rosint.dev](https://www.rosint.dev/) / [zuxu4n/RedditOsint](https://github.com/zuxu4n/RedditOsint).

## When to use
- Challenge gives a Reddit handle (`u/…`, old/new reddit URL, or bare username).
- Need **deleted / removed / private** history that live Reddit hides.
- Correlate SOCMINT leads (subs, phrasing, timestamps) with other identities.

## CLI
```bash
python3 tools/rosint_reddit.py user Wuan_Xijiang
python3 tools/rosint_reddit.py posts Wuan_Xijiang --limit 50
python3 tools/rosint_reddit.py comments Wuan_Xijiang --keywords CTF
# UI twin:
# https://www.rosint.dev/?u=Wuan_Xijiang
```

## Sources (dual, merged)
| Archive | Posts | Comments |
|---------|-------|----------|
| Arctic Shift | `/api/posts/search` | `/api/comments/search` |
| PullPush | `/reddit/search/submission/` | `/reddit/search/comment/` |

Results are **deduped by id**, newest first. One archive may be down (Cloudflare / rate limit) — the other still counts.

## OPSEC
- Use `$CTF_UA` only.
- Soft crawl; do not spam pagination loops.
- Archives ≠ permission to SE / message users.

## Output fields to journal
- `summary.top_subreddits`, `removed` / `deleted` counts
- Post titles / comment bodies (flag-shaped strings)
- `rosint_ui` link for human review
