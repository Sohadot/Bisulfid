# Sovereign Content Automation Engine v1 — Report

**Sprint:** 6D  
**Engine:** `scripts/generate_sovereign_foundation_cohort_v1.py`  
**Cohort:** `COHORT_01_FOUNDATION_GOV`  
**Date:** 2026-05-30  
**Posture:** Non-public draft generation only — no publication

---

## Purpose

Content Automation Engine v1 is the first **controlled, registry-constrained** generator for bisulfid.com. It reads governed 6A–6C inputs and produces **deterministic** COHORT_01 foundation drafts or dry-run manifests. It does **not** use LLM generation, does **not** modify `routes.json`, and does **not** activate indexation, sitemap, or navigation.

---

## Governed inputs (read-only)

| Registry | Role |
| --- | --- |
| `corpus_route_formula.json` | Route dimension model |
| `page_type_registry.json` | Page type validation |
| `audience_layer_registry.json` | Audience posture |
| `reference_layer_registry.json` | Reference layer validation |
| `corpus_production_rules.md` | Production doctrine |
| `SOVEREIGN_CORPUS_GENERATOR_SCHEMA_WAVE_1.json` | Generator constraints |
| `SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json` | Template binding (`TPL_FOUNDATION_GOV_V1`) |
| `SOVEREIGN_EVIDENCE_GRADE_REGISTRY_WAVE_1.json` | Evidence grades |
| `SOVEREIGN_SOURCE_HIERARCHY_MODEL_WAVE_1.json` | Source hierarchy |
| `sources/source_registry.json` | Source lock posture |
| `claims/terminology_claims.json` | Claim lock posture |
| `routes.json` | Registered route count (unchanged) |

---

## COHORT_01 scope (15 units)

Public Sovereign Foundation and Knowledge Reliability Layer — English pre-route drafts:

1. Sovereign reference introduction  
2. Institutional purpose  
3. Methodology  
4. Source policy overview  
5. Claim policy overview  
6. Knowledge reliability model  
7. Multilingual corpus overview  
8. Reference layer overview  
9. Audience layer overview  
10. Chemical-language governance framework  
11. AI-readable reference policy  
12. Child-safe educational policy  
13. Economic/institutional claim restrictions  
14. Corpus status  
15. Launch status / non-public corpus explanation  

---

## How the engine prevents fake, thin, and free-form pages

| Risk | Prevention |
| --- | --- |
| **Free-form LLM pages** | No LLM calls; content from fixed unit definitions and template renderer only |
| **Fake pages** | Each unit requires validated `page_type_id`, `reference_layer_id`, and template applicability; missing registry fields → hard reject |
| **Thin pages** | Every draft includes role, bullets, reliability profile, source/claim status, publication blockers, and internal reference role |
| **Unsupported claims** | `excluded_claim_classes` enforced; narrative scan rejects unsourced safety/medical/market/CAGR phrases |
| **Public activation** | Engine rejects `indexable`, `in_sitemap`, or `in_navigation` true; all outputs `noindex_default: true` |
| **Route publication** | `production_route_registry: false`; `routes.json` never written |
| **Source/claim invention** | Registries read-only; `source_not_required` / `claim_not_required` for governance framing |
| **Evidence upgrade** | `evidence_grade: claim_not_required` (or `economic_context_pending` for REF_ECONOMIC); `L2_draft_cautious` minimum |

---

## Per-unit assignments

Each COHORT_01 unit receives:

- `route_id`, `language`, `page_type_id`, `audience_id` (ALL)
- `reference_layer_id`, `template_id`, `evidence_grade`
- `knowledge_reliability_profile` (full 6C model)
- `source_posture`, `claim_posture`, `indexation_state`
- `internal_link_role`, `noindex_default`, `excluded_claim_classes`
- `unresolved_field_behavior`, `validation_gates` (G0, G1, G2, G4, G7)
- `content_file` path under `main/content/en/pages/foundation/`

---

## Outputs

| Artifact | Description |
| --- | --- |
| `SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_DRY_RUN_MANIFEST.json` | Full unit metadata and engine run record |
| `SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_DRAFT_BLUEPRINTS.json` | Route blueprints (pre-route) |
| `main/content/en/pages/foundation/*.md` | 15 non-public draft markdown files |
| `SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_VALIDATION_REPORT.md` | Post-run validator results |
| `SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_NO_PUBLICATION_GUARDRAIL.md` | Publication lock documentation |

---

## Execution

```text
py scripts/generate_sovereign_foundation_cohort_v1.py           # manifest + blueprints only
py scripts/generate_sovereign_foundation_cohort_v1.py --write-drafts   # + draft markdown files
```

---

## Schema safety decision

L1 validators validate **registered routes** in `routes.json` and existing content bindings. Pre-route foundation drafts under `main/content/en/pages/foundation/` with explicit `status: draft`, `publication_status: non_public`, and no route registry merge are **schema-safe** for v1. All L1/L2 runtimes **PASS** after generation.

---

## Governance unchanged

| Gate | Status |
| --- | --- |
| `production_can_safely_proceed` | **no** |
| `routes.json` | **126 rows — unchanged** |
| Corpus locks | **LOCKED** |
| Source registry | **inactive** |
| Claim registry | **inactive** (1 narrow approved claim) |
| Public HTML | **none** |
| Sitemap / navigation | **not activated** |
