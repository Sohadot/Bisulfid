# Template Next Actions

**Sprint:** 6M-B  
**Date:** 2026-05-30

---

## Recommended next sprint

**6M-C — Governed render wiring and local quarantined QA sample**

1. Wire build engine to publication frame templates (`page.html`, `reference.html`, `term.html`)
2. Migrate registry template references (requires governed `routes.json` sprint)
3. Local uncommitted render to `site/_sample/` (N ≤ 3)
4. Optional: publication lock exception for `site/_sample/**/*.html` in L1 validator

---

## Proceed to production build?

**No** — templates hardened but render wiring incomplete; 0 published routes; locks active.

---

## Proceed to public launch?

**No** — 14,000-page corpus not reached; sources unverified; claims inactive.

---

## Proceed to sitemap / navigation / indexation?

**No** — all locks remain **LOCKED**.

---

## 14,000-page target

**Unchanged** — minimum launch corpus remains **14,000 governed pages**. Current 1,043 routes are pipeline progress only.

---

## 500-page threshold

**Advisory only** — does not replace or reduce the 14,000-page objective.

---

## Source/claim blockers

**Still binding** — 902 COHORT_02 routes require sources; 0 verified in registry.

---

## Criteria for first governed render (local QA)

1. Build engine render mode authorized by decision log
2. Publication frame templates wired
3. Output to `site/_sample/` only
4. `noindex, nofollow` on all output
5. Governance banner visible
6. No commit of sample HTML until publication lock policy updated OR exception documented
7. L1/L2 + template validators PASS

---

## Criteria for registry template migration

1. Sprint authorization to modify `routes.json`
2. Map `reference_page.html` → `reference.html`, `term_page.html` → `term.html`
3. Full route registry integrity gate after migration
4. No publication status changes during migration
