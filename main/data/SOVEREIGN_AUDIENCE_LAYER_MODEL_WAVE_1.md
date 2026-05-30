# Sovereign Audience Layer Model — Wave 1

**Sprint:** 6A  
**Registry:** `main/data/audience_layer_registry.json`  
**Count:** 9 audience layers

---

## Model principle

Every governed page that uses audience targeting assigns exactly one **audience_id** for explainer, comparison, and context page types. Audience layers constrain vocabulary, allowed claim classes, forbidden claim classes, tone, internal links, and safety/medical/market restrictions.

Audience is a **route dimension**—not a marketing persona. `bisulfid + Arabic + researcher` and `bisulfid + Arabic + student` are different routes.

---

## Audience registry summary

| audience_id | Code | Vocabulary | Primary page types |
| --- | --- | --- | --- |
| AUD_CHEMIST | chemist | professional_technical | PT_TERM_CANONICAL, PT_COMPARISON, PT_COMPOUND |
| AUD_RESEARCHER | researcher | academic_technical | All reference types; source/claim clusters |
| AUD_ANALYST | analyst | professional_analytical | PT_INVESTOR_ECONOMIC, PT_COMPARISON |
| AUD_GOVERNMENT | government | institutional_formal | PT_GOVERNMENT_POLICY, PT_SOURCE_BOUND |
| AUD_INVESTOR | investor | professional_financial | PT_INVESTOR_ECONOMIC (verified market only) |
| AUD_COMPANY | company | professional_industry | PT_COMPANY_INDUSTRY, PT_GLOSSARY |
| AUD_STUDENT | student | educational_intermediate | PT_AUDIENCE_EXPLAINER, PT_GLOSSARY, PT_COMPARISON |
| AUD_AI_SYSTEM | ai_system | structured_machine | PT_AI_READABLE, PT_CLAIM_BOUNDARY |
| AUD_CHILD_EDU | child_edu | child_safe_basic | PT_CHILD_SAFE_EDU only |

---

## Claim class matrix (simplified)

| Claim class | Chemist | Researcher | Analyst | Gov | Investor | Company | Student | AI | Child |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| terminology | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| comparison | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — |
| verified_market | — | — | ✓ | — | ✓ | — | — | — | — |
| safety/medical | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| procurement/acquisition | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |

✗ = hard forbidden for all page types targeting that audience.

---

## Internal-link expectations by audience

| Hub type | Primary audiences |
| --- | --- |
| language_hub | All |
| term_spine | Chemist, researcher, student, AI |
| comparison_cluster | Chemist, researcher, student, analyst, investor |
| source_cluster | Researcher, government, AI |
| claim_cluster | Researcher, government, AI |
| audience_cluster | All explainer types |
| glossary_cluster | Student, chemist, child |
| ai_readable_cluster | AI, researcher |
| child_safe_cluster | Child, student |

---

## Audience × language scale contribution

Audience-layer explainers contribute ~350 pages per language in the illustrative 2,000/language decomposition. With 9 audiences and ~200 core entities, eligible intersections are filtered by page type compatibility—not full Cartesian product.

---

## Generator rules

1. Generator reads `audience_layer_registry.json` before content fill.
2. Reject if page type `allowed_audiences` excludes target audience.
3. Reject if claim class not in audience `allowed_claim_classes`.
4. Reject if content contains audience `forbidden_claim_classes`.
5. Child audience: additional PT_CHILD_SAFE_EDU schema required.

---

## Registry reference

Full definitions: `main/data/audience_layer_registry.json`

Cross-reference: `main/data/page_type_registry.json` `allowed_audiences` fields
