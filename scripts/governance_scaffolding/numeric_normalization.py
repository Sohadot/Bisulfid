"""
Source-specific numeric normalization for quantitative evidence.

A quantitative measure must distinguish source_literal (string, as printed) from
normalized_value (machine number) and unit, AND declare a governed numeric
convention id. Convention is SOURCE-SPECIFIC: it is never inferred from language,
country, or file extension, and there is NO silent French fallback.

Governed conventions:
  NUM-FR-DOT-THOUSANDS     : dot '.' = thousands separator (French report). '9.108' -> 9108.
  NUM-EN-DOT-DECIMAL       : dot '.' = decimal point (English/international). '1.099' -> 1.099.
  NUM-PLAIN-INT            : plain integer, no grouping/decimal. '9108' -> 9108.
  NUM-ACCOUNTING-PAREN-NEG : accounting presentation — comma '.' = thousands, dot = decimal,
                             and PARENTHESES mean NEGATIVE. '(8,344)' -> -8344 (signed);
                             '8,344' -> 8344. Parentheses are NEVER silently dropped: a
                             parenthesized literal MUST normalize to a negative value. A
                             positive magnitude for prose is DERIVED via magnitude() and must
                             be labelled as magnitude, never stored as a competing normalized_value.

Pure; no I/O; unwired from CI.
"""

import re

GOVERNED_CONVENTIONS = {"NUM-FR-DOT-THOUSANDS", "NUM-EN-DOT-DECIMAL", "NUM-PLAIN-INT", "NUM-ACCOUNTING-PAREN-NEG"}

_FR_GROUPED = re.compile(r"^[+-]?\d{1,3}(\.\d{3})+$")
_PLAIN_INT = re.compile(r"^[+-]?\d+$")
_EN_DECIMAL = re.compile(r"^[+-]?\d{1,3}(,\d{3})*(\.\d+)?$")  # optional comma-thousands, dot-decimal
_ACCT_MAG = re.compile(r"^\d{1,3}(,\d{3})*(\.\d+)?$")         # comma-thousands, optional dot-decimal magnitude


def _acct_parse(s):
    """Parse an accounting literal -> (signed_value, error). Parentheses => negative."""
    negative = False
    body = s
    if body.startswith("(") and body.endswith(")"):
        negative = True
        body = body[1:-1].strip()
    elif body.startswith("-"):
        negative = True
        body = body[1:].strip()
    if not _ACCT_MAG.match(body):
        return (None, f"'{s}' is not an accounting literal (comma-thousands, parentheses=negative)")
    v = float(body.replace(",", ""))
    v = int(v) if v.is_integer() else v
    return (-v if negative else v, None)


def normalize(literal, convention_id):
    """Return (value, error). value is an int/float when parseable, else None with an error."""
    if not isinstance(literal, str):
        return (None, "source_literal must be a string")
    s = literal.strip()
    if convention_id == "NUM-FR-DOT-THOUSANDS":
        if _FR_GROUPED.match(s):
            return (int(s.replace(".", "")), None)
        if _PLAIN_INT.match(s):
            return (int(s), None)
        return (None, f"'{s}' is not a FR grouped/plain integer")
    if convention_id == "NUM-EN-DOT-DECIMAL":
        if _EN_DECIMAL.match(s):
            v = float(s.replace(",", ""))
            return (int(v) if v.is_integer() else v, None)
        return (None, f"'{s}' is not an EN decimal/thousands literal")
    if convention_id == "NUM-PLAIN-INT":
        if _PLAIN_INT.match(s):
            return (int(s), None)
        return (None, f"'{s}' is not a plain integer")
    if convention_id == "NUM-ACCOUNTING-PAREN-NEG":
        return _acct_parse(s)
    return (None, f"unknown numeric_convention_id '{convention_id}'")


def magnitude(value):
    """Absolute magnitude of a signed accounting value, for prose use ONLY.
    The caller MUST label the result as a magnitude; it is never the stored normalized truth."""
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return None
    return abs(value)


# Backwards-compatible helper (Morocco convention) used by earlier correction tests.
def normalize_fr_grouped(literal):
    v, _ = normalize(literal, "NUM-FR-DOT-THOUSANDS")
    return v


def iter_measures(obj, path="$"):
    """Yield (path, dict) for every mapping carrying both source_literal and normalized_value."""
    if isinstance(obj, dict):
        if "source_literal" in obj and "normalized_value" in obj:
            yield (path, obj)
        for k, v in obj.items():
            yield from iter_measures(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from iter_measures(v, f"{path}[{i}]")


def _convention_of(evidence_record):
    q = evidence_record.get("quantitative") or {}
    return q.get("numeric_convention_id") or evidence_record.get("numeric_convention_id")


def validate_evidence_numbers(evidence_record):
    """Validate normalization for an evidence record using its DECLARED convention.
    Fails (no silent fallback) if quantitative measures exist without a governed convention."""
    errs = []
    measures = list(iter_measures(evidence_record))
    if not measures:
        return errs  # nothing quantitative to normalize
    conv = _convention_of(evidence_record)
    if conv is None:
        return [f"$: quantitative measures present but no governed numeric_convention_id declared "
                f"(source-specific; no French fallback)"]
    if conv not in GOVERNED_CONVENTIONS:
        return [f"$: numeric_convention_id '{conv}' is not a governed convention {sorted(GOVERNED_CONVENTIONS)}"]
    for path, m in measures:
        lit, nv = m.get("source_literal"), m.get("normalized_value")
        if not isinstance(lit, str):
            errs.append(f"{path}: source_literal must be a string"); continue
        if not isinstance(nv, (int, float)) or isinstance(nv, bool):
            errs.append(f"{path}: normalized_value must be numeric"); continue
        expected, e = normalize(lit, conv)
        if e:
            errs.append(f"{path}: {e}"); continue
        if nv != expected:
            errs.append(f"{path}: normalized_value {nv} != {expected} for '{lit}' under {conv}")
    return errs
