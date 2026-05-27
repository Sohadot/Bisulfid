#!/usr/bin/env python3
"""L1 draft content validator — all draft-backed routes (Sprint 5K). Read-only, stdlib only."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
WAVE1_MANIFEST = ROOT / "main/data/DRAFT_PRODUCTION_WAVE_1_MANIFEST.md"

REQUIRED_FM = (
    "route_id", "status", "publication_status", "indexable", "in_sitemap",
    "language", "locale", "source_language",
)

BANNED_FRAMES = (
    "market report", "safety guide", "medical advice", "procurement guide",
    "investment recommendation", "cagr", "market share", "market-share",
    "handling instructions", "dosage", "treatment protocol", "emergency guidance",
    "production data", "trade data", "acquisition-target",
)

NEGATION_PREFIX = re.compile(
    r"(not a|not an|no |never |avoid |without |does not |do not |is not |are not |\*\*not\*\* )",
    re.I,
)
URL_RE = re.compile(r"https?://[^\s\])>]+", re.I)
MD_LINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm: dict[str, str] = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, parts[2]


def load_wave1_targets() -> set[str]:
    if not WAVE1_MANIFEST.exists():
        return set()
    text = WAVE1_MANIFEST.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\[\s*\"[^\"]+\".*?\])\s*```", text, re.S)
    if not match:
        return set()
    return set(json.loads(match.group(1)))


def is_negated(text: str, idx: int) -> bool:
    return bool(NEGATION_PREFIX.search(text[max(0, idx - 48) : idx + 1]))


def claims_locking_complete(text: str) -> bool:
    lower = text.lower()
    for m in re.finditer(r"source-locking is complete", lower):
        before = lower[max(0, m.start() - 35) : m.start()]
        if "not" in before or "does not claim" in before:
            continue
        return True
    return False


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {"drafts_checked": 0}

    routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
    wave1 = load_wave1_targets()
    stats["wave1_strict_count"] = len(wave1)

    for route in routes:
        rid = route["route_id"]
        cf = ROOT / route["content_file"]
        if not cf.exists():
            continue
        stats["drafts_checked"] += 1
        strict = rid in wave1
        text = cf.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        lower = text.lower()

        def fail(msg: str) -> None:
            if strict:
                errors.append(msg)
            else:
                warnings.append(f"{msg} (pre-existing draft; legacy format)")

        for field in REQUIRED_FM:
            if field not in fm:
                fail(f"{rid}: missing frontmatter '{field}'")

        if fm.get("route_id") != rid:
            errors.append(f"{rid}: route_id mismatch in frontmatter")
        if fm.get("status") != "draft":
            errors.append(f"{rid}: status must be draft")
        if fm.get("publication_status") != "non_public":
            fail(f"{rid}: publication_status must be non_public")
        if fm.get("indexable", "").lower() not in ("false", "0"):
            errors.append(f"{rid}: indexable must be false")
        if fm.get("in_sitemap", "").lower() not in ("false", "0"):
            errors.append(f"{rid}: in_sitemap must be false")

        for lf in ("language", "locale", "source_language"):
            if lf not in fm:
                if strict:
                    fail(f"{rid}: missing frontmatter '{lf}'")
            elif fm.get(lf) != route.get(lf):
                fail(f"{rid}: {lf} mismatch with routes.json")

        lang = fm.get("language", route.get("language", "en"))
        if lang == "de":
            notice = ("nichtöffentlich", "nicht veröffentlichungsreif", "nicht veröffentlicht", "nicht indexierbar")
        else:
            notice = ("non-public", "not publication-ready", "not published", "not indexable")
        for ph in notice:
            if ph not in lower:
                warnings.append(f"{rid}: notice may lack '{ph}'")

        if "source and claim status" not in lower and "quellen- und claim-status" not in lower:
            fail(f"{rid}: missing source/claim status section")
        if "publication blockers" not in lower and "veröffentlichungsblocker" not in lower:
            fail(f"{rid}: missing publication blockers section")

        cautious = ("draft review", "candidate support", "source-locking required", "not publication-ready")
        if lang == "de":
            cautious = ("entwurfsprüfung", "kandidatenunterstützung", "source-locking required", "nicht veröffentlichungsreif")
        if not any(c in lower for c in cautious):
            warnings.append(f"{rid}: cautious wording may be incomplete")

        if "[source required]" not in lower:
            if strict or rid not in ("acquire",):
                fail(f"{rid}: missing [SOURCE REQUIRED] marker")

        if URL_RE.search(body):
            errors.append(f"{rid}: raw URL in body")
        if MD_LINK_RE.search(body):
            errors.append(f"{rid}: markdown link in body")

        norm = re.sub(r"\*+", "", lower)
        for term in BANNED_FRAMES:
            pos = 0
            while True:
                idx = norm.find(term, pos)
                if idx == -1:
                    break
                if not is_negated(norm, idx):
                    msg = f"{rid}: banned frame '{term}'"
                    if strict:
                        errors.append(msg)
                    else:
                        warnings.append(f"{msg} (pre-existing; often listed in non-goals)")
                pos = idx + 1

        if claims_locking_complete(text):
            if strict:
                errors.append(f"{rid}: claims source-locking complete")
            else:
                warnings.append(f"{rid}: source-locking language (pre-existing; review)")
        if "claim is approved" in lower and "no claim is approved" not in lower and "kein claim ist freigegeben" not in lower:
            errors.append(f"{rid}: may imply claim approval")

    return errors, warnings, stats


def main() -> int:
    errors, warnings, stats = run_validation()
    print("=== Corpus Drafts L1 Validation ===")
    for k, v in stats.items():
        print(f"{k}: {v}")
    print()
    if errors:
        print("FAIL — errors:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("PASS — no blocking errors")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")
    print(f"\nSummary: {'FAIL' if errors else 'PASS'} ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
