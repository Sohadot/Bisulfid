# PR-C: English and German homepage release readiness

Commit `d0dd6cf796` (13 files changed, 548 insertions(+), 37 deletions(-)). Part of the Release-01 stack; full matrix in `main/data/release/RELEASE_01_READINESS.md`.

## Impact

- Release candidates staged (main/data/release/staged/{home,de}/): directives from the publication
  authority, site footer, reciprocal hreflang en/de/x-default; NOT applied to site/public
- Claim audit of every sentence (18 items: 14 verified, 2 owner confirmations, 2 non-factual);
  two overstatements about the legacy corpus narrowed in both languages
- Publication dependencies recorded automatically: the homepages link to the two governed references
  and must not go live before them
- R11-HOME-EN-001 / R11-HOME-DE-001 prepared for owner review (status proposed; checklist attached)
- Gate 12-I PASS for both; SEO preview checks 4/4

Rollback: revert this commit (no live file changed).

## Public HTML differences

No file under `site/public` changes in this PR.

Staged candidate for `/` (applied only later, by `apply_release.py`):

| | Live | Candidate |
|---|---|---|
| title | Bisulfid — The Missing Letter — Bisulfid Atlas | BISULFID — Sulfur Chemistry Terms and Evidence-Backed Reference |
| robots | index, follow | index, follow |
| canonical | https://bisulfid.com/ | https://bisulfid.com/ |
| hreflang | 0 | 3 |
| json_ld | none | WebSite |
| words | 339 | 470 |

Staged candidate for `/de/` (applied only later, by `apply_release.py`):

| | Live | Candidate |
|---|---|---|
| title | Language gateway sovereign framing — Bisulfid Atlas | BISULFID — Begriffe der Schwefelchemie mit geprüften Belegen |
| robots | index, follow | index, follow |
| canonical | https://bisulfid.com/de/ | https://bisulfid.com/de/ |
| hreflang | 0 | 3 |
| json_ld | none | WebSite |
| words | 339 | 392 |

## Files

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
```

## Merge condition

Safe to merge (staged candidates only). PUBLICATION of / and /de/ needs: owner confirmations in HOMEPAGE_CLAIM_AUDIT.json, signed R11 certifications, and PR-D + PR-E pages public first.

## Rollback

git revert; nothing live changed. After a later publication: re-copy the previous index.html from git history and redeploy.

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
