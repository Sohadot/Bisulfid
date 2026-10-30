# Recovery-01: Legacy Corpus Recovery & Reference Production

**Date:** 2026-10-30 · **Branch:** `claude/corpus-distinctiveness-audit-4wsa9f` · **Baseline:** Gate 12 audit commit `9d944d736d` (unmerged, on top of `main` `37bce9468d`)
**Scope:** design + artifacts + one reconstruction preview. **Not changed:** live HTML (`site/public`), robots directives, sitemaps, `robots.txt`, `routes.json`, `release_ledger.json`, release authorizations. Nothing merged, deployed or opened as a PR.

## 1. Verified baseline

| Layer | Count | State |
|---|---|---|
| Legacy routes (`routes.json`) | **14,000** | all `status: planned`, `indexable: false`, `in_sitemap: false` |
| Released dossiers (`release_ledger.json`) | **13,998** released (`public_dossier`, `indexable: true`) | 2 blocked (`acquire`, `newsletter`: `blocked_high_risk`) |
| Generated public HTML (`site/public`, deploy scope) | **14,041** = 14,000 route pages + 41 pages with no route record | 14,039 `index, follow`; 2 `noindex` (`/en/`, `/newsletter/`) |
| Sitemap URLs | 13,998 | equals the released ledger set |
| Google index (SEO_INDEXATION_STRATEGY.md, 2026-07-24) | 3 indexed | ~3,369 "discovered, not indexed" + 132 "crawled, not indexed" |

These three populations must stay distinct, and they currently disagree:

1. **Registry vs live surface.** `routes.json` says nothing is indexable, but the deployed HTML asks to be indexed on 14,039 pages.
2. **Ledger vs live surface.** `/acquire/` is `blocked`/`not_indexed` in the ledger, yet its HTML is `index, follow`.
3. **Template vs Contract C.** `main/templates/atlas/base.html` hard-codes `<meta name="robots" content="index, follow">`, so the renderer cannot express a Contract-C `noindex`.

Contract C (IP-16.2, rule RL) already defines how a pre-ratification public URL should be held: `legacy_public_holding → (public_noindex, noindex)`, never indexed. The live surface does not conform to that rule today.

Gate 12 audit, refreshed after this sprint's changes:
- **Markdown corpus:** 14,006 FAIL / 9 PASS. The passing pages are the reconstructed MoS₂ draft and 8 hand-written institutional drafts that pass under Gate 12-I (§6).
- **HTML surface:** 14,033 FAIL / 8 PASS. 14,032 indexable pages fail.

The prior branch's tests all pass. `test_distinctiveness.py` still has 23 tests, updated to target the real canonical page instead of the retired control. The Contract-C property suite (23,040 combinations), the IG governance, Pilot 01/02/03, reference-production and independence suites, `validate_scaffolding` and the L0/L1/L2 CI scripts also pass.

## 2. Gate 12 integration assessment

**Problem.** Strict Gate 12 in the deploy workflow blocks every redeploy while 14,032 indexable legacy pages fail. A blanket exemption would let near-duplicates stay indexed, or let new ones in.

**Mechanism implemented.** A bounded legacy hold that implements Contract C RL rather than bypassing it:
- Code: `distinctiveness_core.apply_legacy_hold` and `validate_distinctiveness.py --surface DIR --legacy-hold FILE`.
- Policy: `gate12_policy.json#legacy_migration` (v1.1.0).

| Page state | Result |
|---|---|
| Passes Gate 12 | `PASS` |
| In the sealed baseline, substantive body unchanged, robots `noindex`, absent from every sitemap | `LEGACY_HOLD_NOINDEX` (allowed; this is Contract C RL) |
| Same, but still requests indexation (robots `index` **or** listed in a sitemap) | `BLOCK_LEGACY_INDEXED` |
| Same, under an owner-authorized, unexpired freeze exception (≤ 30 days; reported every run as a Contract-C deviation) | `LEGACY_FREEZE_INDEXED` |
| In the baseline, body changed, still failing | `BLOCK_MODIFIED_LEGACY` |
| Not in the baseline and failing (indexable **or not**) | `BLOCK_NEW_FAILING` |

