#!/usr/bin/env python3
"""Hermes launcher for vendored marouane53/GeoInt scripts.

Resolves GEOINT_HOME (default: skills/geoint/upstream), injects CTF_UA/GEOINT_UA,
and runs upstream CLIs without requiring a global GeoInt install.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HOME = ROOT / "skills" / "geoint" / "upstream"


def geoint_home() -> Path:
    env = (os.environ.get("GEOINT_HOME") or "").strip()
    if env:
        return Path(env).expanduser().resolve()
    return DEFAULT_HOME.resolve()


def scripts_dir() -> Path:
    d = geoint_home() / "scripts"
    if not d.is_dir():
        raise SystemExit(
            f"GeoInt scripts not found at {d}. Expected vendored tree under "
            f"skills/geoint/upstream (see skills/geoint/UPSTREAM.md)."
        )
    return d


def ensure_ua_env() -> None:
    if not (os.environ.get("CTF_UA") or os.environ.get("GEOINT_UA")):
        os.environ.setdefault(
            "GEOINT_UA",
            "HermesOsintCtfAgent/1.0 (geoint; dedicated CTF UA)",
        )


def run_script(script: str, args: list[str], *, use_uv: bool | None = None) -> int:
    ensure_ua_env()
    path = scripts_dir() / script
    if not path.is_file():
        raise SystemExit(f"Unknown GeoInt script: {script}")
    prefer_uv = use_uv
    if prefer_uv is None:
        prefer_uv = shutil.which("uv") is not None
    cwd = str(geoint_home())
    env = os.environ.copy()
    env["GEOINT_HOME"] = str(geoint_home())
    env.setdefault("CLAUDE_SKILL_DIR", str(geoint_home()))
    if prefer_uv:
        cmd = ["uv", "run", str(path), *args]
    else:
        cmd = [sys.executable, str(path), *args]
    return subprocess.call(cmd, cwd=cwd, env=env)


def cmd_status(_: argparse.Namespace) -> int:
    ensure_ua_env()
    home = geoint_home()
    print(
        json.dumps(
            {
                "geoint_home": str(home),
                "exists": home.is_dir(),
                "skill": str(home / "SKILL.md"),
                "scripts": (home / "scripts").is_dir(),
                "data": (home / "data").is_dir(),
                "ctf_ua_set": bool(os.environ.get("CTF_UA")),
                "geoint_ua_set": bool(os.environ.get("GEOINT_UA")),
                "photos_root": os.environ.get("GEOINT_PHOTOS")
                or str(Path.home() / "geoint-photos"),
                "tz": os.environ.get("GEOINT_TZ") or "",
                "proxy": os.environ.get("GEO_PROXY") or "",
                "uv": bool(shutil.which("uv")),
                "upstream": "https://github.com/marouane53/GeoInt",
            },
            indent=2,
        )
    )
    return 0 if home.is_dir() else 1


def main() -> None:
    p = argparse.ArgumentParser(
        description="Run vendored GeoInt tools (marouane53/GeoInt) with Hermes OPSEC env"
    )
    p.add_argument(
        "--no-uv",
        action="store_true",
        help="Force python3 instead of `uv run` (PEP 723 deps may be missing)",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", help="Show GEOINT_HOME and env")

    d = sub.add_parser("doctor", help="Upstream doctor.py")
    d.add_argument("--network", action="store_true")
    d.add_argument("--models", action="store_true")
    d.add_argument("--json", action="store_true")

    for name, script, help_ in (
        ("clues", "clues.py", "Offline clue tables"),
        ("sun", "sun.py", "Sun / shadow / dish / compass geometry"),
        ("osm", "osm.py", "Overpass feature queries"),
        ("geo", "geo.py", "Bearings, FoV, coordinate converts"),
        ("recon", "recon.py", "One-shot local first pass on an image"),
        ("session", "photo_session.py", "Per-photo archive start/finish/truth"),
        ("board", "board.py", "Candidate board / likelihood ledger"),
        ("textgeo", "textgeo.py", "OCR text → country / place signals"),
        ("exif", "exif.py", "EXIF / metadata helpers"),
    ):
        sp = sub.add_parser(name, help=help_)
        sp.add_argument("args", nargs=argparse.REMAINDER)
        sp.set_defaults(_script=script)

    run_p = sub.add_parser("run", help="Raw: run <script.py> -- args…")
    run_p.add_argument("script")
    run_p.add_argument("args", nargs=argparse.REMAINDER)

    ns = p.parse_args()
    args = list(getattr(ns, "args", None) or [])
    if args and args[0] == "--":
        args = args[1:]

    use_uv = False if ns.no_uv else None

    if ns.cmd == "status":
        raise SystemExit(cmd_status(ns))
    if ns.cmd == "doctor":
        dargs = []
        if ns.network:
            dargs.append("--network")
        if ns.models:
            dargs.append("--models")
        if ns.json:
            dargs.append("--json")
        raise SystemExit(run_script("doctor.py", dargs, use_uv=use_uv))
    if ns.cmd == "run":
        script = ns.script if ns.script.endswith(".py") else f"{ns.script}.py"
        raise SystemExit(run_script(script, args, use_uv=use_uv))

    raise SystemExit(run_script(ns._script, args, use_uv=use_uv))


if __name__ == "__main__":
    main()
