# Sovereign Foundation COHORT_01 — Multilingual Expansion Readiness

**Sprint:** 6E  
**Cohort:** `COHORT_01_FOUNDATION_GOV`  
**Date:** 2026-05-30  
**Posture:** Readiness assessment only — no translated drafts, no hreflang activation

---

## Purpose

Assess COHORT_01 readiness for controlled multilingual expansion across the seven language layers defined in 6A architecture. English foundation drafts are the **source institutional layer**; other languages are **not generated** in Sprint 6E.

---

## Language layer model (from 6A)

| Code | Language | COHORT_01 status |
| --- | --- | --- |
| `en` | English (institutional base) | **15 drafts exist** |
| `ar` | Arabic | Not generated — hreflang group reserved |
| `de` | German | Not generated — hreflang group reserved |
| `fr` | French | Not generated — hreflang group reserved |
| `es` | Spanish | Not generated — hreflang group reserved |
| `ja` | Japanese | Not generated — hreflang group reserved |
| `zh` | Chinese | Not generated — hreflang group reserved |

---

## hreflang group assignments (from 6D manifest)

Each English foundation unit has a unique `hreflang_group` for future alternates:

| route_id | hreflang_group |
| --- | --- |
| `en_foundation_sovereign_intro` | `foundation_sovereign_reference_introduction` |
| `en_foundation_institutional_purpose` | `foundation_institutional_purpose` |
| `en_foundation_methodology` | `foundation_methodology` |
| `en_foundation_source_policy` | `foundation_source_policy_overview` |
| `en_foundation_claim_policy` | `foundation_claim_policy_overview` |
| `en_foundation_knowledge_reliability` | `foundation_knowledge_reliability_model` |
| `en_foundation_multilingual_overview` | `foundation_multilingual_corpus_overview` |
| `en_foundation_reference_layers` | `foundation_reference_layer_overview` |
| `en_foundation_audience_layers` | `foundation_audience_layer_overview` |
| `en_foundation_chemical_language_governance` | `foundation_chemical_language_governance_framework` |
| `en_foundation_ai_readable_policy` | `foundation_ai_readable_reference_policy` |
| `en_foundation_child_safe_policy` | `foundation_child_safe_educational_policy` |
| `en_foundation_economic_institutional_restrictions` | `foundation_economic_institutional_claim_restrictions` |
| `en_foundation_corpus_status` | `foundation_corpus_status` |
| `en_foundation_launch_status` | `foundation_launch_status_non_public_corpus` |

**x-default (future):** English institutional path per `SOVEREIGN_SEO_INTERNAL_LINKING_SECURITY_MODEL_WAVE_1.md`.

---

## Expansion readiness checklist

| Requirement | English (en) | Other languages |
| --- | :---: | :---: |
| Source draft exists | ✓ | — |
| `source_language: en` declared | ✓ | N/A |
| `hreflang_group` assigned | ✓ | Pending generation |
| `route_id` naming convention ready | ✓ | `{lang}_foundation_{theme}` |
| Path pattern documented | ✓ | `/{lang}/foundation/{slug}/` |
| Reference layer binding | ✓ | Must mirror en layer |
| Reliability profile template | ✓ | L2_draft_cautious minimum |
| Governance-only claim posture | ✓ | Must not relax in translation |
| No machine-translation spam policy | ✓ | Documented on multilingual overview page |
| Internal link graph extensible | ✓ | Per-language subgraph planned |

---

## Multilingual hub page readiness

`en_foundation_multilingual_overview` (`multilingual-corpus-overview.md`):

- Documents seven language layers.
- States English as institutional base.
- Explicitly forbids machine-translation spam.
- Links (planning graph) to reference_layers and audience_layers.
- Does **not** claim any non-English foundation draft exists.

**Readiness:** ✓ for hub role; expansion content **not generated**.

---

## Future expansion path (not executed)

1. **Wave ML-FOUNDATION-01:** Generate `de`, `fr`, `es` foundation governance mirrors via registry-constrained engine (not LLM free-form).
2. **Wave ML-FOUNDATION-02:** `ar`, `ja`, `zh` with linguistic review gate.
3. Each translated unit must:
   - Share `hreflang_group` with English source.
   - Maintain `claim_not_required` / governance posture.
   - Preserve excluded claim classes.
   - Remain `noindex_default` until indexation charter.
4. Cross-language equivalence links require verified terminology governance — **not automatic**.

---

## Prohibited expansion behaviors

- Bulk machine translation of foundation drafts without human review.
- Relaxing excluded claim classes in non-English layers.
- Publishing hreflang tags before all alternates exist and are validated.
- Creating fake non-English pages without registry-bound engine output.
- Indexing translated foundation pages before English governance review complete.

---

## Unresolved fields (uniform across cohort)

From 6D reliability profile — all 15 units document:

- `public_route_merge`
- `multilingual_expansion`
- `indexation`

Multilingual expansion remains **unresolved** until a future sprint generates and validates alternate-language foundation units.

---

## Internal-link graph multilingual extension

When expansion proceeds:

- Each language gets a **language_hub** root equivalent to `en_foundation_sovereign_intro`.
- Cross-language edges use `hreflang_group` binding, not markdown links between drafts.
- Multilingual overview page becomes the **cross-layer index** for all seven languages.

See `SOVEREIGN_FOUNDATION_COHORT_01_INTERNAL_LINK_GRAPH.md`.

---

## Summary

| Metric | Status |
| --- | --- |
| English foundation layer | **Complete (15 drafts)** |
| Non-English foundation layers | **Not started** |
| hreflang groups reserved | **15 / 15** |
| hreflang tags activated | **No** |
| Multilingual expansion ready for planning | **Yes** |
| Multilingual expansion ready for publication | **No** |
