#!/usr/bin/env python3
"""Read-only L0 validator for Sprint 5J draft production wave 1."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
MANIFEST_PATH = ROOT / "main/data/DRAFT_PRODUCTION_WAVE_1_MANIFEST.md"

REQUIRED_FM = (
    "route_id",
    "status",
    "publication_status",
    "indexable",
    "in_sitemap",
    "language",
    "locale",
    "source_language",
)

BANNED_FRAMES = (
    "market report",
    "safety guide",
    "medical advice",
    "procurement guide",
    "investment recommendation",
    "cagr",
    "market share",
    "market-share",
    "handling instructions",
    "dosage",
    "treatment protocol",
    "emergency guidance",
)

NEGATION_PREFIX = re.compile(
    r"(not a|not an|no |never |avoid |without |does not |do not |is not |are not )",
    re.I,
)

URL_RE = re.compile(r"https?://[^\s\])>]+", re.I)
MD_LINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")

FACTUAL_HINTS = (
    " is ",
    " are ",
    " refers to",
    " defined as",
    " convention",
    " ion",
    " compound",
    " vocabulary",
    " terminology",
)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm: dict[str, str] = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    return fm, parts[2]


def load_wave_targets() -> list[str]:
    if not MANIFEST_PATH.exists():
        return []
    text = MANIFEST_PATH.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\[\s*\"[^\"]+\".*?\])\s*```", text, re.S)
    if not match:
        return []
    return json.loads(match.group(1))


def is_negated(text: str, idx: int, term: str) -> bool:
    window = text[max(0, idx - 40) : idx + len(term)]
    return bool(NEGATION_PREFIX.search(window))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    routes_data = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))
    routes_by_id = {r["route_id"]: r for r in routes_data["routes"]}

    targets = load_wave_targets()
    if not targets:
        errors.append("No wave-1 draft targets found in DRAFT_PRODUCTION_WAVE_1_MANIFEST.md")
        targets = []

    for route_id in targets:
        route = routes_by_id.get(route_id)
        if not route:
            errors.append(f"{route_id}: not in routes.json")
            continue
        cf = ROOT / route["content_file"]
        if not cf.exists():
            errors.append(f"{route_id}: missing draft file {route['content_file']}")
            continue

        text = cf.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)

        for field in REQUIRED_FM:
            if field not in fm:
                errors.append(f"{route_id}: missing frontmatter '{field}'")

        if fm.get("route_id") != route_id:
            errors.append(f"{route_id}: frontmatter route_id mismatch ({fm.get('route_id')})")
        if fm.get("status") != "draft":
            errors.append(f"{route_id}: status must be draft")
        if fm.get("publication_status") != "non_public":
            errors.append(f"{route_id}: publication_status must be non_public")
        if fm.get("indexable", "").lower() not in ("false", "0"):
            errors.append(f"{route_id}: indexable must be false")
        if fm.get("in_sitemap", "").lower() not in ("false", "0"):
            errors.append(f"{route_id}: in_sitemap must be false")

        for lang_field in ("language", "locale", "source_language"):
            if fm.get(lang_field) != route.get(lang_field):
                errors.append(
                    f"{route_id}: {lang_field} mismatch (draft={fm.get(lang_field)!r}, route={route.get(lang_field)!r})"
                )

        lower = text.lower()
        lang = fm.get("language", route.get("language", "en"))
        if lang == "de":
            required_notice = (
                "nichtöffentlich",
                "nicht veröffentlichungsreif",
                "nicht veröffentlicht",
                "nicht indexierbar",
            )
        else:
            required_notice = (
                "non-public",
                "not publication-ready",
                "not published",
                "not indexable",
            )
        for phrase in required_notice:
            if phrase not in lower:
                warnings.append(f"{route_id}: draft notice may be incomplete (missing '{phrase}')")

        if "source and claim status" not in lower and "quellen- und claim-status" not in lower:
            warnings.append(f"{route_id}: missing source/claim status section heading")

        if "[source required]" not in lower:
            errors.append(f"{route_id}: missing [SOURCE REQUIRED] marker")

        if URL_RE.search(body):
            errors.append(f"{route_id}: raw URL detected")
        if MD_LINK_RE.search(body):
            errors.append(f"{route_id}: markdown link detected")

        norm = re.sub(r"\*+", "", lower)
        for term in BANNED_FRAMES:
            pos = 0
            while True:
                idx = norm.find(term, pos)
                if idx == -1:
                    break
                if not is_negated(norm, idx, term):
                    errors.append(f"{route_id}: banned/risky frame '{term}'")
                pos = idx + 1

        if "source-locking is complete" in lower and "not complete" not in lower:
            errors.append(f"{route_id}: claims source-locking complete")
        if "claim is approved" in lower and "no claim is approved" not in lower:
            if "kein claim ist freigegeben" not in lower:
                errors.append(f"{route_id}: may imply claim approval")

    print("=== Content Drafts L0 Validation (Wave 1) ===")
    print(f"Date: {date.today().isoformat()}")
    print(f"Targets expected: {len(targets)}")
    print(f"Routes registry total: {len(routes_by_id)}")
    print()

    if errors:
        print("FAIL — errors:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("PASS — no blocking errors")

    if warnings:
        print()
        print("Warnings:")
        for w in warnings:
            print(f"  - {w}")

    print()
    print(f"Summary: {'FAIL' if errors else 'PASS'} ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
