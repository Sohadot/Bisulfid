# Sovereign Knowledge Reliability Model — Wave 1

**Sprint:** 6C (Scope Amendment)  
**Principle:** Bisulfid.com must not merely appear authoritative — it must expose **why** each page is reliable, what evidence supports it, what claims are allowed, what is excluded, and what remains unresolved.

---

## Knowledge reliability profile (required — not optional)

Every future generated page must include or be governed by a **knowledge reliability profile** with these fields:

| Field | Purpose |
| --- | --- |
| `knowledge_reliability_level` | L0–L5 scale (see evidence grade registry) |
| `evidence_grade` | One of 8 governed grades |
| `source_hierarchy` | Ranked source types used on page |
| `source_count_required` | Minimum verified sources for factual lines |
| `primary_source_required` | Boolean — terminology lines require primary type |
| `secondary_source_allowed` | Supporting sources same claim class only |
| `claim_boundary_required` | Registered claim_ids for factual sections |
| `claim_confidence` | unsettled / narrow_approved / approved / forbidden |
| `citation_mode` | From template contract |
| `provenance_note` | Human-readable reliability summary |
| `last_reviewed_policy` | Review cadence reference |
| `unresolved_fields` | Explicit list of open factual areas |
| `excluded_claim_classes` | Visible on page — not hidden |
| `conflict_resolution_policy` | When sources disagree — defer or boundary |
| `human_review_required` | Trigger from template |
| `machine_readability_level` | For AI-readable templates |
| `audience_simplification_limit` | Max simplification for audience |
| `page_assertion_limit` | Max factual assertions per evidence grade |

---

## Evidence grades

See `SOVEREIGN_EVIDENCE_GRADE_REGISTRY_WAVE_1.json` for machine-readable definitions:

1. **source_verified** — Verified source + approved claim boundary  
2. **claim_approved** — Only approved claims within boundary  
3. **source_pending** — Draft OK; facts not settled  
4. **claim_pending** — Source may exist; claim not approved  
5. **educational_simplification** — Learning audience; no false certainty  
6. **comparative_boundary** — Comparison with per-side sourcing disclosure  
7. **economic_context_pending** — No market conclusions without economic sources  
8. **restricted_claim_class** — Hard reject for forbidden claim classes  

---

## Source hierarchy

See `SOVEREIGN_SOURCE_HIERARCHY_MODEL_WAVE_1.json`. Types ranked — **never flattened**:

authoritative dictionary → nomenclature standard → scientific database → peer-reviewed → institutional/government → standards → educational → economic/market → commercial → unsourced/pending

---

## Page reliability behavior (10 rules)

1. Never state more than evidence grade allows.  
2. Verified dictionary supports terminology only — not safety, market, medical, industrial, production, procurement.  
3. Scientific database supports identifiers/facts — not market or policy claims.  
4. Economic pages cannot use chemistry terminology sources as market evidence.  
5. Educational pages may simplify but must not distort meaning.  
6. Child-safe pages avoid experiment, handling, hazard, medical, procurement guidance.  
7. AI-readable pages expose source status, claim status, excluded claims, unresolved areas.  
8. Comparison pages disclose whether each side is equally sourced, partial, or unresolved.  
9. Weak evidence → noindex / non-public unless explicit status-page charter.  
10. Never convert absence of evidence into factual conclusion.  

---

## Integration with generator schema

`SOVEREIGN_CORPUS_GENERATOR_SCHEMA_WAVE_1.json` requires `knowledge_reliability_profile` on every generation unit. Templates in `SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json` define required evidence grade and reliability notice behavior.

---

## Epistemic credibility goal

Sprint 6C enables production of **highly credible, source-bounded, claim-bounded, reliability-labeled** reference pages — not merely many pages.
