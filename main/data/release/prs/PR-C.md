# PR-C: English and German homepage release readiness

> **NOT AUTHORIZED TO MERGE OR DEPLOY.** Draft for review only.

## 1. Purpose and exact scope

Forward merge of release-01/pr-b into release-01/pr-c. No history rewritten.

## 2. Verified commit SHA

`b3ca3435782d18679a4af820a339da46d65906b5` — the exact head pushed and tested in isolation (31 PASS, 1 NOT_APPLICABLE).

## 3. Dependency

- Base `release-01/pr-b` — https://github.com/Sohadot/Bisulfid/pull/110; head `release-01/pr-c`.
- Depends on PR-B; must merge after it. Next in the stack: PR-D — https://github.com/Sohadot/Bisulfid/pull/112.
- Release matrix: `main/data/release/RELEASE_01_READINESS.md` on `claude/corpus-distinctiveness-audit-4wsa9f`.

## 4. Files changed

`git diff 84d55e3dab..b3ca343578` — 14 files changed, 646 insertions(+), 39 deletions(-)

<details><summary>File list</summary>

```
M	main/data/publication/nonfactual_certifications.json
M	main/data/reference_production/SEO_PREVIEW_ASSESSMENT.json
M	main/data/reference_production/previews/de/index.html
M	main/data/reference_production/previews/home/index.html
M	main/data/reference_production/render_specs/INST-HOME-DE.json
M	main/data/reference_production/render_specs/INST-HOME-EN.json
A	main/data/release/HOMEPAGE_CLAIM_AUDIT.json
A	main/data/release/staged/de/index.html
A	main/data/release/staged/de/release.json
A	main/data/release/staged/home/index.html
A	main/data/release/staged/home/release.json
M	scripts/publication/test_publication_authority.py
M	scripts/reference_production/render_institutional_preview.py
A	scripts/release/build_homepage_claim_audit.py
```

</details>

Public HTML differences:

No file under `site/public` changes in this PR.

Staged candidate for `/` (not applied; `apply_release.py` refuses until Contract C is index-approved):

| | Live | Candidate |
|---|---|---|
| title | Bisulfid — The Missing Letter — Bisulfid Atlas | BISULFID — Sulfur Chemistry Terms and Evidence-Backed Reference |
| robots | index, follow | index, follow |
| canonical | https://bisulfid.com/ | https://bisulfid.com/ |
| hreflang | 0 | 3 |
| json_ld | none | WebSite |
| words | 339 | 473 |

Staged candidate for `/de/` (not applied; `apply_release.py` refuses until Contract C is index-approved):

| | Live | Candidate |
|---|---|---|
| title | Language gateway sovereign framing — Bisulfid Atlas | BISULFID — Begriffe der Schwefelchemie mit geprüften Belegen |
| robots | index, follow | index, follow |
| canonical | https://bisulfid.com/de/ | https://bisulfid.com/de/ |
| hreflang | 0 | 3 |
| json_ld | none | WebSite |
| words | 339 | 397 |

## 5. Production impact

No public file changes; candidates are staged under main/data/release/staged/.

## 6. Isolated test results

Head `b3ca343578` checked out ALONE in a clean worktree (not a cumulative run). ⏸️ BLOCKED_BY_KNOWN_DEPENDENCY = red only because of the pre-existing /acquire/ conflict that PR-B resolves.

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
| ✅ PASS | /acquire/ correction wording and boundaries | `scripts/publication/test_acquire_page.py` | OK |
| ✅ PASS | Deploy gate on site/public | `scripts/publication/validate_publication_authority.py --surface site/public` | PUBLICATION AUTHORITY PASS: nothing escalates, nothing new is unauthorized, nothing modified requests index, no discretionary downgrade without an approved deci |
| ✅ PASS | /acquire/ identical to PR-B revision 2 (e036e30fb6) | `git diff --quiet e036e30fb6 HEAD -- site/public/acquire/index.html` | identical |
| ✅ PASS | Governance invariants (no approval, signature, lock, activation, certification or ratification) | `inline invariant check` | OK |

GitHub CI: `corpus-governance-ci` runs only on pull requests whose base is `main`; this stacked PR therefore has no CI run. Absence of checks is NOT a pass; the isolated local results above are the record.

## 7. Known blockers

- 2 owner confirmations (who publishes the site, EN + DE)
- R11-HOME-EN-001 / R11-HOME-DE-001 not certified
- must not be published before the PR-D and PR-E pages

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

Merge condition (for a FUTURE authorization): Can merge after review (staged files only). Merging does not certify or publish.

## 10. Authorization status

**NOT AUTHORIZED TO MERGE OR DEPLOY.** This PR was opened under a review-only authorization. Merging, deploying, publishing, signing reviews, locking sources, activating claims, changing indexation or ratifying governance requires a new explicit owner authorization. Auto-merge is not enabled.
