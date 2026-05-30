# Sovereign Foundation COHORT_01 — Route-to-Draft Mapping

**Sprint:** 6F  
**Date:** 2026-05-30  
**Registry:** `main/data/routes.json` (141 routes)

---

## Complete mapping (15 routes)

| route_id | content_file | draft exists | hreflang_group | required_internal_links |
| --- | --- | :---: | --- | ---: |
| `en_foundation_sovereign_intro` | `main/content/en/pages/foundation/sovereign-reference-introduction.md` | ✓ | `foundation_sovereign_reference_introduction` | 8 |
| `en_foundation_institutional_purpose` | `main/content/en/pages/foundation/institutional-purpose.md` | ✓ | `foundation_institutional_purpose` | 2 |
| `en_foundation_methodology` | `main/content/en/pages/foundation/methodology.md` | ✓ | `foundation_methodology` | 3 |
| `en_foundation_source_policy` | `main/content/en/pages/foundation/source-policy-overview.md` | ✓ | `foundation_source_policy_overview` | 2 |
| `en_foundation_claim_policy` | `main/content/en/pages/foundation/claim-policy-overview.md` | ✓ | `foundation_claim_policy_overview` | 2 |
| `en_foundation_knowledge_reliability` | `main/content/en/pages/foundation/knowledge-reliability-model.md` | ✓ | `foundation_knowledge_reliability_model` | 3 |
| `en_foundation_multilingual_overview` | `main/content/en/pages/foundation/multilingual-corpus-overview.md` | ✓ | `foundation_multilingual_corpus_overview` | 2 |
| `en_foundation_reference_layers` | `main/content/en/pages/foundation/reference-layer-overview.md` | ✓ | `foundation_reference_layer_overview` | 3 |
| `en_foundation_audience_layers` | `main/content/en/pages/foundation/audience-layer-overview.md` | ✓ | `foundation_audience_layer_overview` | 3 |
| `en_foundation_chemical_language_governance` | `main/content/en/pages/foundation/chemical-language-governance-framework.md` | ✓ | `foundation_chemical_language_governance_framework` | 2 |
| `en_foundation_ai_readable_policy` | `main/content/en/pages/foundation/ai-readable-reference-policy.md` | ✓ | `foundation_ai_readable_reference_policy` | 2 |
| `en_foundation_child_safe_policy` | `main/content/en/pages/foundation/child-safe-educational-policy.md` | ✓ | `foundation_child_safe_educational_policy` | 2 |
| `en_foundation_economic_institutional_restrictions` | `main/content/en/pages/foundation/economic-institutional-claim-restrictions.md` | ✓ | `foundation_economic_institutional_claim_restrictions` | 2 |
| `en_foundation_corpus_status` | `main/content/en/pages/foundation/corpus-status.md` | ✓ | `foundation_corpus_status` | 3 |
| `en_foundation_launch_status` | `main/content/en/pages/foundation/launch-status-non-public-corpus.md` | ✓ | `foundation_launch_status_non_public_corpus` | 2 |

---

## Front matter alignment

Each draft front matter `route_id` matches its registry record. Validators confirm:

- `status: draft` in content ↔ `status: planned` in registry (draft-backed discipline)
- `indexable: false` in both
- `in_sitemap: false` in both (registry); draft front matter includes `in_sitemap: false`
- `language` / `locale` / `source_language`: **en**

No draft file modifications were required in Sprint 6F.

---

## Required internal links detail

### Root hub — `en_foundation_sovereign_intro`

→ institutional_purpose, methodology, knowledge_reliability, multilingual_overview, reference_layers, audience_layers, corpus_status, launch_status

### Governance spine — `en_foundation_methodology`

→ source_policy, claim_policy, knowledge_reliability

### Source ↔ claim pair

- `en_foundation_source_policy` → methodology, claim_policy
- `en_foundation_claim_policy` → methodology, source_policy

### Status pair

- `en_foundation_corpus_status` → sovereign_intro, launch_status, methodology
- `en_foundation_launch_status` → corpus_status, sovereign_intro

Full graph: `SOVEREIGN_FOUNDATION_COHORT_01_INTERNAL_LINK_GRAPH.md`

---

## Binding verification

| Check | Result |
| --- | --- |
| Unique route_id | ✓ |
| Unique path | ✓ |
| Unique content_file | ✓ |
| All content files exist | ✓ (15/15) |
| All link targets registered | ✓ |
| No duplicate with existing 126 routes | ✓ |
