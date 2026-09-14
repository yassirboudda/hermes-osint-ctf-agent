# GitHub OSINT

Use `GITHUB_TOKEN` from `.env` for authenticated API reads when public rate limits block you.  
**Read-only.** Never force-push, never write to foreign repos.

```bash
export GITHUB_TOKEN=****   # in .env
python3 skills/github-osint/github_osint.py --help
```

Focus: commit messages, PR titles, merges, deleted-looking history archaeology.
