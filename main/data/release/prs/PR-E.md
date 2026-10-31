# PR-E: Bisulfid/Bisulfide terminology reference release readiness

> **NOT AUTHORIZED TO MERGE OR DEPLOY.** Draft for review only.

## 1. Purpose and exact scope

Evidence reuse (nothing re-verified without need):
- L3 dated re-fetch 2026-10-31 (captures/TERMINOLOGY_RECAPTURE_2026-10-31.json): every quoted passage of
  all 11 sources reproduced verbatim; L1-L5 now pass for all 11; L6 human signatures still pending
- Identity, qualification, admission and claim matching reused as recorded in Recovery-03

Reference content (only admitted evidence; no new claim):
- Headings narrowed to their sources (e.g. 'Bisulfid in the DWDS: not among its contemporary lexical
  sources'); summary no longer generalizes from DWDS to German dictionaries; Sulfid/sulfide wording
  no longer says 'the meaning is the same'
- At-a-glance becomes a term map labelled by source type (dictionary, IUPAC, database, lexicon)
- New synthesis section: supported / open / not to be inferred from similar spelling, each item
  bound to KO evidence (renderer refuses foreign evidence or unknown verdicts)
- Per-section evidence links into the evidence trail; re-verification date shown only if every
  cited passage was reproduced; Mᴵ formula display filter
- Meta description, hydrosulfide intent, DefinedTerm disulfide(2-), /sources/ link
- PC distinctiveness review vs the legacy page, the DE page and the 4 cohort02 variants
  (variants pairwise S 0.88-0.90, no knowledge; candidate shares no shingles with any)
- Compact gap report: main/data/release/KO-BISULFID-TERMINOLOGY-001_GAP_REPORT.md
- Tests: scripts/reference_production/test_bisulfid_reference.py (10), wired into CI

MoS2 output byte-identical (all renderer features are opt-in). Route and canonical unchanged.

## 2. Verified commit SHA

`9f9488c478f213dce7f6611c17a4a012d9fb048e` — the exact head pushed and tested in isolation (33 PASS).

## 3. Dependency

- Base `release-01/pr-d` — https://github.com/Sohadot/Bisulfid/pull/112; head `release-01/pr-e`.
- Depends on PR-D; must merge after it.
- Release matrix: `main/data/release/RELEASE_01_READINESS.md` on `claude/corpus-distinctiveness-audit-4wsa9f`.

## 4. Files changed

`git diff 24d9762c1f..9f9488c478` — 17 files changed, 1431 insertions(+), 309 deletions(-)

<details><summary>File list</summary>

```
M	.github/workflows/corpus-governance-ci.yml
M	main/content/en/pages/bisulfid-vs-bisulfide.md
M	main/data/distinctiveness/ig_unit_registry.json
A	main/data/evidence/captures/TERMINOLOGY_RECAPTURE_2026-10-31.json
M	main/data/knowledge_objects/knowledge_object_registry.json
M	main/data/publication_candidates/PC-BISULFID-TERMINOLOGY-001.json
M	main/data/reference_production/SEO_PREVIEW_ASSESSMENT.json
M	main/data/reference_production/previews/bisulfid-vs-bisulfide/index.html
M	main/data/reference_production/render_specs/KO-BISULFID-TERMINOLOGY-001.json
A	main/data/release/KO-BISULFID-TERMINOLOGY-001_GAP_REPORT.md
M	main/data/release/claim_dossiers/KO-BISULFID-TERMINOLOGY-001.json
M	main/data/release/review_packets/KO-BISULFID-TERMINOLOGY-001.md
M	main/data/release/source_lock_checklists.json
M	main/data/release/staged/bisulfid-vs-bisulfide/index.html
M	main/data/release/staged/bisulfid-vs-bisulfide/release.json
M	scripts/reference_production/render_ko_reference.py
A	scripts/reference_production/test_bisulfid_reference.py
```

</details>

Public HTML differences:

No file under `site/public` changes in this PR.

Staged candidate for `/bisulfid-vs-bisulfide/` (not applied; `apply_release.py` refuses until Contract C is index-approved):

| | Live | Candidate |
|---|---|---|
| title | Bisulfid vs. Bisulfide — Bisulfid Atlas | Bisulfid vs Bisulfide: Meanings, IUPAC Names, German Usage |
| robots | index, follow | index, follow |
| canonical | https://bisulfid.com/bisulfid-vs-bisulfide/ | https://bisulfid.com/bisulfid-vs-bisulfide/ |
| hreflang | 0 | 0 |
| json_ld | none | DefinedTermSet |
| words | 344 | 1376 |

## 5. Production impact

No public file changes; candidate staged.

## 6. Isolated test results

Head `9f9488c478` checked out ALONE in a clean worktree (not a cumulative run). ⏸️ BLOCKED_BY_KNOWN_DEPENDENCY = red only because of the pre-existing /acquire/ conflict that PR-B resolves.

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
| ✅ PASS | /acquire/ correction wording and boundaries | `scripts/publication/test_acquire_page.py` | OK |
| ✅ PASS | Bisulfid/Bisulfide reference precision, synthesis, evidence navigation | `scripts/reference_production/test_bisulfid_reference.py` | OK |
| ✅ PASS | Deploy gate on site/public | `scripts/publication/validate_publication_authority.py --surface site/public` | PUBLICATION AUTHORITY PASS: nothing escalates, nothing new is unauthorized, nothing modified requests index, no discretionary downgrade without an approved deci |
| ✅ PASS | /acquire/ identical to PR-B revision 2 (e036e30fb6) | `git diff --quiet e036e30fb6 HEAD -- site/public/acquire/index.html` | identical |
| ✅ PASS | Governance invariants (no approval, signature, lock, activation, certification or ratification) | `inline invariant check` | OK |

GitHub CI: `corpus-governance-ci` runs only on pull requests whose base is `main`; this stacked PR therefore has no CI run. Absence of checks is NOT a pass; the isolated local results above are the record.

## 7. Known blockers

- independent review (nomenclature / lexicography, EN + DE) missing
- 11 sources unlocked (L3 re-capture on a later date; L6 signatures)
- owner claim activation and release authorization missing
- AMD-IG-R03-001 not ratified
- CLM-TERM-BISULFID-001 stays pending by design

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

Merge condition (for a FUTURE authorization): Can merge after review (staged files only).

## 10. Authorization status

**NOT AUTHORIZED TO MERGE OR DEPLOY.** This PR was opened under a review-only authorization. Merging, deploying, publishing, signing reviews, locking sources, activating claims, changing indexation or ratifying governance requires a new explicit owner authorization. Auto-merge is not enabled.
