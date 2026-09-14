# Secrets (gitignored)

Put real credentials only in local files ignored by git:

- `../.env`
- `ctfd_session.json` (shape below)
- optional HAR exports for cookie extraction — **never commit**

## `ctfd_session.json` shape

```json
{
  "base_url": "https://your-ctfd.example",
  "cookies": {
    "session": "****"
  }
}
```

## OSINT Industries

Use **API key** auth per https://api.osint.industries/misc/docs — not browser cookies.
