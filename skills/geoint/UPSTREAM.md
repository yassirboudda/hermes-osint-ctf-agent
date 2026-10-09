# GeoInt upstream vendor

Vendored from **[marouane53/GeoInt](https://github.com/marouane53/GeoInt)** (MIT).

| Path | Role |
|------|------|
| `upstream/SKILL.md` | Full geolocation method |
| `upstream/references/` | Playbooks + world clue library |
| `upstream/scripts/` | Tools (`recon`, `clues`, `sun`, `osm`, `pano`, …) |
| `upstream/data/` | Offline lookup tables (see `data/README.md` for licences) |
| `upstream/LICENSE` | MIT (GeoInt contributors / Oldcircle) |

## Hermes-local patches

Kept minimal and documented:

- `scripts/_net.py` — `user_agent()` honors `CTF_UA` / `GEOINT_UA`
- `scripts/clues.py`, `poi.py`, `revimg.py`, `_pano.py` — UA via `_net.user_agent()`

## Refresh from GitHub

```bash
rm -rf /tmp/geoint skills/geoint/upstream
git clone --depth 1 https://github.com/marouane53/GeoInt.git /tmp/geoint
mkdir -p skills/geoint/upstream
cp -a /tmp/geoint/. skills/geoint/upstream/
rm -rf skills/geoint/upstream/.git
# re-apply UA patches (see tools/geoint_cli.py doctor --check-ua or re-run integration notes)
```

Then re-apply the UA env patches above and bump the date in the commit message.
