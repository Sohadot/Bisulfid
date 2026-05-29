#!/usr/bin/env python3
"""L2 production wave plan validator — read-only, stdlib only (Sprint 5O-A)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = (
    "main/data/CORPUS_LAUNCH_THRESHOLD.md",
    "main/data/CORPUS_PRODUCTION_WAVE_MODEL.md",
    "main/data/CORPUS_PRODUCTION_WAVE_CONTROL_MODEL.md",
    "main/data/CORPUS_PRODUCTION_GATE_MODEL.md",
    "main/data/FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md",
)

WAVE_MODEL_REQUIRED = (
    "route registration",
    "draft production",
    "source mapping",
    "claim boundary",
    "internal-link",
    "launch",
    "500",
)

FORBIDDEN_PATTERNS = (
    re.compile(r"mass\s+page\s+generation\s+without\s+(source|claim|gate)", re.I),
    re.compile(r"public\s+launch\s+below\s+500", re.I),
    re.compile(r"page\s+count\s+(is\s+)?more\s+important\s+than\s+authority", re.I),
    re.compile(r"draft\s+wave\s+2\s+(is\s+)?allowed\s+now", re.I),
)

DRAFT_W2_WAIT = re.compile(
    r"draft\s+wave\s+2.*(wait|should\s+still\s+wait|not\s+allowed|defer)",
    re.I | re.S,
)


def read_doc(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def run_validation() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_DOCS:
        if not (ROOT / rel).exists():
            errors.append(f"Missing production wave document: {rel}")

    threshold = read_doc("main/data/CORPUS_LAUNCH_THRESHOLD.md")
    if threshold and "500" not in threshold:
        errors.append("CORPUS_LAUNCH_THRESHOLD.md does not reference 500-page threshold")
    if threshold and "threshold" not in threshold.lower():
        warnings.append("CORPUS_LAUNCH_THRESHOLD.md may lack explicit threshold language")

    wave_model = read_doc("main/data/CORPUS_PRODUCTION_WAVE_MODEL.md")
    wave_control = read_doc("main/data/CORPUS_PRODUCTION_WAVE_CONTROL_MODEL.md")
    combined_wave = wave_model + "\n" + wave_control

    for phrase in WAVE_MODEL_REQUIRED:
        if phrase.lower() not in combined_wave.lower():
            errors.append(f"Wave planning docs missing required concept: {phrase!r}")

    if "route" in combined_wave.lower() and "draft" in combined_wave.lower():
        if "separate" not in combined_wave.lower() and "distinct" not in combined_wave.lower():
            warnings.append("Wave docs should explicitly separate route waves from draft waves")

    gate_model = read_doc("main/data/CORPUS_PRODUCTION_GATE_MODEL.md")
    if gate_model:
        for gate in ("source gate", "claim gate", "publication gate"):
            if gate not in gate_model.lower():
                errors.append(f"CORPUS_PRODUCTION_GATE_MODEL.md missing: {gate}")
    else:
        errors.append("CORPUS_PRODUCTION_GATE_MODEL.md empty or missing")

    scan_corpus = "\n".join(read_doc(rel) for rel in REQUIRED_DOCS)
    scan_corpus += read_doc("main/data/SOURCE_REGISTRY_PROPOSAL_NEXT_ACTIONS_WAVE_1.md")
    scan_corpus += read_doc("main/data/DRAFT_WAVE_1_NEXT_ACTIONS.md")

    for pat in FORBIDDEN_PATTERNS:
        if pat.search(scan_corpus):
            errors.append(f"Forbidden production plan pattern found: {pat.pattern}")

    if not DRAFT_W2_WAIT.search(scan_corpus):
        warnings.append(
            "No explicit draft wave 2 wait/defer language found in scanned planning docs"
        )

    sovereign = read_doc("main/data/FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md")
    if sovereign and "500" not in sovereign:
        errors.append("FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md missing 500-page reference")

    if "source" in combined_wave.lower() and "publication" in combined_wave.lower():
        src_idx = combined_wave.lower().find("source")
        pub_idx = combined_wave.lower().find("publication")
        if pub_idx < src_idx and "precede" not in combined_wave.lower():
            warnings.append("Verify source/claim gates precede publication in wave sequence")

    return errors, warnings


def main() -> int:
    errors, warnings = run_validation()
    print("=== Production Wave Plan L2 Validation ===")
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
