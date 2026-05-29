# Production Dry-Run — Next Actions

**Sprint:** 5O-B  
**Date:** 2026-05-27  
**Status:** Dry-run complete — execution not approved

---

## Recommended next sprint

**Primary:** Sprint **5N-G** — named source candidate intake wave 1 (`de_core_mos2` priority).

**Parallel (not registration):** Draft Wave 1 backlog work — reduce **58** missing drafts before any Draft Wave 2 or Route Registration Wave 2 execution.

---

## Proceed to Route Registration Wave 2 execution?

**No.** Dry-run planning does not authorize registry modification. Execution requires a separate sprint after blockers in `ROUTE_REGISTRATION_WAVE_2_EXECUTION_BLOCKERS.md` clear.

---

## Proceed to another dry-run refinement first?

**Optional, not required.** Current **83** candidates are documented, classified, and validated. Refinement sprint warranted only if:

- Blueprint cohort changes materially, or
- Human review rejects enough needs-review rows to require replacement candidates, or
- Source/claim gate mapping changes eligibility.

---

## Proceed to 5N-G named source candidate intake?

**Yes — recommended.** `de_core_mos2` is the only conditional proposal-readiness candidate (Sprint 5N-F). Source gate clearance for terminology routes depends on named, verified candidates — not dry-run registration.

---

## Proceed to claim-boundary registration/reporting?

**Yes — recommended in parallel with draft/source work.** Strict-registry terminology and disambiguation dry-run candidates require claim gates before publication-ready content. Claim registries remain inactive until this work advances.

---

## Proceed to Draft Wave 2?

**No — not yet.** Draft Wave 2 should wait until:

1. Wave 1 **58** missing drafts are materially addressed, and
2. Source/claim gates show progress for priority routes, and
3. Owners explicitly charter Draft Wave 2 with capacity.

Registering **83** new routes without draft capacity would worsen content debt.

---

## Why Draft Wave 2 should still wait

- **58** registered routes already lack drafts.
- **0** verified sources and **0** approved claims — drafts would retain `[SOURCE REQUIRED]` markers and strict-registry blocks.
- Dry-run candidates are registration **candidates**, not draft assignments.
- Quality at 500+ governed pages requires draft waves paced to source/claim clearance — not parallel registry inflation.

---

## Why route registration execution requires a separate sprint

Sprint 5O-B charter explicitly prohibits:

- Modifying `routes.json`
- Creating content
- Publishing routes
- Approving claims or sources

Execution sprint requires explicit authorization, cleared blockers, runtime PASS, and DECISION_LOG entry — distinct from dry-run planning.

---

## Criteria for moving dry-run candidates into actual routes.json registration

A candidate may move to execution **only when all apply**:

1. Appears in approved execution manifest (may be subset of **83**).
2. Human review complete — needs-review rows accepted or replaced.
3. Source gate mapped for candidate class (minimum registry progress for strict-registry pages).
4. Claim gate workflow ready where matrix flags **claim gate required: yes**.
5. Internal link role defined for index/map and spine clusters.
6. Multilingual governance plan for DE rows.
7. L2 + L1 + guardrail runtimes **PASS** immediately pre-registration.
8. Explicit execution sprint charter and owner sign-off.
9. New routes register as `planned`, non-indexable, out of sitemap/navigation.

---

## Criteria for rejecting candidates

Reject or defer (`reject_from_wave_2` / `defer_to_later_wave`) when:

- Duplicate or near-duplicate of existing route concept.
- Drift into market, procurement, safety, medical, or handling instruction scope.
- High claim risk or `deferred_high_risk_review` eligibility.
- ar/zh/ja expansion before EN/DE governance stable.
- Thin/generic chemistry blog surface without sovereign reference role.
- Source/claim gates cannot be mapped within launch horizon.
- Link graph role cannot be assigned without orphan risk.
- Human review fails for needs-review industrial-language rows.

---

## Criteria for reducing wave size

Reduce below **83** when:

- Draft backlog policy caps registration ahead of draft capacity.
- Source gate clearance supports fewer strict-registry pages than planned.
- Human review rejects needs-review tier (**9** rows).
- Link graph plan cannot support all index/map hubs in one wave.
- Owner policy prefers smaller waves (e.g. **50–60**) for reviewability.

Minimum execution wave should remain purposeful — not bulk filler. **80** is the documented floor of the dry-run band; execution may target lower if gates require.

---

## Criteria for source/claim gate clearance

### Source gate cleared when:

- Named verified candidate exists for priority terminology class, or
- Source class mapping documents acceptable registry entries for candidate batch, and
- `source_registry.json` activation policy approved for execution sprint (separate from 5O-B).

### Claim gate cleared when:

- Terminology claim boundaries registered for candidate batch, and
- Claim registry activation policy approved, and
- No dry-run candidate requires claims beyond mapped boundaries.

---

## Criteria for link graph readiness

Link graph ready when:

- Hub roles assigned for **5** index/map candidates.
- Terminology spine cluster links planned for registered + proposed cohort.
- Disambiguation authority walls linked to triad/boundary pages.
- L2 `validate_internal_link_graph_plan_l2.py` PASS on post-registration plan (dry-run mode).

---

## How this moves the corpus toward 500 governed pages

| Stage | Contribution |
| --- | --- |
| Dry-run **83** candidates | Identifies **66%** registry growth path (126 → 209) without executing |
| Wave 1 **126** + future waves | Multiple 80–120 registration waves + draft production → **500** threshold |
| Governance-first selection | Terminology spine and reference architecture — not thin page count |
| Gate discipline | Governed pages = source-locked, editorially signed, link-integrated — not `planned` rows alone |

Remaining gap after hypothetical Wave 2 registration: **291** routes toward **500** — still requiring additional registration and draft waves.

---

## How this preserves long-term 1,000+ / 3,000+ / massive corpus quality

1. **Repeatable L2 dry-run pattern** for each registration wave before registry mutation.
2. **EN/DE-first** prevents translation spam at scale.
3. **Per-candidate gate flags** scale to thousands of routes without authority bypass.
4. **Category discipline** prevents generic chemistry blog inflation.
5. **Link graph and SEO locks** prevent indexation leakage during long build-out.
6. **Source/claim guardrails** remain merge-blocking at L1 regardless of corpus size.

---

## Summary action table

| Action | Proceed? |
| --- | ---: |
| Route Registration Wave 2 execution | **No** |
| Dry-run refinement | **Optional** |
| 5N-G source candidate intake | **Yes** |
| Claim-boundary registration/reporting | **Yes** (parallel) |
| Draft Wave 1 backlog reduction | **Yes** (parallel) |
| Draft Wave 2 | **No** (wait) |
| Route Registration Wave 2 execution sprint | **Future** — after blockers clear |

---

## Related documents

- `PRODUCTION_DRY_RUN_WAVE_PLANNING_REPORT.md`
- `ROUTE_REGISTRATION_WAVE_2_DRY_RUN_MANIFEST.md`
- `ROUTE_REGISTRATION_WAVE_2_EXECUTION_BLOCKERS.md`
- `ROUTE_REGISTRATION_WAVE_2_RISK_REVIEW.md`
- `PRODUCTION_DRY_RUN_VALIDATION_REPORT.md`
