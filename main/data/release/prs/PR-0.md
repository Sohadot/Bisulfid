# PR-0: Recovery-01..03 governance foundation

> **NOT AUTHORIZED TO MERGE OR DEPLOY.** Draft for review only.

## 1. Purpose and exact scope

Recovery-01..03 foundation: Gate 12 distinctiveness gate + corpus audit; legacy disposition registry and sealed legacy hold; publication authority (single directive resolver) and deploy gate; MoS2 reference reconstruction; terminology evidence admission (16 records, 11 narrow claims) and the Bisulfid/bisulfide preview; homepage previews; indexation-reduction plan (proposals only). Reports: main/data/recovery/RECOVERY_01_REPORT.md, RECOVERY_02_REPORT.md, RECOVERY_03_REPORT.md.

## 2. Verified commit SHA

`4d85bb652035e6ac0608f6506ce7b049f2585fff` — the exact head pushed and tested in isolation (24 PASS, 1 BLOCKED_BY_KNOWN_DEPENDENCY, 5 NOT_APPLICABLE).

## 3. Dependency

- Base `main`; head `release-01/pr-0`.
- Depends on main; must merge after it. Next in the stack: PR-A — https://github.com/Sohadot/Bisulfid/pull/109.
- Release matrix: `main/data/release/RELEASE_01_READINESS.md` on `claude/corpus-distinctiveness-audit-4wsa9f`.

## 4. Files changed

`git diff 37bce9468d..4d85bb6520` — 98 files changed, 90067 insertions(+), 375 deletions(-)

<details><summary>File list</summary>

```
M	.github/workflows/corpus-governance-ci.yml
M	.github/workflows/pages-public-deploy.yml
M	DECISION_LOG.md
M	doctrine/QUALITY_GATE.md
M	main/content/en/pages/bisulfid-vs-bisulfide.md
M	main/content/en/pages/molybdenum-disulfide.md
M	main/data/claims/science_claims.json
M	main/data/claims/terminology_claims.json
A	main/data/distinctiveness/CORPUS_DISTINCTIVENESS_AUDIT.json
A	main/data/distinctiveness/CORPUS_DISTINCTIVENESS_AUDIT.md
A	main/data/distinctiveness/CORPUS_DISTINCTIVENESS_PAGES.tsv
A	main/data/distinctiveness/gate12_policy.json
A	main/data/distinctiveness/ig_unit_registry.json
A	main/data/distinctiveness/institutional_surface_registry.json
A	main/data/distinctiveness/legacy_surface_hold.json
A	main/data/evidence/EVD-TERM-BADGER-BISULFID-USAGE.json
A	main/data/evidence/EVD-TERM-DUDEN-SULFID.json
A	main/data/evidence/EVD-TERM-DWDS-BISULFID.json
A	main/data/evidence/EVD-TERM-DWDS-HYDROGENSULFID.json
A	main/data/evidence/EVD-TERM-DWDS-SULFID.json
A	main/data/evidence/EVD-TERM-FHM-ID-RULE.json
A	main/data/evidence/EVD-TERM-IUPAC-HS-NAMES.json
A	main/data/evidence/EVD-TERM-IUPAC-HSO3-NAME.json
A	main/data/evidence/EVD-TERM-IUPAC-S2-NAMES.json
A	main/data/evidence/EVD-TERM-MW-BISULFIDE.json
A	main/data/evidence/EVD-TERM-MW-BISULFITE.json
A	main/data/evidence/EVD-TERM-MW-DISULFIDE.json
A	main/data/evidence/EVD-TERM-MW-SULFIDE.json
A	main/data/evidence/EVD-TERM-PUBCHEM-BISULFITE.json
A	main/data/evidence/EVD-TERM-PUBCHEM-HS-SYNONYMS.json
A	main/data/evidence/EVD-TERM-SPEKTRUM-HYDROGENSULFIDE.json
A	main/data/evidence/captures/R03_MOS2_RECAPTURE.json
A	main/data/evidence/captures/R03_TERMINOLOGY_CAPTURES.json
M	main/data/information_gain/calibration_pairs.json
A	main/data/information_gain/ig_amendment_proposals.json
M	main/data/knowledge_objects/knowledge_object_registry.json
M	main/data/lexeme_registry.json
M	main/data/ontology/sulfur_terms.json
M	main/data/ontology_node_roles.json
A	main/data/publication/nonfactual_certifications.json
A	main/data/publication/url_decision_rules.json
A	main/data/publication/url_decisions.json
A	main/data/publication_candidates/PC-BISULFID-TERMINOLOGY-001.json
A	main/data/recovery/ACQUIRE_FACTUAL_CLAIM_REVIEW.json
A	main/data/recovery/R03_IDENTITY_SCREEN.json
A	main/data/recovery/R03_INDEXATION_REDUCTION_PLAN.json
A	main/data/recovery/RECOVERY_01_REPORT.md
A	main/data/recovery/RECOVERY_02_REPORT.md
A	main/data/recovery/RECOVERY_03_REPORT.md
A	main/data/recovery/legacy_disposition_registry.jsonl
A	main/data/recovery/legacy_disposition_summary.json
A	main/data/recovery/seo_url_disposition.jsonl
A	main/data/recovery/seo_url_disposition_summary.json
A	main/data/recovery/staged/acquire.patch
A	main/data/recovery/staged/acquire/index.html
A	main/data/reference_production/MOS2_RELEASE_READINESS.json
A	main/data/reference_production/SEO_PREVIEW_ASSESSMENT.json
A	main/data/reference_production/blockers/PLAN-BISULFID-BISULFIDE-BOUNDARY_BLOCKERS.json
A	main/data/reference_production/plans/PLAN-BISULFID-BISULFIDE-BOUNDARY.json
A	main/data/reference_production/previews/bisulfid-vs-bisulfide/index.html
A	main/data/reference_production/previews/de/index.html
A	main/data/reference_production/previews/home/index.html
A	main/data/reference_production/previews/molybdenum-disulfide/index.html
A	main/data/reference_production/render_specs/INST-HOME-DE.json
A	main/data/reference_production/render_specs/INST-HOME-EN.json
A	main/data/reference_production/render_specs/KO-BISULFID-TERMINOLOGY-001.json
A	main/data/reference_production/render_specs/KO-MOS2-SCIENTIFIC-001.json
M	main/data/source_use_qualification_registry.json
M	main/data/sources/source_registry.json
M	main/templates/atlas/base.html
M	scripts/atlas_render_dossier_l3.py
M	scripts/atlas_render_release_l2.py
A	scripts/governance_scaffolding/recovery03_terminology_admission.py
M	scripts/governance_scaffolding/validate_scaffolding.py
A	scripts/publication/generate_sitemaps.py
A	scripts/publication/publication_authority.py
A	scripts/publication/test_publication_authority.py
A	scripts/publication/validate_publication_authority.py
A	scripts/recovery/build_legacy_disposition.py
A	scripts/recovery/build_seo_disposition.py
A	scripts/recovery/screen_generated_identities.py
A	scripts/recovery/stage2_legacy_noindex.py
A	scripts/recovery/stage_acquire_proposal.py
A	scripts/recovery/validate_legacy_disposition.py
A	scripts/reference_production/capture_terminology_sources.py
A	scripts/reference_production/evidence_blockers.py
A	scripts/reference_production/recapture_mos2_values.py
A	scripts/reference_production/render_institutional_preview.py
A	scripts/reference_production/render_ko_reference.py
A	scripts/reference_production/seo_preview_check.py
M	scripts/validators/README.md
A	scripts/validators/distinctiveness_core.py
A	scripts/validators/test_distinctiveness.py
A	scripts/validators/test_legacy_migration.py
M	scripts/validators/validate_all.py
M	scripts/validators/validate_content.py
A	scripts/validators/validate_distinctiveness.py
M	scripts/validators/validate_seo.py
```

