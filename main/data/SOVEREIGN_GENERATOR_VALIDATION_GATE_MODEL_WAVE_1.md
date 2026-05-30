# Sovereign Generator Validation Gate Model — Wave 1

**Sprint:** 6C  
**Purpose:** Define validation gates for generator inputs, template contracts, and generated draft outputs.

---

## Gate architecture

```
G0 Inventory → G1 Template → G2 Reliability → G3 Registry → G4 Draft → G5 Graph → G6 Publication lock
```

All gates must **PASS** before draft merge. Any severity-1 failure **blocks** cohort merge.

---

## G0 — Route inventory validation

| Check | Rule |
| --- | --- |
| Schema compliance | Row matches `SOVEREIGN_ROUTE_INVENTORY_SCHEMA_WAVE_1.json` |
| Matrix compatibility | Row allowed in `SOVEREIGN_ROUTE_GENERATION_MATRIX_WAVE_1.json` |
| Duplicate rejection | Anti-duplication hash unique |
| production_route_registry | false unless merge charter |
| indexable / in_sitemap | false in 6D |

---

## G1 — Template contract validation

| Check | Rule |
| --- | --- |
| template_id exists | In `SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json` |
| page_type match | template applicable to page_type_id |
| audience allowed | audience_id in allowed_audiences |
| reference_layer allowed | reference_layer_id in allowed_reference_layers |
| language allowed | language in allowed_languages |
| required sections defined | allowed_sections non-empty |

---

## G2 — Knowledge reliability validation

| Check | Rule |
| --- | --- |
| Profile present | knowledge_reliability_profile complete |
| evidence_grade valid | In evidence grade registry |
| Grade not upgraded | Matches source_posture + claim_posture |
| Hierarchy preserved | Sources cited with rank — not flattened |
| excluded_claim_classes visible | Not hidden in output |
| page_assertion_limit | Not exceeded |
| human_review flag | Honored when triggered |

See `SOVEREIGN_KNOWLEDGE_RELIABILITY_VALIDATION_REQUIREMENTS_WAVE_1.md` for full checklist.

---

## G3 — Source / claim boundary validation

| Check | Rule |
| --- | --- |
| source_ids exist | In source_registry.json |
| claim_ids exist | In claim registries |
| verified for factual lines | source_verified minimum where asserted |
| claim approved | claim_approved_narrow minimum where asserted |
| forbidden claim scan | L1 corpus claims patterns |
| no new sources/claims | Generator read-only on registries |

---

## G4 — Generated draft validation

| Check | Rule |
| --- | --- |
| Frontmatter complete | Generator schema draft_frontmatter_required |
| status draft | Always |
| publication_status non_public | Always |
| indexable false | Always |
| [SOURCE REQUIRED] preserved | Unresolved factual lines |
| Thin page detection | quality_threshold from template |
| Fake page detection | required_data_fields satisfied |
| Forbidden claim detection | BANNED_FRAMES + excluded classes |
| Reliability notice present | required_reliability_notice templates |
| Draft not presented as final | Wording check |

Existing: `validate_corpus_drafts_l1.py`, `validate_content_drafts_l0.py`

---

## G5 — Internal-link validation

| Check | Rule |
| --- | --- |
| route_id targets exist | Inventory or routes.json |
| No broken edges | L2 internal link graph plan |
| Hub spoke minimum | Hub templates quality_threshold |
| comparison links | Both sides linked |

---

## G6 — Multilingual / hreflang validation

| Check | Rule |
| --- | --- |
| hreflang_group consistency | Alternate routes valid |
| Arabic RTL metadata | rtl flag in frontmatter |
| EN institutional base | x-default policy |
| No MT spam detection | Equivalence sourced per language |

Existing: `validate_multilingual_wave_plan_l2.py`, `validate_seo_indexation_plan_l2.py`

---

## G7 — Indexation validation (future public)

| Check | Rule |
| --- | --- |
| noindex default | All 6D drafts |
| indexation_blocked | source_pending or claim_pending |
| indexable true forbidden | Until launch charter |
| sitemap / navigation false | Until launch charter |

Existing: `validate_corpus_publication_lock_l1.py`

---

## G8 — Generated HTML validation (future only — post-6D)

| Check | Rule |
| --- | --- |
| Build pass | Static site generator |
| No accidental indexation | robots meta |
| CSP/security posture | No regression |
| Broken link scan | Full graph |

**Not executed in Sprint 6C** — design only.

---

## Gate summary table

| Gate | Sprint 6D | Existing validator |
| --- | --- | --- |
| G0 Inventory | Required | Future inventory validator |
| G1 Template | Required | Future template validator |
| G2 Reliability | Required | Future KR validator |
| G3 Source/claim | Required | guardrail runtime L1 |
| G4 Draft | Required | corpus drafts L1 |
| G5 Links | Required | internal link L2 |
| G6 hreflang/SEO | Required | SEO L2 |
| G7 Publication | Required | publication lock L1 |
| G8 HTML | Future | TBD |

---

## Failure policy

- Severity-1: block merge  
- Severity-2: warn + sample human review  
- No bypass without DECISION_LOG charter  