The baseline is `main/data/distinctiveness/legacy_surface_hold.json`:
- **Contents:** 14,033 entries (`path`, entity-masked substantive-body hash, `route_id`), sealed from `site/public` at `9d944d736d` with a count and a sha256 digest.
- **Shrink-only:** `--check-hold --hold-ratchet-ref origin/<base>` rejects any added or re-pinned entry.
- **Freeze exception:** `not_authorized` by default.

**Why this is bounded.** The mechanism has four limits:
- It cannot admit a new page, so it cannot authorize new low-quality content.
- It cannot keep an edited page that fails, so substantial modification must earn Gate 12.
- It cannot raise the unqualified indexable surface: held pages may not request indexation, and the baseline cannot grow.
- It does not override Contract C. Its default output is exactly Contract C RL. The only deviation is the explicit, time-boxed freeze exception, and every run prints it.

**Deployment consequence.**
- Today the deploy step still fails: 14,032 `BLOCK_LEGACY_INDEXED`.
- After the Stage 2 transform it passes: 8 `PASS` + 14,033 `LEGACY_HOLD_NOINDEX` (§5).
- The deadlock therefore lasts only until the owner chooses Stage 2, or authorizes a freeze exception for an urgent non-content deploy.

## 3. Legacy disposition registry

**Files** (in `main/data/recovery/`):
- `legacy_disposition_registry.jsonl`: one record per legacy route plus one per non-route public page, 14,041 records.
- `legacy_disposition_summary.json`: counts, migration impact, reason-code dictionary.
- Builder: `scripts/recovery/build_legacy_disposition.py`, deterministic.
- Invariant validator: `scripts/recovery/validate_legacy_disposition.py`. It passes with 0 violations.

**What each record preserves verbatim:**
- route identity (`route_id`, `path`, `language`);
- the `routes.json` posture;
- the historical release record (`release_status`, `public_status`, `indexable`, `sitemap_file`).

**What each record adds:**
- the live robots and sitemap state;
- the markdown and HTML Gate-12 verdicts;
- legacy-hold membership;
- an entity key and how it was derived;
- category, reason code, consolidation target and bound KO.

**What it authorizes:** nothing. No URL is deleted, redirected, de-indexed or published.

| Category | Routes | Non-route pages | Basis |
|---|---|---|---|
| Independent reference candidate | **1** (`molybdenum_disulfide`) | 0 | governed KO binding (KO-MOS2-SCIENTIFIC-001; PC disposition `governed_reference_no_new_route`) |
| Module of an existing Knowledge Object | **38** | 0 | the `cohort02_en_molybdenum_disulfide_*` variants → modules of KO-MOS2 at `/molybdenum-disulfide/` |
| Valid language/domain-specific reference candidate | **1** (`de_core_mos2`) | 0 | approved `CLM-TERM-MOS2-DE-001` + `LEX-DE-MOS2-001`; IG `valid_domain_specific_reference` |
| Evidence-pending knowledge entity | **245** (EN 160, DE 85) | 0 | the one canonical surface per curated concept/comparison |
| Duplicate or redundant presentation surface | **12,741** | 16 | 12,671 audience/layer/cohort variants → canonical target; 79 internal pipeline-status pages; 5 duplicate institutional functions; 2 German MoS₂ duplicates → `de_core_mos2` |
| Unresolved — requires review | **974** | 25 | 931 generated entities with unverified identity (cohort 04/05 combinatorial names); 50 institutional surfaces → Gate 12-I review; 18 unmatched non-route pages |
| **Total** | **14,000** | **41** | |

**Migration impact (computed, not executed):**
- The 14,041 records collapse onto **943 consolidation targets**.
- **247 canonical knowledge surfaces** remain: 1 independent + 1 language-specific + 245 evidence-pending. These are where real reference value can be produced.
- Four of them have governed evidence today: `molybdenum_disulfide` and `de_core_mos2` (MoS₂), and `what_is_sulfur` / `de_what_is_sulfur`. The sulfur pair is backed by the Pilot 01/02 trade, HS-classification and OCP industrial evidence, which makes sulfur the strongest next Knowledge Object candidate.
- The 931 unverified generated entities (e.g. `c04_min_argentite_crystal`, `cohort04_de_darmstadtium_sulfid`) are not counted as reference potential until their identity is confirmed.
- This is not a cap: the final number of independent pages follows evidence. Each curated concept can carry scientific, linguistic, industrial, economic, geographic and jurisdictional modules, and a dimension becomes its own URL only when the IG gate finds `valid_domain_specific_reference` (as `de_core_mos2` did). URLs are never produced by combining dimensions.

