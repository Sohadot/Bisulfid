# COHORT_02 Full Draft — Knowledge Reliability Coverage Report

**Sprint:** 6J  
**Cohort:** `COHORT_02_EN_TERMINOLOGY_SPINE`  
**Date:** 2026-05-30  
**Scope:** Reliability profile, evidence grade, and epistemic posture across 902 drafts

---

## Verdict

**PASS** — full reliability profile coverage across all 902 COHORT_02 drafts.

---

## Knowledge reliability level

| knowledge_reliability_level | Count | Coverage |
| --- | ---: | :---: |
| L2_draft_cautious | 902 | **902/902** |

All drafts carry cautious draft-level reliability labeling consistent with `SOVEREIGN_KNOWLEDGE_RELIABILITY_MODEL_WAVE_1.md` posture for source-pending terminology inventory.

---

## Evidence grade coverage

| evidence_grade | Count | page_type context |
| --- | ---: | --- |
| terminology_dictionary | 428 | Canonical, compound, audience, child-safe, AI-readable |
| unsourced_pending | 426 | Canonical, compound, audience, child-safe, AI-readable |
| comparative_boundary | 48 | PT_DIFFERENCE_COMPARISON only |

| Check | Result |
| --- | --- |
| Every draft has `evidence_grade` in front matter | **902/902** |
| Every draft has evidence grade in reliability notice table | **902/902** |
| No draft claims L1_publication_ready or equivalent | **PASS** |
| Comparison drafts use comparative_boundary grade | **48/48** |

---

## Source posture coverage

| source_posture | Count |
| --- | ---: |
| source_required_unresolved | 902 |

| Check | Result |
| --- | --- |
| Source posture in front matter | **902/902** |
| Source posture in reliability notice | **902/902** |
| Source and claim status section | **902/902** |
| Source-pending marker in body | **902/902** (`[SOURCE REQUIRED]`) |
| No false source_verified posture | **PASS** |

---

## Claim posture coverage

| claim_posture | Count |
| --- | ---: |
| claim_pending_review | 902 |

| Check | Result |
| --- | --- |
| Claim posture in front matter | **902/902** |
| Claim posture in reliability notice | **902/902** |
| Explicit "no approved publication claim" statement | **902/902** |
| No false claim_approved posture | **PASS** |

---

## Reliability notice table (required fields)

All 902 drafts include reliability notice table with:

| Field | Coverage |
| --- | ---: |
| knowledge_reliability_level | 902/902 |
| evidence_grade | 902/902 |
| source_posture | 902/902 |
| claim_posture | 902/902 |
| generation_eligibility | 902/902 |
| excluded_claim_classes | 902/902 |

---

## Unresolved fields coverage

All 902 drafts document unresolved fields including at minimum:

- source_verification
- claim_approval
- public_route_merge
- indexation
- multilingual_expansion

Comparison drafts (48) additionally document `comparison_boundary_verification`.

---

## Reliability by page type

| page_type_id | Count | L2_draft_cautious | Source pending | Claim pending |
| --- | ---: | :---: | :---: | :---: |
| PT_TERM_CANONICAL | 300 | ✓ | ✓ | ✓ |
| PT_AUDIENCE_EXPLAINER | 250 | ✓ | ✓ | ✓ |
| PT_COMPOUND_ENTITY | 128 | ✓ | ✓ | ✓ |
| PT_AI_READABLE | 100 | ✓ | ✓ | ✓ |
| PT_CHILD_SAFE_EDU | 76 | ✓ | ✓ | ✓ |
| PT_DIFFERENCE_COMPARISON | 48 | ✓ | ✓ | ✓ |

---

## Publication readiness from reliability perspective

| Gate | Status |
| --- | --- |
| Reliability profiles complete | **Yes** |
| Ready for public reference publication | **No** |
| Ready for route registration (reliability only) | **Planning-ready** — subject to separate merge charter and source/claim gates |
| production_can_safely_proceed | **no** |

---

## Summary

| Metric | Result |
| --- | --- |
| Drafts with full reliability profile | **902/902** |
| Missing evidence grade | **0** |
| Missing source/claim posture | **0** |
| **Overall** | **PASS** |

---

*Sprint 6J — COHORT_02 Knowledge Reliability Coverage Report*
