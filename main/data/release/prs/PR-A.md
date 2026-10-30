# PR-A: Publication safety and authority

Commit `a0b9fb71b3` (23 files changed, 1300 insertions(+), 41 deletions(-)). Part of the Release-01 stack; full matrix in `main/data/release/RELEASE_01_READINESS.md`.

## Impact

- Gate: any discretionary robots downgrade or sitemap removal of a legacy page needs an approved,
  signed per-URL decision (BLOCK_UNAPPROVED_DOWNGRADE / _SITEMAP_REMOVAL); only release-ledger and
  Contract-C enforcement are exempt; unsigned or 'proposed' decisions bind nothing
- IG policy 1.1.0: ig_reviewed_route_realization (AMD-IG-R03-001 rev 2). A KO may replace its own
  existing canonical route, never a new or sibling URL. The circular 'no indexable duplicate'
  prerequisite is replaced by 42 non-blocking consolidation obligations (38 MoS2, 4 Bisulfid)
- Authority fails closed: unverified realization, self-declared validation, evidence lock, claim
  activation, release authorization or R11 certification without a signed human record are downgraded
- Release review policy: preparer is never the independent reviewer; L1-L6 source lock checklist
- Tests: 9 downgrade cases, 21 route-realization cases, 18 release-gate cases (positive + adversarial)

## Public HTML differences

No file under `site/public` changes in this PR.

## Files

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

## Merge condition

Safe to merge: changes no public file. After merge the deploy gate stays red only on the pre-existing /acquire/ block until PR-B.

## Rollback

git revert the PR-A merge commit; the gate returns to Recovery-03 behaviour (downgrades unchecked) and the IG policy to 1.0.0.

## Test results — this PR's commit checked out alone

- ✅ `scripts/publication/test_publication_authority.py`
- ✅ `scripts/governance_scaffolding/route_realization_tests.py`
- ✅ `scripts/release/release_checks_tests.py`
- ✅ `scripts/publication/build_consolidation_obligations.py --check`
- – `scripts/release/build_review_packets.py --check`
- ✅ `scripts/reference_production/render_ko_reference.py --check`
- ✅ `scripts/reference_production/render_institutional_preview.py --check`
- ✅ `scripts/governance_scaffolding/validate_scaffolding.py`
- ✅ `scripts/governance_scaffolding/ig_governance_tests.py`
- ✅ `scripts/governance_scaffolding/reference_production_tests.py`
- ✅ `scripts/validators/test_distinctiveness.py`
- ❌ `scripts/publication/validate_publication_authority.py --surface site/public :: PUBLICATION AUTHORITY FAIL: 1 blocking page(s).`

## Test results (whole stack)

- ✅ `scripts/publication/test_publication_authority.py` — OK
- ✅ `scripts/governance_scaffolding/route_realization_tests.py` — RESULT: PASS — route realization holds (positive + adversarial)
- ✅ `scripts/release/release_checks_tests.py` — RESULT: PASS — release gates cannot be self-granted
- ✅ `scripts/publication/build_consolidation_obligations.py --check` — up to date
- ✅ `scripts/release/build_review_packets.py --check` — review packets up to date
- ✅ `scripts/reference_production/render_ko_reference.py --check` — up to date
- ✅ `scripts/reference_production/render_institutional_preview.py --check` — up to date
- ✅ `scripts/reference_production/seo_preview_check.py` — [PASS] Homepage (DE) gate12=PASS words=313 nearest=0.0
- ✅ `scripts/validators/test_distinctiveness.py` — OK
- ✅ `scripts/validators/test_legacy_migration.py` — OK
- ✅ `scripts/validators/validate_distinctiveness.py --gate` — NOTE: no markdown page is currently a publication candidate; every draft remains non-public.
- ✅ `scripts/validators/validate_distinctiveness.py --check-hold --hold-ratchet-ref origin/main` — legacy hold main/data/distinctiveness/legacy_surface_hold.json: 14041 sealed entries, sealed from {'surface': 'site/public', 'commit': 'b1757cb532'}; freeze exception retired (Recovery-02): an unchang
- ✅ `scripts/recovery/validate_legacy_disposition.py` — legacy disposition registry: 14041 records (14000 routes + 41 non-route surfaces); 0 violation(s)
- ✅ `scripts/governance_scaffolding/validate_scaffolding.py` — RESULT: PASS — all scaffolding artifacts valid
- ✅ `scripts/governance_scaffolding/validate_concept_lexeme.py` — RESULT: PASS — concept/lexeme semantic architecture valid
- ✅ `scripts/governance_scaffolding/contract_c_property_tests.py` — RESULT: PASS — all 7 canonical property tests hold
- ✅ `scripts/governance_scaffolding/ig_governance_tests.py` — RESULT: PASS — all IG governance ratification proofs hold
- ✅ `scripts/governance_scaffolding/reference_production_tests.py` — RESULT: PASS — all Reference Production 01 proofs hold
- ✅ `scripts/governance_scaffolding/source_admissibility_tests.py` — RESULT: PASS — all 21 enforcement proofs hold
- ✅ `scripts/corpus_validation_runtime_l1.py` — ============================================================
- ✅ `scripts/source_claim_guardrail_runtime_l1.py` — ============================================================
- ✅ `scripts/corpus_production_runtime_l2.py` — ============================================================
- ✅ `scripts/validate_route_registry_l0.py` — Summary: PASS (0 errors, 120 warnings)
- ✅ `scripts/validate_content_drafts_l0.py` — Summary: PASS (0 errors, 0 warnings)
- ✅ `scripts/publication/validate_publication_authority.py --surface site/public` — PUBLICATION AUTHORITY PASS: nothing escalates, nothing new is unauthorized, nothing modified requests index, no discretionary downgrade without an approved decision.

Not merged and not deployed: awaiting owner authorization.
