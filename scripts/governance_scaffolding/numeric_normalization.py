"""
Numeric normalization law for locale-formatted quantitative evidence.

A quantitative measure must distinguish source_literal (string, as printed) from
normalized_value (machine number) and unit, and record the source numeric convention.
This module catches the specific failure of using an ambiguous locale literal
(e.g. French "9.108" where the dot is a THOUSANDS separator) directly as a machine
float. Normalization is SOURCE-SPECIFIC; do not assume all sources share a convention.

Pure; no I/O; unwired from CI.
"""

import re

# A French-grouped integer literal: 1-3 digits, then groups of exactly 3 digits, dot-separated.
FR_GROUPED = re.compile(r"^[+-]?\d{1,3}(\.\d{3})+$")
# A plain integer literal (no grouping).
PLAIN_INT = re.compile(r"^[+-]?\d+$")


def normalize_fr_grouped(literal):
    """Normalize a French dot-thousands-grouped literal to an int.
    '9.108' -> 9108 ; '18.768' -> 18768 ; '+1.101' -> 1101 ; '1.099' -> 1099.
    Returns int, or None if the literal is not a grouped/plain integer."""
    if not isinstance(literal, str):
        return None
    s = literal.strip()
    if FR_GROUPED.match(s):
        return int(s.replace(".", ""))
    if PLAIN_INT.match(s):
        return int(s)
    return None


def iter_measures(obj, path="$"):
    """Yield (path, dict) for every mapping that carries both source_literal and normalized_value."""
    if isinstance(obj, dict):
        if "source_literal" in obj and "normalized_value" in obj:
            yield (path, obj)
        for k, v in obj.items():
            yield from iter_measures(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from iter_measures(v, f"{path}[{i}]")


def validate_measure(m, convention="fr_dot_thousands"):
    """Return a list of errors for a single {source_literal, normalized_value[, unit]} measure."""
    errs = []
    lit = m.get("source_literal")
    nv = m.get("normalized_value")
    if not isinstance(lit, str):
        errs.append("source_literal must be a string")
        return errs
    if not isinstance(nv, (int, float)) or isinstance(nv, bool):
        errs.append("normalized_value must be numeric")
        return errs
    if convention == "fr_dot_thousands":
        expected = normalize_fr_grouped(lit)
        if expected is None:
            # not a grouped/plain integer literal; nothing to enforce here
            return errs
        if nv != expected:
            errs.append(f"normalized_value {nv} != grouped-normalized {expected} for literal '{lit}'")
        # catch the classic bug: literal '9.108' stored as the naive float 9.108
        if "." in lit and isinstance(nv, float) and abs(nv - float(lit)) < 1e-9 and nv != expected:
            errs.append(f"ambiguous literal '{lit}' stored as naive float {nv} (dot is a thousands separator)")
    return errs


def validate_evidence_numbers(evidence_record, convention="fr_dot_thousands"):
    """Validate every source_literal/normalized_value pair inside an evidence record."""
    errs = []
    for path, m in iter_measures(evidence_record):
        for e in validate_measure(m, convention):
            errs.append(f"{path}: {e}")
    return errs
