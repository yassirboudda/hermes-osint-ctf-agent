#!/usr/bin/env python3
"""OSINT Industries lookup guardrail — max N lookups per session."""
from __future__ import annotations

import json
import os
import time
from pathlib import Path

STATE = Path(
    os.environ.get(
        "OSINT_INDUSTRIES_STATE",
        str(Path(__file__).resolve().parents[1] / "cache" / "osint_industries_lookups.json"),
    )
)
MAX_LOOKUPS = int(os.environ.get("OSINT_INDUSTRIES_MAX_LOOKUPS", "5"))


def _load() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"count": 0, "events": []}


def _save(data: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def remaining() -> int:
    return max(0, MAX_LOOKUPS - int(_load().get("count", 0)))


def consume(query: str, *, quiet: bool = False) -> None:
    data = _load()
    if int(data.get("count", 0)) >= MAX_LOOKUPS:
        raise SystemExit(
            f"BLOCKED: OSINT Industries quota reached ({MAX_LOOKUPS}/session)."
        )
    data["count"] = int(data.get("count", 0)) + 1
    data.setdefault("events", []).append({"ts": time.time(), "query": query[:200]})
    _save(data)
    if not quiet:
        print(f"ok lookups={data['count']}/{MAX_LOOKUPS} remaining={remaining()}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("usage: osint_industries_guard.py status|consume <query>")
        raise SystemExit(0)
    if sys.argv[1] == "status":
        d = _load()
        print(json.dumps({"count": d.get("count", 0), "max": MAX_LOOKUPS, "remaining": remaining()}))
    elif sys.argv[1] == "consume":
        consume(" ".join(sys.argv[2:]) or "unspecified")
    else:
        raise SystemExit("unknown command")
