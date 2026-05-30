# Sovereign Route Path Pattern Model — Wave 1

**Sprint:** 6B  
**Purpose:** Define URL path patterns per page family and language without creating routes in `routes.json`.

---

## Path pattern principles

1. Paths derive from **language + page_type + entity slug + optional audience/reference suffix**.
2. **English** paths are the institutional canonical base for hreflang `x-default`.
3. **Arabic** paths use same pattern structure with `rtl: true` in inventory row — content layer RTL, not URL inversion.
4. All inventory paths are **planned** only until merge charter.
5. No path is published or indexable in 6B.

---

## Language prefix patterns

| Language | Prefix | RTL |
| --- | --- | --- |
| en | `/` or `/en/` | false |
| ar | `/ar/` | **true** |
| de | `/de/` | false |
| fr | `/fr/` | false |
| es | `/es/` | false |
| ja | `/ja/` | false |
| zh | `/zh/` | false |

**English institutional base:** Governance and foundation routes may live at `/` (en) or `/en/` per existing convention; expansion languages always use locale prefix.

---

## Page family path patterns

| page_type_id | path_pattern_id | Pattern (illustrative) |
| --- | --- | --- |
| PT_FOUNDATION | `PATH_FOUNDATION` | `/{lang}/` or `/{lang}/about/` |
| PT_TERM_CANONICAL | `PATH_TERM` | `/{lang}/terminology/{entity_slug}/` |
| PT_COMPOUND_ENTITY | `PATH_COMPOUND` | `/{lang}/terminology/{entity_slug}/` |
| PT_MULTILINGUAL_EQUIV | `PATH_EQUIV` | `/{lang}/equivalence/{entity_slug}/` |
| PT_MULTILINGUAL_HUB | `PATH_ML_HUB` | `/{lang}/hub/multilingual/{hub_scope}/` |
| PT_DIFFERENCE_COMPARISON | `PATH_COMPARE` | `/{lang}/compare/{side_a}-vs-{side_b}/` |
| PT_AUDIENCE_EXPLAINER | `PATH_AUDIENCE` | `/{lang}/reference/{entity_slug}/{audience_code}/` |
| PT_CHILD_SAFE_EDU | `PATH_CHILD_EDU` | `/{lang}/learn/{entity_slug}/` |
| PT_AI_READABLE | `PATH_AI` | `/{lang}/ai-reference/{entity_slug}/` |
| PT_GOVERNMENT_POLICY | `PATH_GOV` | `/{lang}/policy/{topic_slug}/` |
| PT_INVESTOR_ECONOMIC | `PATH_INVESTOR` | `/{lang}/economic-context/{entity_slug}/` |
| PT_COMPANY_INDUSTRY | `PATH_INDUSTRY` | `/{lang}/industry/{topic_slug}/` |
| PT_GLOSSARY_CLUSTER | `PATH_GLOSSARY` | `/{lang}/glossary/{cluster_id}/` |
| PT_SOURCE_BOUND | `PATH_SOURCE` | `/{lang}/sources/{source_id}/` |
| PT_CLAIM_BOUNDARY | `PATH_CLAIM` | `/{lang}/claims/{claim_id}/` |
| PT_METHODOLOGY_GOVERNANCE | `PATH_METHODOLOGY` | `/{lang}/governance/{topic_slug}/` |
| PT_SOURCE_STATUS | `PATH_SOURCE_STATUS` | `/{lang}/status/source/{source_id}/` |
| PT_CLAIM_STATUS | `PATH_CLAIM_STATUS` | `/{lang}/status/claim/{claim_id}/` |
| PT_CORPUS_STATUS | `PATH_CORPUS_STATUS` | `/{lang}/status/corpus/` |

---

## Reference-layer path suffix (optional)

When same page_type + entity + language serves multiple reference layers, path may include reference layer code:

```
/{lang}/reference/{entity_slug}/{reference_layer_code}/{audience_code}/
```

Example: `/ar/reference/bisulfid/research/researcher/` vs `/ar/reference/bisulfid/educational/student/`

Inventory generator chooses suffix when anti-duplication requires distinct URLs.

---

## Comparison path patterns (core SEO)

| comparison_reference_mode | path example (en) |
| --- | --- |
| linguistic_comparison | `/en/compare/bisulfid-vs-bisulfide/` |
| technical_comparison | `/en/compare/mos2-technical-identity/` |
| educational_comparison | `/en/learn/compare/bisulfid-vs-bisulfite/` |
| research_comparison | `/en/reference/compare/sulfide-research-boundary/` |
| economic_relevance_comparison | `/en/economic-context/compare/terminology-vs-market-claim/` |
| institutional_terminology_comparison | `/en/policy/compare/dictionary-vs-regulatory-language/` |

Comparison paths require `comparison_pair_id` in inventory row.

---

## Arabic RTL representation

| Aspect | Rule |
| --- | --- |
| URL structure | Same LTR path segments; locale prefix `/ar/` |
| Content layer | `rtl: true` in inventory row and draft frontmatter (6C+) |
| hreflang | `ar` alternate linked to en institutional base |
| Institutional base | English remains x-default and governance spine |
| Weakness prevention | RTL is content/metadata — not separate URL scheme weakening EN base |

---

## route_id alignment

```
route_id = {language_code}_{page_type_code}_{entity_slug}_{reference_layer_code}_{audience_code}
```

Hub routes omit entity_slug: `{lang}_ml_hub_{hub_scope}`

Existing production routes (126) retain current route_ids until migration charter.

---

## Path validation rules (6C+)

- Unique path per inventory row
- No collision with existing 126 routes.json paths without merge review
- No raw external URLs in path
- Slug: lowercase, hyphen-separated, ASCII transliteration for non-Latin display titles
- Comparison paths: both entity slugs required

---

## Existing path example (production — unchanged)

`de_core_mos2` → `/de/terminology/molybdenum-disulfide/` (126-route set; not modified in 6B)
