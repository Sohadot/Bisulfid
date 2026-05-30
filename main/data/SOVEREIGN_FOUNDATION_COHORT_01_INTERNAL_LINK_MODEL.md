# Sovereign Foundation Cohort 01 — Internal Link Model

**Sprint:** 6D  
**Cohort:** COHORT_01_FOUNDATION_GOV  
**Language:** English first

---

## Hub structure

```
en_foundation_sovereign_intro (language_hub)
    ├── en_foundation_institutional_purpose
    ├── en_foundation_methodology
    ├── en_foundation_source_policy (source_hub)
    ├── en_foundation_claim_policy (claim_hub)
    ├── en_foundation_knowledge_reliability
    ├── en_foundation_multilingual_overview (language_hub)
    ├── en_foundation_reference_layers
    ├── en_foundation_audience_layers (audience_hub)
    ├── en_foundation_chemical_language_governance (term_hub)
    ├── en_foundation_ai_readable_policy (AI_reference_hub)
    ├── en_foundation_child_safe_policy (education_hub)
    ├── en_foundation_economic_institutional_restrictions
    ├── en_foundation_corpus_status
    └── en_foundation_launch_status
```

---

## Required edges (internal reference by route_id)

| From | To | Role |
| --- | --- | --- |
| sovereign_intro | institutional_purpose | orientation |
| sovereign_intro | methodology | process |
| sovereign_intro | launch_status | posture |
| methodology | source_policy | provenance |
| methodology | claim_policy | boundaries |
| methodology | knowledge_reliability | credibility |
| source_policy | claim_policy | governance pair |
| knowledge_reliability | reference_layers | layer model |
| knowledge_reliability | audience_layers | audience model |
| multilingual_overview | reference_layers | linguistic layer |
| reference_layers | audience_layers | matrix |
| chemical_language_governance | source_policy | terminology governance |
| ai_readable_policy | knowledge_reliability | technical disclosure |
| child_safe_policy | audience_layers | AUD_CHILD_EDU |
| economic_institutional_restrictions | source_policy | restricted classes |
| corpus_status | launch_status | production locks |
| launch_status | corpus_status | status pair |

---

## Implementation note

Drafts use **route_id text references only** — no markdown links until route merge charter. Future `internal_links.json` wiring in Sprint 6E.

---

## Multilingual expansion

Each English foundation page defines `hreflang_group` in blueprints. Expansion adds `ar_foundation_*`, `de_foundation_*`, etc. with `language_hub` edges to English institutional base.
