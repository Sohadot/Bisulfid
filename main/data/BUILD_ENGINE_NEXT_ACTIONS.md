# Build Engine Next Actions

**Sprint:** 6M-A  
**Date:** 2026-05-30

---

## Recommended next sprint

**Sprint 6M-B — Template Hardening and Governed Sample Render Planning**

Priority order:

1. Harden templates (head metadata, CSP hooks, governed partials)
2. Define sample output quarantine path (`site/_sample/`)
3. Authorize first non-public sample HTML generation (small N)
4. Optional: add `validate_build_engine_l1.py` to Corpus Governance CI

---

## Proceed to template hardening?

**Yes** — templates are skeleton-only (9 placeholder-like). Build engine strict mode will require production-ready templates before sample render.

---

## Proceed to dry-run sample rendering?

**Not yet** — dry-run sample **planning** is implemented; actual HTML sample render requires Sprint 6M-B authorization after template hardening.

---

## Proceed to production build?

**No** — prerequisites unmet:

- 0 published routes
- Templates not production-ready
- Source registry inactive (0 verified)
- Claim registries predominantly inactive
- `production_can_safely_proceed: no`

---

## Proceed to public launch?

**No** — explicitly out of scope. No sprint authorization exists.

---

## Do source/claim blockers still matter?

**Yes** — binding for any future render or publication:

- 902 COHORT_02 routes have `source_required: true`
- 0 verified sources in registry
- Mass publication impossible without source/claim gate resolution

---

## Does 500-page threshold remain binding?

**Yes** — as advisory publication readiness threshold. Corpus exceeds 500 routes (1,043) but **zero** are published. Threshold now triggers publication readiness **planning**, not automatic build permission.

---

## Does 14,000-page ambition change build requirements?

**Yes, incrementally** — build engine must remain:

- Deterministic at 10k+ routes
- Dry-run capable on full corpus without writes
- Strict on duplicate output paths and flag conflicts
- Fail-closed on any lock breach

6M-A establishes this foundation; scale testing at 10k+ dry-run recommended in 6M-B or 6N.

---

## Criteria for first safe HTML sample generation

All required:

1. Template hardening sprint complete
2. `--dry-run --strict` PASS
3. Explicit DECISION_LOG authorization for sample render
4. Output path quarantined (`site/_sample/`)
5. `noindex, nofollow` on all sample pages
6. Visible non-public labeling in HTML
7. N ≤ 10 routes via `--sample N`
8. No route status changes
9. No commit of sample HTML unless sprint explicitly allows
10. L1/L2/build validators PASS post-render

---

## Criteria for first governed non-public build

All sample criteria **plus**:

1. Multiple route layers represented (gateway, terminology, reference)
2. Source/claim posture documented per rendered route
3. Internal link rendering verified against `internal_links.json`
4. Build audit JSON archived under `main/data/`
5. `production_can_safely_proceed` still **no** unless L2 consensus changes

---

## Criteria for future public launch

1. 14,000-page corpus progress per strategic plan
2. Quality Gate pass on published route set
3. Source verification complete for `source_required` routes
4. Claim registries active with approved claims per route requirements
5. Sitemap and navigation policies activated
6. Security policy gates (CSP, SRI)
7. Zero leakage in publication/indexation/sitemap/navigation audits
8. Explicit public launch sprint in `DECISION_LOG.md`
9. `production_can_safely_proceed: yes` from L2 planner
10. Corpus Governance CI PASS including build engine validator
