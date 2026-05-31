# 7,500-Page Pipeline Next Actions

**Sprint:** 6M-E follow-on  
**Date:** 2026-05-31  
**Context:** Post 1,500-page non-public RC inside fixed 14,000-page launch pipeline

---

## Is 1,500-page RC sufficient to proceed to 7,500?

**Partially.** RC 1,500 proves corpus expansion, batch render at scale, multilingual mix, and validator throughput. It is **sufficient to plan** a **7,500-page** non-public RC with explicit sprint authorization — not sufficient alone for production build or public launch.

---

## Criteria for 7,500-page non-public RC batch

1. **1,500 RC PASS** sustained on main with Corpus Governance CI green
2. Corpus expanded to **≥7,500** draft-backed planned routes (governed expansion only)
3. Deterministic stratified selection validated at 7,500 scale
4. All output remains under `site/_sample/` with noindex and RC markers
5. Source-required visibility ≥98% at batch scale (document exceptions)
6. No duplicate-path or slug-discipline regressions in route registry
7. **14,000-page objective** unchanged — batch is pipeline proof only
8. Render idempotency and manifest integrity at 7,500 pages

---

## Criteria for 14,000-page launch corpus preparation

1. **≥14,000** planned, draft-backed routes registered
2. Source/claim boundaries audited across full inventory
3. Production-grade markdown rendering in build engine
4. Template registry migration complete (if chartered)
5. Publication lock lift proposal — separate launch sprint only
6. Quality Gate validation on representative launch cohort
7. **14,000-page minimum** remains fixed

---

## Criteria for first public launch sprint

1. Explicit launch authorization in DECISION_LOG
2. `production_can_safely_proceed: yes` only after all locks lifted by charter
3. Sitemap/navigation/indexation policy activation with governance sign-off
4. Source verification and claim approval where required per route class
5. No `[SOURCE REQUIRED]` on publish-eligible pages without documented exception process
6. Public HTML outside quarantine with full Quality Gate pass

---

## Route/content expansion required before 7,500?

**Yes.** Current registry holds **1,500** routes. Reaching **7,500** renderable pages requires **~6,000** additional governed routes and drafts — likely COHORT_04+ waves using sovereign generator schema, DE/FR expansion tranches, and disambiguation/governance pages. Expansion must remain planned/non-indexable/non-public.

---

## build.py production-grade markdown/content rendering?

**Yes — recommended before 7,500.** Current quarantine render uses minimal stdlib markdown excerpt. Tables, nested lists, and full body fidelity need hardening before larger RC batches or launch preparation.

---

## Template refinements?

**Optional but likely.** Gateway frame full-body rendering, registry template name migration, and hreflang frame placeholders remain open from 6M-C/6M-D. Not blocking 7,500 planning but blocking launch quality.

---

## Source/claim blockers still matter?

**Yes.** Mass publication remains blocked. Individual source verification and narrow claim approval (e.g. Spektrum) do not authorize corpus-wide publication. `[SOURCE REQUIRED]` must remain on unresolved pages.

---

## Why quality gates remain non-negotiable

The corpus targets **14,000+** pages scaling toward **100,000+**. Premature publication, indexation leak, or implied claim approval would violate doctrine.

---

## Why visibility/publication remains the primary track

Route inventory and draft expansion prove **capacity**. **Publication readiness** — source lock, claim boundary, render quality, indexation discipline — determines when locks may lift. RC batches prove render; they do not authorize visibility.

---

## Why this sprint still does not authorize public launch

- **0** published routes
- **0** indexable / sitemap / navigation routes
- **No** source or claim mass approval
- **1,500-page RC** is engineering proof only
- **14,000-page objective unchanged**

**Recommended next sprint:** 6M-F — 7,500-page non-public RC with governed corpus expansion and markdown rendering improvements, or authorized template registry migration if separately chartered.
