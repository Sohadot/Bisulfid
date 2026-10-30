# PR-E: Bisulfid/Bisulfide terminology reference release readiness

Commit `6a9110f62b` (4 files changed, 26 insertions(+), 19 deletions(-)). Part of the Release-01 stack; full matrix in `main/data/release/RELEASE_01_READINESS.md`.

## Impact

- IG posture ig_reviewed_route_realization (checks pass): replaces the body of /bisulfid-vs-bisulfide/;
  no new URL; 4 cohort02 variants carry consolidation obligations; /de/bisulfid-vs-bisulfide/ is not
  treated as a localization (no hreflang)
- Claim-by-claim dossier + independent-review packet for 11 narrowly approved claims (15 admitted
  records + 2 boundary records); the industry-usage claim stays pending and is not rendered as support
- Source-lock checklist: 11 sources pass L1/L2/L4/L5; L3 needs a re-capture on a later date
  (capture_terminology_sources.py --recapture); L6 human sign-off pending
- Release candidate staged; governance text from signed records only

Rollback: revert this commit (no live file changed).

## Public HTML differences

No file under `site/public` changes in this PR.

Staged candidate for `/bisulfid-vs-bisulfide/` (applied only later, by `apply_release.py`):

| | Live | Candidate |
|---|---|---|
| title | Bisulfid vs. Bisulfide — Bisulfid Atlas | Bisulfid vs Bisulfide: Meanings, IUPAC Names, German Usage |
| robots | index, follow | index, follow |
| canonical | https://bisulfid.com/bisulfid-vs-bisulfide/ | https://bisulfid.com/bisulfid-vs-bisulfide/ |
| hreflang | 0 | 0 |
| json_ld | none | DefinedTermSet |
| words | 344 | 1376 |

## Files

```
M	main/content/en/pages/bisulfid-vs-bisulfide.md
M	main/data/knowledge_objects/knowledge_object_registry.json
M	main/data/publication_candidates/PC-BISULFID-TERMINOLOGY-001.json
M	main/data/release/staged/bisulfid-vs-bisulfide/release.json
```

## Merge condition

Safe to merge (staged candidate only). PUBLICATION needs a signed independent review, 11 source locks (L3 re-capture first), owner claim activation and release authorization.

## Rollback

git revert; nothing live changed. After a later publication: restore the legacy page from git history.

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
