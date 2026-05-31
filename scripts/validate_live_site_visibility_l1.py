#!/usr/bin/env python3
"""L1 live site visibility validator — read-only, stdlib only (Sprint 6M-I).

Validates local site/public artifact posture and optional live HTTPS checks.
Does not modify any files.
"""
from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = ROOT / "site/public"
MANIFEST_PATH = PUBLIC_DIR / "public_launch_manifest.json"
LIVE_HOST = "https://bisulfid.com"

FORBIDDEN_LIVE_PATHS = (
    "/scripts/",
    "/main/",
    "/_sample/",
    "/README.md",
)

REQUIRED_LIVE_MARKERS = (
    "noindex",
    "nofollow",
    "public launch foundation",
)


def fetch_url(url: str, timeout: int = 20) -> tuple[int | None, str, str | None]:
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(url, timeout=timeout, context=ctx) as resp:
            body = resp.read(8000).decode("utf-8", errors="replace")
            return resp.status, body, None
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read(500).decode("utf-8", errors="replace")
        except OSError:
            body = ""
        return exc.code, body, None
    except OSError as exc:
        return None, "", str(exc)


def validate_local_artifact() -> tuple[list[str], dict]:
    errors: list[str] = []
    stats: dict = {}

    if not PUBLIC_DIR.is_dir():
        errors.append("site/public/ missing")
        return errors, stats

    html_files = sorted(PUBLIC_DIR.rglob("index.html"))
    stats["public_html_count"] = len(html_files)
    if len(html_files) != 14000:
        errors.append(f"expected 14000 public pages, found {len(html_files)}")

    slot_files = 0
    md_files = 0
    ds_linked = 0
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        if "Slot reserved" in text:
            slot_files += 1
        if re.search(r"\*\*[^*]+\*\*", text):
            md_files += 1
        if "bisulfid-design-system" in text:
            ds_linked += 1

    stats["qa_slot_files"] = slot_files
    stats["raw_markdown_files"] = md_files
    stats["design_system_linked_files"] = ds_linked

    sample = html_files[:5] if html_files else []
    for path in sample:
        text = path.read_text(encoding="utf-8").lower()
        if "noindex" not in text or "nofollow" not in text:
            errors.append(f"{path.name}: missing noindex,nofollow in local artifact")

    if MANIFEST_PATH.is_file():
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        stats["manifest_rendered"] = manifest.get("rendered_count")
        for gate in ("indexation_gate", "sitemap_gate", "navigation_gate"):
            if manifest.get(gate) != "closed":
                errors.append(f"manifest {gate} not closed")

    if (PUBLIC_DIR / "sitemap.xml").is_file():
        errors.append("sitemap.xml present under site/public/")

    return errors, stats


def validate_live_site() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {"live_checks": {}}

    status, body, err = fetch_url(f"{LIVE_HOST}/")
    stats["live_checks"]["home"] = status
    if err:
        warnings.append(f"live home fetch failed: {err}")
    elif status != 200:
        errors.append(f"live home returned {status}")
    else:
        lower = body.lower()
        for marker in REQUIRED_LIVE_MARKERS:
            if marker not in lower:
                errors.append(f"live home missing marker {marker!r}")
        if "# bisulfid" in lower and "public launch foundation" not in lower:
            warnings.append("live home may be serving README-like content")

    for path in FORBIDDEN_LIVE_PATHS:
        url = f"{LIVE_HOST}{path}"
        code, _, err = fetch_url(url)
        stats["live_checks"][path] = code
        if err:
            warnings.append(f"live {path} fetch error: {err}")
        elif code == 200:
            errors.append(f"forbidden live path exposed: {path}")

    for path in ("/sitemap.xml", "/robots.txt"):
        code, _, _ = fetch_url(f"{LIVE_HOST}{path}")
        stats["live_checks"][path] = code
        if code == 200:
            warnings.append(f"live {path} returned 200 (may be acceptable if empty/disallow)")

    return errors, warnings, stats


def main() -> int:
    print("=" * 60)
    print("Bisulfid Live Site Visibility Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Public dir: {PUBLIC_DIR}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    all_errors: list[str] = []
    all_warnings: list[str] = []

    local_errors, local_stats = validate_local_artifact()
    all_errors.extend(local_errors)

    live_errors, live_warnings, live_stats = validate_live_site()
    all_errors.extend(live_errors)
    all_warnings.extend(live_warnings)

    print("--- Local artifact ---")
    for k, v in local_stats.items():
        print(f"  {k}: {v}")
    print()
    print("--- Live checks (bisulfid.com) ---")
    for k, v in live_stats.get("live_checks", {}).items():
        print(f"  {k}: {v}")
    print()
    print(f"QA slot leakage files (local): {local_stats.get('qa_slot_files', '?')}")
    print(f"Raw markdown files (local): {local_stats.get('raw_markdown_files', '?')}")
    print(f"Design-system linked files: {local_stats.get('design_system_linked_files', '?')}")
    print()

    if all_warnings:
        print("--- Warnings ---")
        for w in all_warnings:
            print(f"  WARN: {w}")
        print()

    if all_errors:
        print("--- Errors ---")
        for e in all_errors:
            print(f"  ERROR: {e}")
        print()
        print("VALIDATION SUMMARY: FAIL")
        print("=" * 60)
        return 1

    print("VALIDATION SUMMARY: PASS")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
