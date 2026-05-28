#!/usr/bin/env python3
"""L1 source evidence requirement guardrail validator — read-only, stdlib only (Sprint 5N-B)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EVIDENCE_MATRIX = ROOT / "main/data/SOURCE_EVIDENCE_REQUIREMENT_MATRIX_WAVE_1.md"
PROPOSAL_MATRIX = ROOT / "main/data/SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md"

SELECTED_ROUTE_IDS = (
    "sulfur_element_term_record",
    "de_core_biogenic_lang",
    "copper_sulfides_language",
    "de_core_fes",
    "de_core_mos2",
)


def parse_matrix_table(path: Path) -> tuple[list[str], list[list[str]]]:
    if not path.exists():
        return [], []
    header: list[str] = []
    rows: list[list[str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|") or re.match(r"^\|\s*-+\s*\|", line):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if not cells:
            continue
        if not header:
            header = cells
        else:
            rows.append(cells)
    return header, rows


def col_index(header: list[str], name: str) -> int | None:
    for i, col in enumerate(header):
        if col.lower() == name.lower():
            return i
    return None


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {"evidence_rows": 0}

    if not EVIDENCE_MATRIX.exists():
        return [f"missing {EVIDENCE_MATRIX.relative_to(ROOT)}"], [], stats

    header, rows = parse_matrix_table(EVIDENCE_MATRIX)
    stats["evidence_rows"] = len(rows)

    if len(rows) != 5:
        errors.append(f"evidence matrix expected 5 rows, found {len(rows)}")

    route_col = col_index(header, "route_id")
    acceptable_col = col_index(header, "acceptable future source class")
    unacceptable_col = col_index(header, "unacceptable source class")
    doctrine_col = col_index(header, "internal doctrine alone sufficient")
    teaching_col = col_index(header, "academic teaching support useful")
    formal_col = col_index(header, "formal authority required")
    notes_col = col_index(header, "notes")

    if route_col is None:
        errors.append("evidence matrix missing route_id column")

    seen: set[str] = set()
    for row in rows:
        if route_col is None or route_col >= len(row):
            break
        rid = row[route_col]
        seen.add(rid)

        for label, idx in (
            ("acceptable future source class", acceptable_col),
            ("unacceptable source class", unacceptable_col),
        ):
            if idx is None or idx >= len(row) or not row[idx].strip():
                errors.append(f"{rid}: missing {label}")

        if doctrine_col is not None and doctrine_col < len(row):
            if row[doctrine_col].strip().lower() == "yes":
                errors.append(
                    f"{rid}: internal doctrine alone must not be sufficient for external factual authority"
                )

        notes = row[notes_col].lower() if notes_col is not None and notes_col < len(row) else ""
        acceptable = row[acceptable_col].lower() if acceptable_col is not None and acceptable_col < len(row) else ""

        if teaching_col is not None and teaching_col < len(row) and row[teaching_col].strip().lower() == "yes":
            if "supporting" not in acceptable and "supporting only" not in notes:
                if "sole" not in notes and "do not use teaching" not in notes:
                    warnings.append(
                        f"{rid}: teaching support marked useful — confirm notes bound teaching tier"
                    )

        if "dictionary" in acceptable or "authoritative_dictionary" in acceptable:
            if "chemical authority" in notes and "not" not in notes:
                errors.append(f"{rid}: treats dictionary as chemical authority")
            if "do not" not in notes and "naming" not in notes and "lexical" not in notes:
                warnings.append(f"{rid}: dictionary row should scope naming/usage only")

        if "multilingual" in notes and "universal equivalence" in notes and "not" not in notes:
            errors.append(f"{rid}: treats multilingual equivalence as universal")

        if formal_col is not None and formal_col < len(row):
            formal = row[formal_col].strip().lower()
            if rid in ("copper_sulfides_language", "de_core_fes", "de_core_mos2") and formal != "yes":
                errors.append(f"{rid}: formal authority required should be yes")

    missing = set(SELECTED_ROUTE_IDS) - seen
    if missing:
        errors.append(f"evidence matrix missing route_ids: {sorted(missing)}")

    if PROPOSAL_MATRIX.exists():
        p_header, p_rows = parse_matrix_table(PROPOSAL_MATRIX)
        pub_col = col_index(p_header, "publication-ready")
        if pub_col is not None:
            for row in p_rows:
                if pub_col < len(row) and row[pub_col].strip().lower() != "no":
                    rid = row[col_index(p_header, "route_id") or 0] if p_header else "?"
                    errors.append(f"{rid}: associated proposal row publication-ready must be no")

    return errors, warnings, stats


def main() -> int:
    errors, warnings, stats = run_validation()
    print("=== Source Evidence Requirements L1 Validation ===")
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