## 4. MoS₂ reference reconstruction (canonical route, no new URL)

**Pipeline:** `KO-MOS2-SCIENTIFIC-001` → render spec → `scripts/reference_production/render_ko_reference.py`. The spec (`main/data/reference_production/render_specs/KO-MOS2-SCIENTIFIC-001.json`) owns wording only. Every displayed value is resolved from an evidence record.

The renderer refuses to render (proven by tests) when:
- a value is absent from the evidence;
- evidence is not governed, not `evidence_verified`, or about another entity;
- `source_admissibility.admissible()` does not admit the evidence for its declared use;
- evidence is not bound to the module's claim in the KO (boundary evidence only in boundary modules);
- two sources disagree on a cross-checked value;
- the canonical route is anything other than an existing `routes.json` route.

**Outputs** (non-public):
- **Canonical draft:** `main/content/en/pages/molybdenum-disulfide.md`. It replaces the 22-token legacy draft of route `molybdenum_disulfide` in place and stays `status: draft`, `non_public`, `indexable: false`. It passes the L0/L1 draft validators.
- **HTML preview:** `main/data/reference_production/previews/molybdenum-disulfide/index.html`. It carries `robots: noindex, nofollow`, its canonical points to `/molybdenum-disulfide/`, and it lives outside `site/public`, so it cannot deploy.
- **IG units:** written to `ig_unit_registry.json` for the canonical page. The earlier stand-alone control page is retired: its role is now served by the real canonical draft.

**Content.** 7 modules:
- formula identity;
- layered S–Mo–S bulk structure;
- the 1T/2H/3R polytype framework;
- the 2H space group P6₃/mmc with both c-axis determinations;
- the origin of the "2H" label (historical evidence);
- the two coexisting lattice-a determinations (3.15(2) Å and 3.161 Å, not averaged);
- the 3R boundary.

Plus an "at a glance" table, explicit "not established" scope, and an evidence trail of the 11 admitted evidence records with originating works, records, roles, lock status and retrieval dates. The "2H" origin is drawn from the 1923 and 1983 excerpts, and the trail separates the database records from the originating studies they reproduce. No band-gap, industrial, safety, market or German-terminology statement is made.

| | Legacy (before) | Reconstruction (after) |
|---|---|---|
| Markdown draft | 22 substantive tokens; S = 1.000 vs `hydrogen-sulfide-risk.md`; template ratio 1.00; 0 IG units; **FAIL** | 585 tokens; S = 0.000 vs all 14,015 pages; template ratio 0.00; skeleton unshared; **7/7 IG units**; **PASS** |
| Live `/molybdenum-disulfide/` HTML | 143 tokens; S = 0.766 vs `/en/terminology/molybdenum-disulfide/aud/gov/inst/`; template ratio 0.90; **FAIL** | preview: 591 tokens; S = 0.000 vs all 14,041 public pages; template ratio 0.00 |
| Similarity legacy ↔ reconstruction | — | 0.000 (markdown and HTML) |
| Contract C | — | **(not_public, noindex)**: Gate 12 PASS cannot override |

**Path to release.** Postures move one at a time, each owned by its governance owner. `contract_c_derive.derive` results:

| Step | Contract C |
|---|---|
| Today | (not_public, noindex) |
| Claims activated | (not_public, noindex) |
| Validated | (not_public, noindex) |
| Governance = governed | (not_public, noindex) |
| Release authorized | (not_public, noindex) |
| IG route re-review → `ig_reviewed_pass` | (public_noindex, noindex) |
| Sources locked → `evidence_locked` | (public_indexable, index_approved) |

On the IG step: the gate's `evaluate()` on the proposed pair `molybdenum_disulfide` vs `de_core_mos2` returns `valid_domain_specific_reference`. The legacy-route comparison that produced `near_duplicate` no longer applies once the KO *is* that route and its variants become modules. Recording that re-review is a governance act and is **not** done here.

## 5. Staged migration plan

