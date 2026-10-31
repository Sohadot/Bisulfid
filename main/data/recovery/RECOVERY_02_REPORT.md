# Recovery-02: SEO-Safe Migration & Reference Authority Foundation

**Date:** 2026-10-30 · **Branch:** `claude/corpus-distinctiveness-audit-4wsa9f` (Recovery-01 at `1f072f8598`) · **Live surface provenance:** `site/public` last changed at `b1757cb532`; the live homepage was fetched on 2026-10-30 and matches the repository (robots, title).

**Not changed:** live HTML, robots directives, sitemaps, `robots.txt`, routes, release records. Nothing merged or deployed. No noindex, redirect or deletion.

## 0. Recommendation (GO / NO-GO)

| Action | Verdict | Why |
|---|---|---|
| Mass noindex (Recovery-01 Stage 2: 14,032 URLs + 13,998 sitemap entries) | **NO-GO** | Only 79 of the 14,032 are appropriate noindex targets (internal pipeline-status pages). It would noindex all 8 brand/identity surfaces, including `/`. It discards signals on 453 URLs that have a valid canonical destination. It removes every sitemap URL while 0 URLs are approved to replace them. Search Console evidence for these URLs is missing (§2.1). |
| Merge the revised PR-1 (this branch) | **GO, conditional** | Deploys can no longer deadlock: the live surface passes the new deploy gate except for `/acquire/`, a one-URL owner decision (§3). PR-1 changes no served byte. |
| Targeted noindex of 79 pipeline-status pages | **Conditional GO** | Only after the Search Console export confirms no impressions or external links for them. |
| `rel=canonical` consolidation of 453 true duplicates | **Conditional GO** | Head-only and fully reversible. Apply after the Search Console export (Google-selected canonical per URL). |
| Switch sitemaps to approved-only | **NO-GO now** | Approved-only lists 0 URLs today. Switch when the first URLs are Contract-C index_approved. |
| Publish the MoS₂ reference at `/molybdenum-disulfide/` | **NO-GO** | Contract C = (not_public, noindex). Claims are pilot/non-operational, sources are `candidate`, and the IG route re-review is not recorded. The content is ready (§5). |
| Publish the rebuilt homepage | **NO-GO** | Requires a Contract-C R11 certification; Gate 12-I PASS is not enough. The content is ready (§5). |
| Bisulfid/bisulfide boundary page | **NO-GO: BLOCKED_ON_EVIDENCE** | 0 of 5 modules renderable (§5.3). |

## 1. Review of the Recovery-01 PR-1 / PR-2 sequence

| # | Finding | Severity | Resolution in this sprint |
|---|---|---|---|
| 1 | **Deploy deadlock.** Gate 12 hold mode in the deploy workflow fails until mass noindex. With mass noindex not authorized, every future deploy (even a security or typo fix) would fail indefinitely. | blocker | The deploy gate is now `scripts/publication/validate_publication_authority.py`. The live surface passes, with 14,040 pages LEGACY_STATUS_QUO and 1 owner decision. |
| 2 | **Unsafe exception.** The freeze exception was free text in a repository file (anyone with commit rights could "authorize" it), renewable without limit, and it overrode Contract C RL. | high | **Retired** (policy 1.2.0). Code ignores it even when filled in (test `test_freeze_exception_is_retired`). |
| 3 | **Template authority.** `atlas/base.html` hard-coded `index, follow`. Both atlas renderers re-render all 13,998 released routes into `site/public`, so any re-render would re-stamp index on every page. | high | Template uses `{{robots_directive}}`. Both renderers take robots and canonical from the resolver, skip unauthorized pages, refuse unresolved placeholders, and support `--out`. A full staged re-render produced 13,998 pages with robots identical to what was served, 0 escalations and 0 placeholders. |
| 4 | **Repair deadlock.** Hold mode blocked any modified failing legacy page, so incremental repairs were impossible. | medium | A modified legacy page may deploy while it requests no indexation (LEGACY_REPAIR_NOINDEX). Head-only changes (canonical, robots downgrade) keep the body hash, so they never count as modifications. |
| 5 | **Gate 12-I as de-facto indexation authority.** In hold mode, the 8 institutional pages that pass Gate 12-I stayed indexable as PASS. | medium | Gate 12 and 12-I are vetoes only. A non-factual page becomes index-eligible only through a Contract-C R11 certification. The 7 indexable institutional pages stay indexable only as recorded legacy status quo (basis `legacy_status_quo`). |
| 6 | **Stage 2 noindexed brand surfaces** (`/`, `/de/`, `/bisulfid/`, `/what-is-bisulfid/`, …). | high | Rule R-BRAND-1: never noindex brand surfaces; rebuild first. |
| 7 | **noindex used where canonicalization is correct.** | medium | Decision rules (§4) and the per-URL SEO disposition (§2.3). |
| 8 | **Empty sitemaps after Stage 2.** All 13,998 URLs removed with no approved set to replace them. | medium | The sitemap generator has two policies. Approved-only is not deployed until approvals exist. |
| 9 | **Hosting.** GitHub Pages cannot send HTTP 301/308 or 410. | medium | Encoded in R-REDIRECT-1 and R-RETIRE-1. Prefer canonical. Static redirect stubs only for retired URLs, or move hosting if many permanent redirects are needed. |
| 10 | The deploy workflow asserts exactly 14,041 pages, so any registration, retirement or new hub fails the count check. | low | Recorded for PR-3+: replace the fixed count with the authority check, which already detects unapproved removals and unauthorized additions. |
| 11 | The hold ratchet runs only on PRs (`origin/<base>`), not in the deploy job. | low | The deploy job now validates every served directive against the sealed baseline directly. The baseline digest covers path, body hash, robots, sitemap membership and canonical. |

