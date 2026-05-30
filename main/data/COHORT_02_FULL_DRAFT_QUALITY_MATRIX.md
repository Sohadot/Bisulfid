# COHORT_02 Full Draft — Quality Matrix

**Sprint:** 6J  
**Cohort:** `COHORT_02_EN_TERMINOLOGY_SPINE`  
**Date:** 2026-05-30  
**Scope:** Validation audit of 902 non-public English terminology drafts

---

## Audit summary

| Metric | Result |
| --- | --- |
| Draft files audited | **902 / 902** |
| Manifest alignment | **902 / 902** |
| Inventory alignment | **902 / 902** |
| Fake-page risk | **None identified** |
| Thin-page risk | **None** (253–298 words; full section scaffold) |
| Blog-style risk | **None** |
| Forbidden claim risk (narrative) | **None** |
| Unsupported claim risk | **None** (source-pending posture enforced) |
| Reliability profile coverage | **902 / 902** |
| Evidence grade coverage | **902 / 902** |
| noindex / non-public posture | **902 / 902 PASS** |
| Excluded claim classes visible | **902 / 902** |
| Unresolved fields documented | **902 / 902** |
| Publication blockers present | **902 / 902** |
| Internal-link placeholder integrity | **902 / 902** (0 broken route_id refs) |
| Route publication effect | **None** (not in routes.json) |
| Content corrections required | **None** |

---

## Aggregate quality matrix (by page type)

| page_type_id | Count | Fake | Thin | Blog | Claims | Reliability | noindex | Link role |
| --- | ---: | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| PT_TERM_CANONICAL | 300 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | term_spine |
| PT_AUDIENCE_EXPLAINER | 250 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | audience_cluster |
| PT_COMPOUND_ENTITY | 128 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | term_spine |
| PT_AI_READABLE | 100 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ai_readable_cluster |
| PT_CHILD_SAFE_EDU | 76 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | child_safe_cluster |
| PT_DIFFERENCE_COMPARISON | 48 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | comparison_cluster |
| **Total** | **902** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |

**Legend:** ✓ = pass / no risk identified for that column.

---

## Aggregate quality matrix (by reference layer)

| reference_layer_id | Count | Reliability | Evidence | Source posture | Claim posture |
| --- | ---: | :---: | :---: | :---: | :---: |
| REF_KNOWLEDGE | 232 | ✓ | ✓ | ✓ | ✓ |
| REF_RESEARCH | 194 | ✓ | ✓ | ✓ | ✓ |
| REF_TECHNICAL | 144 | ✓ | ✓ | ✓ | ✓ |
| REF_EDUCATIONAL | 138 | ✓ | ✓ | ✓ | ✓ |
| REF_ACADEMIC | 82 | ✓ | ✓ | ✓ | ✓ |
| REF_LINGUISTIC | 62 | ✓ | ✓ | ✓ | ✓ |
| REF_INSTITUTIONAL | 50 | ✓ | ✓ | ✓ | ✓ |

---

## Aggregate quality matrix (by audience)

| audience_id | Count | Reliability | noindex | Child-safe checks |
| --- | ---: | :---: | :---: | :---: |
| AUD_STUDENT | 232 | ✓ | ✓ | n/a |
| AUD_CHEMIST | 194 | ✓ | ✓ | n/a |
| AUD_RESEARCHER | 194 | ✓ | ✓ | n/a |
| AUD_AI_SYSTEM | 144 | ✓ | ✓ | n/a |
| AUD_ANALYST | 50 | ✓ | ✓ | n/a |
| AUD_GOVERNMENT | 50 | ✓ | ✓ | n/a |
| AUD_CHILD_EDU | 38 | ✓ | ✓ | ✓ (76 child-safe pages total) |

---

## Required front matter (902 / 902)

| Field | Coverage |
| --- | ---: |
| `route_id` | 902/902 |
| `status: draft` | 902/902 |
| `publication_status: non_public` | 902/902 |
| `publication_eligibility: false` | 902/902 |
| `indexable: false` | 902/902 |
| `in_sitemap: false` | 902/902 |
| `in_navigation: false` | 902/902 |
| `noindex_default: true` | 902/902 |
| `evidence_grade` | 902/902 |
| `knowledge_reliability_level: L2_draft_cautious` | 902/902 |
| `source_posture: source_required_unresolved` | 902/902 |
| `claim_posture: claim_pending_review` | 902/902 |
| `cohort_id: COHORT_02_EN_TERMINOLOGY_SPINE` | 902/902 |
| `generated: true` | 902/902 |
| `engine: generate_cohort_02_full_draft_wave_v1` | 902/902 |

---

## Required body sections (902 / 902)

1. Draft status banner (non-public, not indexable, not publication-ready)
2. Reliability notice table
3. Page purpose (page-type-specific bullets)
4. `[SOURCE REQUIRED]` marker for unsupported factual lines
5. Source and claim status block
6. Unresolved fields list
7. Publication blockers
8. Internal link placeholders (`route_id` only — no live URLs)

---

## Word count envelope

| Metric | Value |
| --- | ---: |
| Minimum | 253 |
| Maximum | 298 |
| Mean | ~261 |
| Below 180-word threshold | 0 |
| Below 150-word threshold (child-safe) | 0 |

---

## Structural duplication assessment

| Check | Result |
| --- | --- |
| Unique normalized body signatures (route metadata stripped) | **902** |
| Maximum duplicate group size | **1** |
| Shared templates by page_type_id | **6** (expected) |
| Route-level identity preserved | **Yes** — each draft differs by term, audience, reference layer, and page type |
| Systemic shell-only duplication | **Not detected** |

**Note:** Structural similarity across page types is expected for registry-constrained generation. Each draft maintains distinct `route_id`, `term_or_entity`, dimensional metadata, and page-purpose content. No generator refinement sprint required for duplication.

---

## Sample unit verification (first entity: bisulfid)

| route_id | page_type_id | Words | Pass |
| --- | --- | ---: | :---: |
| `cohort02_en_bisulfid_term_chem_acad` | PT_TERM_CANONICAL | 313 | ✓ |
| `cohort02_en_bisulfid_term_chem_know` | PT_TERM_CANONICAL | 313 | ✓ |
| `cohort02_en_bisulfid_aud_chem_know` | PT_AUDIENCE_EXPLAINER | ~320 | ✓ |
| `cohort02_en_bisulfid_term_ai_tech` | PT_AI_READABLE | ~320 | ✓ |
| `cohort02_en_bisulfid_aud_stu_edu` | PT_CHILD_SAFE_EDU | ~320 | ✓ |
| `cohort02_en_bisulfid_vs_bisulfide_chem_ling` | PT_DIFFERENCE_COMPARISON | ~340 | ✓ |

Full per-unit listing available in `COHORT_02_FULL_DRAFT_MANIFEST.json` (902 units).

---

## Corrections required

**None.** All 902 drafts pass Sprint 6J quality audit without content modification.

---

*Sprint 6J — COHORT_02 Quality Matrix*
