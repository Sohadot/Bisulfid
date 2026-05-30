# Sovereign Foundation COHORT_01 — Route Mapping Readiness

**Sprint:** 6E  
**Cohort:** `COHORT_01_FOUNDATION_GOV`  
**Date:** 2026-05-30  
**Posture:** Future route mapping documentation — **routes.json not modified**

---

## Purpose

Document how COHORT_01 pre-route drafts would map into the production route registry when a separate merge charter authorizes registration. This sprint defines readiness only; no routes are published.

---

## Current registry posture

| Field | Value |
| --- | --- |
| Registered routes in routes.json | **126** |
| COHORT_01 routes registered | **0** |
| COHORT_01 draft files | **15** |
| production_can_safely_proceed | **no** |
| Route publication lock | **LOCKED** |

---

## Future route registration matrix

Each row is the **planned** route record shape when merge is authorized. Fields reflect 6D blueprints and 6E validation. **Not written to routes.json in Sprint 6E.**

| route_id | path | page_type_id | reference_layer_id | route_state | indexation |
| --- | --- | --- | --- | --- | --- |
| `en_foundation_sovereign_intro` | `/en/foundation/sovereign-reference-introduction/` | PT_FOUNDATION | REF_KNOWLEDGE | draft_backed | noindex_default |
| `en_foundation_institutional_purpose` | `/en/foundation/institutional-purpose/` | PT_FOUNDATION | REF_INSTITUTIONAL | draft_backed | noindex_default |
| `en_foundation_methodology` | `/en/foundation/methodology/` | PT_METHODOLOGY_GOVERNANCE | REF_ACADEMIC | draft_backed | noindex_governance |
| `en_foundation_source_policy` | `/en/foundation/source-policy-overview/` | PT_METHODOLOGY_GOVERNANCE | REF_INSTITUTIONAL | draft_backed | noindex_governance |
| `en_foundation_claim_policy` | `/en/foundation/claim-policy-overview/` | PT_METHODOLOGY_GOVERNANCE | REF_INSTITUTIONAL | draft_backed | noindex_governance |
| `en_foundation_knowledge_reliability` | `/en/foundation/knowledge-reliability-model/` | PT_METHODOLOGY_GOVERNANCE | REF_RESEARCH | draft_backed | noindex_governance |
| `en_foundation_multilingual_overview` | `/en/foundation/multilingual-corpus-overview/` | PT_FOUNDATION | REF_LINGUISTIC | draft_backed | noindex_default |
| `en_foundation_reference_layers` | `/en/foundation/reference-layer-overview/` | PT_FOUNDATION | REF_KNOWLEDGE | draft_backed | noindex_default |
| `en_foundation_audience_layers` | `/en/foundation/audience-layer-overview/` | PT_FOUNDATION | REF_KNOWLEDGE | draft_backed | noindex_default |
| `en_foundation_chemical_language_governance` | `/en/foundation/chemical-language-governance-framework/` | PT_METHODOLOGY_GOVERNANCE | REF_ACADEMIC | draft_backed | noindex_governance |
| `en_foundation_ai_readable_policy` | `/en/foundation/ai-readable-reference-policy/` | PT_METHODOLOGY_GOVERNANCE | REF_TECHNICAL | draft_backed | noindex_governance |
| `en_foundation_child_safe_policy` | `/en/foundation/child-safe-educational-policy/` | PT_METHODOLOGY_GOVERNANCE | REF_EDUCATIONAL | draft_backed | noindex_governance |
| `en_foundation_economic_institutional_restrictions` | `/en/foundation/economic-institutional-claim-restrictions/` | PT_METHODOLOGY_GOVERNANCE | REF_ECONOMIC | draft_backed | noindex_governance |
| `en_foundation_corpus_status` | `/en/foundation/corpus-status/` | PT_CORPUS_STATUS | REF_INSTITUTIONAL | draft_backed | noindex_governance |
| `en_foundation_launch_status` | `/en/foundation/launch-status-non-public-corpus/` | PT_CORPUS_STATUS | REF_INSTITUTIONAL | draft_backed | noindex_governance |

---

## Content file binding (ready)

| route_id | content_file | Draft exists |
| --- | --- | :---: |
| All 15 COHORT_01 units | `main/content/en/pages/foundation/{slug}.md` | ✓ |

Content paths match `SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_DRAFT_BLUEPRINTS.json` exactly.

---

## Merge prerequisites (future charter)

Before any COHORT_01 route enters routes.json:

1. Separate **route registration merge charter** approved by human review.
2. All L1/L2 runtimes **PASS** at merge time.
3. `production_can_safely_proceed` gate evaluated — expected **no** until broader corpus gates clear.
4. Internal link graph validated against registered targets (`SOVEREIGN_FOUNDATION_COHORT_01_INTERNAL_LINK_GRAPH.md`).
5. No indexation, sitemap, or navigation activation in the same sprint as registration unless explicitly chartered.
6. Source and claim registries remain unchanged unless separate sprint authorizes.

---

## Future navigation eligibility (not activated)

| Navigation slot | Candidate route_id | Priority |
| --- | --- | --- |
| Foundation root | `en_foundation_sovereign_intro` | 1 |
| About / purpose | `en_foundation_institutional_purpose` | 2 |
| Governance section | `en_foundation_methodology` | 3 |
| Source policy | `en_foundation_source_policy` | 4 |
| Claim policy | `en_foundation_claim_policy` | 5 |
| Status footer | `en_foundation_corpus_status`, `en_foundation_launch_status` | 6 |

**Sprint 6E:** `in_navigation: false` on all units. Navigation JSON not modified.

---

## Future sitemap eligibility (not activated)

| Sitemap partition (future) | Routes | Eligible when |
| --- | --- | --- |
| `sitemap-foundation-en.xml` | All 15 COHORT_01 | Indexation charter + noindex lifted |
| Governance subset | methodology, source, claim, reliability, policies | Separate governance indexation review |
| Status subset | corpus_status, launch_status | Launch authorization only |

**Sprint 6E:** `in_sitemap: false` on all units. No sitemap files created.

---

## Indexation posture (default locked)

| Indexation class | Count | Default |
| --- | ---: | --- |
| `noindex_default` | 5 | Locked |
| `noindex_governance` | 10 | Locked |
| `indexable_approved` | 0 | — |

No COHORT_01 page is indexation-eligible without a future charter.

---

## Validation gates at merge time (planned)

From 6D manifest — each unit requires: **G0, G1, G2, G4, G7**.

Additional 6E gates for merge:

- **G-LINK-01:** All required internal-link edges resolvable to registered route_id.
- **G-LINK-02:** Zero orphans in COHORT_01 subgraph.
- **G-ROUTE-01:** content_file exists and matches route record.
- **G-PUB-01:** indexable, in_sitemap, in_navigation remain false unless charter overrides.

---

## Route formula alignment

COHORT_01 paths follow corpus route formula dimensions:

```text
/{language}/foundation/{slug}/
```

- **language:** `en`
- **page_family:** `foundation`
- **slug:** kebab-case from theme
- **audience_id:** ALL (foundation layer)
- **reference_layer_id:** per-unit (9 layers represented)

Formula registry not modified in Sprint 6E.

---

## Summary

COHORT_01 is **route-mapping ready** at the documentation and content-file level. Registration is **blocked** until merge charter. **routes.json unchanged (126).**