## 2. SEO consequences of Stage 2

### 2.1 Evidence available, and what is missing

**Available:**
- **Search Console snapshot of 2026-07-24** (`SEO_INDEXATION_STRATEGY.md`): 3 pages indexed, 3,369 "discovered – not indexed", 132 "crawled – not indexed", 3 404, 2 noindex, 2 redirects, ~13,998 sitemap URLs.
- **Live fetch, 2026-10-30:** `/` and `/molybdenum-disulfide/` return 200; homepage robots/title equal the repository.
- **Third-party web search API observations, 2026-10-30** (not Google; one query each; no ranks):
  - "bisulfide vs bisulfid meaning" returns Wikipedia/Wiktionary-derived pages.
  - The query "bisulfid.com" did not return the domain.
  - MoS₂ structure queries return arXiv/RSC/PMC/ChemicalBook-type pages.

**Missing.** None of these figures is estimated anywhere in this report:
- which 3 URLs are indexed;
- any impressions, clicks or queries;
- external backlinks;
- index state after July;
- crawl stats;
- manual actions;
- Google-selected canonicals.

**Exact data requirements** (owner-side, Search Console property `bisulfid.com`):
1. **Pages (indexing):** the indexed URL list, plus the URL list for each "not indexed" reason (export is capped at 1,000 rows per reason; use the URL Inspection API beyond that).
2. **Performance:** 16 months, by page and by query (CSV).
3. **Links:** top linked pages (external), top linking sites, top internally linked pages.
4. **Sitemaps:** report status and discovered counts.
5. **URL Inspection API for 263 URLs:** the 8 brand surfaces, the 247 canonical knowledge surfaces, the 7 indexable institutional pages and `/acquire/`. Fields: coverage state, Google-selected canonical, last crawl.
6. **Crawl stats** by response and purpose.
7. **Manual actions and Security issues.**
8. **Optional:** Bing Webmaster Tools.

GitHub Pages provides no server logs. Store the exports under `main/data/seo/` as aggregates.

### 2.2 What Stage 2 would do, by URL class

Source: `seo_url_disposition_summary.json`.

| SEO class | URLs | Stage 2 noindex | Correct treatment |
|---|---|---|---|
| True duplicate, valid canonical destination (same language; destination live, indexable, self-canonical; raw similarity ≥ 0.80) | 453 | 453 | `rel=canonical` to the destination (consolidates signals). Never noindex. |
| Duplicate without a valid destination (raw similarity < 0.80 to destination: canonical likely ignored) | 900 | 900 | Status quo until the destination is rebuilt |
| Needs evidence-backed reconstruction (canonical surface of a curated concept) | 245 | 245 | Status quo, then rebuild in place from a Knowledge Object |
| Independent reference potential (`/molybdenum-disulfide/`, `/de/terminology/molybdenum-disulfide/`) | 2 | 2 | Rebuild in place; promote via Contract C |
| Institutional & navigation (55 Gate-12-I surfaces) | 55 | 46 | Holders: re-render + R11. Duplicate functions: canonical to holder. |
| Internal pipeline-status pages | 79 | 79 | **Targeted noindex** (after data check) |
| Generated entities with unverified identity (931 canonical names + their variants) | 12,289 | 12,289 | Identity review first; then rebuild (entity exists) or retire with its variants |
| Non-route pages with no concept match | 18 | 18 | Register as a route (if it is the better URL) or retire after link review |
| **Total** | **14,041** | **14,032** | appropriate noindex: **79**; inappropriate or premature: **13,953** |

