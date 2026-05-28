#!/usr/bin/env python3
"""L1 source registration proposal guardrail validator — read-only, stdlib only (Sprint 5N-B)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PROPOSAL_FILES = (
    ROOT / "main/data/SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md",
    ROOT / "main/data/SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md",
    ROOT / "main/data/SOURCE_EVIDENCE_REQUIREMENT_MATRIX_WAVE_1.md",
    ROOT / "main/data/SOURCE_REGISTRATION_RISK_REVIEW_WAVE_1.md",
    ROOT / "main/data/SOURCE_REGISTRATION_NEXT_ACTIONS_WAVE_1.md",
)

SELECTED_ROUTE_IDS = (
    "sulfur_element_term_record",
    "de_core_biogenic_lang",
    "copper_sulfides_language",
    "de_core_fes",
    "de_core_mos2",
)

URL_RE = re.compile(r"https?://[^\s\])>]+", re.I)
BIBLIO_RE = re.compile(r"\b(ISBN[- ]?\d|DOI[:/]|doi\.org/)\b", re.I)

NEGATION_WINDOW = 40


def parse_matrix_table(path: Path) -> tuple[list[str], list[list[str]]]:
    if not path.exists():
        return [], []
    lines = path.read_text(encoding="utf-8").splitlines()
    header: list[str] = []
    rows: list[list[str]] = []
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        if re.match(r"^\|\s*-+\s*\|", line):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if not cells:
            continue
        if not header:
            header = cells
            continue
        rows.append(cells)
    return header, rows


def col_index(header: list[str], name: str) -> int | None:
    target = name.lower()
    for i, col in enumerate(header):
        if col.lower() == target:
            return i
    return None


def has_unnegated(text: str, phrase: str) -> bool:
    lower = text.lower()
    phrase_l = phrase.lower()
    start = 0
    while True:
        idx = lower.find(phrase_l, start)
        if idx == -1:
            return False
        before = lower[max(0, idx - NEGATION_WINDOW) : idx]
        if any(n in before for n in ("not ", "no ", "never ", "without ", "≠", "does not ", "do not ")):
            start = idx + len(phrase_l)
            continue
        return True
    return False


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {"proposal_files": 0, "matrix_rows": 0}

    for path in PROPOSAL_FILES:
        if not path.exists():
            errors.append(f"missing proposal file: {path.relative_to(ROOT)}")
        else:
            stats["proposal_files"] += 1

    matrix_path = ROOT / "main/data/SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md"
    header, rows = parse_matrix_table(matrix_path)
    stats["matrix_rows"] = len(rows)

    if not rows:
        errors.append("proposal matrix has no data rows")
    elif len(rows) != 5:
        errors.append(f"proposal matrix expected 5 rows, found {len(rows)}")

    route_col = col_index(header, "route_id") if header else None
    reg_col = col_index(header, "source registry entry allowed now") if header else None
    claim_col = col_index(header, "claim approval allowed now") if header else None
    pub_col = col_index(header, "publication-ready") if header else None

    seen_routes: set[str] = set()
    for row in rows:
        if route_col is None or route_col >= len(row):
            errors.append("proposal matrix missing route_id column")
            break
        rid = row[route_col]
        seen_routes.add(rid)
        for label, idx in (
            ("source registry entry allowed now", reg_col),
            ("claim approval allowed now", claim_col),
            ("publication-ready", pub_col),
        ):
            if idx is None or idx >= len(row):
                errors.append(f"{rid}: missing column {label}")
                continue
            val = row[idx].strip().lower()
            if val != "no":
                errors.append(f"{rid}: {label} must be 'no' (got {row[idx]!r})")

    missing = set(SELECTED_ROUTE_IDS) - seen_routes
    extra = seen_routes - set(SELECTED_ROUTE_IDS)
    if missing:
        errors.append(f"proposal matrix missing route_ids: {sorted(missing)}")
    if extra:
        errors.append(f"proposal matrix unexpected route_ids: {sorted(extra)}")

    for path in PROPOSAL_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if URL_RE.search(text):
            errors.append(f"{rel}: raw URL found in proposal document")
        if BIBLIO_RE.search(text):
            errors.append(f"{rel}: invented bibliographic detail pattern detected")
        if has_unnegated(text, "is source-locked"):
            errors.append(f"{rel}: states page is source-locked")
        if has_unnegated(text, "are source-locked"):
            errors.append(f"{rel}: states pages are source-locked")
        if has_unnegated(text, "page is publication-ready"):
            errors.append(f"{rel}: states page is publication-ready")
        if has_unnegated(text, "source registry entry allowed now: yes"):
            errors.append(f"{rel}: allows source registry entry now")
        if has_unnegated(text, "claim approval allowed now: yes"):
            errors.append(f"{rel}: allows claim approval now")
        if has_unnegated(text, "approved source"):
            if "mistaken for approved" not in text.lower():
                errors.append(f"{rel}: treats source as approved")
        if has_unnegated(text, "verified source") and "candidate" not in text.lower():
            warnings.append(f"{rel}: verify 'verified source' language is negated in context")
        if "source_registry.json was modified" in text.lower() or "registry entries added" in text.lower():
            if "not modified" not in text.lower() and "no entries added" not in text.lower():
                errors.append(f"{rel}: implies source_registry.json was modified")
        if "candidate" not in text.lower() and path.name.endswith("MATRIX_WAVE_1.md"):
            warnings.append(f"{rel}: matrix should distinguish candidate families from registry rows")

    report = ROOT / "main/data/SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md"
    if report.exists():
        rt = report.read_text(encoding="utf-8").lower()
        if "registry entries added" not in rt and "0" not in rt:
            warnings.append("proposal report should document zero registry entries added")
        if "candidate" not in rt or "verified" not in rt:
            warnings.append("proposal report should distinguish candidate vs verified sources")

    return errors, warnings, stats


def main() -> int:
    errors, warnings, stats = run_validation()
    print("=== Source Registration Proposals L1 Validation ===")
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
