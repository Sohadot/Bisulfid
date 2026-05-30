# Sovereign Content Automation Engine v1 — No Publication Guardrail

**Sprint:** 6D  
**Engine:** `sovereign_content_automation_engine_v1`  
**Posture:** Controlled draft generation — no publication

---

## Sprint boundary

| Action | Performed? |
| --- | --- |
| Content Automation Engine v1 implemented | **Yes** |
| COHORT_01 dry-run manifest | **Yes** |
| Draft blueprints | **Yes** |
| Non-public foundation draft files (15) | **Yes** |
| LLM / free-form generation | **No** |
| routes.json modified | **No** |
| Routes published | **No** |
| Public HTML generated | **No** |
| indexable / sitemap / navigation activated | **No** |
| New sources registered | **No** |
| New claims approved | **No** |
| [SOURCE REQUIRED] markers removed | **No** |
| Validators weakened | **No** |

---

## Engine output locks (mandatory on every draft)

```yaml
status: draft
publication_status: non_public
indexable: false
in_sitemap: false
in_navigation: false
noindex_default: true
production_route_registry: false
generated: true
engine: sovereign_content_automation_engine_v1
```

---

## Hard rejects (engine abort)

- Missing required unit fields (`route_id`, `slug`, `h1`, `summary`, `bullets`)
- Unknown `page_type_id` or `reference_layer_id`
- Page type not applicable to `TPL_FOUNDATION_GOV_V1`
- Any unit with `indexable`, `in_sitemap`, or `in_navigation` true
- Narrative fields containing unsupported claim phrases without explicit negation

---

## Forbidden engine behaviors

- Modify `routes.json` or merge pre-route IDs into production registry  
- Set `indexable: true`, `in_sitemap: true`, or `in_navigation: true`  
- Generate public HTML or activate sitemap/navigation  
- Use LLM or invent sources, claims, facts, market data, or safety advice  
- Remove `[SOURCE REQUIRED]` from existing content  
- Approve claims or register sources  
- Create placeholder public pages or thin stub pages  
- Upgrade `evidence_grade` beyond registry allowance  

---

## Pre-route posture

COHORT_01 drafts exist as **pre-route** content files. They are **not** in `routes.json`. Internal reference is by `route_id` metadata only until a separate merge charter authorizes route registration.

---

## Governance unchanged

| Gate | Status |
| --- | --- |
| `production_can_safely_proceed` | **no** |
| Registered routes | **126 — unchanged** |
| All corpus locks | **LOCKED** |
| Workflows / packages / dependencies | **unchanged** |

---

## Epistemic guardrail

Engine v1 produces **governance framing only**. It never converts absence of evidence into factual conclusion. Weak-evidence and doctrine pages remain **noindex / non-public** until explicit publication charter.
