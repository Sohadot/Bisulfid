# COHORT_02 English Comparison Route Subset Model

**Sprint:** 6H  
**Cohort:** `COHORT_02_EN_TERMINOLOGY_SPINE`  
**Date:** 2026-05-30  
**Posture:** Comparison inventory subset — cautious claim posture only

---

## Purpose

Document the **48 comparison inventory rows** (12 pairs × 4 audience/reference combinations) included in COHORT_02. Comparison routes are high-intent SEO family pages — included only with **cautious claim posture** and **future source/claim verification** requirement before content generation.

---

## Inclusion rule

Comparison rows included **only if**:

1. Both sides exist as registered entity IDs in the spine model
2. `page_type_id`: PT_DIFFERENCE_COMPARISON
3. `template_id`: TPL_COMPARE_V1
4. `evidence_grade`: comparative_boundary
5. `source_posture`: source_required_unresolved (both sides)
6. `claim_posture`: claim_pending_review
7. `publication_eligibility`: false
8. `generation_eligibility`: conditional — distinction framing only; no unsupported winner claims
9. Distinction intent documented in `comparison_reference_mode`

---

## Comparison pairs (12)

| comparison_pair_id | Side A | Side B | Mode | Inventory rows |
| --- | --- | --- | --- | ---: |
| bisulfid_vs_bisulfide | bisulfid | bisulfide | linguistic_comparison | 4 |
| sulfid_vs_sulfide | sulfid | sulfide | linguistic_comparison | 4 |
| bisulfide_vs_hydrosulfide | bisulfide | hydrosulfide | technical_comparison | 4 |
| bisulfide_vs_sulfide | bisulfide | sulfide | technical_comparison | 4 |
| bisulfite_vs_bisulfide | bisulfite_disambiguation | bisulfide | linguistic_comparison | 4 |
| sulfur_vs_sulfide | sulfur | sulfide | technical_comparison | 4 |
| disulfide_vs_sulfide | disulfide | sulfide | technical_comparison | 4 |
| sodium_bisulfide_vs_hydrosulfide | sodium_bisulfide | sodium_hydrosulfide | technical_comparison | 4 |
| mos2_vs_disulfide | molybdenum_disulfide | disulfide | technical_comparison | 4 |
| sulfate_vs_sulfide | sulfate | sulfide | technical_comparison | 4 |
| sulfite_vs_sulfide | sulfite | sulfide | technical_comparison | 4 |
| thiosulfate_vs_sulfate | thiosulfate | sulfate | technical_comparison | 4 |

**Total:** 48 rows

---

## Audience × reference combinations (per pair)

| audience_id | reference_layer_id | Rationale |
| --- | --- | --- |
| AUD_CHEMIST | REF_LINGUISTIC | Chemical-language distinction |
| AUD_RESEARCHER | REF_RESEARCH | Research-grade boundary framing |
| AUD_STUDENT | REF_EDUCATIONAL | Educational distinction (no conclusion) |
| AUD_AI_SYSTEM | REF_TECHNICAL | Machine-readable comparison record |

---

## Forbidden comparison content (generation + publication)

- Unsupported winner claims ("X is better than Y")
- Safety contrast without per-side source
- Market or procurement comparison
- Medical or handling instruction contrast
- Conclusion without `[SOURCE REQUIRED]` on factual lines
- Indexation before comparative_boundary satisfied (G3/G4)

---

## Overlap with existing routes.json

Some comparison themes overlap existing planned routes (e.g. `bisulfid_vs_bisulfide`, `sulfid_vs_sulfide`). COHORT_02 inventory rows use **distinct route_ids** (`cohort02_en_*`) and **dimensional path patterns** for audience/reference-layer expansion. Merge charter must resolve canonical route deduplication before publication.

---

## Internal link requirements

Each comparison row requires (planning):

- `en_foundation_sovereign_intro`
- `glossary`
- Side A canonical inventory row
- Side B canonical inventory row
- `internal_link_role`: comparison_cluster

---

## Validation gates (comparison-specific)

**G0–G7** plus comparison-specific checks:

- Both sides addressed (TPL_COMPARE quality threshold)
- Sourcing disclosure section required in future draft
- Human review trigger: first 100 comparison pages (6C template contract)

---

*Sprint 6H — Comparison Route Subset Model*
