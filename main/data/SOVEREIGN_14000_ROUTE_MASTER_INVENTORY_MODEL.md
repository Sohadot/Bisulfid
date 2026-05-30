# Sovereign 14,000-Route Master Inventory Model

**Sprint:** 6B  
**Date:** 2026-05-30  
**Branch:** `claude/sprint-6b-14000-route-master-inventory-model`  
**Scope:** Master route inventory model — no production routes, no content, no HTML

---

## Purpose

Transform Sprint **6A** architecture into an **executable route inventory model** for 14,000+ governed multilingual reference pages. This sprint produces **model and schema only** — not route publication, not page generation, not HTML.

Bisulfid.com is **not** producing many pages by repetition. It produces a **governed reference matrix** where each page exists because a specific **field, audience, language, reference layer, and evidence posture** requires a distinct reference surface.

---

## Scope amendment: reference_layer dimension

6B extends the 6A formula with **`reference_layer`** as a ninth core dimension:

```
term/entity × language × audience × reference_layer × page_type × source posture × claim posture × route state × indexation state × internal-link role
```

**Registry:** `main/data/reference_layer_registry.json` (9 reference layers)

| reference_layer_id | Purpose |
| --- | --- |
| REF_ACADEMIC | Citation-aware academic reference |
| REF_KNOWLEDGE | General knowledge with controlled simplification |
| REF_RESEARCH | Deep inquiry with source/claim mapping |
| REF_EDUCATIONAL | Student and child-safe educational reference |
| REF_ECONOMIC | Source-bound economic context only |
| REF_INSTITUTIONAL | Governance, policy, compliance framing |
| REF_TECHNICAL | Machine-readable / AI-safe structured reference |
| REF_LINGUISTIC | Multilingual equivalence and false-friend prevention |
| REF_LOGISTICAL | Documentation language only — not operational instruction |

---

## Strategic scale

| Metric | Value |
| --- | ---: |
| Minimum routes | **14,000** |
| Languages | **7** |
| Routes per language | **2,000** |
| Derivation | Dimensional intersection + reference layer — not volume inflation |

---

## Current production baseline (unchanged)

| Metric | Value |
| --- | ---: |
| `routes.json` rows | **126** |
| Draft-backed | **68** |
| Published | **0** |
| `production_can_safely_proceed` | **no** |

**6B does not modify `routes.json`.** Master inventory is a separate model layer (`corpus_master_inventory.json` — future file, not created as rows in 6B).

---

## Machine-readable artifacts (6B)

| File | Role |
| --- | --- |
| `SOVEREIGN_ROUTE_INVENTORY_SCHEMA_WAVE_1.json` | Row schema, states, anti-fake rules |
| `SOVEREIGN_ROUTE_GENERATION_MATRIX_WAVE_1.json` | Language × page_type × audience × reference_layer matrix |
| `reference_layer_registry.json` | Nine reference layers with eligibility rules |

---

## Route state model

| route_state | Meaning |
| --- | --- |
| `inventory_planned` | Row in master inventory; not in routes.json |
| `draft_eligible` | Gates allow draft generation (6D) |
| `draft_backed` | Content file exists |
| `source_pending` | Awaiting source verification |
| `claim_pending` | Awaiting claim approval |
| `source_verified` | Source posture satisfied |
| `claim_approved` | Claim posture satisfied |
| `source_lock_candidate` | Source verified; lock not applied |
| `publication_blocked` | Explicit block — default for inventory |
| `indexation_blocked` | Cannot index until launch gate |

---

## Indexation state model

| indexation_state | Meaning |
| --- | --- |
| `noindex_default` | All new inventory rows |
| `indexation_candidate` | Gates nearly satisfied |
| `indexation_approved` | Owner launch charter only |
| `indexation_blocked` | Missing source/claim/publication gates |

---

## Internal-link roles

`language_hub`, `term_hub`, `source_hub`, `claim_hub`, `audience_hub`, `glossary_hub`, `comparison_hub`, `AI_reference_hub`, `education_hub`

---

## Anti-fake page rules

1. No route may become public without data completeness.
2. No route may become indexable without source/claim eligibility.
3. No route enters sitemap/navigation before publication gates clear.
4. No shallow duplication — reference_layer must change page purpose or structure.
5. All inventory rows: `indexable: false`, `production_route_registry: false`.

---

## Batch production cohorts

See `SOVEREIGN_ROUTE_COHORT_MODEL_WAVE_1.md` for seven cohort definitions.

---

## Sprint 6C handoff

Generator must read: inventory schema, generation matrix, reference_layer registry, page_type registry, audience registry, source/claim registries, ontology. **No free-form LLM generation.**

---

## Related documents

- `SOVEREIGN_ROUTE_COHORT_MODEL_WAVE_1.md`
- `SOVEREIGN_ROUTE_PATH_PATTERN_MODEL_WAVE_1.md`
- `SOVEREIGN_ROUTE_INVENTORY_NO_PUBLICATION_GUARDRAIL_WAVE_1.md`
- `corpus_route_formula.json` (6A — not modified)
- `corpus_production_rules.md` (6A — not modified)

---

## Hard constraints preserved

No `routes.json` modification. No content. No HTML. No publication. No fake pages. No validator weakening.
