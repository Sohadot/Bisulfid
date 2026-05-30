# Initial 14,000-Page Launch Corpus Charter

**Sprint:** 6G  
**Date:** 2026-05-30  
**Site:** bisulfid.com  
**Posture:** Execution charter only — **not publication**, **not mass generation**

---

## Strategic declaration

The **14,000-page corpus is the minimum initial launch corpus** for bisulfid.com as a sovereign-grade, strategic, institutional, academic, multilingual reference asset. It is **not** a distant future target.

The long-term objective is expansion to **100,000+** and ultimately **300,000+** governed reference pages without architectural collapse, SEO dilution, link decay, or governance failure.

Bisulfid.com is built as **scalable sovereign reference infrastructure from the beginning** — not a small website that later becomes larger.

---

## Current baseline (post 6F)

| Metric | Value |
| --- | ---: |
| Registered routes (`routes.json`) | **141** |
| Draft-backed routes | **83** |
| COHORT_01 foundation (EN) | **15** registered, non-public |
| Published routes | **0** |
| Indexable routes | **0** |
| `production_can_safely_proceed` | **no** |

**Gap to launch minimum:** **13,859** governed pages (inventory + drafts + validation path).

---

## Launch minimum target

| Dimension | Requirement |
| --- | ---: |
| **Total governed pages** | **≥ 14,000** |
| **Languages** | **7** (en, ar, de, fr, es, ja, zh) |
| **Pages per language** | **2,000** |
| **Page families (page types)** | **19** |
| **Reference layers** | **9** |
| **Audience layers** | **9** |

Every launch page must carry:

- `source_posture` and `claim_posture`
- `knowledge_reliability_profile` (evidence grade, reliability level)
- `route_state` and `indexation_state`
- `internal_link_role`
- Registry-bound generation — **no free-form LLM**

---

## Core launch dimensions

Aligned with 6A `corpus_route_formula.json` and 6B inventory model:

1. **language** — ISO 639-1 layer (en institutional base)
2. **term/entity** — ontology-bound term, compound, concept, comparison_pair, governance_object, hub_scope
3. **page_type** — 19 registered page families
4. **audience_layer** — 9 audience layers with forbidden claim classes
5. **reference_layer** — 9 reference layers (anti-duplication enforced)
6. **source_posture** — source_not_required through source_required_unresolved
7. **claim_posture** — claim_not_required through claim_required_unresolved
8. **knowledge_reliability_level** — L2 minimum for drafts; L3+ for indexation candidates
9. **evidence_grade** — from `SOVEREIGN_EVIDENCE_GRADE_REGISTRY_WAVE_1.json`
10. **route_state** — inventory_planned → draft_backed → publication gates
11. **indexation_state** — noindex_default until explicit launch gate
12. **internal_link_role** — hub/spoke/cluster binding; orphan forbidden

---

## Launch composition (summary)

**Derivation:** dimensional intersection — not volume inflation.

Per language: **2,000** eligible routes (see `INITIAL_14000_PAGE_LAUNCH_COMPOSITION_MODEL.json`).

| Bucket (per language) | Target pages |
| --- | ---: |
| Canonical terminology and compound reference | 400 |
| Difference / comparison intent | 200 |
| Multilingual equivalence and hubs | 150 |
| Audience layer explainers | 350 |
| Source-bound and claim boundary | 200 |
| Glossary and cluster pages | 200 |
| Governance / methodology / status | 100 |
| Government / investor / company context | 200 |
| Child-safe and AI-readable | 200 |
| **Sum per language** | **2,000** |
| **× 7 languages** | **14,000** |

Illustrative bucket source: `corpus_route_formula.json` `scale_derivation.illustrative_decomposition_per_language`.

---

## Cohort execution sequence

See `INITIAL_14000_PAGE_LAUNCH_COHORT_SEQUENCE.md`.

**Phase 0 (complete):** COHORT_01 foundation/governance (15 EN routes registered).

**Phase 1–8 (planned):** Core terminology → comparison → multilingual → audience → reference layer → compound/entity → source/claim status → language expansion waves.

---

## Quality and governance gates

| Document | Scope |
| --- | --- |
| `INITIAL_14000_PAGE_LAUNCH_QUALITY_THRESHOLDS.md` | Minimum quality per page family |
| `INITIAL_14000_PAGE_LAUNCH_INTERNAL_LINK_REQUIREMENTS.md` | Link density and orphan rules |
| `INITIAL_14000_PAGE_LAUNCH_INDEXATION_STRATEGY.md` | Controlled indexation and permanent noindex classes |

All pages pass validation gates **G0–G7** (6C model) before route merge. Human sample audit **≥10%** per cohort wave.

---

## Automation throughput

| Phase | Minimum | Target |
| --- | ---: | ---: |
| Generator stable | **100** governed draft pages/day | — |
| Validator mature | — | **500** governed draft pages/day |
| Cohort wave size | 500–1,000 rows | 2,000 rows |

Source: `SOVEREIGN_BATCH_GENERATION_AUTOMATION_DESIGN_WAVE_1.md`. Engine: Content Automation Engine v1 lineage (`scripts/generate_sovereign_foundation_cohort_v1.py` pattern).

---

## Pre-source vs blocked generation

| Can generate (non-public draft) | Must remain blocked |
| --- | --- |
| Governance / foundation (claim_not_required) | Factual chemistry without verified source |
| Terminology scaffolds with `[SOURCE REQUIRED]` | Pages asserting market/CAGR/pricing |
| Comparison frames without conclusion | Safety/medical/handling instruction |
| Multilingual equivalence maps (unverified) | claim_approved without registry row |
| Source/claim **status** pages (posture only) | indexable_approved before launch gate |
| Audience explainers (L2_draft_cautious) | source_locked content without lock charter |

---

## Long-term scale

See `SOVEREIGN_CORPUS_SCALE_TO_100K_PLUS_MODEL.md`.

Architecture supports **100,000+** and **300,000+** pages via:

- Partitioned master inventory (not monolithic routes.json edits)
- Language-partitioned sitemaps
- Hub-spoke link graph discipline
- Reference-layer anti-duplication
- Cohort-wave validation at scale

---

## Sprint 6G boundaries

| Action | This sprint |
| --- | --- |
| Execution charter | **Yes** |
| Composition model | **Yes** |
| Cohort sequence | **Yes** |
| Generate 14,000 pages | **No** |
| Publish routes | **No** |
| Modify routes.json | **No** |
| Public HTML | **No** |
| Sitemap / navigation activation | **No** |
| Approve claims / register sources | **No** |

---

## Next sprint (6H)

**Route inventory generation for the first large launch cohort** — executable inventory rows for COHORT_02 (core English terminology spine), not further strategic discussion.

Deliverable target: master inventory emission or wave manifest for **500–1,000** EN terminology routes with registry validation — still non-public.

---

## Doctrine references

- `corpus_route_formula.json` (6A)
- `SOVEREIGN_14000_ROUTE_MASTER_INVENTORY_MODEL.md` (6B)
- `SOVEREIGN_ROUTE_GENERATION_MATRIX_WAVE_1.json` (6B)
- `SOVEREIGN_CORPUS_GENERATOR_SCHEMA_WAVE_1.json` (6C)
- `SOVEREIGN_KNOWLEDGE_RELIABILITY_MODEL_WAVE_1.md` (6C)
- Content Automation Engine v1 + COHORT_01 (6D–6F)

---

*Sprint 6G — Initial 14,000-Page Launch Corpus Charter*
