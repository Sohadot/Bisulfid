#!/usr/bin/env python3
"""L2 multilingual wave plan validator — read-only, stdlib only (Sprint 5O-A)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ML_MODEL_PATH = ROOT / "main/data/CORPUS_PRODUCTION_MULTILINGUAL_MODEL.md"

REQUIRED_LANGUAGES = ("english", "german", "arabic", "chinese", "japanese")
REQUIRED_TOPICS = (
    "controlled terminology",
    "not simple translation",
    "hreflang",
    "translation registry",
    "anti-translation-spam",
    "source governance",
    "deferred",
)

FORBIDDEN = (
    re.compile(r"bulk\s+translation\s+allowed", re.I),
    re.compile(r"translation\s+spam\s+allowed", re.I),
    re.compile(r"ar/zh/ja\s+expansion\s+now", re.I),
    re.compile(r"multilingual\s+publication\s+without\s+hreflang", re.I),
)

NEGATION = re.compile(
    r"(no |not |never |forbidden|without authorization|is not permitted|are not permitted|\*\*no )",
    re.I,
)


def is_negated(text: str, start: int, end: int) -> bool:
    before = text[max(0, start - 48) : start + 1]
    after = text[end : end + 48]
    if NEGATION.search(before):
        return True
    if re.search(r"\b(forbidden|prohibited|not permitted)\b", after, re.I):
        return True
    return False


def run_validation() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not ML_MODEL_PATH.exists():
        errors.append("Missing CORPUS_PRODUCTION_MULTILINGUAL_MODEL.md")
        return errors, warnings

    text = ML_MODEL_PATH.read_text(encoding="utf-8")
    lower = text.lower()

    for lang in REQUIRED_LANGUAGES:
        if lang not in lower:
            errors.append(f"Multilingual model missing language layer: {lang}")

    for topic in REQUIRED_TOPICS:
        if topic not in lower:
            errors.append(f"Multilingual model missing topic: {topic}")

    for pat in FORBIDDEN:
        for match in pat.finditer(text):
            if not is_negated(text, match.start(), match.end()):
                errors.append(f"Forbidden multilingual plan pattern: {pat.pattern}")
                break

    if "terminology role" not in lower and "controlled record" not in lower:
        errors.append("Every multilingual page must have a controlled terminology role")

    if "ar" in lower or "arabic" in lower:
        if "deferred" not in lower and "until" not in lower:
            warnings.append("Arabic layer should document deferral until governance ready")

    return errors, warnings


def main() -> int:
    errors, warnings = run_validation()
    print("=== Multilingual Wave Plan L2 Validation ===")
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