| Stage | Change | Executable now | Gate/validation | Rollback condition → action |
|---|---|---|---|---|
| **0 (done)** | Gate 12 + legacy hold + Gate 12-I + disposition registry + MoS₂ preview, all in repo data/scripts | — | 40 Gate-12/recovery tests; registry invariants; renderer `--check` | any regression → revert the PR; nothing live changed |
| **1** | Merge Gate 12 enforcement (CI + deploy step in hold mode). No HTML change. | yes | PR CI: tests, `--gate`, `--check-hold` ratchet, renderer `--check`, registry validator | deploy needed before Stage 2 → owner sets a ≤ 30-day freeze exception (reported deviation) or reverts the deploy step |
| **2** | Contract C RL conformance: `scripts/recovery/stage2_legacy_noindex.py --authorized-stage2 --out site/public` flips 14,032 held pages to `noindex, follow` and removes 13,998 URLs from sitemaps. No deletion or redirect. | yes (refuses `site/public` without the flag) | Rehearsal on a copy: 14,032 flips, 13,998 sitemap removals, Gate 12 hold-mode **PASS** (8 PASS + 14,033 LEGACY_HOLD_NOINDEX). Negative rehearsals block (§6). | traffic or crawl regression the owner rejects → revert the commit (every change is a robots meta line or a sitemap `<url>` block; manifest sha256 recorded) |
| **3** | Fix the renderer: `atlas/base.html` takes robots from Contract C instead of hard-coding `index, follow`; add a reference-object layout without the dossier boilerplate. Re-render institutional pages from their hand-written drafts (these pass Gate 12-I as markdown). | design ready | Gate 12-I on rendered output | rendered page fails Gate 12-I → keep the held legacy page; the baseline is untouched |
| **4** | MoS₂ promotion at `/molybdenum-disulfide/`: claim activation, validation, governed posture, IG route re-review, release authorization; then render the preview into `site/public` (public_noindex until sources lock) | blocked by Contract C (by design) | Gate 12 PASS (already); Contract C derive must leave not_public; remove the path from the hold (ratchet shrink) | any posture regresses → derive returns not_public; page reverts to the held legacy version |
| **5** | Consolidation per KO: `rel=canonical` from module/variant surfaces to their canonical target, then (owner decision) 301 or retire; one entity at a time, starting with the 38 MoS₂ modules | after Stage 4 | registry targets are canonical (validated); ratchet shrink | inbound links or traffic lost → restore the held page (body hash unchanged) |
| **6** | KO production for evidence-pending entities, ordered by governed evidence: sulfur (Pilot 01/02 evidence) first. Identity review of the 931 generated entities before any KO work. | per KO | Gate 12 + Contract C per page | KO fails Gate 12 or IG → it stays a module, edge or data object, not a URL |

## 6. Validation evidence

**Unit tests.**
- `test_distinctiveness.py`: **23/23 PASS**, 0.2 s. These are the original Gate 12 proofs, now run against the real canonical page.
- `test_legacy_migration.py`: **17/17 PASS**, 0.8 s. It covers:
  - baseline sealing;
  - indexed legacy blocks; noindex + sitemap removal → RL;
  - a sitemap listing alone counts as an indexation request;
  - a new noindex clone blocks; a modified legacy page blocks; a rebuilt page without IG still blocks;
  - a tampered baseline is detected; the ratchet is shrink-only, including re-pinning;
  - the freeze exception is explicit, bounded, expiring, and never admits new pages;
  - Gate 12-I: a distinct registered page passes without IG; the same page unregistered fails; templates are not relaxed; a duplicate function fails;
  - the renderer is up to date and fail-closed (a missing value, boundary evidence on a claim, a wrong admitted use, and a new URL are all refused);
  - the preview is noindex and outside the deploy root.

**Real surface (14,041 pages).**

| Run | Result |
|---|---|
| As-is, hold mode | **FAIL**: 14,032 BLOCK_LEGACY_INDEXED, 8 PASS, 1 HOLD_NOINDEX, 0 new, 0 modified |
| Stage-2 rehearsal on a copy | **PASS**: 8 PASS, 14,033 LEGACY_HOLD_NOINDEX |
| Same + one injected near-duplicate (noindex) + one edited legacy page | **FAIL**: BLOCK_NEW_FAILING 1, BLOCK_MODIFIED_LEGACY 1 |
| Strict mode (`validate_all`, unchanged default) | **FAIL**: 14,032 indexable pages |