**Measured canonical quality.** Raw (un-masked) similarity of curated-concept variants to their Recovery-01 destination has a median of 0.770, and only 33.5% reach 0.80. Many "variants" are different page types (audience explainer vs term page) of the same concept, so a canonical would likely be ignored.

**Better URLs.** 15 concepts already have a shorter existing URL (e.g. `/pyrite/`, `/zinc-sulfide/`, `/sulfide/`) that has no route record. These should become the canonical routes before consolidation (R-CANON-2).

### 2.3 Risk assessment

- **Index loss.** Bounded today by the 3 indexed URLs, but those 3 are unknown, and the brand surfaces are the most likely candidates. noindex is asymmetric: it is fast to apply and slow to recover from.
- **Link graph.** Long-term noindex tends to be treated as nofollow. Future canonical destinations are mostly linked from the variants Stage 2 would noindex.
- **Crawl budget.** The real benefit of Stage 2, fewer low-value URLs, is mostly delivered by sitemap pruning, canonicalization and targeted noindex, without touching brand or concept surfaces.
- **Quality signals.** About 12,289 pages of combinatorially generated entities (e.g. `cohort04_de_darmstadtium_sulfid`) remain the largest site-quality liability. They are handled by identity review, not blanket noindex.

**Artifacts:**
- `main/data/recovery/seo_url_disposition.jsonl` (14,041 records, proposals only)
- `main/data/recovery/seo_url_disposition_summary.json`

## 3. Contract C, Gate 12, Gate 12-I and the renderer: reconciliation

**Directive authority** (`scripts/publication/publication_authority.py`; first match wins):
1. **Contract C** for URLs bound to a governed object: a KO via a render spec plus publication candidate, or an R11 certification (`main/data/publication/nonfactual_certifications.json`, empty). `index_approved` → `index, follow` + sitemap. `public_noindex` → `noindex, follow`. `not_public` → the legacy page keeps the URL.
2. **Legacy status quo:** the sealed baseline `legacy_surface_hold.json`, 14,041 pages with body hash and the robots, sitemap and canonical as served, sha256-sealed. A page may keep at most these directives.
3. **Release-ledger blocks:** may only downgrade.
4. **Owner-approved per-URL decisions** (`main/data/publication/url_decisions.json`, empty): noindex, `canonical_to` (only to an indexable self-canonical target), `redirect_to`, `retire`. They may only downgrade.
5. **Otherwise:** not authorized to exist.

**Gate 12 and Gate 12-I are vetoes, never grants.** The deploy gate fails a URL whose directives differ from the resolved ones, in any of these cases:

| Case | Gate result |
|---|---|
| index requested where noindex is resolved | BLOCK_DIRECTIVE_ESCALATION |
| sitemap entry not allowed | BLOCK_SITEMAP_ESCALATION |
| canonical differs, or noindex combined with a new cross-URL canonical | BLOCK_CANONICAL_MISMATCH / BLOCK_CANONICAL_CONFLICT |
| page not authorized to exist | BLOCK_UNAUTHORIZED_PAGE |
| modified legacy page requesting index | BLOCK_MODIFIED_INDEXED |
| index-approved page failing Gate 12/12-I | BLOCK_GATE12_VETO |
| legacy URL removed without an approved decision | BLOCK_UNAPPROVED_REMOVAL |

**Named surfaces:**

