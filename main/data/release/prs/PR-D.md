# PR-D: MoS2 reference release readiness

Commit `a32a0f60b8` (27 files changed, 2489 insertions(+), 50 deletions(-)). Part of the Release-01 stack; full matrix in `main/data/release/RELEASE_01_READINESS.md`.

## Impact

- IG posture ig_reviewed_route_realization (policy 1.1.0 checks pass): the KO replaces the body of
  /molybdenum-disulfide/; no new URL; 38 consolidation obligations recorded
- Claim-by-claim approval dossier and independent-review packet (3 claims, 11 admitted records);
  review record skeleton names the automated preparer, which can never be the reviewer
- Source-lock checklist (L1-L6): COD x2, PubChem, NIST pass L1-L5 (live recapture 2026-10-30 matches
  the 2026-09-20 values); 4 uploaded-excerpt sources lack a capture (L2/L3 pending; RSC HTML 403);
  L6 human sign-off pending for all 8
- Release candidate staged (main/data/release/staged/molybdenum-disulfide/): directives from the
  authority, governance text from signed records only ('independent review not yet performed')
- Fix: IG units are now found for the SERVED HTML (registry served_url). Without it Gate 12 would
  have vetoed the reference on deploy; a legacy body at the same URL still gets 0 valid units
- apply_release.py refuses unless Contract C is index-approved; simulate_release.py rehearses the gate

Rollback: revert this commit (no live file changed).

## Public HTML differences

No file under `site/public` changes in this PR.

Staged candidate for `/molybdenum-disulfide/` (applied only later, by `apply_release.py`):

| | Live | Candidate |
|---|---|---|
| title | Molybdenum Disulfide — Bisulfid Atlas | Molybdenum Disulfide (MoS2): Structure, Polytypes, Lattice |
| robots | index, follow | index, follow |
| canonical | https://bisulfid.com/molybdenum-disulfide/ | https://bisulfid.com/molybdenum-disulfide/ |
| hreflang | 0 | 0 |
| json_ld | none | ChemicalSubstance |
| words | 363 | 1033 |

## Files

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

## Merge condition

Safe to merge (staged candidate only). PUBLICATION needs a signed independent review, 8 source locks, owner claim activation and release authorization; apply_release.py refuses until then.

## Rollback

git revert; nothing live changed. After a later publication: restore the legacy page from git history (same URL, same directives).

## Test results — this PR's commit checked out alone

- ✅ `scripts/publication/test_publication_authority.py`
- ✅ `scripts/governance_scaffolding/route_realization_tests.py`
- ✅ `scripts/release/release_checks_tests.py`
- ✅ `scripts/publication/build_consolidation_obligations.py --check`
- ✅ `scripts/release/build_review_packets.py --check`
- ✅ `scripts/reference_production/render_ko_reference.py --check`
- ✅ `scripts/reference_production/render_institutional_preview.py --check`
- ✅ `scripts/governance_scaffolding/validate_scaffolding.py`
- ✅ `scripts/governance_scaffolding/ig_governance_tests.py`
- ✅ `scripts/governance_scaffolding/reference_production_tests.py`
- ✅ `scripts/validators/test_distinctiveness.py`
- ✅ `scripts/publication/validate_publication_authority.py --surface site/public`

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
