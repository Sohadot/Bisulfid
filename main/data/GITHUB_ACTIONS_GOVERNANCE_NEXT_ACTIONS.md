# GitHub Actions Governance — Next Actions

**Sprint:** 5P-A  
**Date:** 2026-05-29  
**Status:** Governance CI established — deployment **not authorized**

---

## Recommended next sprint

**Sprint 5N-H prep — human external verification** for `de_core_mos2` named candidates (Spektrum primary; PubChem/NIST supporting; Chemie.de secondary only).

**Parallel:** Enable branch protection requiring **Corpus Governance CI** on `main` (repository admin action).

---

## Whether to proceed to 5N-H named candidate human verification

**Yes — recommended.** Named targets are documented (**5N-G**); verification is the next source-track gate. Governance CI does not substitute for human verification.

---

## Whether to proceed to Route Registration Wave 2 execution

**No.** Dry-run planning complete (**5O-B**); execution **not approved**. CI enforces locks — it does not authorize registry waves.

---

## Whether to proceed to Draft Wave 2

**No.** **58** missing drafts remain. Draft Wave 2 **not approved** (**5O-B**).

---

## Why Route Registration Wave 2 still requires a separate execution sprint

- Dry-run documented **83** candidates; **0** added to `routes.json`.
- `production_can_safely_proceed: no`.
- Source/claim gates not cleared for bulk registration.
- CI validates discipline on merge — it does not charter registry mutation sprints.

---

## Why Draft Wave 2 should still wait

- Wave 1 draft backlog (**58** routes).
- **0** verified sources; **0** approved claims.
- Named MoS2 candidates unverified.
- Governance CI blocks **bad** merges — it does not create draft capacity.

---

## Why workflows must remain governance-only for now

| Reason | Detail |
| --- | --- |
| Launch threshold | **500** governed pages not met (**126** routes) |
| Publication lock | All routes `planned`, non-indexable |
| Source registry | **inactive** |
| Claim registries | **inactive** |
| Doctrine | Generation/deployment before gates = thin corpus and authority risk |

Adding deploy workflows now would contradict sovereign reference discipline.

---

## Criteria for adding future route/content generation automation

All must be true:

1. Explicit sprint charter for generation automation — not bundled with deploy.
2. Governance CI **PASS** required on all changes.
3. Source/claim gates documented per wave.
4. Output remains non-public until publication sprint.
5. No bypass of L0/L1/L2/guardrail runtimes.
6. Human review for wave size and category mix.

---

## Criteria for adding future deployment automation

All must be true:

1. **500-page** threshold met or formal waiver.
2. Publication/indexation locks cleared through documented process.
3. Separate security review (`GITHUB_ACTIONS_GOVERNANCE_SECURITY_MODEL.md` checklist).
4. Secrets scoped minimally; environments per stage.
5. Governance CI remains required on PRs.
6. Rollback documented.
7. No Cloudflare/Pages until owner sign-off — separate sprint.

---

## Criteria for adding future security/technical workflows

- Dependency scanning only if dependencies exist (currently stdlib-only validators).
- Secret scanning — repository default GitHub features; no custom secret exfiltration.
- CodeQL or similar — optional future sprint; not required for stdlib scripts today.
- Any new workflow: `contents: read` default unless write explicitly justified.

---

## How this helps scale toward 500 governed pages

| Contribution | Mechanism |
| --- | --- |
| Merge gates | Every PR to `main` runs same validators as local pre-merge |
| Lock enforcement | Publication/indexation/source/claim locks cannot silently regress |
| Wave discipline | L2 production validators catch planning violations early |
| Human + CI | Reviewers plus automated PASS/FAIL reduce governance drift |

CI supports scale; it does not replace draft production, source verification, or route registration sprints.

---

## How this helps future 1,000+ / 3,000+ / massive corpus scale

1. **Repeatable merge gate** as corpus and contributor count grow.
2. **Manual `workflow_dispatch`** for on-demand audits without deploy.
3. **Foundation for path-filtered workflows** later (e.g. only run heavy checks when `routes.json` changes) — optional optimization sprint.
4. **Separation of concerns** — governance CI stable before generation/deploy CI added.
5. **Audit trail** — GitHub Actions logs per PR for compliance review.

---

## Summary action table

| Action | Proceed? |
| --- | ---: |
| Merge Sprint 5P-A governance workflow | **Yes** (after review) |
| Enable branch protection for Corpus Governance CI | **Yes** (admin) |
| 5N-H human verification | **Yes** |
| Route Registration Wave 2 execution | **No** |
| Draft Wave 2 | **No** |
| Deployment / Cloudflare / Pages workflows | **No** |

---

## Related documents

- `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`
- `GITHUB_ACTIONS_GOVERNANCE_SECURITY_MODEL.md`
- `GITHUB_ACTIONS_GOVERNANCE_VALIDATION_REPORT.md`
- `PRODUCTION_DRY_RUN_NEXT_ACTIONS.md`
- `NAMED_SOURCE_CANDIDATE_NEXT_ACTIONS_WAVE_1.md`
