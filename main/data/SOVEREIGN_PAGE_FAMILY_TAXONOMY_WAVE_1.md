# Sovereign Page Family Taxonomy — Wave 1

**Sprint:** 6A  
**Registry:** `main/data/page_type_registry.json`  
**Count:** 19 page families

---

## Taxonomy principle

Every governed page belongs to exactly one **page family** (`page_type_id`). Page families define purpose, audience eligibility, source/claim requirements, SEO role, and generation eligibility. Invalid page types are rejected by inventory and generator validators.

---

## Core page families

| # | page_type_id | Name | SEO / reference role |
| --- | --- | --- | --- |
| 1 | PT_FOUNDATION | Public sovereign foundation pages | Brand and trust anchor |
| 2 | PT_TERM_CANONICAL | Canonical terminology reference | Primary term reference |
| 3 | PT_COMPOUND_ENTITY | Compound/entity pages | Entity reference |
| 4 | PT_MULTILINGUAL_EQUIV | Multilingual equivalence | hreflang discovery |
| 5 | PT_SOURCE_BOUND | Source-bound reference | Provenance |
| 6 | PT_CLAIM_BOUNDARY | Claim-boundary pages | Governance transparency |
| 7 | PT_AUDIENCE_EXPLAINER | Audience-layer explainers | Intent-matched reference |
| 8 | PT_CHILD_SAFE_EDU | Child-safe educational | Educational discovery |
| 9 | PT_AI_READABLE | AI-readable reference | Machine-readable authority |
| 10 | PT_GOVERNMENT_POLICY | Government/policy reference | Institutional reference |
| 11 | PT_INVESTOR_ECONOMIC | Investor/economic context | Analyst/investor intent |
| 12 | PT_COMPANY_INDUSTRY | Company/industry context | Industry reference |
| 13 | PT_GLOSSARY_CLUSTER | Glossary cluster pages | Cluster discovery |
| 14 | **PT_DIFFERENCE_COMPARISON** | **Difference/comparison intent** | **Primary high-intent SEO** |
| 15 | PT_METHODOLOGY_GOVERNANCE | Methodology/governance | Trust and methodology |
| 16 | PT_SOURCE_STATUS | Source status pages | Provenance status |
| 17 | PT_CLAIM_STATUS | Claim status pages | Claim transparency |
| 18 | PT_CORPUS_STATUS | Corpus status pages | Corpus transparency |
| 19 | PT_MULTILINGUAL_HUB | Multilingual hub pages | Multilingual anchor |

---

## Difference/comparison intent — core SEO class

`PT_DIFFERENCE_COMPARISON` is **not** a secondary article type. It is a **core reference and SEO class** for high-intent queries from chemists, researchers, students, analysts, and AI systems.

### Required fields

- `comparison_pair_id`
- `side_a_entity_id`, `side_b_entity_id`
- `language`
- `source_ids`, `claim_ids` (per side where distinction stated)

### Canonical comparison examples

| Comparison | Audience value |
| --- | --- |
| bisulfid vs bisulfide | EN/DE spelling and terminology boundary |
| bisulfid vs sulfide | Family terminology distinction |
| bisulfid vs bisulfite | Critical disambiguation (distinct compounds) |
| Molybdän(IV)-sulfid vs molybdenum disulfide | DE/EN equivalence |
| German terminology vs English terminology | Multilingual document language |
| dictionary-entry meaning vs industrial usage | Authority scope boundary |
| terminology boundary vs safety claim | Claim class separation |
| source-supported claim vs unsupported claim | Provenance literacy |

### Internal-link role

`comparison_cluster` — pages link within comparison hubs and to term spine, source cluster, and audience clusters.

---

## Per-language distribution (illustrative, 2,000 pages/language)

| Bucket | Est. pages/lang |
| --- | ---: |
| Canonical terminology + compound reference | 400 |
| **Difference/comparison intent** | **200** |
| Multilingual equivalence + hubs | 150 |
| Audience-layer explainers | 350 |
| Source-bound + claim-boundary | 200 |
| Glossary clusters | 200 |
| Governance/methodology/status | 100 |
| Government/investor/company context | 200 |
| Child-safe + AI-readable | 200 |
| **Total** | **2,000** |

---

## Quality gate: anti-thin rules per family

| Family | Minimum substance |
| --- | --- |
| PT_TERM_CANONICAL | Term identity, source-bound lines, boundaries |
| PT_DIFFERENCE_COMPARISON | Both sides addressed, distinction sourced |
| PT_GLOSSARY_CLUSTER | ≥3 sourced terms or reject |
| PT_AUDIENCE_EXPLAINER | Audience-appropriate depth, not boilerplate clone |
| Hub types | Valid alternate route map, not empty stub |

---

## Registry reference

Full machine-readable definitions: `main/data/page_type_registry.json`

Production rules: `main/data/corpus_production_rules.md`