</details>

Public HTML differences:

No file under `site/public` changes in this PR.

## 5. Production impact

No file under site/public changes. Adds the publication-authority deploy gate to the MANUAL Pages workflow and the governance suites to CI. After merge a manual deploy fails closed on the pre-existing /acquire/ conflict until PR-B; nothing is deployed automatically (the deploy workflow is workflow_dispatch only).

## 6. Isolated test results

Head `4d85bb6520` checked out ALONE in a clean worktree (not a cumulative run). ⏸️ BLOCKED_BY_KNOWN_DEPENDENCY = red only because of the pre-existing /acquire/ conflict that PR-B resolves.

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
| – NOT_APPLICABLE | IG route-realization safeguards | `scripts/governance_scaffolding/route_realization_tests.py` | tool not present at this commit |
| – NOT_APPLICABLE | Consolidation obligations current | `scripts/publication/build_consolidation_obligations.py --check` | tool not present at this commit |
| – NOT_APPLICABLE | Human review + source-lock safeguards / fail-closed | `scripts/release/release_checks_tests.py` | tool not present at this commit |
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

GitHub CI: `corpus-governance-ci` runs only on pull requests whose base is `main` — it runs on this PR.

## 7. Known blockers

- none for review; it is the base every Release-01 PR depends on

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

git revert the merge commit; site/public is unaffected either way.

Merge condition (for a FUTURE authorization): Can merge after review: it changes no public file. Merging it does not ratify, sign or publish anything.

## 10. Authorization status

**NOT AUTHORIZED TO MERGE OR DEPLOY.** This PR was opened under a review-only authorization. Merging, deploying, publishing, signing reviews, locking sources, activating claims, changing indexation or ratifying governance requires a new explicit owner authorization. Auto-merge is not enabled.
