# Initial 14,000-Page Launch Quality Thresholds

**Sprint:** 6G  
**Date:** 2026-05-30  
**Posture:** Minimum quality requirements per page family at launch scale

---

## Universal minimum (all 14,000 pages)

| Requirement | Threshold |
| --- | --- |
| Registry binding | Every page maps to valid page_type, audience, reference_layer |
| Generation method | Deterministic, registry-constrained — **no LLM free-form** |
| Reliability profile | Required on every page |
| Minimum reliability level (draft) | **L2_draft_cautious** |
| Evidence grade | From registry — never upgraded without charter |
| Fake-page rejection | Invalid dimension intersection → hard reject |
| Thin-page rejection | Below family minimum word/section count → hard reject |
| Unsupported claims | Forbidden claim classes enforced |
| `[SOURCE REQUIRED]` | Preserved on all unresolved factual lines |
| Publication posture | `non_public` until launch gate |
| Indexation default | `noindex_default` or `noindex_governance` |
| Orphan policy | Zero orphans in cohort subgraph at registration |

---

## Per page family thresholds

### PT_TERM_CANONICAL / PT_COMPOUND_ENTITY

| Field | Minimum |
| --- | --- |
| Body words (excl. front matter) | **≥ 180** |
| Required sections | definition, scope boundary, source/claim status, publication blockers |
| Source posture (draft) | source_required_unresolved or source_verified |
| Claim posture (draft) | claim_pending_review or claim_approved_narrow minimum for publication |
| Reliability level (indexation candidate) | **L3_source_bound** minimum |
| Evidence grade | terminology_dictionary or academic_citation minimum for indexation |
| `[SOURCE REQUIRED]` on factual chemistry | **Required** until source_locked |

### PT_DIFFERENCE_COMPARISON

| Field | Minimum |
| --- | --- |
| Body words | **≥ 200** |
| Required sections | distinction intent, side definitions, non-conclusion framing, source/claim status |
| Entity requirement | comparison_pair with both sides in ontology |
| Forbidden | Unsupported conclusion without source |
| Reliability level (indexation candidate) | **L3_source_bound** |
| Internal links | ≥ 2 (hub + both term records) |

### PT_AUDIENCE_EXPLAINER

| Field | Minimum |
| --- | --- |
| Body words | **≥ 160** |
| Audience simplification limit | Per audience_layer_registry |
| Forbidden claim classes | Per audience (e.g. AUD_CHILD_EDU: safety, medical, handling) |
| Anti-duplication | Must differ from sibling by reference_layer or vocabulary level |

### PT_MULTILINGUAL_EQUIV / PT_MULTILINGUAL_HUB

| Field | Minimum |
| --- | --- |
| hreflang_group | Required |
| Cross-language link | Planning graph only until alternates validated |
| Forbidden | Machine-translation spam; unverified equivalence asserted as fact |

### PT_FOUNDATION / PT_METHODOLOGY_GOVERNANCE / PT_CORPUS_STATUS

| Field | Minimum |
| --- | --- |
| Body words | **≥ 200** (COHORT_01 baseline: 225–242) |
| Source/claim posture | source_not_required / claim_not_required |
| Indexation | **noindex_governance** even post-launch default |
| COHORT_01 reference | 15 EN pages validated 6E |

### PT_CHILD_SAFE_EDU

| Field | Minimum |
| --- | --- |
| Body words | **≥ 150** |
| Reference layer | REF_EDUCATIONAL only |
| Forbidden | Handling, experiment, hazard instruction |
| Reliability level | L2_draft_cautious maximum until educational review gate |

### PT_AI_READABLE

| Field | Minimum |
| --- | --- |
| Structured provenance block | Required |
| Machine readability level | structured or enhanced |
| Excluded claims | Visible in metadata |
| Forbidden | Inferred facts beyond registry |

### PT_SOURCE_BOUND / PT_CLAIM_BOUNDARY / PT_SOURCE_STATUS / PT_CLAIM_STATUS

| Field | Minimum |
| --- | --- |
| Registry reference | Must cite actual source_id or claim_id |
| Forbidden | Implies approval not in registry |
| Posture transparency | Registry inactive state documented |

### PT_INVESTOR_ECONOMIC / PT_COMPANY_INDUSTRY / PT_GOVERNMENT_POLICY

| Field | Minimum |
| --- | --- |
| Reference layer | REF_ECONOMIC or REF_INSTITUTIONAL |
| Source posture (publication) | source_verified minimum |
| Forbidden | CAGR, pricing, market share without verified source |
| Indexation | **noindex_default** until economic source gate cleared |

### PT_GLOSSARY_CLUSTER

| Field | Minimum |
| --- | --- |
| Cluster scope declared | Required |
| Minimum terms indexed | **≥ 5** route_id references |
| Hub link | ≥ 1 inbound from terminology spine |

---

## Knowledge reliability by reference layer

| reference_layer_id | Min reliability (draft) | Min reliability (indexation candidate) | Evidence grade floor |
| --- | --- | --- | --- |
| REF_ACADEMIC | L2_draft_cautious | L3_source_bound | academic_citation |
| REF_KNOWLEDGE | L2_draft_cautious | L3_source_bound | terminology_dictionary |
| REF_RESEARCH | L2_draft_cautious | L4_research_verified | research_primary |
| REF_EDUCATIONAL | L2_draft_cautious | L3_source_bound | educational_simplified |
| REF_ECONOMIC | L2_draft_cautious | L4_research_verified | economic_context_verified |
| REF_INSTITUTIONAL | L2_draft_cautious | L2_draft_cautious | claim_not_required |
| REF_TECHNICAL | L2_draft_cautious | L3_source_bound | structured_technical |
| REF_LINGUISTIC | L2_draft_cautious | L3_source_bound | terminology_dictionary |
| REF_LOGISTICAL | L2_draft_cautious | L3_source_bound | documentation_reference |

---

## Anti-thin and anti-duplication (14k scale)

1. **Thin reject:** Below family word minimum OR missing required sections.
2. **Duplicate reject:** Same `route_key` hash (language + entity + page_type + audience + reference_layer).
3. **Shallow duplicate reject:** reference_layer change does not alter structure, vocabulary, evidence standard, or claim boundary (6B rule).
4. **Volume inflation reject:** Cartesian product without compatibility filter pass.

---

## Validation gates (all cohorts)

**G0** schema · **G1** registry · **G2** template · **G3** source · **G4** claim · **G5** reliability · **G6** link graph · **G7** indexation lock

Publication requires **G0–G7 pass** + human sample audit ≥10%.

---

*Sprint 6G — Launch Quality Thresholds*
