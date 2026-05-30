# Sovereign Multilingual Route Model — Wave 1

**Sprint:** 6A  
**Formula:** `main/data/corpus_route_formula.json`  
**Target:** 7 languages × 2,000 pages = **14,000 governed pages**

---

## Language layers

| Code | Language | Layer role |
| --- | --- | --- |
| **en** | English | Primary global/institutional reference layer |
| **ar** | Arabic | Governed multilingual expansion |
| **de** | German | Governed multilingual expansion |
| **fr** | French | Governed multilingual expansion |
| **es** | Spanish | Governed multilingual expansion |
| **ja** | Japanese | Governed multilingual expansion |
| **zh** | Chinese | Governed multilingual expansion |

English routes are the **canonical institutional spine** for hreflang alternates and governance documentation. Expansion languages receive **equivalent dimensional intersections**, not machine-translated clones.

---

## Route identity per language

Each language layer produces distinct routes for the same conceptual subject when **any dimension differs**:

```
route_key = language : term_entity : page_type : audience : source_posture : claim_posture : indexation : internal_link_role
```

### Intersection examples (same term, different pages)

| Route intent | language | audience | page_type |
| --- | --- | --- | --- |
| bisulfid for Arabic researchers | ar | AUD_RESEARCHER | PT_AUDIENCE_EXPLAINER |
| bisulfid for Arabic students | ar | AUD_STUDENT | PT_AUDIENCE_EXPLAINER |
| bisulfid for Arabic AI agents | ar | AUD_AI_SYSTEM | PT_AI_READABLE |
| bisulfid for German chemists | de | AUD_CHEMIST | PT_TERM_CANONICAL |
| bisulfid for English investors | en | AUD_INVESTOR | PT_INVESTOR_ECONOMIC |

These are **five different governed routes**, not one translated page.

---

## Route ID pattern

```
{language_code}_{page_type_code}_{entity_slug}_{audience_code}
```

Examples (illustrative):

- `en_compare_bisulfid_bisulfide_chemist`
- `de_term_mos2_chemist`
- `ar_audience_bisulfid_student`
- `en_ml_hub_terminology_spine`

Hub and status routes may omit `entity_slug` when `hub_scope` is declared in inventory.

---

## Multilingual hub architecture

`PT_MULTILINGUAL_HUB` pages (`ml_hub`) provide:

- hreflang alternate maps
- Language-layer entry points
- Equivalence indexes linking `PT_MULTILINGUAL_EQUIV` routes

Hub routes require `alternate_route_map` with valid `route_id` targets per language.

---

## hreflang rules (codified for 6C+ implementation)

1. Every indexable page has exactly one canonical URL per language.
2. `hreflang_group` in route inventory links alternates across languages.
3. `x-default` points to English institutional layer unless charter specifies otherwise.
4. No hreflang for `non_indexable` or `planned` routes.
5. Equivalence pages (`PT_MULTILINGUAL_EQUIV`) must not claim universal rules without authority.

---

## Translation governance

| Allowed | Forbidden |
| --- | --- |
| Governed template fill from registry-backed content | Bulk MT EN→all languages |
| Human-reviewed terminology equivalents | Translation spam for count |
| Per-language source verification | Publishing without language-appropriate sources |

---

## Current multilingual baseline

| Language | Registered routes (approx.) | Notes |
| --- | ---: | --- |
| en | Majority of 126 | Institutional spine started |
| de | Wave 1 DE drafts present | e.g. `de_core_mos2` |
| ar, fr, es, ja, zh | Inventory expansion in 6B | Not yet at 2,000/language |

---

## 6B next action

Generate **master inventory model** enumerating eligible intersections per language toward 2,000/language—without creating content or publishing routes.