| Surface | Today | Authority outcome |
|---|---|---|
| `/` homepage | `index, follow`; rendered page fails Gate 12-I (template) | **Status quo index (never noindexed: R-BRAND-1).** Rebuilt preview passes Gate 12-I; indexation authority only via an R11 certification. |
| `/acquire/` | `index, follow`; release ledger `blocked_high_risk`; passes Gate 12-I | **Conflict.** The ledger owns release, so the resolver says noindex. **Owner decision before the first deploy:** authorize the release in the ledger, or serve noindex. This is the only deploy blocker. |
| 7 indexable institutional pages (`/acquire/`, `/atlas/`, `/compounds/`, `/languages/`, `/materials/`, `/methodology/`, `/terminology/`) | `index, follow`; pass Gate 12-I | Indexable only as recorded status quo, not because of Gate 12-I (tested). `/atlas/` and the other five have no route record, so Contract C cannot govern them until they are registered. |
| 41 non-route pages | 39 `index`, 2 `noindex`; no route/ledger record | Status quo; cannot become governed until registered. 16 duplicate a route concept (several are the better short URL); 25 unresolved (German suffix pages, hubs) → register or retire after link review. |
| `routes.json` (14,000 × planned / indexable false) vs live index | conflict | `routes.json` is not a directive authority for legacy pages (Contract C principle: no single legacy file controls indexation). The status quo is the explicit, shrinking debt record: **Contract C RL debt = 14,032 indexed legacy pages failing Gate 12**, printed on every deploy check. |

**Renderer.** `main/templates/atlas/base.html` now carries `{{robots_directive}}`. `atlas_render_dossier_l3.py` and `atlas_render_release_l2.py` call `Authority.render_directives()`, skip pages it refuses, and fail on any leftover placeholder. **Re-rendering cannot reactivate indexation on a held page:** the directive comes from the sealed status quo or a downgrade, and the deploy gate rejects any escalation.

**Sitemaps.** `scripts/publication/generate_sitemaps.py` writes only to a staging directory (it refuses `site/public` without `--authorized-publication`) and re-validates its output:

| Policy | URLs | Validation |
|---|---|---|
| `approved_only` | 0 today | valid, empty |
| `status_quo` | exactly the 13,998 already listed | never adds a URL |

## 4. Canonical / noindex / redirect decision rules

These are in `main/data/publication/url_decision_rules.json`, proposed for ratification.

| Rule | When | Decision |
|---|---|---|
| R-CANON-1 | true duplicate with a valid destination (raw similarity ≥ 0.80, live, indexable, self-canonical) | `canonical_to`; robots unchanged; head-only, reversible |
| R-CANON-2 | the concept has a shorter existing URL | register it as the canonical route first |
| R-HOLD-1 | no valid destination / needs reconstruction / independent potential | status quo |
| R-REBUILD-1 | rebuilt from a KO | same URL; noindex while repairing; indexation only via Contract C |
| R-NOINDEX-1 | internal pipeline status, or an entity disproven by identity review | targeted noindex after Search Console check |
| R-NOINDEX-2 | release ledger blocks a served-index URL | owner decides; resolver enforces noindex meanwhile |
| R-REDIRECT-1 | no independent value + approved destination + links or impressions | static redirect stub (GitHub Pages has no 301); prefer canonical |
| R-RETIRE-1 | disproven entity, no impressions, no external links | 404 (no 410 on GitHub Pages) |
| R-BRAND-1 | brand/identity surfaces | never noindex; rebuild |
| R-SITEMAP-1 | always | only the generator writes sitemaps |

Two further rules hold throughout:
- never combine noindex with a cross-URL canonical;
- never canonicalize to a noindex, redirected or non-self-canonical URL.

## 5. Reference-quality previews

All previews are non-public: robots `noindex`, written outside `site/public`, Contract C not_public. Automated checks are in `SEO_PREVIEW_ASSESSMENT.json`, produced by `scripts/reference_production/seo_preview_check.py`. Gate 12 PASS is necessary but not proof of SEO quality; the checks below cover head, structure, links and intent.

### 5.1 MoS₂ (`/molybdenum-disulfide/`, existing canonical route; no new URL)

**Automated checks.** All pass:
- **Head:** title 58 chars, description 149; one absolute canonical; JSON-LD `ChemicalSubstance` whose `molecularFormula` comes from the PubChem evidence record and whose `sameAs` URLs come from the cited PubChem/NIST source records.
- **Structure:** one h1; no skipped heading level; 591 substantive words.
- **Links:** 7 internal links resolve; 11 external provenance links.
- **Gate 12:** PASS (7/7 IG units).
- **Distinctiveness:** nearest public page S = 0.000; template ratio 0.00.

**Search intents served:** entity lookup ("molybdenum disulfide", "MoS2"), structure ("MoS2 space group", "is MoS2 layered"), polytype comparison ("2H vs 3R MoS2"), lattice parameter.

