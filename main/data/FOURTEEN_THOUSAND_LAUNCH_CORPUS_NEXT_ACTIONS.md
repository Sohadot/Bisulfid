# 14,000 Launch Corpus Next Actions

**Sprint:** 6M-F follow-on  
**Date:** 2026-05-31  
**Context:** Post 7,500-page non-public RC inside fixed 14,000-page launch pipeline

---

## Is 7,500-page RC sufficient to proceed to 14,000?

**Partially.** RC 7,500 proves governed corpus expansion at scale, deterministic stratified batch render, multilingual mix, slug discipline (with documented remediation), and validator throughput at 7,500 pages. It is **sufficient to plan** a **14,000-page launch-corpus candidate** with explicit sprint authorization — not sufficient alone for production build or public launch.

---

## Criteria for 14,000-page launch-corpus candidate

1. **7,500 RC PASS** sustained on main with Corpus Governance CI green
2. Corpus expanded to **≥14,000** draft-backed planned routes (governed expansion only)
3. Deterministic stratified selection validated at 14,000 scale
4. All output remains under `site/_sample/` with noindex and RC markers until launch charter
5. Source-required visibility ≥98% at batch scale (document exceptions)
6. No duplicate-path or slug-discipline regressions in route registry
7. **14,000-page objective** unchanged — batch is pipeline proof only
8. Render idempotency and manifest integrity at 14,000 pages
9. Production-grade markdown rendering evaluated for launch-corpus quality

---

## Criteria for first public launch sprint

1. Explicit launch authorization in DECISION_LOG
2. `production_can_safely_proceed: yes` only after all locks lifted by charter
3. Sitemap/navigation/indexation policy activation with governance sign-off
4. Source verification and claim approval where required per route class
5. No `[SOURCE REQUIRED]` on publish-eligible pages without documented exception process
6. Public HTML outside quarantine with full Quality Gate pass

---

## Route/content expansion required before 14,000?

**Yes.** Current registry holds **7,500** routes. Reaching **14,000** renderable pages requires **~6,500** additional governed routes and drafts — likely COHORT_05+ waves using sovereign generator schema, expanded DE/FR tranches, and disambiguation/governance pages. Expansion must remain planned/non-indexable/non-public.

---

## build.py production-grade markdown/content rendering?

**Yes — recommended before 14,000.** Current quarantine render uses minimal stdlib markdown excerpt. Tables, nested lists, and full body fidelity need hardening before the 14,000-page launch-corpus candidate or any public launch preparation.

---

## Template refinements?

**Optional but likely.** Gateway frame full-body rendering, registry template name migration, and hreflang frame placeholders remain open from 6M-C through 6M-F. Not blocking 14,000 planning but blocking launch quality.

---

## Source/claim blockers still matter?

**Yes.** Mass publication remains blocked. Individual source verification and narrow claim approval (e.g. Spektrum) do not authorize corpus-wide publication. `[SOURCE REQUIRED]` must remain on unresolved pages.

---

## Multilingual expansion sufficient or needs strengthening before 14,000?

**Needs strengthening.** DE coverage grew from 100 to 242 rendered pages in the 7,500 RC. The 14,000 launch corpus requires a deliberate DE (and future FR) tranche plan proportional to launch charter — not ad hoc expansion.

---

## Why quality gates remain non-negotiable

The corpus targets **14,000+** pages scaling toward **100,000+**. Premature publication, indexation leak, or implied claim approval would violate doctrine.

---

## Why visibility/publication remains the primary track

Engineering RC batches prove render and governance at scale. **Public launch** remains a separate, explicitly authorized sprint after the **14,000-page launch corpus** is registered, validated, and approved — not inferred from RC batch size.

---

## Why this sprint still does not authorize public launch

Sprint 6M-F produced a **7,500-page non-public RC** under `site/_sample/` only. No routes were published, no routes were made indexable, no routes were added to sitemap or navigation, no sources or claims were approved, and `[SOURCE REQUIRED]` markers remain unresolved. The **14,000-page minimum launch corpus** objective is unchanged.
