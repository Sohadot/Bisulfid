# Sovereign Foundation COHORT_01 — Route Registration No-Publication Guardrail

**Sprint:** 6F  
**Posture:** Routes registered — **not published**

---

## Sprint boundary

| Action | Performed? |
| --- | --- |
| 15 COHORT_01 routes added to routes.json | **Yes** |
| Route count 126 → 141 | **Yes** |
| Draft-to-route binding | **Yes** |
| Internal-link targets in registry | **Yes** |
| Route status set to published | **No** |
| indexable set to true | **No** |
| in_sitemap set to true | **No** |
| in_navigation set to true | **No** |
| Public HTML generated | **No** |
| Sitemap activated | **No** |
| Navigation activated | **No** |
| Indexation approved | **No** |
| New sources registered | **No** |
| New claims approved | **No** |
| Validators weakened | **No** |

---

## Mandatory locks on all 15 new routes

```json
{
  "status": "planned",
  "indexable": false,
  "in_sitemap": false,
  "in_navigation": false,
  "source_required": false,
  "required_claim_groups": []
}
```

---

## Registry-level rule (unchanged)

From `routes.json` header:

> Routes may enter this registry as planned, but no route may enter sitemap, production navigation, or production output until it is published and passes the Quality Gate.

COHORT_01 routes enter as **planned** only. They are **draft-backed** (content file exists) but **not publication-ready**.

---

## Forbidden in this sprint

- Setting any route `status` to `published`
- Setting `indexable: true` on any route
- Setting `in_sitemap: true` or `in_navigation: true`
- Generating public HTML or activating sitemap/navigation configs
- Modifying `internal_links.json` to live edges
- Removing `[SOURCE REQUIRED]` markers from existing corpus pages
- Approving claims or registering sources

---

## Draft content discipline (unchanged)

Foundation drafts retain:

- `publication_status: non_public`
- `noindex_default: true`
- No markdown links in body (pre-publication discipline)
- Governance framing only — no unsupported claims

---

## production_can_safely_proceed

Route registration **does not** change production readiness. Expected value remains **no** until source/claim gates and broader corpus thresholds clear.

---

## Epistemic guardrail

Registered routes describe governance posture. Registration is **not** evidence of factual approval, source-locking completion, or public launch authorization.

---

*Sprint 6F — No Publication Guardrail*