**Differentiation vs observed competitors:**
- Each value is scoped to its polytype (2H/3R).
- The two lattice determinations are quoted, not averaged.
- The 1923 and 1983 originating studies are separated from the database that serves them.
- The origin of the "2H" label is documented.

The search snapshot itself shows why this matters: compilations give 2H/3R values and also DFT values that differ slightly from the measurements.

**Known gaps, blocked on evidence:** band gap (bulk vs monolayer), density, decomposition behaviour, uses (lubricant, catalysis), safety data, monolayer properties. These are the main intents competitors serve, so this page will be narrow until evidence is admitted.

**Multilingual:** it links to the German terminology record as a separate object. No hreflang is emitted, because that record is not an equivalent page.

**Provenance and E-E-A-T:** a full evidence trail with originating works, records, roles, source-lock status and retrieval dates. No author or credential is claimed, because none is recorded. Publishing an editorial-responsibility statement is an owner decision.

### 5.2 Homepage (`/`)

**Automated checks.** All pass:
- **Head:** title 63, description 143; canonical `/`; JSON-LD `WebSite` (name, url, inLanguage only; no organization or author claims).
- **Structure:** one h1; 254 substantive words.
- **Links:** 10 internal links resolve.
- **Gate 12-I:** PASS (`gateway_home`).
- **Distinctiveness:** nearest public page S = 0.000; template ratio 0.00.

**Content:**
- **States no chemistry or terminology fact.** The name question is presented as a claim pending review, with no assertion that "Bisulfid is the German form". This is tested.
- **Uses computed figures only.** Its two numbers come from the registries at render time (11 admitted MoS₂ evidence records; 4 related terminology claims pending).

**Search intents served:**
- **Brand / navigational.** It routes definition queries to the terminology page.
- **hreflang deferred:** `/de/` is still the legacy template.

**Indexation path:** an R11 certification in `nonfactual_certifications.json`.

### 5.3 Bisulfid / bisulfide boundary (`/bisulfid-vs-bisulfide/`): blocked on evidence

**Artifacts:**
- Plan: `main/data/reference_production/plans/PLAN-BISULFID-BISULFIDE-BOUNDARY.json` (search intents, observed competitors, 5 modules).
- Blockers: `main/data/reference_production/blockers/PLAN-BISULFID-BISULFIDE-BOUNDARY_BLOCKERS.json`.

**Result: 0 of 5 modules renderable.** There are 11 claim bindings, and every one is blocked at the same admission steps:

| Step | Blocker | Count |
|---|---|---|
| 2 | claim `pending_review` | 11 |
| 3 | source only `seeded` (Merriam-Webster, Duden, IUPAC Gold Book/1971, Badger Meter, FH Münster, Uni Rostock, PubChem hydrosulfide) | 14 |
| 4 | no source-use qualification | 12 |
| 5 | no evidence record | 12 |

**Required acquisition work**, in order:
1. Identity-verify each source.
2. Write a use qualification per source.
3. Capture an evidence record with the verbatim passage, locator and retrieval date.
4. Review the claims against admitted evidence.

The German-usage claim rests on a single industry web page (Badger Meter) and also needs an independent second source. No prose was written around the gaps.

## 6. Tests, negative cases, rollback

### Test suites

| Suite | Result |
|---|---|
| `scripts/publication/test_publication_authority.py` (new) | **27/27 PASS** |
| `scripts/validators/test_legacy_migration.py` (freeze exception now proven retired) | **17/17 PASS** |
| `scripts/validators/test_distinctiveness.py` | **23/23 PASS** |
| Contract-C property, IG governance, Pilot 01/02/03, reference production, independence, source admissibility, relationship grammar, `validate_scaffolding`; L0/L1/L2 CI scripts | all PASS |
| `validate_legacy_disposition.py` | 0 violations |
| Renderer `--check` (MoS₂, homepage) | current |

The new suite covers:
- **Resolver precedence:** status quo, unknown page, Gate 12-I never grants, R11 certification (and a proposed certification ignored), Contract C index/noindex/not_public, `/acquire/` downgrade, decisions (downgrade only, proposals ignored, canonical to a noindex target refused, redirect).
- **Surface negatives:**
  - the untouched surface passes (no deadlock);
  - re-activated index blocks; an added sitemap entry blocks; a new noindex page blocks;
  - a modified indexed page blocks, while noindex repair is allowed;
  - noindex plus a new cross-canonical blocks;
  - an unapproved removal blocks; an approved retire passes;
  - an index-approved page failing Gate 12 is vetoed;
  - an applied canonical decision is served correctly.
