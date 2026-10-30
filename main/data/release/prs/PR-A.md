# PR-A: Publication safety and authority

> **NOT AUTHORIZED TO MERGE OR DEPLOY.** Draft for review only.

## 1. Purpose and exact scope

- Gate: any discretionary robots downgrade or sitemap removal of a legacy page needs an approved,
  signed per-URL decision (BLOCK_UNAPPROVED_DOWNGRADE / _SITEMAP_REMOVAL); only release-ledger and
  Contract-C enforcement are exempt; unsigned or 'proposed' decisions bind nothing
- IG policy 1.1.0 PROPOSES ig_reviewed_route_realization (AMD-IG-R03-001 rev 2), status
  'awaiting_owner_ratification'. A KO may replace its own existing canonical route, never a new or
  sibling URL; the circular 'no indexable duplicate' prerequisite becomes 42 non-blocking
  consolidation obligations. Opening or merging this PR is NOT ratification; until a named owner
  records it, the authority refuses the posture (fail-closed)
- Authority fails closed: unratified/unverified realization, self-declared validation, evidence lock,
  claim activation, release authorization or R11 certification without a signed human record
- Release review policy: preparer is never the independent reviewer; L1-L6 source lock checklist
- Tests: downgrade, route-realization and release-gate cases (positive + adversarial)

## 2. Verified commit SHA

`d1da411bcba406587f3fed329f20a2394f000971` — the exact head pushed and tested in isolation (27 PASS, 1 BLOCKED_BY_KNOWN_DEPENDENCY, 2 NOT_APPLICABLE).

## 3. Dependency

- Base `release-01/pr-0` — https://github.com/Sohadot/Bisulfid/pull/108; head `release-01/pr-a`.
- Depends on PR-0; must merge after it. Next in the stack: PR-B — https://github.com/Sohadot/Bisulfid/pull/110.
- Release matrix: `main/data/release/RELEASE_01_READINESS.md` on `claude/corpus-distinctiveness-audit-4wsa9f`.

## 4. Files changed

`git diff 4d85bb6520..d1da411bcb` — 23 files changed, 1359 insertions(+), 41 deletions(-)

<details><summary>File list</summary>

```
M	.github/workflows/corpus-governance-ci.yml
M	main/data/information_gain/calibration_pairs.json
M	main/data/information_gain/ig_amendment_proposals.json
M	main/data/information_gain/ig_governance_policy.json
M	main/data/knowledge_objects/knowledge_object_registry.json
A	main/data/publication/consolidation_obligations.json
M	main/data/publication_candidates/PC-BISULFID-TERMINOLOGY-001.json
M	main/data/publication_candidates/PC-MOS2-SCIENTIFIC-001.json
M	main/data/recovery/R03_INDEXATION_REDUCTION_PLAN.json
A	main/data/release/owner_acts.json
A	main/data/release/release_review_policy.json
A	main/data/sources/source_lock_records.json
M	scripts/governance_scaffolding/contract_c_derive.py
M	scripts/governance_scaffolding/ig_governance_tests.py
A	scripts/governance_scaffolding/route_realization.py
A	scripts/governance_scaffolding/route_realization_tests.py
M	scripts/governance_scaffolding/validate_scaffolding.py
A	scripts/publication/build_consolidation_obligations.py
M	scripts/publication/publication_authority.py
M	scripts/publication/test_publication_authority.py
M	scripts/publication/validate_publication_authority.py
A	scripts/release/release_checks.py
A	scripts/release/release_checks_tests.py
```

</details>

Public HTML differences:

No file under `site/public` changes in this PR.

## 5. Production impact

No public file changes. The deploy gate becomes stricter (unapproved downgrades block). Proposes IG policy 1.1.0.

## 6. Isolated test results

Head `d1da411bcb` checked out ALONE in a clean worktree (not a cumulative run). ⏸️ BLOCKED_BY_KNOWN_DEPENDENCY = red only because of the pre-existing /acquire/ conflict that PR-B resolves.

