# PR-B: /acquire/ correction

Commit `3e7b28c0e6` (7 files changed, 45 insertions(+), 245 deletions(-)). Part of the Release-01 stack; full matrix in `main/data/release/RELEASE_01_READINESS.md`.

## Impact

- robots 'index, follow' -> 'noindex, follow' (release-ledger enforcement; ledger unchanged)
- AQ-1..AQ-5 replaced with statements supported by the Recovery-03 evidence and site data;
  two link labels that repeated AQ-1 reworded
- Public access, canonical, mailto contact and all 18 link targets unchanged
- Deploy gate on site/public: PASS (14040 LEGACY_STATUS_QUO + 1 LEGACY_REPAIR_NOINDEX)
- Staging script and staged copies retired; tests now check the applied page

Rollback: git revert this commit (restores the previous page byte-for-byte).

## Public HTML differences

```diff
diff --git a/site/public/acquire/index.html b/site/public/acquire/index.html
index 8e64111efa..511b1ab9cc 100644
--- a/site/public/acquire/index.html
+++ b/site/public/acquire/index.html
@@ -5,7 +5,7 @@
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Acquire bisulfid.com — Strategic Reference Asset Acquisition | bisulfid.com</title>
 <meta name="description" content="bisulfid.com is a strategic reference asset available for acquisition by an aligned principal. The domain, governed content framework, terminology ontology, multilingual architecture, and source governance layer are available as a whole.">
-<meta name="robots" content="index, follow">
+<meta name="robots" content="noindex, follow">
 <link rel="canonical" href="https://bisulfid.com/acquire/">
 <link rel="stylesheet" href="/assets/bisulfid-design-system/bisulfid-frame.css">
 <link rel="stylesheet" href="/assets/bisulfid-design-system/public-surface.css">
@@ -47,10 +47,15 @@
 
       <h2>What the Asset Is</h2>
       <p>
-        bisulfid.com holds the German-form spelling of a chemically and industrially
-        relevant compound class. The domain sits at a documented nomenclature boundary:
-        the point where German chemical naming conventions diverge from English ones.
-        That position is not accidental &mdash; it is the structural thesis of the asset.
+        bisulfid.com uses the spelling Bisulfid. Whether it is simply the German form of
+        the English word bisulfide is not established: English dictionaries and chemical
+        databases attach the word bisulfide to more than one species, and general German
+        dictionaries do not record Bisulfid. BISULFID documents that question with sources
+        rather than assuming an answer.
+      </p>
+      <p>
+        German chemical names end in -id where English names end in -ide (Sulfid, sulfide).
+        The domain name follows the German spelling convention, and that choice is deliberate.
       </p>
       <p>
         The asset is available in its entirety. The domain, the content framework,
@@ -62,8 +67,7 @@
 
       <h3>The Domain</h3>
       <p>
-        bisulfid.com &mdash; the German-form spelling of a compound at the intersection
-        of industrial chemistry, multilingual nomenclature, and search intent.
+        bisulfid.com &mdash; the domain and the reference project built on it.
       </p>
 
       <h3>Reference Architecture</h3>
@@ -74,13 +78,15 @@
       </p>
 
       <h3>Multilingual Structure</h3>
-      <p>Seven-language architecture with distinct strategic roles:</p>
+      <p>The site is currently published in two languages:</p>
       <ul>
         <li><strong>English</strong> &mdash; source layer and canonical term definitions</li>
-        <li><strong>German</strong> &mdash; identity layer (nomenclature origin of the domain name)</li>
-        <li><strong>Arabic</strong> &mdash; market-chain coverage layer</li>
-        <li><strong>Chinese, Japanese, French, Spanish</strong> &mdash; extended multilingual coverage layers</li>
+        <li><strong>German</strong> &mdash; the language whose spelling convention the domain name follows</li>
       </ul>
+      <p>
+        Further languages (Arabic, Chinese, Japanese, French, Spanish) are planned and are
+        not yet published.
+      </p>
       <p>
         The language architecture is explored further at <a href="/languages/">Language Boundary</a>.
       </p>
@@ -96,8 +102,9 @@
 
       <h3>Source Governance Framework</h3>
       <p>
-        The machinery ensuring no claim reaches a public page without a traceable,
-        verified source. Built in from the ground up. Full description at
+        A source-governance framework that new reference pages must pass before release:
+        each statement is traced to an admitted, cited source. Most pages published before
+        the framework was introduced are being reviewed or rebuilt under it. Full description at
         <a href="/sources/">Source Discipline</a>.
       </p>
 
@@ -123,8 +130,8 @@
 
       <h2>Related Atlas Pages</h2>
       <ul>
-        <li><a href="/what-is-bisulfid/">What is Bisulfid?</a> &mdash; The compound, the term, and the domain thesis</li>
-        <li><a href="/bisulfid-vs-bisulfide/">Bisulfid vs Bisulfide</a> &mdash; The spelling boundary that defines the asset</li>
+        <li><a href="/what-is-bisulfid/">What is Bisulfid?</a> &mdash; The term and the domain</li>
+        <li><a href="/bisulfid-vs-bisulfide/">Bisulfid vs Bisulfide</a> &mdash; How the two spellings relate</li>
         <li><a href="/languages/">Language Boundary</a> &mdash; The multilingual architecture</li>
         <li><a href="/sources/">Source Discipline</a> &mdash; The governance framework included in the asset</li>
       </ul>

```

## Files

```
M	main/data/publication/url_decisions.json
M	main/data/recovery/ACQUIRE_FACTUAL_CLAIM_REVIEW.json
D	main/data/recovery/staged/acquire.patch
D	main/data/recovery/staged/acquire/index.html
M	scripts/publication/test_publication_authority.py
D	scripts/recovery/stage_acquire_proposal.py
M	site/public/acquire/index.html
```

## Merge condition

Merge after the owner signs URL-DEC-R03-ACQUIRE-001 (approved_by + approved_on). The gate already passes through the release-ledger exception; the signature is the owner's approval of the wording.

## Rollback

git revert the PR-B merge commit and redeploy: restores the previous page byte-for-byte (robots index, original text).

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
