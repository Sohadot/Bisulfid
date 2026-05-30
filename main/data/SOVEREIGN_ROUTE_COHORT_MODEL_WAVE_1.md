# Sovereign Route Cohort Model — Wave 1

**Sprint:** 6B  
**Purpose:** Define batch production cohorts for governed route inventory generation in waves — not single-page cycles.

---

## Cohort principle

Routes enter the master inventory in **cohorts** aligned to page families, reference layers, and gate readiness. Each cohort has a target size band, eligibility rules, and validator requirements. Cohorts generate **inventory rows first**; `routes.json` merge is a separate charter per cohort.

---

## Cohort definitions

### Cohort 1 — Public foundation and governance

| Field | Value |
| --- | --- |
| `cohort_id` | `COHORT_01_FOUNDATION_GOV` |
| Page families | PT_FOUNDATION, PT_METHODOLOGY_GOVERNANCE, PT_CORPUS_STATUS |
| Reference layers | REF_INSTITUTIONAL, REF_KNOWLEDGE |
| Audiences | All (governance-facing) |
| Languages | All 7 (en first) |
| Est. routes per language | ~50 |
| route_state entry | `inventory_planned` |
| source_posture | `source_not_required` (governance framing) |
| claim_posture | `claim_not_required` |
| Wave priority | **First** — establishes institutional spine |

---

### Cohort 2 — Core terminology routes

| Field | Value |
| --- | --- |
| `cohort_id` | `COHORT_02_CORE_TERMINOLOGY` |
| Page families | PT_TERM_CANONICAL, PT_GLOSSARY_CLUSTER |
| Reference layers | REF_ACADEMIC, REF_KNOWLEDGE, REF_LINGUISTIC, REF_RESEARCH |
| Audiences | AUD_CHEMIST, AUD_RESEARCHER, AUD_STUDENT, AUD_AI_SYSTEM |
| Languages | All 7 |
| Est. routes per language | ~500 combined |
| route_state entry | `inventory_planned` → `source_pending` / `claim_pending` |
| Gate | Requires ontology term + verified source + approved claim for publication path |

---

### Cohort 3 — Multilingual equivalence routes

| Field | Value |
| --- | --- |
| `cohort_id` | `COHORT_03_MULTILINGUAL_EQUIV` |
| Page families | PT_MULTILINGUAL_EQUIV, PT_MULTILINGUAL_HUB |
| Reference layers | REF_LINGUISTIC only |
| Audiences | AUD_CHEMIST, AUD_RESEARCHER, AUD_STUDENT, AUD_AI_SYSTEM |
| Languages | All 7 (hreflang groups required) |
| Est. routes per language | ~150 |
| Special rules | Arabic RTL layer; English institutional base for x-default |
| Gate | Per-language source verified; no assumed cross-language identity |

---

### Cohort 4 — Audience-layer routes

| Field | Value |
| --- | --- |
| `cohort_id` | `COHORT_04_AUDIENCE_LAYER` |
| Page families | PT_AUDIENCE_EXPLAINER |
| Reference layers | REF_KNOWLEDGE, REF_RESEARCH, REF_EDUCATIONAL, REF_ECONOMIC, REF_LOGISTICAL |
| Audiences | All 9 audience layers (filtered by page type compatibility) |
| Languages | All 7 |
| Est. routes per language | ~350 |
| Anti-duplication | Same term + language requires different audience OR reference_layer |

---

### Cohort 5 — Comparison / difference routes (core SEO)

| Field | Value |
| --- | --- |
| `cohort_id` | `COHORT_05_COMPARISON` |
| Page families | PT_DIFFERENCE_COMPARISON |
| Reference layers | REF_LINGUISTIC, REF_RESEARCH, REF_EDUCATIONAL, REF_TECHNICAL, REF_ECONOMIC, REF_INSTITUTIONAL |
| comparison_modes | linguistic, technical, educational, research, economic_relevance, institutional_terminology |
| Audiences | AUD_CHEMIST, AUD_RESEARCHER, AUD_STUDENT, AUD_ANALYST, AUD_AI_SYSTEM, AUD_INVESTOR |
| Languages | All 7 |
| Est. routes per language | ~200 |
| Gate | Both comparison sides registered; sources per side; no unsupported distinction claims |

**Examples:** bisulfid vs bisulfide; bisulfid vs bisulfite; Molybdän(IV)-sulfid vs molybdenum disulfide; dictionary-entry vs industrial usage.

---

### Cohort 6 — Source and claim status routes

| Field | Value |
| --- | --- |
| `cohort_id` | `COHORT_06_SOURCE_CLAIM_STATUS` |
| Page families | PT_SOURCE_BOUND, PT_CLAIM_BOUNDARY, PT_SOURCE_STATUS, PT_CLAIM_STATUS |
| Reference layers | REF_INSTITUTIONAL, REF_RESEARCH, REF_ACADEMIC, REF_TECHNICAL |
| Audiences | AUD_RESEARCHER, AUD_GOVERNMENT, AUD_AI_SYSTEM |
| Languages | All 7 |
| Est. routes per language | ~200 |
| Gate | Registry alignment read-only; no fabricated status |

---

### Cohort 7 — Entity and compound routes

| Field | Value |
| --- | --- |
| `cohort_id` | `COHORT_07_ENTITY_COMPOUND` |
| Page families | PT_COMPOUND_ENTITY, PT_CHILD_SAFE_EDU, PT_AI_READABLE, PT_GOVERNMENT_POLICY, PT_INVESTOR_ECONOMIC, PT_COMPANY_INDUSTRY |
| Reference layers | Per page family from reference_layer_registry |
| Audiences | Per page type allowed_audiences |
| Languages | All 7 |
| Est. routes per language | ~550 combined |
| Gate | Compound identity sourced; economic routes require verified market sources |

---

## Cohort execution order

```
COHORT_01 → COHORT_02 → COHORT_05 → COHORT_03 → COHORT_04 → COHORT_06 → COHORT_07
```

Comparison cohort (5) early because core SEO class. Foundation (1) first for institutional spine.

---

## Batch size targets (6D+ execution)

| Phase | Inventory rows per wave | Draft generation |
| --- | --- | --- |
| Initial | 500–1,000 inventory rows | After 6C generator |
| Stable | 2,000+ inventory rows per wave | 100–500 drafts/day benchmark |

---

## Cohort validation (each wave)

1. Schema validation against `SOVEREIGN_ROUTE_INVENTORY_SCHEMA_WAVE_1.json`
2. Matrix compatibility check against `SOVEREIGN_ROUTE_GENERATION_MATRIX_WAVE_1.json`
3. reference_layer allowed_page_families check
4. Anti-duplication hash check
5. L1/L2 runtime pass (no regression)
6. `production_route_registry: false` on all new rows

---

## Sprint 6C generator requirements

- Input: cohort_id + inventory row schema
- Output: draft template binding only — not inventory row invention
- Must read all registries; no free-form LLM generation
- Validation: schema + matrix + guardrail runtime before merge
