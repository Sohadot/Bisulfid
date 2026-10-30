# PR-B: /acquire/ correction

> **NOT AUTHORIZED TO MERGE OR DEPLOY.** Draft for review only.

## 1. Purpose and exact scope

- robots 'index, follow' -> 'noindex, follow' (release-ledger enforcement; ledger unchanged)
- AQ-1..AQ-5 replaced with statements supported by the Recovery-03 evidence and site data;
  two link labels that repeated AQ-1 reworded
- Public access, canonical, mailto contact and all 18 link targets unchanged
- Deploy gate on site/public: PASS (14040 LEGACY_STATUS_QUO + 1 LEGACY_REPAIR_NOINDEX)
- Staging script and staged copies retired; tests now check the applied page

Rollback: git revert this commit (restores the previous page byte-for-byte).

## 2. Verified commit SHA

`326a2fa8ca22c39421d3fe6eb04d792aab1fad4b` — the exact head pushed and tested in isolation (28 PASS, 2 NOT_APPLICABLE).

## 3. Dependency

- Base `release-01/pr-a` — https://github.com/Sohadot/Bisulfid/pull/109; head `release-01/pr-b`.
- Depends on PR-A; must merge after it. Next in the stack: PR-C — https://github.com/Sohadot/Bisulfid/pull/111.
- Release matrix: `main/data/release/RELEASE_01_READINESS.md` on `claude/corpus-distinctiveness-audit-4wsa9f`.

## 4. Files changed

`git diff d1da411bcb..326a2fa8ca` — 7 files changed, 45 insertions(+), 245 deletions(-)

<details><summary>File list</summary>

```
M	main/data/publication/url_decisions.json
M	main/data/recovery/ACQUIRE_FACTUAL_CLAIM_REVIEW.json
D	main/data/recovery/staged/acquire.patch
D	main/data/recovery/staged/acquire/index.html
M	scripts/publication/test_publication_authority.py
D	scripts/recovery/stage_acquire_proposal.py
M	site/public/acquire/index.html
```

</details>

Public HTML differences:

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

## 5. Production impact

Changes ONE public page once deployed: /acquire/ becomes 'noindex, follow' (still public, same URL, contact and links unchanged) and five unsupported or contradicted statements are replaced. Deployment remains a separate manual step.

## 6. Isolated test results

Head `326a2fa8ca` checked out ALONE in a clean worktree (not a cumulative run). ⏸️ BLOCKED_BY_KNOWN_DEPENDENCY = red only because of the pre-existing /acquire/ conflict that PR-B resolves.

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
| ✅ PASS | Deploy gate on site/public | `scripts/publication/validate_publication_authority.py --surface site/public` | PUBLICATION AUTHORITY PASS: nothing escalates, nothing new is unauthorized, nothing modified requests index, no discretionary downgrade without an approved deci |
| ✅ PASS | Governance invariants (no approval, signature, lock, activation, certification or ratification) | `inline invariant check` | OK |

GitHub CI: `corpus-governance-ci` runs only on pull requests whose base is `main`; this stacked PR therefore has no CI run. Absence of checks is NOT a pass; the isolated local results above are the record.

## 7. Known blockers

- URL-DEC-R03-ACQUIRE-001 is 'proposed': the owner must review the wording and sign it (approved_by, approved_on); no signature is generated

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

git revert the merge commit and redeploy: restores the previous page byte-for-byte.

Merge condition (for a FUTURE authorization): Merge only after the owner signs URL-DEC-R03-ACQUIRE-001. The gate passes through the release-ledger exception, but the signature is the owner's approval.

## 10. Authorization status

**NOT AUTHORIZED TO MERGE OR DEPLOY.** This PR was opened under a review-only authorization. Merging, deploying, publishing, signing reviews, locking sources, activating claims, changing indexation or ratifying governance requires a new explicit owner authorization. Auto-merge is not enabled.