- **Sitemaps:** approved-only contains exactly the approved URLs; status quo never adds; refuses `site/public`.
- **Renderer:** template has no hard-coded robots; a full renderer run with a substituted authority (unauthorized page not written; downgraded page stays noindex; status-quo home unchanged); placeholder refusal.
- **Previews:** current and noindex; homepage asserts no unapproved claim; homepage numbers come from registries and invented keys are refused; JSON-LD values come from evidence; no hreflang tag; the boundary page is blocked, not written; pilot claims count as unapproved.
- **Mass-noindex tool:** still refuses `site/public`.

### Real-surface runs

| Run | Result |
|---|---|
| Publication authority on `site/public` | 14,040 LEGACY_STATUS_QUO, 1 BLOCK (`/acquire/`), Contract C RL debt 14,032 |
| Full staged re-render | 13,998 pages, robots identical to served, 0 escalations |

### Rollback

| Change | Rollback | Limit |
|---|---|---|
| PR-1 (code, data, templates, workflows) | revert the merge | none: no served byte changes |
| Owner decision on `/acquire/` | flip one robots line or one ledger field back | re-indexing latency if noindexed |
| `rel=canonical` wave | remove the link (head-only; body hash unchanged) | Google re-evaluates on recrawl |
| Targeted noindex (79) | robots back to index | slow re-indexing; hence the Search Console check first |
| Sitemap changes | regenerate | none |
| Redirect stubs / retire | restore the file | crawl history and processed redirects are not instantly recoverable; GitHub Pages has no 301/410 |
| Rebuilt page promotion | Contract C posture regression → resolver returns not_public; legacy page body is sealed in the baseline | none |

## 7. Revised PR and deployment sequence

| PR | Permitted changes | Deployment consequence |
|---|---|---|
| **PR-1 (this branch, revised)** | Gate 12 / 12-I code and tests; publication authority (resolver, deploy gate, sitemap generator); renderer conformance (`atlas/base.html`, two renderers); sealed baseline; registries and dispositions; previews (outside `site/public`); MoS₂ non-public draft; CI and deploy workflows; docs. **No** `site/public`, sitemap, robots, routes or ledger change. | The served site is byte-identical. The next deploy passes once the owner decides `/acquire/`. |
| **PR-2 `/acquire/`** | One of: ledger record → released, or `/acquire/` robots → noindex (+ approved decision) | Clears the only deploy blocker |
| **PR-3 Search Console intake** | Aggregate exports under `main/data/seo/`; re-run `build_seo_disposition.py` with indexed/impression/link flags; protect every URL with impressions or links | none (data only) |
| **PR-4 targeted noindex** | ≤ 79 approved `noindex` decisions (pipeline-status pages) after PR-3 | 79 URLs noindex, out of sitemaps |
| **PR-5 canonical wave 1** | ≤ 453 approved `canonical_to` decisions; head-only re-render via the resolver; register the 15 shorter URLs first where they are better (R-CANON-2) | duplicates consolidate; sitemap drops them |
| **PR-6 homepage** | R11 certification for `/` + deploy the rebuilt homepage | `/` stays indexable; status-quo debt −1 |
| **PR-7 MoS₂ promotion** | Claim activation, validation, governed posture, IG route re-review pair, release authorization (each by its owner); render the preview to `/molybdenum-disulfide/`; remove its baseline entry | `public_noindex` (R9) until sources lock, then index |
| **PR-8 terminology evidence** | Verify/qualify sources and capture evidence for the boundary plan; render when ≥ 3 modules pass | The boundary page joins the Contract C path |
| **PR-9+** | Identity review of the 931 generated entities (retire or rebuild); KO waves (sulfur next: Pilot 01/02 evidence); switch sitemaps to approved-only once approvals exist | The debt shrinks only through governed decisions |

## Exact next production action

The owner decides **`/acquire/`**: authorize its release in `release_ledger.json`, or serve it noindex. The owner also provides the **Search Console exports** listed in §2.1. With those two inputs, PR-1 can merge and deploy without changing any served page, and PR-4/PR-5 can be decided per URL on evidence.
