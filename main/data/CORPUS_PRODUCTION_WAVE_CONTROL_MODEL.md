# Corpus Production Wave Control Model — Layer 2

**Sprint:** 5O-A  
**Date:** 2026-05-29  
**Status:** Planning control model — read-only automation support

---

## Purpose

Define **wave types**, **maximum safe sizes**, **mandatory order**, and **human-review boundaries** for sovereign-scale corpus production from **126** planned routes toward **500** governed launch pages and beyond (**1,000+**, **3,000+**, optional massive scale only under governance).

---

## Wave types

| Wave type | Purpose | Typical size | Output |
| --- | --- | --- | --- |
| **Route registration waves** | Add `planned` rows to `routes.json` | **80–120** routes | Registry rows only; no publication |
| **Draft production waves** | Create non-public `content_file` bodies | **40–60** pages | Drafts with markers; no publication |
| **Source mapping waves** | Align sources to draft markers | **40–60** pages | Mapping reports; registry proposals |
| **Claim boundary waves** | Scope claim groups per draft | **40–60** pages | Boundary reports; no approval unless chartered |
| **Internal link graph waves** | Wire cluster edges in planning graph | **40–60** edges | `internal_links.json` slices; route_id only |
| **SEO metadata waves** | Validate title/description/H1/canonical | Cohort samples + cluster audits | Metadata readiness reports |
| **Multilingual waves** | Controlled terminology records per language | **20–40** pages per language slice | Non-public localized records |
| **Sitemap/indexation waves** | Policy-aligned inclusion planning | Launch cohort only | Sitemap plan; no live indexation pre-gate |
| **Technical/security validation waves** | Build, security, indexation guard checks | Full cohort sample | Validation reports |
| **Publication readiness waves** | Quality Gate + editorial signoff | **500** page minimum cohort | Authorized publication only after all gates |

**Route waves and draft waves remain separate.** Do not mix registration and draft production in one sprint unless explicitly chartered and validated.

---

## Maximum safe wave sizes

| Constraint | Rule |
| --- | --- |
| Single sprint route registration | **≤ 120** new planned routes |
| Single sprint draft production | **≤ 60** new drafts |
| Single sprint registry execution | **≤ 3** verified source rows (source program) |
| Single sprint link wiring | **≤ 60** new edges |
| Launch publication batch | **≥ 500** pages **only after** all gates pass — not incremental public dribble |

Exceeding sizes without charter increases thin-content, broken-link, and governance-debt risk.

---

## Required order of operations

```
1. Route registration wave      → planned only; locks enforced
2. Draft production wave        → non-public; [SOURCE REQUIRED] preserved
3. Source mapping / verification → gates before claim approval
4. Claim boundary wave          → scoping only unless activation chartered
5. Internal link graph wave     → route_id targets; no live unpublished links
6. SEO metadata wave            → before any publication authorization
7. Multilingual wave            → after terminology governance per language
8. Technical/security validation
9. Publication readiness wave   → ONLY after ≥ 500 governed pages pass ALL gates
10. Sitemap/indexation wave     → ONLY after publication readiness authorization
```

**Source gate and claim gate precede publication.** Draft wave 2 is **not allowed** until governance debt is reduced (named source candidates, registry rows, claim boundaries, L1+L2 validation PASS).

---

## What must never be automated without human review

| Surface | Human review required |
| --- | --- |
| Source registry row writes | Always |
| Claim approval / registry activation | Always |
| Marker removal | Always — audited linkage only |
| Route publication (`status: published`) | Always — Quality Gate + owner signoff |
| `indexable: true` / `in_sitemap: true` | Always — launch program authorization |
| Multilingual public pages (ar/zh/ja) | Always — deferred until hreflang + source governance ready |
| Mass page generation | **Forbidden** without source/claim/link/SEO gates |
| Bibliographic details | Never invented by automation |

---

## Relationship to existing wave 1 artifacts

- `ROUTE_REGISTRATION_WAVE_1_REPORT.md` — governance test; not sufficient alone for launch scale
- `DRAFT_PRODUCTION_WAVE_1_REPORT.md` — draft discipline proof; draft wave 2 waits
- Source/claim programs (5N-*) — mandatory gates before production scale-up

---

*Sprint 5O-A — Corpus Production Wave Control Model Layer 2*
