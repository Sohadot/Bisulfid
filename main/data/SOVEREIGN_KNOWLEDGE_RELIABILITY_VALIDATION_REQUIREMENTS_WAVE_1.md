# Sovereign Knowledge Reliability Validation Requirements — Wave 1

**Sprint:** 6C (Scope Amendment)  
**Purpose:** Knowledge reliability validation checklist for future generator outputs.

---

## Mandatory checks (severity-1 — block merge)

| ID | Check |
| --- | --- |
| KR-01 | No unsupported factual claim on page |
| KR-02 | No unsupported comparison distinction |
| KR-03 | No market/economic claim without economic/market source type |
| KR-04 | No safety/medical/procurement/handling claim without separately approved source class |
| KR-05 | No educational oversimplification that changes meaning |
| KR-06 | AI-readable page includes source_status, claim_status, excluded_claims, unresolved_fields |
| KR-07 | No high-authority language on source_pending or claim_pending grade |
| KR-08 | No indexable page with source_pending or claim_pending |
| KR-09 | knowledge_reliability_profile present on every generated draft |
| KR-10 | excluded_claim_classes not hidden |
| KR-11 | Draft not presented as final (reliability notice + draft status) |
| KR-12 | evidence_grade matches registry postures — no upgrade |
| KR-13 | Source hierarchy ranks preserved in citations |
| KR-14 | page_assertion_limit not exceeded |
| KR-15 | comparative_boundary pages include per-side sourcing disclosure |

---

## Comparison-specific (KR-COMP)

| ID | Check |
| --- | --- |
| KR-C01 | Both comparison sides addressed |
| KR-C02 | Side A sourcing status disclosed |
| KR-C03 | Side B sourcing status disclosed |
| KR-C04 | No winner/loser claim without source |
| KR-C05 | bisulfite/bisulfide conflation forbidden |

---

## Educational / child-safe (KR-EDU)

| ID | Check |
| --- | --- |
| KR-E01 | No experiment instructions |
| KR-E02 | No handling or hazard detail |
| KR-E03 | simplification_limit enforced |
| KR-E04 | child_safe_flag when AUD_CHILD_EDU |

---

## Economic / institutional / logistical (KR-ECON)

| ID | Check |
| --- | --- |
| KR-X01 | No unsourced CAGR, pricing, trade, procurement |
| KR-X02 | No acquisition targeting language |
| KR-X03 | Terminology source not used as market evidence |
| KR-X04 | economic_context_pending until market sources verified |
| KR-X05 | No operational transport/storage guidance on logistical pages |

---

## AI-readable (KR-AI)

| ID | Check |
| --- | --- |
| KR-A01 | structured provenance block present |
| KR-A02 | excluded_claims machine-readable list |
| KR-A03 | unresolved_fields explicit array |
| KR-A04 | No inferred facts beyond registry |

---

## Implementation note (6D+)

These requirements specify **future validators** (`validate_knowledge_reliability_l1.py` — not created in 6C). Existing L1 runtimes remain unchanged; no weakening.

---

## Reliability profile schema validation

All 18 profile fields must be present in generation manifest JSON even if some values are `null` or empty arrays — **never omitted**.
