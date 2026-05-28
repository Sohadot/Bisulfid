#!/usr/bin/env python3
"""L1 claim boundary preparation guardrail validator — read-only, stdlib only (Sprint 5N-B)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PREP_PATH = ROOT / "main/data/DRAFT_WAVE_1_MEDIUM_RISK_CLAIM_BOUNDARY_PREP.md"

NEGATION_WINDOW = 40


def parse_claim_prep_table(path: Path) -> tuple[list[str], list[list[str]]]:
    """Parse only the medium-risk prep data table (not summary tables)."""
    if not path.exists():
        return [], []
    lines = path.read_text(encoding="utf-8").splitlines()
    header: list[str] = []
    rows: list[list[str]] = []
    in_target = False
    for line in lines:
        if not line.strip().startswith("|"):
            if in_target and rows:
                break
            continue
        if re.match(r"^\|\s*-+\s*\|", line):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if not cells:
            continue
        if "claim registration allowed now" in cells[0].lower() or any(
            "claim registration allowed now" == c.lower() for c in cells
        ):
            header = cells
            in_target = True
            continue
        if not in_target:
            continue
        if cells[0].startswith("*Rows:"):
            break
        if re.match(r"^[a-z0-9_]+$", cells[0]):
            rows.append(cells)
    return header, rows


def col_index(header: list[str], name: str) -> int | None:
    for i, col in enumerate(header):
        if col.lower() == name.lower():
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
        if any(n in before for n in ("not ", "no ", "never ", "without ", "does not ", "do not ", "remains ")):
            start = idx + len(phrase_l)
            continue
        return True
    return False


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {"prep_rows": 0}

    if not PREP_PATH.exists():
        return [f"missing {PREP_PATH.relative_to(ROOT)}"], [], stats

    text = PREP_PATH.read_text(encoding="utf-8")
    header, rows = parse_claim_prep_table(PREP_PATH)
    stats["prep_rows"] = len(rows)

    if len(rows) != 20:
        errors.append(f"claim boundary prep expected 20 rows, found {len(rows)}")

    route_col = col_index(header, "route_id")
    claim_reg_col = col_index(header, "claim registration allowed now")
    pub_col = col_index(header, "publication-ready")
    source_map_col = col_index(header, "source mapping allowed now")
    blocked_col = col_index(header, "blocked claim types")
    cautious_col = col_index(header, "statements that must remain cautious")

    for row in rows:
        if route_col is None or route_col >= len(row):
            errors.append("prep matrix missing route_id")
            break
        rid = row[route_col]
        for label, idx in (
            ("claim registration allowed now", claim_reg_col),
            ("publication-ready", pub_col),
            ("source mapping allowed now", source_map_col),
        ):
            if idx is None or idx >= len(row):
                errors.append(f"{rid}: missing column {label}")
                continue
            if row[idx].strip().lower() != "no":
                errors.append(f"{rid}: {label} must be 'no' (got {row[idx]!r})")

        if blocked_col is not None and blocked_col < len(row) and not row[blocked_col].strip():
            errors.append(f"{rid}: blocked claim types must be documented")

        if cautious_col is not None and cautious_col < len(row) and not row[cautious_col].strip():
            warnings.append(f"{rid}: cautious statements column empty")

    if has_unnegated(text, "claim approved"):
        errors.append("prep document implies claims approved")
    if has_unnegated(text, "status: approved"):
        errors.append("prep document references approved claim status")
    if "terminology_claims.json was modified" in text.lower():
        if "not modified" not in text.lower() and "remains unchanged" not in text.lower():
            errors.append("prep document implies terminology_claims.json was modified")
    if "enter source mapping" in text.lower() and "deferred" not in text.lower() and "before" not in text.lower():
        warnings.append("prep document should defer medium-risk drafts from premature source mapping")

    if "*rows: 20*" not in text.lower():
        warnings.append("prep document row count footer should state Rows: 20")

    return errors, warnings, stats


def main() -> int:
    errors, warnings, stats = run_validation()
    print("=== Claim Boundary Preparation L1 Validation ===")
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
