# PR-B: /acquire/ correction

> **NOT AUTHORIZED TO MERGE OR DEPLOY.** Draft for review only.

## 1. Purpose and exact scope

Owner decision (recorded, not signed): /acquire/ is a commercial access page and stays
'noindex, follow' and out of every sitemap indefinitely, independent of release status.

- main/data/publication/indexing_policies.json: per-URL indexing ceilings; separates access,
  publication and indexing. Only page_class commercial_access; refused for any KO-bound route
- publication_authority.resolve(): ceiling applied last; only lowers (noindex + no sitemap); never
  changes access or canonical; no ledger release, URL decision, Contract C or R11 can lift it
- deploy gate: policy-enforced downgrade is a named enforcement exception (like the ledger)
- url_decisions.json: the ledger-based lift condition is superseded; the record stays proposed
  and unsigned and now states exactly what the owner's signature approves
- 7 regression tests (future ledger release, R11/Contract C, refused ceilings, no other URL
  changes, sitemaps, robots.txt); DECISION_LOG entry. Contract C unchanged.

## 2. Verified commit SHA

`84d55e3dab73082cbc71b73b4cc83d589676bf22` — the exact head pushed and tested in isolation (30 PASS, 2 NOT_APPLICABLE).

## 3. Dependency

- Base `release-01/pr-a` — https://github.com/Sohadot/Bisulfid/pull/109; head `release-01/pr-b`.
- Depends on PR-A; must merge after it. Next in the stack: PR-C — https://github.com/Sohadot/Bisulfid/pull/111.
- Release matrix: `main/data/release/RELEASE_01_READINESS.md` on `claude/corpus-distinctiveness-audit-4wsa9f`.

## 4. Files changed

`git diff d1da411bcb..84d55e3dab` — 14 files changed, 362 insertions(+), 258 deletions(-)

<details><summary>File list</summary>

```
M	.github/workflows/corpus-governance-ci.yml
M	DECISION_LOG.md
A	main/data/publication/indexing_policies.json
M	main/data/publication/url_decisions.json
M	main/data/recovery/ACQUIRE_FACTUAL_CLAIM_REVIEW.json
D	main/data/recovery/staged/acquire.patch
D	main/data/recovery/staged/acquire/index.html
M	main/data/reference_production/SEO_PREVIEW_ASSESSMENT.json
M	scripts/publication/publication_authority.py
A	scripts/publication/test_acquire_page.py
M	scripts/publication/test_publication_authority.py
M	scripts/publication/validate_publication_authority.py
D	scripts/recovery/stage_acquire_proposal.py
M	site/public/acquire/index.html
```

</details>

Public HTML differences:

```diff
diff --git a/site/public/acquire/index.html b/site/public/acquire/index.html
index 8e64111efa..083cc19f31 100644
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
@@ -42,15 +42,29 @@
         bisulfid.com is not a domain-for-sale listing. It is a strategic reference asset
         available for acquisition by a principal whose intended use is aligned with the
         asset&rsquo;s architecture: sovereign sulfur terminology, German/English nomenclature
-        boundary, and governed multilingual reference.
+        boundary, and a governed multilingual reference in development.
       </p>
 
       <h2>What the Asset Is</h2>
       <p>
-        bisulfid.com holds the German-form spelling of a chemically and industrially
-        relevant compound class. The domain sits at a documented nomenclature boundary:
-        the point where German chemical naming conventions diverge from English ones.
-        That position is not accidental &mdash; it is the structural thesis of the asset.
+        bisulfid.com uses the spelling Bisulfid. Whether it is simply the German form of
+        the English word bisulfide is not established by the sources examined so far. In
+        English, the Merriam-Webster dictionary defines bisulfide as disulfide, while the
+        PubChem database lists bisulfide as a synonym for the hydrosulfide ion (HS&minus;).
+        In German, the DWDS (Digitales W&ouml;rterbuch der deutschen Sprache) reports that
+        Bisulfid is not among its contemporary lexical sources; this describes that one
+        dictionary, not every German dictionary or technical text.
+      </p>
+      <p>
+        In German inorganic nomenclature the name of the negatively charged partner of a
+        binary compound ends in -id where English uses -ide, as in Sulfid and sulfide; a German
+        university teaching text on nomenclature states this rule. The domain name uses that
+        spelling pattern. The pattern explains the form of the name, but it does not by itself
+        establish Bisulfid as the standardized German equivalent of bisulfide.
+      </p>
+      <p>
+        A sourced terminology reference on these questions is being prepared. It has not been
+        published yet, and this page does not depend on its conclusions.
       </p>
       <p>
         The asset is available in its entirety. The domain, the content framework,
@@ -62,8 +76,7 @@
 
       <h3>The Domain</h3>
       <p>
-        bisulfid.com &mdash; the German-form spelling of a compound at the intersection
-        of industrial chemistry, multilingual nomenclature, and search intent.
+        bisulfid.com &mdash; the domain and the reference project built on it.
       </p>
 
       <h3>Reference Architecture</h3>
@@ -74,13 +87,15 @@
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
@@ -96,8 +111,9 @@
 
       <h3>Source Governance Framework</h3>
       <p>
-        The machinery ensuring no claim reaches a public page without a traceable,
-        verified source. Built in from the ground up. Full description at
+        A source-governance framework that new reference pages must pass before release:
+        each statement is traced to an admitted, cited source. Most pages published before
+        the framework was introduced are being reviewed or rebuilt under it. Full description at
         <a href="/sources/">Source Discipline</a>.
       </p>
 
@@ -123,8 +139,8 @@
 
       <h2>Related Atlas Pages</h2>
       <ul>
-        <li><a href="/what-is-bisulfid/">What is Bisulfid?</a> &mdash; The compound, the term, and the domain thesis</li>
-        <li><a href="/bisulfid-vs-bisulfide/">Bisulfid vs Bisulfide</a> &mdash; The spelling boundary that defines the asset</li>
+        <li><a href="/what-is-bisulfid/">What is Bisulfid?</a> &mdash; The term and the domain</li>
+        <li><a href="/bisulfid-vs-bisulfide/">Bisulfid vs Bisulfide</a> &mdash; Terminology page (a sourced revision is in preparation and not yet published)</li>
         <li><a href="/languages/">Language Boundary</a> &mdash; The multilingual architecture</li>
         <li><a href="/sources/">Source Discipline</a> &mdash; The governance framework included in the asset</li>
       </ul>
```

## 5. Production impact

Changes ONE public page once deployed: /acquire/ becomes 'noindex, follow' (still public, same URL, contact and links unchanged) and five unsupported or contradicted statements are replaced. Deployment remains a separate manual step.

## 6. Isolated test results

Head `84d55e3dab` checked out ALONE in a clean worktree (not a cumulative run). ⏸️ BLOCKED_BY_KNOWN_DEPENDENCY = red only because of the pre-existing /acquire/ conflict that PR-B resolves.

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
| ✅ PASS | /acquire/ correction wording and boundaries | `scripts/publication/test_acquire_page.py` | OK |
| ✅ PASS | Deploy gate on site/public | `scripts/publication/validate_publication_authority.py --surface site/public` | PUBLICATION AUTHORITY PASS: nothing escalates, nothing new is unauthorized, nothing modified requests index, no discretionary downgrade without an approved deci |
| ✅ PASS | /acquire/ identical to PR-B revision 2 (e036e30fb6) | `git diff --quiet e036e30fb6 HEAD -- site/public/acquire/index.html` | identical |
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