**What passes, fails and stays blocked.**
- **Passes Gate 12:**
  - MoS₂ canonical draft and preview;
  - 8 public institutional pages (`/acquire/`, `/atlas/`, `/compounds/`, `/languages/`, `/materials/`, `/methodology/`, `/newsletter/`, `/terminology/`; `/newsletter/` is already `noindex`);
  - 8 hand-written institutional drafts (home, glossary, sources, quality-gate, acquire, internal-linking, DE corpus-map, DE translator-playbook).
- **Fails Gate 12:** every other page. Rendered home and policy pages fail Gate 12-I on template prose and near-duplication, so nothing was relaxed for them.
- **Still blocked by Contract C:** everything, including MoS₂ (not_public).
- **Blocked at deploy:** the current surface, until Stage 2.

**Regressions.** Contract-C property tests, IG governance, Pilot 01/02/03, reference production, independence, source admissibility, relationship grammar, `validate_scaffolding`, and the L0/L1/L2 CI scripts all PASS.

## 7. Gate 12 page-type semantics (homepage, navigation, methodology)

Non-factual institutional surfaces cannot carry evidence-backed IG units by nature. Requiring them would force fake facts onto the homepage.

**Gate 12-I** (`gate12_policy.json#page_classes`, `institutional_surface_registry.json`) therefore:
- **replaces only** the IG-unit requirement, with a closed function vocabulary (41 functions, 55 bindings), one surface per function per language;
- **keeps** the near-duplicate, review-band, template-prose, structural-template and thin-body rules;
- **does not relax** Gate 04 sourcing of any factual sentence on the page, or Contract C (indexing a non-factual page still needs R11 certification).

Pipeline-status pages are deliberately not institutional functions. All 79 are classified redundant.

**Result:** 8 of 55 registered institutional HTML pages pass and 47 fail. The rendered home page fails (template ratio 0.69). The hand-written `index.md` passes, which isolates the defect in the renderer, not in the content.

## 8. Proposed PR sequence

| PR | Exact permitted changes | Deployment consequence |
|---|---|---|
| **PR-1 Gate 12 + recovery tooling** (this branch: commits `9d944d736d` + Recovery-01) | `scripts/validators/*distinctiveness*`, `test_legacy_migration.py`, `validate_all.py`, `doctrine/QUALITY_GATE.md`, `main/data/distinctiveness/**`, `main/data/recovery/**`, `scripts/recovery/**`, `scripts/reference_production/**`, `main/data/reference_production/**`, `main/templates` untouched, `main/content/en/pages/molybdenum-disulfide.md` (non-public draft), both workflows, `DECISION_LOG.md`. **No** `site/public`, sitemap, robots, routes or ledger change. | PR CI gains the Gate-12, hold-ratchet, renderer and registry checks. The **next Pages deploy fails** until PR-2 lands (or a freeze exception is authorized). Live site unchanged. |
| **PR-2 Contract C RL conformance** | Only the output of `stage2_legacy_noindex.py --authorized-stage2`: robots meta lines on 14,032 held pages + sitemap `<url>` removals (13,998). No other byte. Requires owner authorization. | Deploy passes Gate 12. Live: 14,032 URLs stay reachable but noindex; 7 institutional pages stay indexable (owner may also noindex them pending R11). |
| **PR-3 Renderer conformance** | `main/templates/atlas/base.html` robots from Contract C; new reference-object layout; re-render institutional drafts; their paths leave the hold only if they pass Gate 12-I. | Rendered institutional pages replace held ones only when passing; the hold shrinks. |
| **PR-4 MoS₂ promotion** | Posture records only (claim activation, validation, governance, IG route re-review pair, release authorization), each with its own evidence; then render the preview to `/molybdenum-disulfide/`; remove its hold entry. | `/molybdenum-disulfide/` becomes public_noindex (R9) until sources lock, then indexable. |
| **PR-5+ consolidation and KO waves** | Per entity: canonical tags, then owner-decided 301/retire; new KOs from governed evidence (sulfur first). | Indexable surface grows only through Gate 12 + Contract C. |

## Exact next production action

**The owner decides on PR-1 and authorizes PR-2.** Concretely:
1. Review and merge PR-1, whose deploy step stays closed.
2. Run `python3 scripts/recovery/stage2_legacy_noindex.py --authorized-stage2 --out site/public` on a PR-2 branch.
3. Confirm `validate_distinctiveness.py --surface site/public --legacy-hold main/data/distinctiveness/legacy_surface_hold.json` passes.
4. Deploy.

Until that decision, no deploy should run, and none can pass the new gate.