| Status | Area | Command | Detail |
|---|---|---|---|
| ✅ PASS | Contract C | `scripts/governance_scaffolding/contract_c_property_tests.py` | RESULT: PASS — all 7 canonical property tests hold |
| ✅ PASS | Publication authority + approved-decision enforcement | `scripts/publication/test_publication_authority.py` | OK |
| ✅ PASS | Gate 12 | `scripts/validators/test_distinctiveness.py` | OK |
| ✅ PASS | Gate 12 (corpus gate) | `scripts/validators/validate_distinctiveness.py --gate` | NOTE: no markdown page is currently a publication candidate; every draft remains non-public. |
| ✅ PASS | Gate 12-I + legacy migration | `scripts/validators/test_legacy_migration.py` | OK |
| ✅ PASS | Legacy hold integrity + shrink-only ratchet vs main | `scripts/validators/validate_distinctiveness.py --check-hold --hold-ratchet-ref origin/main` | legacy hold main/data/distinctiveness/legacy_surface_hold.json: 14041 sealed entries, sealed from {'surface': 'site/public', 'commit': 'b1757cb532'}; freeze exc |
| ✅ PASS | Legacy disposition registry | `scripts/recovery/validate_legacy_disposition.py` | legacy disposition registry: 14041 records (14000 routes + 41 non-route surfaces); 0 violation(s) |
| ✅ PASS | IG governance | `scripts/governance_scaffolding/ig_governance_tests.py` | RESULT: PASS — all IG governance ratification proofs hold |
| ✅ PASS | IG route-realization safeguards | `scripts/governance_scaffolding/route_realization_tests.py` | RESULT: PASS — route realization holds (positive + adversarial) |
| ✅ PASS | Consolidation obligations current | `scripts/publication/build_consolidation_obligations.py --check` | up to date |
| ✅ PASS | Human review + source-lock safeguards / fail-closed | `scripts/release/release_checks_tests.py` | RESULT: PASS — release gates cannot be self-granted |
| – NOT_APPLICABLE | Review packets current | `scripts/release/build_review_packets.py --check` | tool not present at this commit |
| – NOT_APPLICABLE | Homepage claim audit current | `scripts/release/build_homepage_claim_audit.py --check` | tool not present at this commit |
| ✅ PASS | KO renderer outputs current | `scripts/reference_production/render_ko_reference.py --check` | up to date |
| ✅ PASS | Institutional renderer outputs current | `scripts/reference_production/render_institutional_preview.py --check` | up to date |
| ✅ PASS | SEO previews + internal links | `scripts/reference_production/seo_preview_check.py` | [PASS] Homepage (DE) gate12=PASS words=295 nearest=0.0 |
| ✅ PASS | Scaffolding validator | `scripts/governance_scaffolding/validate_scaffolding.py` | RESULT: PASS — all scaffolding artifacts valid |
| ✅ PASS | Concept/lexeme validator | `scripts/governance_scaffolding/validate_concept_lexeme.py` | RESULT: PASS — concept/lexeme semantic architecture valid |
| ✅ PASS | Source admissibility | `scripts/governance_scaffolding/source_admissibility_tests.py` | RESULT: PASS — all 21 enforcement proofs hold |
| ✅ PASS | Reference production | `scripts/governance_scaffolding/reference_production_tests.py` | RESULT: PASS — all Reference Production 01 proofs hold |
| ✅ PASS | Independence semantics | `scripts/governance_scaffolding/independence_semantics_tests.py` | RESULT: PASS — all independence-semantics proofs hold |
| ✅ PASS | Pilot 03 | `scripts/governance_scaffolding/pilot_03_tests.py` | RESULT: PASS — all Pilot 03 proofs hold |
| ✅ PASS | CI: L1 corpus runtime | `scripts/corpus_validation_runtime_l1.py` | ============================================================ |
| ✅ PASS | CI: source/claim guardrails | `scripts/source_claim_guardrail_runtime_l1.py` | ============================================================ |
| ✅ PASS | CI: L2 production runtime | `scripts/corpus_production_runtime_l2.py` | ============================================================ |
| ✅ PASS | CI: L2 planner | `scripts/corpus_production_planner_l2.py` | ============================================================ |
| ✅ PASS | CI: L0 route registry | `scripts/validate_route_registry_l0.py` | Summary: PASS (0 errors, 120 warnings) |
| ✅ PASS | CI: L0 content drafts | `scripts/validate_content_drafts_l0.py` | Summary: PASS (0 errors, 0 warnings) |
| ⏸️ BLOCKED_BY_KNOWN_DEPENDENCY | Deploy gate on site/public | `scripts/publication/validate_publication_authority.py --surface site/public` | 1 blocking: /acquire/ BLOCK_DIRECTIVE_ESCALATION; resolved by PR-B (release ledger unchanged) |
| ✅ PASS | Governance invariants (no approval, signature, lock, activation, certification or ratification) | `inline invariant check` | OK |

GitHub CI: `corpus-governance-ci` runs only on pull requests whose base is `main`; this stacked PR therefore has no CI run. Absence of checks is NOT a pass; the isolated local results above are the record.

## 7. Known blockers

- AMD-IG-R03-001 (ig_reviewed_route_realization) awaits a SEPARATE owner ratification; merging this PR is not ratification
- a manual deploy stays blocked on /acquire/ until PR-B

## 8. Pending owner and reviewer decisions

- AMD-IG-R03-001 ratification (owner) — not ratified; opening or merging any PR is not ratification
- `/acquire/` URL decision URL-DEC-R03-ACQUIRE-001 (owner) — proposed, unsigned
- R11-HOME-EN-001 / R11-HOME-DE-001 certification (owner) — proposed
- Independent reviews of KO-MOS2-SCIENTIFIC-001 and KO-BISULFID-TERMINOLOGY-001 (named human reviewers) — none recorded
- Source-lock L6 signatures (source registry owner) — 0 of 19
- Claim activations and release authorizations (owner) — none
- Adoption of the release review policy (owner) — proposed; it only restricts
- Every production publication and deployment decision (owner)

## 9. Rollback

git revert the merge commit; the gate returns to the PR-0 behaviour and the IG policy to 1.0.0.

Merge condition (for a FUTURE authorization): Can merge after review: changes no public file. Merging does not ratify AMD-IG-R03-001.

## 10. Authorization status

**NOT AUTHORIZED TO MERGE OR DEPLOY.** This PR was opened under a review-only authorization. Merging, deploying, publishing, signing reviews, locking sources, activating claims, changing indexation or ratifying governance requires a new explicit owner authorization. Auto-merge is not enabled.
