# PR-D: MoS2 reference release readiness

> **NOT AUTHORIZED TO MERGE OR DEPLOY.** Draft for review only.

## 1. Purpose and exact scope

- PC/KO record IG posture ig_reviewed_route_realization: its four structural conditions pass
  (replaces the body of /molybdenum-disulfide/; no new URL; 38 consolidation obligations). It is NOT
  honoured until AMD-IG-R03-001 is ratified by a named owner; the authority treats it as
  ig_reviewed_no_new_route until then
- Claim-by-claim approval dossier and independent-review packet (3 claims, 11 admitted records);
  the review record names the automated preparer, which can never be the reviewer
- Source-lock checklist (L1-L6): COD x2, PubChem, NIST pass L1-L5 (live recapture 2026-10-30 matches
  the 2026-09-20 values); 4 uploaded-excerpt sources lack a capture (L2/L3 pending; RSC HTML 403);
  L6 human sign-off pending for all 8
- Release candidate staged (main/data/release/staged/molybdenum-disulfide/): directives from the
  authority, governance text from signed records only ('independent review not yet performed')
- Fix: IG units are found for the SERVED HTML (registry served_url). Without it Gate 12 would have
  vetoed the reference on deploy; a legacy body at the same URL still gets 0 valid units
- apply_release.py refuses unless Contract C is index-approved; simulate_release.py rehearses the gate

Rollback: revert this commit (no live file changed).

## 2. Verified commit SHA

`a65669f084787c392b34c83acef5b2099898e24c` — the exact head pushed and tested in isolation (30 PASS).

## 3. Dependency

- Base `release-01/pr-c` — https://github.com/Sohadot/Bisulfid/pull/111; head `release-01/pr-d`.
- Depends on PR-C; must merge after it. Next in the stack: PR-E — https://github.com/Sohadot/Bisulfid/pull/113.
- Release matrix: `main/data/release/RELEASE_01_READINESS.md` on `claude/corpus-distinctiveness-audit-4wsa9f`.

## 4. Files changed

`git diff 092048c069..a65669f084` — 27 files changed, 2494 insertions(+), 51 deletions(-)

<details><summary>File list</summary>

```
M	main/content/en/pages/molybdenum-disulfide.md
M	main/data/distinctiveness/ig_unit_registry.json
M	main/data/knowledge_objects/knowledge_object_registry.json
M	main/data/publication_candidates/PC-MOS2-SCIENTIFIC-001.json
M	main/data/reference_production/previews/bisulfid-vs-bisulfide/index.html
M	main/data/reference_production/previews/molybdenum-disulfide/index.html
A	main/data/release/claim_dossiers/KO-BISULFID-TERMINOLOGY-001.json
A	main/data/release/claim_dossiers/KO-MOS2-SCIENTIFIC-001.json
A	main/data/release/review_packets/KO-BISULFID-TERMINOLOGY-001.md
A	main/data/release/review_packets/KO-MOS2-SCIENTIFIC-001.md
A	main/data/release/reviews/KO-BISULFID-TERMINOLOGY-001.json
A	main/data/release/reviews/KO-MOS2-SCIENTIFIC-001.json
A	main/data/release/source_lock_checklists.json
A	main/data/release/staged/bisulfid-vs-bisulfide/index.html
A	main/data/release/staged/bisulfid-vs-bisulfide/release.json
A	main/data/release/staged/molybdenum-disulfide/index.html
A	main/data/release/staged/molybdenum-disulfide/release.json
M	scripts/governance_scaffolding/reference_production_tests.py
M	scripts/publication/test_publication_authority.py
M	scripts/reference_production/capture_terminology_sources.py
M	scripts/reference_production/render_ko_reference.py
A	scripts/release/apply_release.py
A	scripts/release/build_review_packets.py
M	scripts/release/release_checks.py
M	scripts/release/release_checks_tests.py
A	scripts/release/simulate_release.py
M	scripts/validators/distinctiveness_core.py
```

</details>

Public HTML differences:

No file under `site/public` changes in this PR.

Staged candidate for `/molybdenum-disulfide/` (not applied; `apply_release.py` refuses until Contract C is index-approved):

| | Live | Candidate |
|---|---|---|
| title | Molybdenum Disulfide — Bisulfid Atlas | Molybdenum Disulfide (MoS2): Structure, Polytypes, Lattice |
| robots | index, follow | index, follow |
| canonical | https://bisulfid.com/molybdenum-disulfide/ | https://bisulfid.com/molybdenum-disulfide/ |
| hreflang | 0 | 0 |
| json_ld | none | ChemicalSubstance |
| words | 363 | 1033 |

## 5. Production impact

No public file changes; candidate staged. apply_release.py refuses publication until Contract C is index-approved.

## 6. Isolated test results

Head `a65669f084` checked out ALONE in a clean worktree (not a cumulative run). ⏸️ BLOCKED_BY_KNOWN_DEPENDENCY = red only because of the pre-existing /acquire/ conflict that PR-B resolves.

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
| ✅ PASS | Review packets current | `scripts/release/build_review_packets.py --check` | review packets up to date |
| ✅ PASS | Homepage claim audit current | `scripts/release/build_homepage_claim_audit.py --check` | {'items': 18, 'verified': 14, 'owner_confirmation_required': 2, 'not_a_factual_claim': 2, 'unclassified': 0} |
| ✅ PASS | KO renderer outputs current | `scripts/reference_production/render_ko_reference.py --check` | up to date |
| ✅ PASS | Institutional renderer outputs current | `scripts/reference_production/render_institutional_preview.py --check` | up to date |
| ✅ PASS | SEO previews + internal links | `scripts/reference_production/seo_preview_check.py` | [PASS] Homepage (DE) gate12=PASS words=318 nearest=0.0 |
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
| ✅ PASS | Deploy gate on site/public | `scripts/publication/validate_publication_authority.py --surface site/public` | PUBLICATION AUTHORITY PASS: nothing escalates, nothing new is unauthorized, nothing modified requests index, no discretionary downgrade without an approved deci |
| ✅ PASS | Governance invariants (no approval, signature, lock, activation, certification or ratification) | `inline invariant check` | OK |

GitHub CI: `corpus-governance-ci` runs only on pull requests whose base is `main`; this stacked PR therefore has no CI run. Absence of checks is NOT a pass; the isolated local results above are the record.

## 7. Known blockers

- independent review (chemistry / crystallography) missing
- 8 sources unlocked (4 lack a capture; L6 signatures)
- owner claim activation and release authorization missing
- AMD-IG-R03-001 not ratified

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

git revert; nothing live changes.

Merge condition (for a FUTURE authorization): Can merge after review (staged files only). Merging does not validate, lock, activate or publish.

## 10. Authorization status

**NOT AUTHORIZED TO MERGE OR DEPLOY.** This PR was opened under a review-only authorization. Merging, deploying, publishing, signing reviews, locking sources, activating claims, changing indexation or ratifying governance requires a new explicit owner authorization. Auto-merge is not enabled.
