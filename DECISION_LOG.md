# DECISION LOG

This document records decisions that affect the architecture, doctrine, data, or direction of bisulfid.com.

All structural decisions require an entry here. Changes to doctrine require an entry here.

---

## Log Format

Each entry includes:

- **Date**
- **Sprint / Phase**
- **Decision**
- **Rationale**
- **Doctrine reference** (if applicable)
- **Files affected**

---

## Entries

### 2026-05-15 — Sprint 0A: Doctrine Foundation

**Decision:** Establish the minimum sovereign doctrine foundation for bisulfid.com.

**Rationale:** The README defines bisulfid.com as a Global Sovereign Sulfur Intelligence Gateway with a governed doctrine folder. Before any content, code, or deployment decisions are made, the governing documents that define what this asset is, how it operates, and what conditions must be met before launch must exist in the repository. These documents serve as the single source of truth for all future decisions.

**Doctrine reference:** `ASSET_THESIS.md` — all documents flow from it.

**Files created:**

- `doctrine/ASSET_THESIS.md` — top doctrine document; defines what this asset is.
- `doctrine/PROJECT_DOCTRINE.md` — governs all operations.
- `doctrine/MULTILINGUAL_POLICY.md` — governs language architecture and hreflang integrity.
- `doctrine/GLOBAL_REFERENCE_STANDARD.md` — governs global reference quality.
- `doctrine/SOURCE_POLICY.md` — governs claims and sources.
- `doctrine/QUALITY_GATE.md` — defines the 11 launch conditions.
- `doctrine/SECURITY_POLICY.md` — governs security posture.
- `DECISION_LOG.md` — this document.
- `main/data/languages.json` — machine-readable language registry.

**Not created in this sprint:** frontend UI, HTML, CSS, JS, images, GitHub Actions, scripts, package.json, CURSOR_RULES.md, generated site output, placeholder content pages.

---

### 2026-05-15 — Sprint 0B: Data Skeleton and Route Governance Established

**Decision:** Create planned route, ontology, source, claim, sitemap, hreflang, translation, and internal-link registries.

**Rationale:** Before content or UI work can begin, the data governance skeleton must exist. Routes, ontology terms, and claim categories must be registered in a planned or inactive state so that content creation has a governed framework to operate within. No routes were published. No sitemap entries were activated. No claims were approved. No sources were fabricated.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`

**Files created:**

- `main/data/routes.json` — planned EN v1 route registry (21 routes, all planned, none published).
- `main/data/hreflang_groups.json` — empty hreflang group registry, inactive.
- `main/data/translation_registry.json` — empty translation registry, inactive.
- `main/data/internal_links.json` — planned internal link graph (route_id references only, not raw URLs).
- `main/data/sitemap_policy.json` — sitemap governance policy, inactive, no active URLs.
- `main/data/ontology/sulfur_terms.json` — governed ontology skeleton with 14 terms, all planned.
- `main/data/ontology/spatial_nodes.json` — Interactive Term Map node registry, 11 nodes, all planned.
- `main/data/ontology/term_edges.json` — semantic edge registry, 12 edges, all planned, no sources locked.
- `main/data/sources/source_registry.json` — source registry structure established, no sources added.
- `main/data/claims/terminology_claims.json` — empty claim registry, inactive.
- `main/data/claims/science_claims.json` — empty claim registry, inactive.
- `main/data/claims/industry_claims.json` — empty claim registry, inactive.
- `main/data/claims/safety_claims.json` — empty claim registry, inactive, blocked patterns defined.
- `main/data/claims/market_claims.json` — empty claim registry, inactive, blocked patterns defined.
- `main/data/claims/acquisition_claims.json` — empty claim registry, inactive.

**Files updated:**

- `DECISION_LOG.md` — Sprint 0B entry appended.

**Not created in this sprint:** HTML pages, markdown content pages, templates, CSS, JS, scripts, GitHub Actions, package.json, dependencies, site/ output, placeholder content.

---

### 2026-05-15 — Sprint 0C: Multilingual Content Skeleton Established

**Decision:** Create the governed multilingual content directory structure for EN, DE, AR, ZH, JA, FR, and ES, plus shared disclaimer, source-note, and canonical-claim folders.

**Rationale:** Before any content work begins, the directory structure must exist in a governed state. Content directories make clear where files belong, what layer each language occupies, and that file presence is not the same as publication. The shared disclaimer folder establishes a controlled location for site-wide governance fragments that must be attached to pages before any route may pass the Quality Gate.

**Doctrine reference:** `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`

**Files created:**

- `main/content/README.md` — content directory governance document.
- `main/content/en/pages/.gitkeep`
- `main/content/en/term-records/.gitkeep`
- `main/content/en/fragments/.gitkeep`
- `main/content/de/pages/.gitkeep`
- `main/content/de/term-records/.gitkeep`
- `main/content/de/fragments/.gitkeep`
- `main/content/ar/pages/.gitkeep`
- `main/content/ar/term-records/.gitkeep`
- `main/content/ar/fragments/.gitkeep`
- `main/content/zh/pages/.gitkeep`
- `main/content/zh/term-records/.gitkeep`
- `main/content/zh/fragments/.gitkeep`
- `main/content/ja/pages/.gitkeep`
- `main/content/ja/term-records/.gitkeep`
- `main/content/ja/fragments/.gitkeep`
- `main/content/fr/pages/.gitkeep`
- `main/content/fr/term-records/.gitkeep`
- `main/content/fr/fragments/.gitkeep`
- `main/content/es/pages/.gitkeep`
- `main/content/es/term-records/.gitkeep`
- `main/content/es/fragments/.gitkeep`
- `main/content/shared/canonical-claims/.gitkeep`
- `main/content/shared/source-notes/.gitkeep`
- `main/content/shared/disclaimers/editorial-disclaimer.md` — draft, not attached to any route.
- `main/content/shared/disclaimers/safety-disclaimer.md` — draft, not attached to any route.
- `main/content/shared/disclaimers/translation-disclaimer.md` — draft, not attached to any route.
- `main/content/shared/disclaimers/sponsorship-disclaimer.md` — draft, not attached to any route.
- `main/content/shared/disclaimers/acquisition-disclaimer.md` — draft, not attached to any route.

**Files updated:**

- `DECISION_LOG.md` — Sprint 0C entry appended.

**Not created in this sprint:** public content pages, index.md, route content files, templates, CSS, JS, scripts, GitHub Actions, package.json, dependencies, site/ output. No routes were published. No sitemap or navigation state was changed. No claims or sources were added.

---

### 2026-05-15 — Sprint 0D: Validator Skeleton Established

**Decision:** Create safe placeholder validator files aligned with the 11 Quality Gates and route/source/claim/multilingual governance requirements.

**Rationale:** Before a build system exists, the validator surface area must be reserved in code. Validators need to exist as named, documented files so that future build-system integration has stable entry points. Each validator documents what it will enforce without claiming to enforce it yet. Placeholder behavior (print warning, exit 0) prevents false failures in CI stubs while making the non-enforcement status explicit and undeniable.

**Doctrine reference:** `doctrine/QUALITY_GATE.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/SECURITY_POLICY.md`

**Sprint 0D constraints (all observed):**
- Validators are intentionally non-enforcing at this stage.
- No build system was created.
- No GitHub Actions workflows were created.
- No dependencies were added.
- No package.json was created.
- No public pages were created.
- No routes were modified.
- No claim files were modified.
- No source registry was modified.
- No content directories were modified.
- README.md was not modified.
- Placeholder validators must not be treated as proof of launch readiness.

**Files created:**

- `scripts/validators/README.md` — validator directory governance document.
- `scripts/validators/validate_all.py` — orchestrator; runs all validators in Quality Gate order.
- `scripts/validators/validate_links.py` — future Gate 01 + Gate 08 (links and orphans).
- `scripts/validators/validate_content.py` — future Gate 02 + Gate 09 (content quality).
- `scripts/validators/validate_indexation.py` — future Gate 03 (sitemap and indexation).
- `scripts/validators/validate_sources.py` — future Gate 04 (source registry).
- `scripts/validators/validate_claims.py` — future Gate 04 + blocked-claim patterns.
- `scripts/validators/validate_seo.py` — future Gate 05 (SEO compliance).
- `scripts/validators/validate_security.py` — future Gate 06 (security posture).
- `scripts/validators/validate_accessibility.py` — future Gate 07 (accessibility).
- `scripts/validators/validate_routes.py` — future route registry governance.
- `scripts/validators/validate_schema.py` — future structured data (JSON-LD) checks.
- `scripts/validators/validate_hreflang.py` — future Gate 11 (hreflang correctness).
- `scripts/validators/validate_translations.py` — future Gate 11 (translation integrity).
- `scripts/validators/validate_language_routes.py` — future Gate 11 (language routes).
- `scripts/validators/validate_supply_chain.py` — future supply chain security checks.

**Files updated:**

- `DECISION_LOG.md` — Sprint 0D entry appended.

**Not created in this sprint:** build system, GitHub Actions, package.json, dependencies, templates, CSS, JS, HTML pages, site/ output, frontend UI.

---

### 2026-05-15 — Sprint 1: Static Build Skeleton Established

**Decision:** Create a minimal Python-stdlib-only static build skeleton: config layer, template skeletons, build scripts, and sitemap/robots generators. Zero public pages are generated. All routes remain in `planned` state.

**Rationale:** A governed build system must exist before any content can be placed into production. The build skeleton establishes the machinery — config, templates, scripts — without activating any route, publishing any page, or enabling any indexation. The prelaunch posture (full robots.txt disallow, zero-URL sitemap, `noindex` SEO config) is enforced at the script level, not merely declared. This sprint creates the assembly line, not the product.

**Doctrine reference:** `doctrine/QUALITY_GATE.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/SECURITY_POLICY.md`

**Sprint 1 constraints (all observed):**
- Python standard library only. No external dependencies.
- No package.json created.
- No GitHub Actions workflows created.
- No deployment config created.
- No Cloudflare config created.
- No routes marked published.
- No routes marked indexable.
- No routes marked in_sitemap.
- No routes.json modified.
- No claim files modified.
- No source registry modified.
- No content directories modified.
- No real content pages created.
- No inline JS in any template.
- No external scripts referenced.
- No tracking of any kind.
- No visual UI, advanced CSS, or animations.
- All templates carry skeleton disclaimer comment.
- Placeholder validators must not be treated as proof of launch readiness.

**Files created:**

- `main/config/build.json` — build orchestrator config; `publish_planned_routes: false`, `generate_only_published_routes: true`.
- `main/config/seo.json` — SEO governance config; `default_robots: "noindex, nofollow"`.
- `main/config/security.json` — security policy config; inline JS and external scripts disallowed.
- `main/config/navigation.json` — navigation config; status inactive, items empty.
- `main/config/site.json` — site identity config; status prelaunch.
- `main/templates/base.html` — base layout skeleton; no inline JS, no external scripts.
- `main/templates/home.html` — home page skeleton.
- `main/templates/term.html` — term record page skeleton.
- `main/templates/category.html` — category page skeleton.
- `main/templates/language_index.html` — language index page skeleton.
- `main/templates/404.html` — 404 error page skeleton.
- `main/templates/robots.txt` — robots.txt template (prelaunch: full disallow).
- `main/templates/partials/header.html` — header partial skeleton.
- `main/templates/partials/footer.html` — footer partial skeleton.
- `main/templates/partials/nav.html` — navigation partial skeleton (inactive).
- `main/templates/partials/breadcrumb.html` — breadcrumb partial skeleton.
- `main/templates/partials/hreflang_block.html` — hreflang link block partial.
- `main/templates/partials/structured_data.html` — JSON-LD structured data partial skeleton.
- `main/templates/partials/disclaimer_block.html` — disclaimer block partial skeleton.
- `main/templates/partials/interactive_term_map.html` — Interactive Term Map partial; documents data sources and JS-disabled fallback.
- `scripts/build.py` — build orchestrator; loads config and routes; generates `site/build-status.json` only; 0 public pages.
- `scripts/generate_robots.py` — generates `site/robots.txt`; prelaunch full-disallow policy.
- `scripts/generate_sitemap.py` — generates `site/sitemap.xml`; filters published+indexable+in_sitemap; 0 URLs pass.
- `scripts/generate_placeholders.py` — generates placeholder HTML skeletons for planned routes (dev/review use only; no public output).
- `scripts/README.md` — scripts directory governance document.
- `site/.gitkeep` — reserves site/ output directory.

**Files updated:**

- `DECISION_LOG.md` — Sprint 1 entry appended.

**Not created in this sprint:** public content pages, real index.html, published routes, sitemap URLs, GitHub Actions, package.json, external dependencies, deployment config, Cloudflare config, visual UI, animations, inline JS, external scripts, tracking.

---

### 2026-05-15 — Sprint 2: English Source Drafts Established

**Decision:** Create the first non-public English source-layer draft pages for the homepage, Bisulfid definition, spelling boundary, German-English sulfur terminology, source discipline, and strategic acquisition surface.

**Rationale:** Before any route can be considered for publication, draft content must exist in a governed state. Draft pages establish what each route will say, identify which claims require source-locking, and provide reviewable material for the source registry population sprint. Draft presence is not publication — no route was published, no claim was approved, no source was added.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 2 constraints (all observed):**
- No route was published.
- No sitemap or navigation state was changed.
- No claims were approved.
- No sources were added.
- No fake source citations were included.
- No external links were included as verified.
- No numerical market claims were stated as verified.
- No specific companies were named as acquisition targets.
- No chemical handling instructions were included.
- No medical or therapeutic advice was included.
- No safety thresholds were included.
- Bisulfid and bisulfite were not conflated.
- routes.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- source_registry.json was not modified.
- Claim files were not modified.
- README.md was not modified.
- No HTML output was created.
- No dependencies were added.
- No GitHub Actions were created.
- All draft pages carry `status: draft` and `publication_status: non_public`.
- All draft pages carry `indexable: false` and `in_sitemap: false`.
- Claims requiring source-locking are marked `[SOURCE REQUIRED]` inline.

**Files created:**

- `main/content/en/README.md` — English source layer governance document.
- `main/content/en/pages/index.md` — homepage draft; Global Sovereign Sulfur Intelligence Gateway positioning; six strategic layers; language architecture; Interactive Term Map as planned future interface; link intent by route_id.
- `main/content/en/pages/what-is-bisulfid.md` — defines Bisulfid as the central term; domain thesis vs chemical definition; center-node position; disambiguation from bisulfite; German-form spelling boundary.
- `main/content/en/pages/bisulfid-vs-bisulfide.md` — The Missing Letter; bisulfide→bisulfid; English vs German spelling boundary; E is not missing; asset architecture.
- `main/content/en/pages/sulfid-vs-sulfide.md` — broader -id/-ide suffix pattern; Oxide/Oxid and Chloride/Chlorid examples (all [SOURCE REQUIRED]); supports German identity layer.
- `main/content/en/pages/sources.md` — source discipline; no source entry = no published claim; blocked source types; registry not yet populated; draft content is not public evidence.
- `main/content/en/pages/acquire.md` — strategic acquisition surface; what a buyer acquires; no price; no urgency; no named targets; contact agent@sohadot.com.

**Files updated:**

- `DECISION_LOG.md` — Sprint 2 entry appended.

**Not created in this sprint:** HTML output, published pages, sitemap entries, navigation items, source entries, approved claims, GitHub Actions, dependencies, package.json, route modifications.

---

### 2026-05-15 — Sprint 2B: English Draft Alignment Review Completed

**Decision:** Review and align all six English source-layer draft pages against route governance, internal link planning, ontology, source discipline, and acquisition discipline. Make minimal corrections only.

**Rationale:** The Sprint 2 drafts contained a systematic route ID format error: all six pages used `en-*` prefixed, hyphen-separated route IDs (e.g., `en-home`, `en-what-is-bisulfid`) rather than the IDs defined in `routes.json` (e.g., `home`, `what_is_bisulfid`). This would prevent the build system from matching content files to their routes. Additional issues included incomplete planned link sections and a reference to a nonexistent route. All corrections were minimal and did not alter content, remove [SOURCE REQUIRED] markers, or change any governance state.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 2B constraints (all observed):**
- No new pages created.
- No route was published.
- No sitemap or navigation state was changed.
- No claims were approved.
- No sources were added.
- No [SOURCE REQUIRED] markers removed.
- All pages remain `status: draft` and `publication_status: non_public`.
- All pages remain `indexable: false` and `in_sitemap: false`.
- routes.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- source_registry.json was not modified.
- Claim files were not modified.
- root README.md was not modified.
- No HTML output was created.
- No dependencies were added.
- No GitHub Actions were created.

**Issues corrected:**

- All six pages: `route_id` corrected from `en-*` format to `routes.json` format (e.g., `en-home` → `home`, `en-what-is-bisulfid` → `what_is_bisulfid`).
- All inline route references: corrected to use `routes.json` format throughout.
- `index.md`: removed reference to `en-term-bisulfid` (no corresponding route in routes.json); added `what_is_sulfur` and `industrial_sulfur_systems` to planned link section.
- `what-is-bisulfid.md`: added `bisulfide_hydrosulfide_sulfide` and `german_english_chemical_terms` to planned link section.
- `bisulfid-vs-bisulfide.md`: added `german_english_chemical_terms` and `bisulfide_hydrosulfide_sulfide` to planned link section.
- `sulfid-vs-sulfide.md`: added `what_is_bisulfid`, `glossary`, and `sources` to planned link section.
- `sources.md`: added planned link section (`what_is_bisulfid`, `glossary`, `home`).
- `acquire.md`: added planned link section (`home`, `what_is_bisulfid`, `industrial_sulfur_systems`).

**Infrastructure note recorded:**

`routes.json` `content_file` fields point to `main/content/en/*.md` while actual files are in `main/content/en/pages/*.md`. This path discrepancy requires resolution in a future sprint.

**Files created:**

- `main/content/en/DRAFT_ALIGNMENT_REPORT.md` — full alignment review report.

**Files updated:**

- `main/content/en/pages/index.md` — route_id corrected; link intent aligned.
- `main/content/en/pages/what-is-bisulfid.md` — route_id corrected; link intent aligned.
- `main/content/en/pages/bisulfid-vs-bisulfide.md` — route_id corrected; link intent aligned.
- `main/content/en/pages/sulfid-vs-sulfide.md` — route_id corrected; link intent aligned.
- `main/content/en/pages/sources.md` — route_id corrected; planned link section added.
- `main/content/en/pages/acquire.md` — route_id corrected; planned link section added.
- `DECISION_LOG.md` — Sprint 2B entry appended.

**Not modified in this sprint:** routes.json, sitemap_policy.json, navigation.json, source_registry.json, claim files, root README.md, templates, scripts, doctrine files, ontology files, data registries.

---

### 2026-05-15 — Sprint 2C: Route Content Paths Aligned

**Decision:** Update all 21 `content_file` paths in `routes.json` to point to the governed `main/content/en/pages/` directory structure. Correct the `home` route to point to `index.md` rather than the non-existent `home.md`.

**Rationale:** Sprint 0B created `routes.json` with `content_file` paths pointing to `main/content/en/*.md`. Sprint 0C established `main/content/en/pages/` as the governed directory for English page drafts. Sprint 2 created draft files in `pages/`. This path mismatch was identified in Sprint 2B and recorded as an infrastructure issue. Sprint 2C resolves it. No route status, indexation, sitemap, navigation, or governance state was changed — only the `content_file` field values.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`

**Sprint 2C constraints (all observed):**
- No route was published.
- No route `status` value was changed.
- No route `indexable` value was changed.
- No route `in_sitemap` value was changed.
- No route `in_navigation` value was changed.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- source_registry.json was not modified.
- Claim files were not modified.
- No new content pages were created.
- No generated HTML route pages were created.
- Templates were not modified.
- Root README.md was not modified.

**Path corrections (all 21 routes):**

- `home`: `main/content/en/home.md` → `main/content/en/pages/index.md`
- `what_is_sulfur`: `main/content/en/what-is-sulfur.md` → `main/content/en/pages/what-is-sulfur.md`
- `sulfur_compounds`: `main/content/en/sulfur-compounds.md` → `main/content/en/pages/sulfur-compounds.md`
- `sulfur_uses`: `main/content/en/sulfur-uses.md` → `main/content/en/pages/sulfur-uses.md`
- `what_is_bisulfid`: `main/content/en/what-is-bisulfid.md` → `main/content/en/pages/what-is-bisulfid.md`
- `bisulfid_vs_bisulfide`: `main/content/en/bisulfid-vs-bisulfide.md` → `main/content/en/pages/bisulfid-vs-bisulfide.md`
- `sulfid_vs_sulfide`: `main/content/en/sulfid-vs-sulfide.md` → `main/content/en/pages/sulfid-vs-sulfide.md`
- `bisulfide_hydrosulfide_sulfide`: `main/content/en/bisulfide-hydrosulfide-sulfide.md` → `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md`
- `sodium_bisulfide`: `main/content/en/sodium-bisulfide.md` → `main/content/en/pages/sodium-bisulfide.md`
- `disulfide_bonds`: `main/content/en/disulfide-bonds.md` → `main/content/en/pages/disulfide-bonds.md`
- `industrial_sulfur_systems`: `main/content/en/industrial-sulfur-systems.md` → `main/content/en/pages/industrial-sulfur-systems.md`
- `sulfur_safety_context`: `main/content/en/sulfur-safety-context.md` → `main/content/en/pages/sulfur-safety-context.md`
- `hydrogen_sulfide_risk`: `main/content/en/hydrogen-sulfide-risk.md` → `main/content/en/pages/hydrogen-sulfide-risk.md`
- `sds_and_sulfur_terms`: `main/content/en/sds-and-sulfur-terms.md` → `main/content/en/pages/sds-and-sulfur-terms.md`
- `protein_disulfide_structure`: `main/content/en/protein-disulfide-structure.md` → `main/content/en/pages/protein-disulfide-structure.md`
- `molybdenum_disulfide`: `main/content/en/molybdenum-disulfide.md` → `main/content/en/pages/molybdenum-disulfide.md`
- `german_english_chemical_terms`: `main/content/en/german-english-chemical-terms.md` → `main/content/en/pages/german-english-chemical-terms.md`
- `glossary`: `main/content/en/glossary.md` → `main/content/en/pages/glossary.md`
- `sources`: `main/content/en/sources.md` → `main/content/en/pages/sources.md`
- `newsletter`: `main/content/en/newsletter.md` → `main/content/en/pages/newsletter.md`
- `acquire`: `main/content/en/acquire.md` → `main/content/en/pages/acquire.md`

**Files created:**

- `main/data/ROUTE_CONTENT_PATH_ALIGNMENT_REPORT.md` — alignment report documenting issue, corrections, and governance state.

**Files updated:**

- `main/data/routes.json` — all 21 `content_file` paths corrected.
- `DECISION_LOG.md` — Sprint 2C entry appended.

**Not modified in this sprint:** route status values, indexation state, sitemap state, navigation state, sitemap_policy.json, navigation.json, source_registry.json, claim files, content draft pages, templates, scripts, doctrine files, ontology files, root README.md.

---

### 2026-05-15 — Sprint 3: Source Registry Seeded

**Decision:** Seed the first real source entries into `source_registry.json`, assign candidate `source_ids` to eight ontology terms in `sulfur_terms.json`, and register five terminology claims and three science claims in the claim registries. All claims remain `pending_review`. No claim is approved.

**Rationale:** The source registry must be populated before any claim can progress toward publication. Sprint 3 seeds authoritative dictionary, chemical nomenclature standard, and government scientific database sources that correspond to the terminology and chemical identity claims most central to the bisulfid.com domain thesis. All sources are `seeded` and `candidate` — none are final or permanently approved. No [SOURCE REQUIRED] markers were removed from draft content pages. No route was published. This sprint establishes the first layer of the three-layer source discipline: source_registry.json → claim registries → content pages.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 3 constraints (all observed):**
- No route was published.
- No route status, indexable, in_sitemap, or in_navigation value was changed.
- No claim was approved. All claims remain pending_review.
- No [SOURCE REQUIRED] marker was removed from any content page.
- No content pages were created or modified.
- All source entries carry status: seeded and source_lock_status: candidate.
- All ontology term statuses remain planned.
- No term was marked verified or published.
- market_claims.json was not modified.
- safety_claims.json was not modified.
- industry_claims.json was not modified.
- acquisition_claims.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- routes.json was not modified.
- root README.md was not modified.
- templates were not modified.
- scripts were not modified.
- No market statistics were added.
- No Gulf, Morocco, or China production or trade data was added.
- No acquisition-target company claims were added.
- No dependencies were added.
- No GitHub Actions were created.
- No HTML output was created.
- This sprint does not constitute publication readiness.

**Sources seeded (8):**

- `SRC-MW-BISULFIDE` — authoritative_dictionary — Merriam-Webster — bisulfide
- `SRC-MW-SULFIDE` — authoritative_dictionary — Merriam-Webster — sulfide
- `SRC-MW-BISULFITE` — authoritative_dictionary — Merriam-Webster — bisulfite
- `SRC-DUDEN-SULFID` — authoritative_dictionary — Duden — Sulfid
- `SRC-IUPAC-HYDROSULFIDES` — chemical_nomenclature_standard — IUPAC Gold Book — hydrosulfides
- `SRC-PUBCHEM-HYDROSULFIDE` — government_scientific_database — PubChem / NIH — Hydrosulfide
- `SRC-PUBCHEM-SODIUM-HYDROSULFIDE` — government_scientific_database — PubChem / NIH — Sodium hydrosulfide
- `SRC-NIST-HYDROGEN-SULFIDE` — government_scientific_database — NIST Chemistry WebBook — Hydrogen sulfide

**Terminology claims registered (5):** CLM-TERM-001 through CLM-TERM-005, all pending_review.

**Science claims registered (3):** CLM-SCI-001 through CLM-SCI-003, all pending_review.

**Ontology terms receiving candidate source_ids (8):** bisulfide, sulfide, sulfid, bisulfite_disambiguation, hydrosulfide, sodium_hydrosulfide, sodium_bisulfide, hydrogen_sulfide.

**Terms with no source_ids this sprint (6):** bisulfid (center node — highest priority for next source sprint), disulfide, disulfid, molybdenum_disulfide, molybdenum_disulfide_mos2, sulfur.

**Files created:**

- `main/data/SOURCE_REGISTRY_SEED_REPORT.md` — seed report documenting sources, claims, term mappings, gaps, and publication state.

**Files updated:**

- `main/data/sources/source_registry.json` — 8 sources added.
- `main/data/claims/terminology_claims.json` — 5 pending_review claims added.
- `main/data/claims/science_claims.json` — 3 pending_review claims added.
- `main/data/ontology/sulfur_terms.json` — candidate source_ids added to 8 terms.
- `DECISION_LOG.md` — Sprint 3 entry appended.

**Not modified in this sprint:** routes.json, sitemap_policy.json, navigation.json, market_claims.json, safety_claims.json, industry_claims.json, acquisition_claims.json, content draft pages, templates, scripts, doctrine files, root README.md.

---

### 2026-05-16 — Sprint 3 Patch: Source Governance Fields Completed

**Decision:** Add structured `use_for`, `do_not_use_for`, and `risk_notes` fields to all eight seeded source entries in `source_registry.json`.

**Summary:** Sprint 3 patch added structured use_for, do_not_use_for, and risk_notes fields to all seeded source entries, preserving candidate status and non-public claim state.

**Rationale:** Pre-merge review identified that the source schema required three structured governance fields per entry. The original Sprint 3 commit used a single freeform `notes` field. This patch adds the three required fields as arrays of strings to all 8 entries. The `notes` field was retained alongside the new structured fields. No source status, claim status, ontology term status, routes, content pages, or publication state was changed.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`

**Patch constraints (all observed):**
- Only `main/data/sources/source_registry.json` and `DECISION_LOG.md` were modified.
- No claim files were modified.
- No ontology files were modified.
- No routes were modified.
- No content pages were modified.
- All source entries retain `status: seeded`.
- All source entries retain `source_lock_status: candidate`.
- No new sources were added.
- No sources were removed.
- No claim was approved.
- No public route or sitemap state was changed.
- No dependencies, workflows, generated output, or README modifications.

**Files updated:**

- `main/data/sources/source_registry.json` — `use_for`, `do_not_use_for`, and `risk_notes` arrays added to all 8 source entries.
- `DECISION_LOG.md` — Sprint 3 patch entry appended.

---

### 2026-05-16 — Sprint 3B: Bisulfid Center Node Candidate Source Added

**Decision:** Add candidate source support for the `bisulfid` center node in `source_registry.json`, assign that source to `bisulfid.source_ids` in `sulfur_terms.json`, register a corresponding pending_review terminology claim, and document the sprint in `BISULFID_CENTER_SOURCE_REPORT.md`.

**Summary:** Sprint 3B addressed the highest-priority Sprint 3 source gap by adding candidate source support for the bisulfid center node. The source support is limited to German technical usage and does not make the center node verified. No routes were published. No claims were approved. No sitemap, navigation, content, market, safety, or acquisition state was changed. The center node still requires stronger source-locking before publication.

**Rationale:** The `bisulfid` center node is the conceptual and linguistic anchor of bisulfid.com. Sprint 3 explicitly flagged it as the highest-priority remaining source gap. No authoritative dictionary, nomenclature standard, or government scientific database entry directly under the term 'Bisulfid' was identified for seeding in this sprint. The Badger Meter German-language technical page was identified as the strongest currently available candidate source: it directly uses 'Bisulfid und Schwefelwasserstoff' in a German water-quality monitoring context. It was added as an `industry_publication` source with strict use limitations. The center node remains `planned` and requires a stronger tier-1 source before any publication pathway opens.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 3B constraints (all observed):**
- No route was published.
- No route status, indexable, in_sitemap, or in_navigation value was changed.
- No claim was approved. All claims remain pending_review.
- No [SOURCE REQUIRED] marker was removed from any content page.
- No content pages were created or modified.
- New source entry carries status: seeded and source_lock_status: candidate.
- bisulfid term status remains planned.
- bisulfid was not marked verified.
- market_claims.json was not modified.
- safety_claims.json was not modified.
- science_claims.json was not modified.
- industry_claims.json was not modified.
- acquisition_claims.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- routes.json was not modified.
- root README.md was not modified.
- templates were not modified.
- scripts were not modified.
- No market data was added.
- No Gulf, Morocco, or China production or trade data was added.
- No acquisition-target company claims were added.
- No dependencies were added.
- No GitHub Actions were created.
- No HTML output was created.
- No Wikipedia or AI summary sources were used.
- This sprint does not constitute publication readiness.

**Source added (1):**

- `SRC-BADGER-BISULFID-H2S` — industry_publication — Badger Meter — Messung von Bisulfid und Schwefelwasserstoff im Wasser

**Ontology update:** `bisulfid.source_ids` updated from `[]` to `["SRC-BADGER-BISULFID-H2S"]`. Status remains `planned`.

**Terminology claim added (1):** CLM-TERM-BISULFID-001, pending_review, candidate usage only.

**Remaining gap:** Bisulfid center node still requires a tier-1 source (Duden 'Bisulfid' entry, IUPAC direct entry, German regulatory database, or peer-reviewed academic reference) before the center node can be considered for source-locking.

**Files created:**

- `main/data/BISULFID_CENTER_SOURCE_REPORT.md` — source evaluation report for the bisulfid center node.

**Files updated:**

- `main/data/sources/source_registry.json` — SRC-BADGER-BISULFID-H2S added.
- `main/data/ontology/sulfur_terms.json` — bisulfid.source_ids updated; notes updated.
- `main/data/claims/terminology_claims.json` — CLM-TERM-BISULFID-001 added, pending_review.
- `DECISION_LOG.md` — Sprint 3B entry appended.

**Not modified in this sprint:** routes.json, sitemap_policy.json, navigation.json, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json, content draft pages, templates, scripts, doctrine files, root README.md.

---

### 2026-05-16 — Sprint 3C: Source-to-Claim Governance Alignment Completed

**Decision:** Review the seeded source registry, pending terminology claims, pending science claims, ontology source mappings, and English draft pages. Produce a source-to-claim alignment report. Correct structural inconsistencies in claim entries.

**Summary:** Sprint 3C reviewed the seeded source registry, pending terminology claims, pending science claims, ontology source mappings, and English draft pages. The sprint produced a source-to-claim alignment report. No claims were approved. No routes were published. No sitemap or navigation state was changed. No content pages were modified. No market, safety, acquisition, or industrial data was added.

**Structural corrections made:**
- `main/data/claims/terminology_claims.json`: CLM-TERM-001 through CLM-TERM-005 were missing three governance fields (`allowed_pages`, `prohibited_uses`, `risk_level`) present in CLM-TERM-BISULFID-001. These fields were added to all five claims. No claim status was changed.
- `main/data/claims/science_claims.json`: CLM-SCI-001 through CLM-SCI-003 were missing the same three governance fields. These fields were added to all three claims. No claim status was changed.

**Key findings:**
- All 9 source entries confirmed complete with required fields and appropriate scope.
- 6 terminology claims and 3 science claims all remain pending_review.
- No claim uses out-of-scope source material (no market data, safety advice, medical claims, or bisulfite data used as bisulfide data).
- No ontology term is marked verified.
- bisulfid center node remains planned with candidate source support only.
- sources.md contains a stale statement (“The source registry is not populated yet”) — correction deferred to a future content update sprint.
- sulfid_vs_sulfide is the most heavily blocked page: three distinct source gaps with no registered claims covering Oxide/Oxid or Chloride/Chlorid examples or a formal suffix-pattern nomenclature standard.

**Rationale:** A governance alignment review was required before any claim approval sprint can proceed. Claims missing `allowed_pages`, `prohibited_uses`, and `risk_level` cannot be safely approved or scoped to pages. Correcting the structural inconsistency in this sprint ensures the claim registries are in a state where future approval decisions can be made against a complete schema.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 3C constraints (all observed):**
- No route was published.
- No route status, indexable, in_sitemap, or in_navigation value was changed.
- No claim was approved. All claims remain pending_review.
- Claim registries remain inactive.
- No [SOURCE REQUIRED] marker was removed from any content page.
- No content pages were created or modified.
- source_registry.json was not modified.
- ontology/sulfur_terms.json was not modified.
- routes.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- market_claims.json was not modified.
- safety_claims.json was not modified.
- industry_claims.json was not modified.
- acquisition_claims.json was not modified.
- root README.md was not modified.
- No dependencies, workflows, or generated output were created.
- No Wikipedia or AI summary sources were used.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/data/SOURCE_CLAIM_ALIGNMENT_REPORT.md` — source-to-claim alignment report.

**Files updated:**

- `main/data/claims/terminology_claims.json` — `allowed_pages`, `prohibited_uses`, `risk_level` added to CLM-TERM-001 through CLM-TERM-005.
- `main/data/claims/science_claims.json` — `allowed_pages`, `prohibited_uses`, `risk_level` added to CLM-SCI-001 through CLM-SCI-003.
- `DECISION_LOG.md` — Sprint 3C entry appended.

**Not modified in this sprint:** routes.json, sitemap_policy.json, navigation.json, source_registry.json, ontology/sulfur_terms.json, market_claims.json, safety_claims.json, industry_claims.json, acquisition_claims.json, content draft pages, templates, scripts, doctrine files, root README.md.

---

### 2026-05-16 — Sprint 3D: Sources Page Draft Statement Corrected

**Decision:** Correct a stale statement in `main/content/en/pages/sources.md` that said “The source registry is not populated yet.” after Sprint 3 and Sprint 3B had populated the registry with seeded candidate sources.

**Summary:** Sprint 3D corrected a stale non-public draft statement in sources.md after the source registry gained seeded candidate sources. The page now distinguishes candidate source entries from approved publication claims. No route was published. No claim was approved. No sitemap, navigation, source registry, or claim registry state changed.

**Rationale:** Sprint 3C’s `SOURCE_CLAIM_ALIGNMENT_REPORT.md` explicitly flagged the statement as inaccurate following the source seeding work of Sprint 3 and Sprint 3B. Leaving a factually incorrect description of the source registry in a governed draft page creates an internal inconsistency that must be resolved before any publication sprint proceeds.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`

**Sprint 3D constraints (all observed):**
- No route was published.
- No route status, indexable, in_sitemap, or in_navigation value was changed.
- No claim was approved.
- No [SOURCE REQUIRED] marker was removed.
- No other content pages were modified.
- source_registry.json was not modified.
- ontology/sulfur_terms.json was not modified.
- routes.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- market_claims.json was not modified.
- safety_claims.json was not modified.
- industry_claims.json was not modified.
- science_claims.json was not modified.
- terminology_claims.json was not modified.
- acquisition_claims.json was not modified.
- root README.md was not modified.
- No dependencies, workflows, or generated output were created.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/data/SOURCES_PAGE_DRAFT_CORRECTION_REPORT.md` — correction report.

**Files updated:**

- `main/content/en/pages/sources.md` — “Current Registry Status” section rewritten; stale statement removed; new wording distinguishes candidate sources from approved claims.
- `DECISION_LOG.md` — Sprint 3D entry appended.

**Not modified in this sprint:** source_registry.json, routes.json, sitemap_policy.json, navigation.json, claim registries, ontology files, templates, scripts, doctrine files, root README.md. No other content pages were modified.

---

### 2026-05-16 — Sprint 4A: German Suffix Pattern Candidate Sources Added

**Decision:** Add candidate lexical source support for German `Oxid` and `Chlorid`, align those sources with existing `Sulfid` support as a cautious German `-id` lexical comparison set, and add English IUPAC nomenclature context as candidate support only.

**Summary:** Sprint 4A added candidate lexical source support for German Oxid and Chlorid and aligned these with existing Sulfid support as a cautious German -id lexical comparison set. No formal German suffix rule was claimed. No claims were approved. No routes were published. No content pages were modified. The sulfid-vs-sulfide draft remains blocked until stronger nomenclature source-locking is completed.

**Rationale:** Sprint 3C identified `sulfid_vs_sulfide` as the most blocked draft page because its Oxide/Oxid and Chloride/Chlorid examples lacked registered source and claim support. Duden dictionary entries can support individual German lexical forms, but not a formal chemical nomenclature rule. The IUPAC 1971 source can provide English `-ide` nomenclature context only and cannot prove a German suffix-compression rule.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4A constraints (all observed):**
- No route was published.
- No route status, indexable, in_sitemap, or in_navigation value was changed.
- routes.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- No claim was approved. All new claims remain pending_review.
- Claim registries remain inactive.
- No [SOURCE REQUIRED] marker was removed from any content page.
- No content pages were created or modified.
- No ontology term was marked verified.
- No market_claims, safety_claims, science_claims, industry_claims, or acquisition_claims files were modified.
- No market data was added.
- No Gulf, Morocco, China, production, trade, CAGR, or market-share data was added.
- No acquisition-target company claims were added.
- Root README.md was not modified.
- Templates were not modified.
- No generated HTML route pages were created.
- No dependencies were added.
- No GitHub Actions workflows were created.
- No Wikipedia or AI summary sources were used.
- No formal German suffix rule source was found.
- This sprint does not constitute publication readiness.

**Sources added (3):**

- `SRC-DUDEN-OXID` — authoritative_dictionary — Duden — Oxid.
- `SRC-DUDEN-CHLORID` — authoritative_dictionary — Duden — Chlorid.
- `SRC-IUPAC-INORGANIC-NOMENCLATURE-1971` — chemical_nomenclature_standard — IUPAC / Pure and Applied Chemistry — Nomenclature of Inorganic Chemistry.

**Terminology claims added (4):**

- `CLM-TERM-OXID-001` — pending_review lexical claim for Oxid.
- `CLM-TERM-CHLORID-001` — pending_review lexical claim for Chlorid.
- `CLM-TERM-GERMAN-ID-PATTERN-001` — pending_review cautious lexical comparison-set claim for Sulfid, Oxid, and Chlorid.
- `CLM-TERM-ENGLISH-IDE-CONTEXT-001` — pending_review English -ide nomenclature context claim.

**Files created:**

- `main/data/SULFID_SUFFIX_SOURCE_REPORT.md` — Sprint 4A source report and publication readiness conclusion.

**Files updated:**

- `main/data/sources/source_registry.json` — Duden Oxid, Duden Chlorid, and IUPAC 1971 candidate sources added.
- `main/data/claims/terminology_claims.json` — four pending_review terminology claims added.
- `DECISION_LOG.md` — Sprint 4A entry appended.

**Not modified in this sprint:** routes.json, sitemap_policy.json, navigation.json, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json, ontology files, content draft pages, templates, scripts, doctrine files, root README.md.

---

### 2026-05-16 — Sprint 4B: Formal German Nomenclature Source Search Completed

**Decision:** Evaluate stronger German nomenclature sources for the `-id` pattern behind the `sulfid_vs_sulfide` draft and document the source-category gap for academic teaching and textbook/book-chapter materials.

**Summary:** Sprint 4B evaluated stronger German nomenclature sources for the -id pattern behind the sulfid-vs-sulfide draft. No sources were added because the evaluated German academic teaching and book/chapter sources do not fit an existing governed source category without inventing or stretching the registry taxonomy. No formal German suffix rule was claimed. No claims were approved. No routes were published. No content pages were modified. The sulfid-vs-sulfide draft remains non-public until source-locking and claim approval are completed.

**Rationale:** Sprint 4A established lexical candidate support for `Sulfid`, `Oxid`, and `Chlorid`, but did not close the formal German nomenclature gap. Sprint 4B searched for stronger German support and found potentially useful academic or teaching sources, but the current source registry categories do not include academic teaching PDFs, textbook chapters, or book chapters as governed source types unless they qualify as formal chemical nomenclature standards or peer-reviewed journals. No new category was created.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4B constraints (all observed):**
- source_registry.json was not modified.
- No unsupported source category was invented.
- No source was added, so no source was marked final, locked, approved, verified, or public-ready.
- terminology_claims.json was not modified.
- No claim was approved.
- Claim registries remain inactive.
- No market_claims, safety_claims, science_claims, industry_claims, or acquisition_claims files were modified.
- sulfur_terms.json was not modified.
- routes.json was not modified.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No Wikipedia or AI summary sources were used as sources.
- No market data, Gulf data, Morocco data, China data, production data, trade data, CAGR data, or market-share data was added.
- No acquisition-target company claims were added.
- This sprint does not constitute publication readiness.

**Sources evaluated but not added:**

- `SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR` — academic/teaching PDF; category not currently governed.
- `SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN` — university teaching PDF; category not currently governed.
- `SRC-SPRINGER-JANDER-ANORGANISCHE-NOMENKLATUR-ID` — book/chapter or textbook material; category not currently governed.
- `SRC-IUPAC-BRIEF-GUIDE-INORGANIC-2005` — English IUPAC nomenclature context only; not distinct German suffix-rule authority beyond the Sprint 4A IUPAC context source.

**Claims added:** None.

**Files created:**

- `main/data/GERMAN_NOMENCLATURE_SOURCE_SEARCH_REPORT.md` — Sprint 4B source-search report documenting evaluated sources, category gap, formal-source status, and publication readiness.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4B entry appended.

**Not modified in this sprint:** source_registry.json, terminology_claims.json, routes.json, sitemap_policy.json, navigation.json, ontology files, content draft pages, templates, scripts, doctrine files, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Sprint 4C: Source Category Governance Expansion Reviewed

**Decision:** Review whether Bisulfid should later expand its source governance system to include academic teaching references, textbook references, or technical educational references.

**Summary:** Sprint 4C reviewed whether Bisulfid should expand its source governance system to include academic teaching references, textbook references, or technical educational references. No source category was added. No source was added. No claim was added or approved. No route was published. No content page was modified. The sprint produced a governance review report to guide a future implementation decision.

**Rationale:** Sprint 4B identified useful German academic/teaching/book sources for the `-id` nomenclature pattern, but those sources were not added because current source categories do not govern those source types. Sprint 4C evaluates whether a future controlled category could preserve useful instructional evidence without weakening source discipline or treating teaching material as formal nomenclature authority.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4C constraints (all observed):**
- `SOURCE_CATEGORY_GOVERNANCE_REVIEW.md` was created.
- SOURCE_POLICY.md was not modified.
- source_registry.json was not modified.
- No source category was added.
- No source entries were added.
- terminology_claims.json was not modified.
- No claim entries were added.
- No claim was approved.
- Claim registries remain inactive.
- routes.json was not modified.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market data or acquisition-target company claims were added.
- This sprint does not constitute publication readiness.

**Recommendation:** Add no category in Sprint 4C. Consider a future narrow `academic_teaching_reference` category, with a separate `textbook_reference` category or sub-scope only if explicit safeguards are implemented first. Any such category should remain candidate-only by default and should not approve claims alone or prove formal nomenclature authority.

**Files created:**

- `main/data/SOURCE_CATEGORY_GOVERNANCE_REVIEW.md` — governance review report for possible future source category expansion.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4C entry appended.

**Not modified in this sprint:** SOURCE_POLICY.md, source_registry.json, terminology_claims.json, routes.json, sitemap_policy.json, navigation.json, ontology files, content draft pages, templates, scripts, doctrine files, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Sprint 4D: Controlled Academic Teaching Source Category Implemented

**Decision:** Implement a narrow governed source category named `academic_teaching_reference`.

**Summary:** Sprint 4D implemented a narrow governed source category named academic_teaching_reference. The category is candidate-only and may support source-search review or cautious educational terminology context, but it cannot serve as formal nomenclature authority, cannot approve claims alone, cannot publish routes, and cannot remove [SOURCE REQUIRED] markers by itself. No source entries were added. No claims were added or approved. No routes were published. No content pages were modified.

**Rationale:** Sprint 4B identified useful German academic/teaching/book sources that did not fit existing source categories, and Sprint 4C recommended a narrow controlled category rather than a broad educational catch-all. Sprint 4D implements the category-level governance needed before any future sprint evaluates specific academic teaching sources.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4D constraints (all observed):**
- SOURCE_POLICY.md was modified only to add the governed `academic_teaching_reference` category and its constraints.
- source_registry.json remains valid JSON.
- `academic_teaching_reference` was added to the governed source categories.
- No source entries were added.
- No existing source entry status was changed.
- No source was marked final, locked, approved, verified, or public-ready.
- terminology_claims.json was not modified.
- No claim entries were added.
- No claim was approved.
- Claim registries remain inactive.
- routes.json was not modified.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market data or acquisition-target company claims were added.
- No actual FH Münster, Rostock, Springer/Jander, or other source entries were added.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/data/ACADEMIC_SOURCE_CATEGORY_IMPLEMENTATION_REPORT.md` — implementation report for the controlled academic teaching source category.

**Files updated:**

- `doctrine/SOURCE_POLICY.md` — `academic_teaching_reference` added as a governed candidate-only category with constraints.
- `main/data/sources/source_registry.json` — `academic_teaching_reference` added to `source_categories`; no source entries added.
- `DECISION_LOG.md` — Sprint 4D entry appended.

**Not modified in this sprint:** terminology_claims.json, routes.json, sitemap_policy.json, navigation.json, ontology files, content draft pages, templates, scripts, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Sprint 4E: Academic Teaching Candidate Sources Registered

**Decision:** Register selected German academic teaching references under the governed `academic_teaching_reference` category.

**Summary:** Sprint 4E registered candidate academic teaching references under the newly governed academic_teaching_reference category where permitted by SOURCE_POLICY.md. The sources may support draft/source-search review and cautious educational terminology context only. They do not establish formal nomenclature authority, do not approve claims alone, do not publish routes, and do not remove [SOURCE REQUIRED] markers by themselves. No claims were approved. No routes were published. No content pages were modified.

**Rationale:** Sprint 4D created a narrow candidate-only category for university and academic instructional chemistry sources. Sprint 4E applies that category to FH Münster and Universität Rostock teaching references while leaving Springer/Jander unregistered because publisher-hosted textbook/book-chapter material is not clearly governed by the current category.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4E constraints (all observed):**
- source_registry.json remains valid JSON.
- All newly added source entries use `category: academic_teaching_reference`.
- Every new source has `status: seeded` and `source_lock_status: candidate`.
- Every new source has `use_for`, `do_not_use_for`, and `risk_notes` arrays.
- No new source is marked final, locked, approved, verified, or public-ready.
- No source outside the governed category boundary was added.
- Springer/Jander was not added because SOURCE_POLICY.md does not clearly govern textbook/book-chapter sources under `academic_teaching_reference`.
- terminology_claims.json remains valid JSON.
- New claims are status: pending_review only.
- No claim was approved.
- Claim registry remains inactive.
- market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, and acquisition_claims.json were not modified.
- SOURCE_POLICY.md was not modified.
- sulfur_terms.json was not modified.
- routes.json was not modified.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety, medical, procurement, handling, Gulf, Morocco, China, production, trade, CAGR, market-share, or acquisition-target claims were added.
- This sprint does not constitute publication readiness.

**Sources added (2):**

- `SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR` — academic_teaching_reference — FH Münster — Anorganische Nomenklatur.
- `SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN` — academic_teaching_reference — Universität Rostock — Materialdesign / Nomenklatur.

**Sources evaluated but not added:**

- `SRC-SPRINGER-JANDER-ANORGANISCHE-NOMENKLATUR-ID` — not registered because textbook/book-chapter material is not clearly governed by the current `academic_teaching_reference` category.

**Claims added (1):**

- `CLM-TERM-GERMAN-ID-ACADEMIC-001` — pending_review candidate academic teaching support only.

**Files created:**

- `main/data/ACADEMIC_TEACHING_SOURCE_REGISTRATION_REPORT.md` — Sprint 4E source registration report.

**Files updated:**

- `main/data/sources/source_registry.json` — two academic teaching candidate source entries added.
- `main/data/claims/terminology_claims.json` — one pending_review terminology claim added.
- `DECISION_LOG.md` — Sprint 4E entry appended.

**Not modified in this sprint:** SOURCE_POLICY.md, routes.json, sitemap_policy.json, navigation.json, ontology files, content draft pages, templates, scripts, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Sprint 4F: Academic Source Claim Boundaries Reviewed

**Decision:** Review and document the claim boundaries of the registered `academic_teaching_reference` sources before any claim approval, source-locking, content edit, or publication decision.

**Summary:** Sprint 4F reviewed the claim boundaries of the newly registered academic_teaching_reference sources. The sprint documented what FH Münster and Universität Rostock may support as candidate academic teaching context, and what they cannot support without stronger formal authority. No claims were approved. No source entries were modified. No routes were published. No content pages were modified. [SOURCE REQUIRED] markers remain in place.

**Rationale:** Sprint 4E added candidate academic teaching references and a pending-review claim. Before any future source-locking or content sprint, the project needs an explicit boundary record stating that these sources can support cautious educational context only, not formal DIN, official German IUPAC, GDCh, route publication, ontology verification, or marker removal.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4F constraints (all observed):**
- `ACADEMIC_SOURCE_CLAIM_BOUNDARY_REPORT.md` was created.
- SOURCE_POLICY.md was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- No source entries were added.
- No source entries were modified.
- No claim entries were added.
- No claim was approved.
- Claim registries remain inactive.
- routes.json was not modified.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety, medical, procurement, handling, or acquisition claims were added.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/data/ACADEMIC_SOURCE_CLAIM_BOUNDARY_REPORT.md` — boundary report for academic teaching sources and `CLM-TERM-GERMAN-ID-ACADEMIC-001`.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4F entry appended.

**Not modified in this sprint:** SOURCE_POLICY.md, source_registry.json, terminology_claims.json, routes.json, sitemap_policy.json, navigation.json, ontology files, content draft pages, templates, scripts, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Sprint 4G: German-English Chemical Terms Draft Path Reviewed

**Decision:** Review the missing German-English chemical terms draft path and route/content alignment state without creating content or changing route governance.

**Summary:** Sprint 4G reviewed the missing German-English chemical terms draft path identified in Sprint 4F. The sprint diagnosed the route/content alignment state without creating the missing page, modifying routes, publishing any route, approving claims, or removing [SOURCE REQUIRED] markers. The result will guide a future content-alignment sprint.

**Rationale:** `routes.json` contains a planned `german_english_chemical_terms` route pointing to `main/content/en/pages/german-english-chemical-terms.md`, but the content file does not exist. Internal links reference the route by `route_id`, and the route remains planned and non-public. The review also found that this is part of a broader planned-route/content inventory gap, not a unique missing page.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4G constraints (all observed):**
- `GERMAN_ENGLISH_TERMS_DRAFT_PATH_REVIEW.md` was created.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were created.
- No content pages were modified.
- `main/content/en/pages/german-english-chemical-terms.md` was not created.
- No [SOURCE REQUIRED] markers were removed.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- This sprint does not constitute publication readiness.

**Finding:** `german_english_chemical_terms` is a planned route with a valid expected content path, but the draft file is missing. It is one of multiple planned English routes without content drafts.

**Files created:**

- `main/data/GERMAN_ENGLISH_TERMS_DRAFT_PATH_REVIEW.md` — diagnostic route/content path review for `german_english_chemical_terms`.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4G entry appended.

**Not modified in this sprint:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, source_registry.json, terminology_claims.json, sulfur_terms.json, content pages, templates, scripts, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — German-English Chemical Terms Non-Public Draft Created

**Decision:** Create the missing English draft page for `german_english_chemical_terms` as a terminology-control file aligned with Sprint 4G route/content path findings, without changing route metadata, link registries, or claim state.

**Summary:** Sprint 4H created the missing non-public English draft for `german_english_chemical_terms` at `main/content/en/pages/german-english-chemical-terms.md`. The route remains planned, indexable remains false, sitemap inclusion remains false, and the draft is not publication-ready. No claims were approved. No source entries were modified. No routes or internal links were changed. [SOURCE REQUIRED] markers remain in place.

**Rationale:** Sprint 4G diagnosed a missing `content_file` at the governed path while `routes.json` already pointed to it. Adding the draft file closes that gap for future source-locking and Quality Gate work. The page is explicitly non-public, cautious, and marked with [SOURCE REQUIRED] where factual support is not yet approved; academic teaching sources are not conflated with DIN or official German IUPAC authority, and no universal English-to-German suffix rule is asserted as fact.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4H constraints (all observed):**
- `main/content/en/pages/german-english-chemical-terms.md` was created with required frontmatter.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No [SOURCE REQUIRED] markers were removed from any page.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety, medical, procurement, handling, or acquisition claims were added.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/content/en/pages/german-english-chemical-terms.md` — non-public terminology-control draft for `german_english_chemical_terms`.
- `main/data/GERMAN_ENGLISH_TERMS_DRAFT_CREATION_REPORT.md` — sprint record and remaining blockers.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4H entry appended.

**Not modified in this sprint:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, source_registry.json, terminology_claims.json, sulfur_terms.json, templates, scripts, other content draft pages (except the new file listed above), root README.md, package files, workflows, generated output, ontology files, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — English Draft Inventory Reviewed

**Decision:** Map all planned English routes to draft file presence, content-directory inventory, and internal link dependencies without creating or editing drafts or changing route metadata.

**Summary:** Sprint 4I reviewed the English planned route inventory and mapped routes to existing draft content files. The sprint identified which planned English routes already have drafts, which routes remain missing drafts, and which routes should be prioritized in future draft-creation sprints. No content pages were created or modified. No routes were published. No claims were approved. [SOURCE REQUIRED] markers remain in place.

**Rationale:** Sprint 4G framed a broader route/content inventory gap beyond `german_english_chemical_terms`. Sprint 4H created that one missing draft; remaining English routes still lack `content_file` bodies. A consolidated table and link-demand view reduces ad hoc planning risk and keeps prioritization explicit while routes stay `planned` and non-indexable.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4I constraints (all observed):**
- `ENGLISH_DRAFT_INVENTORY_REVIEW.md` was created.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were created.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety, medical, procurement, handling, or acquisition claims were added.
- This sprint does not constitute publication readiness.

**Finding (English):** 21 `language: en` routes; 7 draft-backed; 14 missing `content_file`. Highest planned link demand among missing routes targets `glossary` (18 referring link groups), then `sodium_bisulfide` (7), `industrial_sulfur_systems` (6), and `sulfur_safety_context` (5). `newsletter` has no incoming planned internal link targets.

**Files created:**

- `main/data/ENGLISH_DRAFT_INVENTORY_REVIEW.md` — English planned-route draft inventory and prioritization notes.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4I entry appended.

**Not modified in this sprint:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, source_registry.json, terminology_claims.json, sulfur_terms.json, content pages, templates, scripts, root README.md, package files, workflows, generated output, ontology files, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Terminology Reference Spine Batch 1 Established

**Decision:** Create the first batch of non-public English drafts for the terminology reference spine (`glossary`, `sulfur_compounds`, `bisulfide_hydrosulfide_sulfide`) as internal reference infrastructure without changing route metadata, link registries, or claim state.

**Summary:** Sprint 4J added governed draft bodies at the exact `content_file` paths declared in `routes.json` for `glossary`, `sulfur_compounds`, and `bisulfide_hydrosulfide_sulfide`. The drafts function as a terminology chamber scaffold, a sulfur-compound scope map, and a bisulfide/hydrosulfide/sulfide disambiguation authority file. All remain non-public, non-indexable, not sitemap-listed, and not publication-ready. No routes were published. No claims were approved. No registries were modified. [SOURCE REQUIRED] markers remain on all relevant drafts and were not removed from other pages.

**Rationale:** Sprint 4I showed heavy planned internal-link demand on `glossary` and related terminology routes. Establishing these three drafts closes the highest-priority missing-body gap for the terminology spine while keeping strict separation from safety handling, market data, and publication workflows.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4J constraints (all observed):**
- Three target `content_file` drafts created with required frontmatter; paths verified against `routes.json`; no pre-existing files overwritten.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No [SOURCE REQUIRED] markers were removed from any page.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety-handling, medical, procurement, or acquisition-target content was added.
- No raw URLs or publication-assuming links were added.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/content/en/pages/glossary.md` — controlled terminology chamber draft.
- `main/content/en/pages/sulfur-compounds.md` — sulfur terminology scope map draft.
- `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md` — disambiguation authority draft.
- `main/data/TERMINOLOGY_REFERENCE_SPINE_BATCH_1_REPORT.md` — sprint record.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4J entry appended.

**Not modified in this sprint:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, source_registry.json, terminology_claims.json, sulfur_terms.json, templates, scripts, other existing content draft pages (except the three new files listed above), root README.md, package files, workflows, generated output, ontology files, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Terminology Reference Spine Batch 1 Completion Patch

**Decision:** Close Sprint 4J pre-merge acceptance gaps by expanding terminology spine draft coverage and report inventory accounting without publishing routes, changing registries, or removing [SOURCE REQUIRED] markers.

**Summary:** This patch completed the Sprint 4J reference-spine acceptance gaps by expanding the glossary term coverage, strengthening the sulfur compound scope map, preserving the bisulfite disambiguation boundary in the bisulfide/hydrosulfide/sulfide draft, and completing the Sprint 4J report with the remaining missing draft count. No routes were published. No claims were approved. No registries or route records were modified. [SOURCE REQUIRED] markers remain in place.

**Rationale:** Initial batch 4J drafts met governance scope but lacked full controlled-term tables, explicit scope-map sections, dedicated non-claim and registry-status sections on the disambiguation page, bisulfite separation language, and explicit 14/3/11 missing-draft accounting in the sprint report.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Patch constraints (all observed):**
- Only the three spine drafts, `TERMINOLOGY_REFERENCE_SPINE_BATCH_1_REPORT.md`, and `DECISION_LOG.md` were edited for this patch.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No [SOURCE REQUIRED] markers were removed from any page.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety-handling, medical, procurement, production, trade, CAGR, market-share, or acquisition-target content was added.
- No raw URLs or publication-assuming links were added.
- This patch does not constitute publication readiness.

**Files updated:**

- `main/content/en/pages/glossary.md` — expanded controlled term table and distinction rules.
- `main/content/en/pages/sulfur-compounds.md` — expanded terminology groups and teaching vs authority section.
- `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md` — bisulfite boundary; what this page does not claim; source and claim status.
- `main/data/TERMINOLOGY_REFERENCE_SPINE_BATCH_1_REPORT.md` — spine vs generic framing; 11 remaining missing drafts; blockers; no publication recommendation.
- `DECISION_LOG.md` — this patch entry appended.

**Not modified in this patch:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, source_registry.json, terminology_claims.json, sulfur_terms.json, templates, other content draft pages outside the three spine files above, root README.md, package files, workflows, generated output, ontology files, claim data JSON beyond those listed, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Terminology Reference Spine Boundaries Reviewed

**Decision:** Read-only boundary review of the first terminology reference spine (`glossary`, `sulfur_compounds`, `bisulfide_hydrosulfide_sulfide`) after Sprint 4J, without creating or modifying content pages or changing route or registry state.

**Summary:** Sprint 4K reviewed the first non-public terminology reference spine created in Sprint 4J. The review confirmed the glossary, sulfur_compounds, and bisulfide_hydrosulfide_sulfide drafts remain non-public reference infrastructure and not publication-ready content. The sprint documented claim boundaries, source boundaries, bisulfite disambiguation boundaries, and future internal reference roles. No content pages were created or modified. No claims were approved. No routes were published. [SOURCE REQUIRED] markers remain in place.

**Rationale:** Before expanding the English draft inventory (11 routes still missing `content_file` bodies), the project needs a recorded check that spine copy stays within terminology governance, does not imply approved claims, and does not drift into generic chemistry, safety, or market content.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/SOURCE_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4K constraints (all observed):**
- `TERMINOLOGY_REFERENCE_SPINE_BOUNDARY_REVIEW.md` was created.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified (path: `main/data/sources/source_registry.json` on disk).
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were created.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety, medical, procurement, acquisition, production, or trade content was added.
- No raw URLs or publication-assuming links were added by this sprint.
- This sprint does not constitute publication readiness.

**Finding:** Spine drafts align with terminology-first infrastructure roles; bisulfite boundary and teaching-vs-authority separation are preserved in copy; registries remain unchanged and inactive for approval work.

**Files created:**

- `main/data/TERMINOLOGY_REFERENCE_SPINE_BOUNDARY_REVIEW.md` — boundary review record for the first terminology reference spine.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4K entry appended.

**Not modified in this sprint:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, `main/data/sources/source_registry.json`, terminology_claims.json, sulfur_terms.json, all English and other content draft pages, templates, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Core Term Drafts Batch 2 Sprint Record (Route Targets Absent)

**Decision:** Execute Sprint 4L pre-flight against `main/data/routes.json` before drafting core term pages; do not create orphan `content_file` bodies when `route_id` records are missing.

**Summary:** Sprint 4L targeted non-public English core term drafts for `bisulfid`, `sulfid`, and `hydrosulfide`, but pre-flight review found **none** of those `route_id` values in `routes.json`. Per project rules, no `bisulfid.md`, `sulfid.md`, or `hydrosulfide.md` files were added. The sprint created `CORE_TERM_DRAFTS_BATCH_2_REPORT.md` documenting the blocker, nearest existing related routes (`what_is_bisulfid`, `sulfid_vs_sulfide`, `bisulfide_hydrosulfide_sulfide`), and recommended follow-up. **Remaining missing English draft count stays 11** (unchanged from post–Sprint 4J). No routes were published. No claims were approved. No source entries, route records, internal links, sitemap policy, navigation, hreflang, translation registry, ontology, or claim registries were modified. `[SOURCE REQUIRED]` markers on existing pages remain unchanged.

**Rationale:** Core term drafts must map 1:1 to authoritative `content_file` paths in `routes.json`. Inventing routes or orphan markdown files would break inventory integrity and violate Sprint 4L constraints.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/SOURCE_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4L validation (observed where applicable):**

- Target `route_id` values `bisulfid`, `sulfid`, and `hydrosulfide` **do not** exist in `routes.json` — **blocker recorded**; no page files created for those names.
- All **existing** routes remain `status: planned`, `language: en` where declared, `indexable: false`, `in_sitemap: false` — verified on read of `routes.json`; **no edits** made.
- **No** new content pages created; **no** existing content pages modified.
- **No** `[SOURCE REQUIRED]` markers removed from any file.
- **No** raw URLs or publication-assuming links added by this sprint.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- No claim has `status: approved`; claim registries remain **inactive**.
- No generated HTML pages, dependencies, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `main/data/CORE_TERM_DRAFTS_BATCH_2_REPORT.md` exists; states remaining missing draft count **11** after this sprint; **8** is the modeled count only if all three target routes had existed and all three drafts had been created.
- `DECISION_LOG.md` updated with this entry.
- This sprint does **not** recommend publication.

**Files created:**

- `main/data/CORE_TERM_DRAFTS_BATCH_2_REPORT.md` — Sprint 4L record; pre-flight route absence; next steps.

**Files updated:**

- `DECISION_LOG.md` — this entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, all existing content draft pages, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-18 — Sovereign Reference Corpus Architecture Established

**Decision:** Record Bisulfid.com as a **large, sovereign-grade, multilingual chemical-language reference corpus** with **300 governed pages** as the **minimum public launch threshold**, not the final ambition, and scale horizons toward **500 / 1,000 / 3,000+** pages only under strict quality gates.

**Summary:** Sprint **5A** established long-term corpus architecture and launch-cohort blueprint documentation. The sprint defined the difference between **minimum public launch cohort**, **long-term reference corpus**, and **full authority system**; specified multilingual layers (English spine, German identity, Arabic, Chinese, Japanese technical references); documented expansion rules, anti-thin and anti-generic discipline, and launch thresholds. **CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md** lists **307** proposed page concepts (blueprint only—**not** added to `routes.json`). **No** routes were published. **No** content pages were created or modified. **No** claims were approved. **No** registry files (`routes.json`, `internal_links.json`, sitemap/navigation, source or claim registries, ontology) were modified. **No** public HTML or dependencies were added.

**Rationale:** The owner rejects weak visibility and generic chemistry sites; reference trust requires doctrine-first scaling and a planned path to a **large** corpus—not a stop at 300 pages.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/SOURCE_POLICY.md`, `doctrine/QUALITY_GATE.md`, `doctrine/MULTILINGUAL_POLICY.md`

**Sprint 5A validation (observed where applicable):**

- `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md` created; states **300 pages** = **minimum launch cohort**, **not** the final goal.
- `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` created; **≥ 300** proposed concepts (**307** rows).
- `main/data/CORPUS_EXPANSION_MODEL.md` created; defines expansion beyond 300 pages with strict gates.
- `main/data/CORPUS_LAUNCH_THRESHOLD.md` created; minimum threshold and no-publication conditions.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified** (this sprint).
- **No** content under `main/content/` created or modified.
- **No** `[SOURCE REQUIRED]` markers removed.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true`.
- **No** generated HTML pages, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `DECISION_LOG.md` updated with this entry.

**Files created:**

- `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md` — corpus thesis, layers, categories, multilingual model, authority standard, risks, next sprint.
- `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` — launch cohort blueprint table (**307** concepts).
- `main/data/CORPUS_EXPANSION_MODEL.md` — expansion horizons and governance rules.
- `main/data/CORPUS_LAUNCH_THRESHOLD.md` — launch and no-go gates.

**Files updated:**

- `DECISION_LOG.md` — Sprint 5A entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, all content draft pages, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-19 — Launch Cohort Blueprint Quality Reviewed

**Decision:** Record a **blueprint-only quality review** of the **307** proposed launch-cohort concepts from Sprint **5A**; **do not** treat the raw blueprint as **launch-cohort-ready** without refinement.

**Summary:** Sprint **5B** evaluated `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` against sovereign-grade doctrine: thesis fit, anti-thin / anti-generic posture, source and claim risk, multilingual discipline (controlled terminology vs translation spam), duplicate/merge needs, and utility pages vs reference pages. Findings are recorded in **`LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md`** and **`LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md`**. **No** routes were created. **No** content pages were created or modified. **No** claims were approved. **No** registries (`routes.json`, `internal_links.json`, sitemap/navigation, source/claim/ontology JSON) were modified. **No** public HTML, dependencies, or workflows were added.

**Rationale:** A 307-row scaffold is necessary but **not sufficient** for a sovereign first launch; **EN+DE** must lead, **ar/zh/ja** bulk mirrors should **defer**, **H₂S** and **MoS₂/WS₂** concepts should **merge**, and **newsletter/acquire** must be **excluded from the 300 reference-page** cohort accounting.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`; corpus docs from Sprint 5A.

**Sprint 5B validation (observed where applicable):**

- `main/data/LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md` created.
- `main/data/LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md` created.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- **No** `main/content/**` changes.
- **No** `[SOURCE REQUIRED]` markers removed.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true` changes.
- Root `README.md` **not modified**.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not ready for publication** (review/reporting sprint only).

**Files created:**

- `main/data/LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md` — methodology, classification, strengths/risks, multilingual and source/claim assessment, launch-cohort-ready verdict (**no**), refinement prerequisites.
- `main/data/LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md` — keep/revise/merge/defer/reject lists, first implementation batch size (**40–55** routes recommended), Sprint **5C** options.

**Files updated:**

- `DECISION_LOG.md` — Sprint 5B entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md`, `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`, `main/data/CORPUS_EXPANSION_MODEL.md`, `main/data/CORPUS_LAUNCH_THRESHOLD.md`, all content draft pages, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-18 — Launch Cohort Implementation Batch 1 Planned

**Decision:** Record Sprint **5C** as a **planning and implementation-readiness** sprint that defines **Batch 1** (**55** proposed `route_id` concepts: **44** English, **11** German) for later controlled routing and drafting—**without** registering new routes, **without** creating or modifying content pages, and **without** publication.

**Summary:** Sprint **5C** converted the Sprint **5A**/ **5B** launch-cohort architecture and quality review into a disciplined first implementation batch. The sprint did **not** create routes, did **not** create content pages, did **not** publish any route, and did **not** approve any claim. The selected batch prioritizes source-governed terminology, German–English chemical language, disambiguation authority, corpus methodology, source/nomenclature governance, and controlled reference infrastructure while deferring weak, mirrored, utility, or insufficiently governed concepts (`newsletter` / `acquire`, `ar` / `zh` / `ja` mirrors, high-risk safety substance pages in this batch, and broad DE term grids). Deliverables: `LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md`, `ROUTE_IMPLEMENTATION_READINESS_MATRIX.md`, `SPRINT_5C_ROUTE_SELECTION_RATIONALE.md`.

**Rationale:** A 307-row blueprint is necessary but insufficient; a **55-route** governed slice proves editorial depth, citation discipline, and linking density before scaling toward the **300-page** minimum launch cohort—without lowering the threshold or recommending public launch.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`, `doctrine/PROJECT_DOCTRINE.md`; Sprint **5A**/**5B** corpus documentation.

**Sprint 5C validation (observed where applicable):**

- `main/data/LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md` exists; **55** proposed concepts (within **40–55** batch intent stated in 5B as a range; Batch 1 lands at **55** as the upper disciplined bound).
- `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md` exists; all **55** rows classified.
- `main/data/SPRINT_5C_ROUTE_SELECTION_RATIONALE.md` exists.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified** (this sprint).
- **No** `main/content/**` pages created or modified.
- **No** `[SOURCE REQUIRED]` markers removed.
- No claim has `status: approved`; claim registries remain **inactive**.
- All existing routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true` changes from this sprint (no `routes.json` edits).
- **No** generated HTML pages, dependencies, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not ready for publication** (strategy/planning sprint only).

**Files created:**

- `main/data/LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md` — Batch 1 roster, governance logic, and full per-concept specifications.
- `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md` — readiness classification and next actions for each concept.
- `main/data/SPRINT_5C_ROUTE_SELECTION_RATIONALE.md` — selection thesis and exclusions.

**Files updated:**

- `DECISION_LOG.md` — Sprint 5C entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md`, `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`, `main/data/CORPUS_EXPANSION_MODEL.md`, `main/data/CORPUS_LAUNCH_THRESHOLD.md`, `main/data/LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md`, `main/data/LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md`, all content draft pages, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-20 — Ready Route Planning Batch 1A Added

**Decision:** Register the Sprint **5C** **`ready_for_route_planning`** slice (**7** concepts) in `routes.json` as **`planned`**, non-indexable, non-sitemap routes—**without** duplicating pre-existing `route_id`s and **without** creating `content_file` bodies.

**Summary:** Sprint **5D** added **five** new route records (`corpus_methodology_overview`, `internal_linking_discipline`, `quality_gate_public_explainer`, `de_method_corpus_map`, `de_method_translator_playbook`). **`home`** and **`sources`** were **already** in `routes.json`; no duplicate rows were inserted (documented in `ROUTE_PLANNING_BATCH_1A_REPORT.md`). The sprint did **not** create or modify content pages, did **not** modify `internal_links.json`, did **not** publish routes, did **not** approve claims, and did **not** alter source, claim, sitemap, navigation, or ontology registries. The remaining Sprint **5C** concepts remain outside `routes.json` until source mapping, claim-boundary review, merge/scope refinement, or later-phase governance is completed.

**Rationale:** Execute Batch **1A** as a **route-planning-only** increment that matches the readiness matrix’s lowest-friction cohort while keeping the **300-page** launch threshold and Quality Gate doctrine unchanged.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`, `doctrine/SOURCE_POLICY.md`; Sprint **5C** planning documents.

**Sprint 5D validation (observed where applicable):**

- `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md` lists exactly **7** `ready_for_route_planning` concepts; **no** concepts from other buckets were added.
- `main/data/routes.json` parses as valid JSON; **26** route records total (**21** prior + **5** new).
- Every **new** route: `status: planned`, `indexable: false`, `in_sitemap: false`.
- `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- **No** `main/content/**` files created or modified.
- No claim has `status: approved`; claim registries remain **inactive** (no edits this sprint).
- **No** generated HTML, dependencies, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `main/data/ROUTE_PLANNING_BATCH_1A_REPORT.md` created.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not public launch**; all routes remain **planned** and non-sitemap.

**Files created:**

- `main/data/ROUTE_PLANNING_BATCH_1A_REPORT.md` — Batch 1A scope, sources, adds vs skips, confirmations, deferred cohort counts.

**Files updated:**

- `main/data/routes.json` — **five** new planned route records.
- `DECISION_LOG.md` — Sprint 5D entry appended.

**Not modified in this sprint:** `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `main/data/LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md`, `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md`, `main/data/SPRINT_5C_ROUTE_SELECTION_RATIONALE.md`, `main/data/CORPUS_LAUNCH_THRESHOLD.md`, all existing content draft pages, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-21 — Batch 1A Non-Public Drafts Created

**Decision:** Create **non-public** Markdown drafts for the **five** Sprint **5D** Batch **1A** `route_id` records—matching **`routes.json`** `content_file` paths—without changing route publication state, registries, or the internal link graph.

**Summary:** Sprint **5E** added draft bodies for `corpus_methodology_overview`, `internal_linking_discipline`, `quality_gate_public_explainer`, `de_method_corpus_map`, and `de_method_translator_playbook`. Drafts support sovereign corpus **methodology**, **internal linking discipline**, **Quality Gate** explanation, and **German** methodology layers. **No** routes were published. **No** `routes.json` fields were edited. **No** `internal_links.json` changes. **No** claims were approved. **No** source, sitemap, navigation, or ontology registries were modified. **`[SOURCE REQUIRED]`** markers remain where claims are not yet registry-backed.

**Rationale:** Route shells from Sprint **5D** require reviewable text while keeping all assets **planned**, **non-indexable**, and **non-sitemap** until Quality Gate and source/claim work catch up.

**Doctrine reference:** `doctrine/QUALITY_GATE.md`, `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`.

**Sprint 5E validation (observed where applicable):**

- Five target `content_file` paths exist with YAML frontmatter: `route_id`, `status: draft`, `publication_status: non_public`, `indexable: false`, `in_sitemap: false`, language fields aligned with `routes.json`.
- Draft bodies state **non-public** / **not publication-ready** posture; include **`[SOURCE REQUIRED]`** where appropriate; do **not** claim source-locking complete; do **not** approve claims; use **route_id** plain references only (**no** raw URLs; **no** markdown links assuming publication).
- German drafts (`de_method_corpus_map`, `de_method_translator_playbook`) are written in **German**; do **not** assert DIN or official German IUPAC authority.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true` introduced.
- **No** generated HTML, dependencies, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `main/data/BATCH_1A_NON_PUBLIC_DRAFT_CREATION_REPORT.md` created.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not public launch**; drafts are **inventory for review** only.

**Files created:**

- `main/content/en/pages/corpus-methodology.md`
- `main/content/en/pages/internal-linking-discipline.md`
- `main/content/en/pages/quality-gate.md`
- `main/content/de/pages/corpus-map.md`
- `main/content/de/pages/translator-playbook.md`
- `main/data/BATCH_1A_NON_PUBLIC_DRAFT_CREATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5E entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json. **Pre-existing** content draft pages (every file other than the five new Batch 1A targets above) — **not modified**.

---

### 2026-05-22 — Batch 1A Source and Claim Boundaries Reviewed

**Decision:** Record a **report-only** governance review of the five Batch **1A** non-public methodology drafts against source policy, claim boundaries, German authority constraints, internal-link readiness, and publication blockers—**without** mutating content, routes, or registries.

**Summary:** Sprint **5F** reviewed `corpus_methodology_overview`, `internal_linking_discipline`, `quality_gate_public_explainer`, `de_method_corpus_map`, and `de_method_translator_playbook` for source requirements, claim boundaries, German terminology authority boundaries, internal-link readiness, and publication blockers. **No** content pages were modified. **No** routes were published. **No** claims were approved. **No** registries were modified. **`[SOURCE REQUIRED]`** markers remain in place.

**Rationale:** Batch **1A** drafts are review inventory; explicit boundary mapping prevents premature publication, marker stripping, or linking batches that assume public eligibility.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/QUALITY_GATE.md`, `doctrine/PROJECT_DOCTRINE.md`.

**Sprint 5F validation (observed where applicable):**

- `main/data/BATCH_1A_SOURCE_CLAIM_BOUNDARY_REVIEW.md` exists and documents reviewed files, per-page assessments, German boundary review, blocker matrix, and **not ready for publication** conclusion.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `main/data/claims/terminology_claims.json`, `main/data/ontology/sulfur_terms.json` — **not modified**.
- **No** `main/content/**` files modified; **no** `[SOURCE REQUIRED]` markers removed.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true` introduced.
- **No** generated HTML, dependencies, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not ready for publication**; **not** public launch.

**Files created:**

- `main/data/BATCH_1A_SOURCE_CLAIM_BOUNDARY_REVIEW.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5F entry appended.

**Not modified in this sprint:** All content pages, `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, templates, root `README.md`, package files, workflows, generated output.

---

### 2026-05-27 — Batch 1B Existing Planned Route Drafts Created

**Decision:** Create the next controlled batch of **non-public draft pages** from **existing planned routes** in `routes.json`—increasing real corpus inventory without publishing routes, modifying route state, or mutating governance registries.

**Summary:** Sprint **5G** created non-public drafts for `what_is_sulfur`, `disulfide_bonds`, and `protein_disulfide_structure`—the full set of **safe eligible** planned routes whose `content_file` paths did not yet exist. **Eight** other missing routes were skipped (safety, industrial/procurement, substance operations, utility). **No** routes were published. **No** claims were approved. **No** registries were modified. **`[SOURCE REQUIRED]`** markers remain in all created and pre-existing drafts.

**Rationale:** Move Bisulfid.com from planning into **controlled corpus production** while preserving sovereign-grade discipline. Only **3** of **11** missing registered routes met low-risk eligibility; target range 8–12 could not be met without adding new routes (out of scope) or drafting high-risk pages (forbidden).

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/QUALITY_GATE.md`, `doctrine/PROJECT_DOCTRINE.md`.

**Sprint 5G validation (observed where applicable):**

- All selected `route_id` values pre-existed in `routes.json`; **no** new route records added.
- Every created `content_file` matches the exact path in `routes.json`; **no** existing file overwritten.
- Every created draft has matching frontmatter: `status: draft`, `publication_status: non_public`, `indexable: false`, `in_sitemap: false`.
- Every created draft states non-public / not publication-ready posture; includes **`[SOURCE REQUIRED]`** where factual support is pending.
- **No** draft claims source-locking complete; **no** draft approves or implies claim approval; **no** raw URLs or markdown links assuming publication.
- **No** market, safety handling, medical, procurement, production, trade, CAGR, market-share, or acquisition-target content in created drafts.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `main/data/claims/terminology_claims.json`, `main/data/ontology/sulfur_terms.json` — **not modified**.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true`.
- **No** generated HTML, dependencies, workflows, or root `README.md` changes.
- `main/data/BATCH_1B_EXISTING_ROUTE_DRAFT_CREATION_REPORT.md` created; `DECISION_LOG.md` updated.

**Publication readiness:** **Not ready for publication**; **not** public launch.

**Draft-backed route count:** **18** of **26** registered routes now have draft bodies (**3** created this sprint).

**Files created:**

- `main/content/en/pages/what-is-sulfur.md`
- `main/content/en/pages/disulfide-bonds.md`
- `main/content/en/pages/protein-disulfide-structure.md`
- `main/data/BATCH_1B_EXISTING_ROUTE_DRAFT_CREATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5G entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, templates, root `README.md`, package files, workflows, generated output, **pre-existing** content draft pages (every file other than the three Batch 1B targets above).

---

### 2026-05-27 — Five Hundred Page Sovereign Launch Program Established

**Decision:** Upgrade Bisulfid.com’s **minimum public launch threshold** from **300** to **500 governed reference pages** and establish the strategic production program, expansion model, blueprint expansion, and wave-based production architecture required to reach that threshold—**without** publishing routes, creating content, or modifying registries.

**Summary:** Sprint **5H** revised `SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `CORPUS_EXPANSION_MODEL.md`, and `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` to reflect the **500-page minimum** first public launch cohort (300 is no longer the launch threshold). Created `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md` and `CORPUS_PRODUCTION_WAVE_MODEL.md`. Blueprint expansion adds **193** concepts to the original **307** for **500** total proposed reference pages. **No** routes were published. **No** content pages were created or modified. **No** claims were approved. **No** registries were modified.

**Rationale:** The owner judged **300 pages insufficient** for a sovereign-grade first public surface. **500** is the new **floor** (not the ceiling); long-term ambition remains **1,000+** and **3,000+** pages under strict governance. Small batch sprints proved discipline; **wave-based production** is now required to reach launch scale without thin pages, translation spam, or fake readiness.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`, `doctrine/SOURCE_POLICY.md`.

**Sprint 5H validation (observed where applicable):**

- `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md` and `CORPUS_PRODUCTION_WAVE_MODEL.md` exist with layer allocation, audience map, wave sizes, production sequence, and rejected shortcuts.
- `SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md` states **500 pages** as minimum public launch threshold; **300** superseded.
- `CORPUS_LAUNCH_THRESHOLD.md` defines **500** governed pages as minimum cohort with full launch gates (metadata, links, SEO, technical/security, no markers, no thin pages).
- `CORPUS_EXPANSION_MODEL.md` defines horizons: **500** launch, **1,000+** authority, **3,000+** multilingual, optional **5,000+**.
- `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` acknowledges **307 insufficient**; expansion register totals **500** proposed concepts.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `main/data/claims/terminology_claims.json`, `main/data/ontology/sulfur_terms.json` — **not modified**.
- **No** content pages created or modified; **no** `[SOURCE REQUIRED]` markers removed.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true`.
- **No** generated HTML, dependencies, workflows, or root `README.md` changes.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not ready for publication**; **not** public launch. **No publication before 500-page threshold.**

**Files created:**

- `main/data/FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`
- `main/data/CORPUS_PRODUCTION_WAVE_MODEL.md`

**Files updated:**

- `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`
- `main/data/CORPUS_LAUNCH_THRESHOLD.md`
- `main/data/CORPUS_EXPANSION_MODEL.md`
- `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md`
- `DECISION_LOG.md` — Sprint 5H entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, templates, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Corpus Automation Control Layer Established

**Decision:** Establish the **governed automation control layer** for Bisulfid.com’s **500-page sovereign reference corpus program**—defining how future automation may support wave production without publishing routes, approving claims, generating weak pages, or bypassing human governance.

**Summary:** Sprint **5I-A** created `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_MANIFEST.md`, `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`, and `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`. The layer defines automation boundaries for route registration, draft production, source mapping, claim boundary review, internal-link wiring, SEO/metadata validation, and technical/pre-publication validation. **No** scripts, workflows, dependencies, routes, content pages, or registries were created or modified.

**Rationale:** Sprint **5H** established **500-page** wave production; scaling to 80–120 route waves and 40–60 draft waves requires **repeatable validation and manifest discipline** before tooling is implemented. Automation follows doctrine; human review remains mandatory at merge, sample audit, source/claim signoff, and launch authorization (S9).

**Doctrine reference:** `CORPUS_PRODUCTION_WAVE_MODEL.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`, `doctrine/QUALITY_GATE.md`, `doctrine/SOURCE_POLICY.md`.

**Sprint 5I-A validation (observed where applicable):**

- `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_MANIFEST.md`, `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`, and `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md` exist with stage definitions, wave protocol, validation check IDs, and publication lock rules.
- **No** scripts created; **no** GitHub workflows created; **no** dependencies added.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `main/data/claims/terminology_claims.json`, `main/data/ontology/sulfur_terms.json` — **not modified**.
- **No** content pages created or modified.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true`.
- **No** generated HTML; root `README.md` **not modified**.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not ready for publication**; **not** public launch. **No publication before 500-page threshold.**

**Files created:**

- `main/data/CORPUS_AUTOMATION_CONTROL_LAYER.md`
- `main/data/CORPUS_AUTOMATION_MANIFEST.md`
- `main/data/CORPUS_AUTOMATION_WAVE_PROTOCOL.md`
- `main/data/CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5I-A entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, templates, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output, scripts directories.

---

### 2026-05-27 — Route Registration Wave 1 Added

**Decision:** Register the **first large wave** of low-risk **planned** routes toward the **500-page sovereign launch threshold** and introduce a read-only **L0 route registry validator**.

**Summary:** Sprint **5I-B** added **100** new route records to `routes.json` (26 → **126** total). Created `scripts/validate_route_registry_l0.py`, `ROUTE_REGISTRATION_WAVE_1_MANIFEST.md`, `ROUTE_REGISTRATION_WAVE_1_REPORT.md`, and `ROUTE_REGISTRY_L0_VALIDATION_REPORT.md`. **No** content pages were created. **No** routes were published. All new routes remain `planned`, `indexable: false`, `in_sitemap: false`, `in_navigation: false`. **No** claims were approved. **No** internal links, source registries, claim registries, sitemap, navigation, generated HTML, dependencies, workflows, or root README files were modified.

**Rationale:** Sprint **5H** set the 500-page launch threshold; Sprint **5I-A** defined automation control and wave protocol. Route-scale production must begin with governed **registry-only** waves (80–120 routes) before draft production, preserving publication and claim locks.

**Doctrine reference:** `CORPUS_PRODUCTION_WAVE_MODEL.md`, `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`, `doctrine/QUALITY_GATE.md`.

**Sprint 5I-B validation:**

- `routes.json` remains valid JSON; **100** new route records added (target 80–120 met).
- Every new `route_id` was absent before this sprint; no duplicate `route_id` or `path`.
- Every new route: `status: planned`, `indexable: false`, `in_sitemap: false`, `in_navigation: false`.
- **No** content files created or modified; **no** generated HTML.
- `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- No claim `status: approved`; claim registries remain **inactive**.
- `scripts/validate_route_registry_l0.py` exists; L0 validation **PASS**.
- Manifest, report, and validation report artifacts exist.

**Publication readiness:** **Not ready for publication**. Registry expansion only. **374** routes remain to be registered toward the 500-page threshold.

**Recommended next sprint:** Draft production wave 1 (40–60 governed drafts for highest-priority newly registered routes) and/or route registration wave 2.

**Files created:**

- `scripts/validate_route_registry_l0.py`
- `main/data/ROUTE_REGISTRATION_WAVE_1_MANIFEST.md`
- `main/data/ROUTE_REGISTRATION_WAVE_1_REPORT.md`
- `main/data/ROUTE_REGISTRY_L0_VALIDATION_REPORT.md`

**Files updated:**

- `main/data/routes.json` — 100 planned routes added (126 total).
- `DECISION_LOG.md` — Sprint 5I-B entry appended.

**Not modified in this sprint:** `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, templates, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Route Registration Wave 1 Report Corrected

**Decision:** Correct the Sprint **5I-B** route registration report so audit documentation explicitly records the `routes.json` modification and the intentional **30 English / 70 German** wave split.

**Summary:** This patch corrected `ROUTE_REGISTRATION_WAVE_1_REPORT.md` by explicitly stating that **`main/data/routes.json` was modified** in Sprint 5I-B to add **100** planned route records (26 → **126** total) and by documenting why the wave is **German-heavy**. Bisulfid.com’s strategic identity depends on **German lexical and terminology boundaries** while **English remains the global base layer** through EN terminology, disambiguation, governance, and index infrastructure routes. Arabic, Chinese, and Japanese routes remain deferred until EN/DE spine and hreflang/translation governance are stronger. **No** routes were changed. **No** content pages were created. **No** routes were published. **No** claims were approved. **No** registries, validator, generated output, dependencies, workflows, or root README files were modified.

**Rationale:** Post-merge verification (Sprint 5I-B) passed registry and governance checks but identified two documentation gaps: the report did not explicitly name `routes.json` as a modified artifact, and it did not explain the German-heavy language split. This patch closes those gaps without altering registry state.

**Sprint 5I-B report-correction validation:**

- Only `ROUTE_REGISTRATION_WAVE_1_REPORT.md` and `DECISION_LOG.md` changed.
- Report explicitly states `routes.json` was modified; **100** new planned records; count **26 → 126**.
- Report explains **30 EN / 70 DE** split and German-heavy strategic rationale; preserves EN as global base layer.
- Report does not imply `routes.json` was unmodified.
- `routes.json`, validator, manifest, validation report, content, registries — **not modified**.

**Files updated:**

- `main/data/ROUTE_REGISTRATION_WAVE_1_REPORT.md` — registry modification statement and German-heavy rationale added.
- `DECISION_LOG.md` — corrective entry appended.

**Not modified in this patch:** `main/data/routes.json`, `scripts/validate_route_registry_l0.py`, `main/data/ROUTE_REGISTRATION_WAVE_1_MANIFEST.md`, `main/data/ROUTE_REGISTRY_L0_VALIDATION_REPORT.md`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, all `main/content/**` pages, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Draft Production Wave 1 Created

**Decision:** Create the **first large wave** of **non-public draft pages** for selected low-risk planned routes under the **500-page sovereign launch program** and automation control doctrine.

**Summary:** Sprint **5J** created **50** non-public Markdown drafts at exact `routes.json` `content_file` paths (draft-backed routes: **18 → 68**). Created `scripts/validate_content_drafts_l0.py`, `DRAFT_PRODUCTION_WAVE_1_MANIFEST.md`, `DRAFT_PRODUCTION_WAVE_1_REPORT.md`, and `CONTENT_DRAFTS_L0_VALIDATION_REPORT.md`. **No** routes were published. **`routes.json` was not modified.** All created drafts remain `non_public`, non-indexable, out of sitemap, and not publication-ready. **No** claims were approved. **No** internal links, source registries, claim registries, sitemap, navigation, generated HTML, dependencies, workflows, or root README files were modified.

**Rationale:** Sprint **5I-B** registered 100 new routes; Sprint **5I-A** defines draft production as stage S2 (40–60 drafts per wave). Controlled draft bodies must precede publication, source-locking, and claim approval.

**Doctrine reference:** `CORPUS_PRODUCTION_WAVE_MODEL.md`, `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`.

**Sprint 5J validation:**

- **50** non-public drafts created (target 40–60 met).
- Every draft matches an existing `route_id` and exact `content_file` path; **no overwrites**.
- Required frontmatter, non-public notices, and `[SOURCE REQUIRED]` markers present.
- No raw URLs or markdown links to unpublished routes.
- `routes.json`, registries, and pre-existing draft pages (except new wave targets) governance posture unchanged.
- L0 content validation **PASS**.
- All routes remain `planned`; no claim approved; registries inactive.

**Publication readiness:** **Not ready for publication**. Draft review and source/claim work required.

**Recommended next sprint:** Draft production wave 2 (next 40–60 drafts) or route registration wave 2.

**Files created:**

- **50** draft Markdown files under `main/content/en/pages/` and `main/content/de/pages/`
- `scripts/validate_content_drafts_l0.py`
- `main/data/DRAFT_PRODUCTION_WAVE_1_MANIFEST.md`
- `main/data/DRAFT_PRODUCTION_WAVE_1_REPORT.md`
- `main/data/CONTENT_DRAFTS_L0_VALIDATION_REPORT.md`

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Corpus Automation Runtime Layer 1 Established

**Decision:** Establish the first **executable read-only automation runtime layer** (L1) for Bisulfid.com’s sovereign reference corpus validation.

**Summary:** Sprint **5K** added L1 validators for route registry integrity, draft content discipline, publication locks, claim locks, and internal reference discipline, plus a local orchestration runtime (`corpus_validation_runtime_l1.py`). Created automation documentation and validation reports. **No** routes, content pages, registries, workflows, dependencies, or public HTML were added or modified. **No** routes were published. **No** claims were approved. All routes remain `planned`; all claim registries remain **inactive**.

**Rationale:** After Sprint **5I-B** (126 routes) and Sprint **5J** (68 draft-backed pages), isolated L0 wave validators are insufficient for corpus-scale governance. L1 provides repeatable, stdlib-only, read-only validation toward the **500-page** launch threshold and later **1,000+** / **3,000+** expansion without lowering quality, trust, SEO, security, or governance control.

**Doctrine reference:** `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_MANIFEST.md`, `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`, `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`.

**Sprint 5K validation:**

- All new L1 scripts exist under `scripts/`; Python standard library only; read-only.
- `python scripts/corpus_validation_runtime_l1.py` — **PASS** (all L1 validators; L0 informational PASS).
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- **No** content pages created or modified; **no** generated HTML; root `README.md` **not modified**.
- **No** GitHub workflows created; **no** dependencies added.
- All **126** routes remain `status: planned`; **no** `indexable: true`, `in_sitemap: true`, or `in_navigation: true`.
- Claim registries remain **inactive**; **0** approved claims; **14** pending_review.
- L1 warnings documented for **18** legacy pre-5J drafts and **4** pre-existing safety-context route metadata keywords — **not auto-fixed**.
- `CORPUS_AUTOMATION_SCRIPT_REGISTRY.md`, `CORPUS_AUTOMATION_RUNTIME_LAYER_1_REPORT.md`, `CORPUS_L1_VALIDATION_REPORT.md`, and `CORPUS_AUTOMATION_NEXT_WAVE_RECOMMENDATIONS.md` exist.

**Publication readiness:** **Not ready for publication**. Validation infrastructure only. **374** routes remain to be registered toward the 500-page threshold; **58** routes lack drafts.

**Recommended next sprint:** Source and claim boundary review for Sprint 5J drafts (Sprint 5L), then draft production wave 2.

**Files created:**

- `scripts/corpus_validation_runtime_l1.py`
- `scripts/validate_corpus_routes_l1.py`
- `scripts/validate_corpus_drafts_l1.py`
- `scripts/validate_corpus_publication_lock_l1.py`
- `scripts/validate_corpus_claims_l1.py`
- `scripts/validate_corpus_references_l1.py`
- `main/data/CORPUS_AUTOMATION_SCRIPT_REGISTRY.md`
- `main/data/CORPUS_AUTOMATION_RUNTIME_LAYER_1_REPORT.md`
- `main/data/CORPUS_L1_VALIDATION_REPORT.md`
- `main/data/CORPUS_AUTOMATION_NEXT_WAVE_RECOMMENDATIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5K entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, `scripts/validate_route_registry_l0.py`, `scripts/validate_content_drafts_l0.py`, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Draft Wave 1 Source and Claim Boundaries Reviewed

**Decision:** Review and classify source and claim boundaries for all **50** Sprint **5J** non-public drafts before the next large draft-production wave.

**Summary:** Sprint **5L** classified wave-1 drafts by source requirement level, claim-risk level, publication blockers, and readiness for future source-mapping and claim-boundary work. Created boundary review report and four supporting matrices/action documents. **No** content pages were modified. **No** routes were published. **No** claims were approved. **No** source entries, claim registries, route records, internal links, sitemap, navigation, generated HTML, dependencies, workflows, or root README files were modified. `[SOURCE REQUIRED]` markers remain in place.

**Rationale:** Sprint **5K** established L1 automation and recommended source/claim boundary review (5L) before draft wave 2. With **68** draft-backed routes and **50** new standardized drafts, unclassified source/claim debt would compound toward the **500-page** launch threshold.

**Doctrine reference:** `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `CORPUS_PRODUCTION_WAVE_MODEL.md`, `DRAFT_PRODUCTION_WAVE_1_MANIFEST.md`, `CORPUS_AUTOMATION_NEXT_WAVE_RECOMMENDATIONS.md`.

**Sprint 5L validation:**

- **50/50** Sprint 5J drafts exist, match `routes.json`, remain `draft` / `non_public` / non-indexable.
- L1 runtime **PASS** (pre-flight).
- **0** drafts publication-ready; **12** ready for source-mapping cohort A; **3** blocked pending reframe.
- Matrices contain **50** rows each.
- `routes.json`, registries, content pages — **not modified**.
- No claim `status: approved`; registries remain **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Classification sprint only.

**Recommended next sprint:** Source mapping wave 1 (cohort A, 10–15 drafts) plus claim boundary registration report for medium-risk drafts.

**Files created:**

- `main/data/DRAFT_WAVE_1_SOURCE_CLAIM_BOUNDARY_REVIEW.md`
- `main/data/DRAFT_WAVE_1_SOURCE_REQUIREMENT_MATRIX.md`
- `main/data/DRAFT_WAVE_1_CLAIM_RISK_MATRIX.md`
- `main/data/DRAFT_WAVE_1_PUBLICATION_BLOCKER_MATRIX.md`
- `main/data/DRAFT_WAVE_1_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5L entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, L1/L0 validator scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Draft Wave 1 Source Mapping Wave 1 Completed

**Decision:** Complete the first **source-mapping wave** for the **12** lowest-risk Sprint **5J** drafts identified by Sprint **5L**, and prepare claim-boundary notes for **20** medium-risk drafts.

**Summary:** Sprint **5M** mapped source requirements, source category gaps, and claim posture for cohort-A drafts and produced medium-risk claim-boundary preparation for **20** drafts. **No** source entries were added. **No** claim registries, content pages, or route records were modified. **No** claims were approved. **No** routes were published. `[SOURCE REQUIRED]` markers remain in place.

**Rationale:** Sprint **5L** classified wave-1 drafts and recommended source mapping before draft wave 2. Mapping defines audit-grade plans for future source registration without falsely claiming source-lock completion.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `DRAFT_WAVE_1_SOURCE_CLAIM_BOUNDARY_REVIEW.md`, `DRAFT_WAVE_1_NEXT_ACTIONS.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`.

**Sprint 5M validation:**

- **12/12** cohort-A drafts mapped; **20/20** medium-risk drafts covered in claim-boundary prep.
- L1 runtime **PASS** (pre-flight).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed.
- **0** publication-ready drafts; **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Mapping and preparation sprint only.

**Recommended next sprint:** Source registration proposal wave 1 (4–6 drafts, report-only) and claim boundary registration report (20 medium-risk drafts).

**Files created:**

- `main/data/DRAFT_WAVE_1_SOURCE_MAPPING_WAVE_1_REPORT.md`
- `main/data/DRAFT_WAVE_1_SOURCE_MAPPING_MATRIX.md`
- `main/data/DRAFT_WAVE_1_SOURCE_CATEGORY_GAP_ANALYSIS.md`
- `main/data/DRAFT_WAVE_1_MEDIUM_RISK_CLAIM_BOUNDARY_PREP.md`
- `main/data/DRAFT_WAVE_1_SOURCE_MAPPING_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5M entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Source Registration Proposal Wave 1 Completed

**Decision:** Prepare the first **source registration proposal wave** for **5** selected low-risk drafts from the Sprint **5M** source-mapped cohort.

**Summary:** Sprint **5N-A** prepared source registration proposals for **5** lowest-gap cohort-A drafts (`sulfur_element_term_record`, `de_core_biogenic_lang`, `copper_sulfides_language`, `de_core_fes`, `de_core_mos2`). The sprint identified future source authority needs, source evidence requirements, source policy gaps, and registration risks without adding source entries, modifying `source_registry.json`, editing content pages, approving claims, modifying claim registries, publishing routes, or removing `[SOURCE REQUIRED]` markers. The output prepares a future source discovery or source registration sprint while preserving strict human governance.

**Rationale:** Sprint **5M** mapped **12** cohort-A drafts but forbade registry edits. Proposals define what future registration would require—evidence types, authority tiers, policy gaps, and rejection criteria—before any candidate source is treated as verified or any page advances toward publication.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `DRAFT_WAVE_1_SOURCE_MAPPING_WAVE_1_REPORT.md`, `DRAFT_WAVE_1_SOURCE_MAPPING_MATRIX.md`, `DRAFT_WAVE_1_SOURCE_MAPPING_NEXT_ACTIONS.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`.

**Sprint 5N-A validation:**

- **5/5** selected drafts from Sprint **5M** cohort-A; **7** cohort-A drafts deferred with documented rationale.
- **5/5** selected drafts exist, match `routes.json`, remain `draft` / `non_public` / non-indexable.
- L1 runtime **PASS** (pre-flight).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed; **no** generated HTML.
- **0** publication-ready drafts; **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Proposal sprint only.

**Recommended next sprint:** Sprint **5N-B** (claim boundary registration report, 20 medium-risk drafts) in parallel with Sprint **5N-C** (candidate source discovery for 5 proposed drafts).

**Files created:**

- `main/data/SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md`
- `main/data/SOURCE_EVIDENCE_REQUIREMENT_MATRIX_WAVE_1.md`
- `main/data/SOURCE_REGISTRATION_RISK_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRATION_NEXT_ACTIONS_WAVE_1.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-A entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-28 — Source and Claim Automation Guardrails Established

**Decision:** Establish specialized read-only automation guardrails for Bisulfid.com's source and claim governance layer before candidate source discovery or registry edits.

**Summary:** Sprint **5N-B** established specialized read-only automation guardrails for Bisulfid.com's source and claim governance layer. The sprint added validators for source registration proposals, source evidence requirements, claim-boundary preparation, source registry locks, and claim registry locks without adding sources, modifying `source_registry.json`, approving claims, modifying claim registries, editing content pages, publishing routes, generating public output, adding dependencies, creating workflows, or removing `[SOURCE REQUIRED]` markers. The guardrail layer protects the future source registration process before the corpus advances toward public launch readiness.

**Rationale:** Sprint **5N-A** produced source registration proposals; Sprint **5M** mapped sources and prepared medium-risk claim boundaries. Before 5N-C candidate discovery or registry execution, automation must verify proposals and registries remain controlled, non-approved, and non-misleading. Sources are the trust root of the sovereign reference corpus.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md`, `DRAFT_WAVE_1_MEDIUM_RISK_CLAIM_BOUNDARY_PREP.md`, `CORPUS_AUTOMATION_SCRIPT_REGISTRY.md`, `CORPUS_LAUNCH_THRESHOLD.md`.

**Sprint 5N-B validation:**

- **6** guardrail scripts created; stdlib-only; read-only.
- Guardrail runtime **PASS** (2026-05-28).
- Corpus L1 runtime **PASS** (informational).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed.
- **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Automation sprint only.

**Recommended next sprint:** Sprint **5N-C** (candidate source discovery for 5 proposed drafts) with guardrail runtime as pre/post gate.

**Files created:**

- `scripts/source_claim_guardrail_runtime_l1.py`
- `scripts/validate_source_registration_proposals_l1.py`
- `scripts/validate_source_evidence_requirements_l1.py`
- `scripts/validate_claim_boundary_preparation_l1.py`
- `scripts/validate_source_registry_lock_l1.py`
- `scripts/validate_claim_registry_lock_l1.py`
- `main/data/SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_SCRIPT_REGISTRY.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_VALIDATION_REPORT.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-B entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, existing L0/L1 corpus validator scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-28 — Candidate Source Discovery Wave 1 Completed

**Decision:** Create the first candidate source discovery layer for the **5** selected source-registration proposal drafts from Sprint **5N-A**.

**Summary:** Sprint **5N-C** created the first candidate source discovery layer for the five selected source-registration proposal drafts. The sprint classified candidate source families, authority requirements, rejection rules, and next actions without adding source entries, modifying `source_registry.json`, approving claims, modifying claim registries, editing content pages, publishing routes, adding raw URLs, or inventing bibliographic details. Candidate sources remain discovery targets only and are not approved, source-locked, or publication-ready.

**Rationale:** Sprint **5N-A** proposals and Sprint **5N-B** guardrails established prerequisites. Discovery names **families and search targets** for human review before any registry execution — preserving the trust root without false source-lock progress.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md`, `SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md`, `SOURCE_EVIDENCE_REQUIREMENT_MATRIX_WAVE_1.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `CORPUS_LAUNCH_THRESHOLD.md`.

**Sprint 5N-C validation:**

- **5/5** selected drafts covered in discovery matrices.
- Guardrail runtime **PASS** (pre- and post-sprint).
- Corpus L1 runtime **PASS** (pre- and post-sprint).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed; **no** raw URLs; **no** invented bibliographic details.
- **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Discovery-planning sprint only.

**Recommended next sprint:** Sprint **5N-D** — human candidate source review wave 1 (name and evaluate candidates; still no registry edits unless execution sprint chartered).

**Files created:**

- `main/data/CANDIDATE_SOURCE_DISCOVERY_WAVE_1_REPORT.md`
- `main/data/CANDIDATE_SOURCE_DISCOVERY_MATRIX_WAVE_1.md`
- `main/data/CANDIDATE_SOURCE_AUTHORITY_REQUIREMENTS_WAVE_1.md`
- `main/data/CANDIDATE_SOURCE_REJECTION_RULES_WAVE_1.md`
- `main/data/CANDIDATE_SOURCE_DISCOVERY_NEXT_ACTIONS_WAVE_1.md`
- `main/data/CANDIDATE_SOURCE_DISCOVERY_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-C entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-28 — Human Candidate Source Review Wave 1 Completed

**Decision:** Complete human candidate source review documentation for the **5** candidate-source-discovery drafts from Sprint **5N-C**.

**Summary:** Sprint **5N-D** completed human candidate source review documentation for the five candidate-source-discovery drafts from Sprint **5N-C**. The sprint evaluated candidate source families, authority requirements, acceptance criteria, rejection decisions, and future registry actions without adding source entries, modifying `source_registry.json`, approving claims, modifying claim registries, editing content pages, publishing routes, adding raw URLs, or inventing bibliographic details. Candidate sources remain unapproved and no page is source-locked or publication-ready.

**Rationale:** Sprint **5N-C** identified discovery families and search targets. Human review applies governance acceptance/rejection logic and documents verification gaps before any registry proposal or execution — preserving the trust root without false progress.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `CANDIDATE_SOURCE_DISCOVERY_WAVE_1_REPORT.md`, `HUMAN_SOURCE_ACCEPTANCE_CRITERIA_WAVE_1.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `CORPUS_LAUNCH_THRESHOLD.md`.

**Sprint 5N-D validation:**

- **5/5** selected drafts covered in human review matrix.
- Guardrail runtime **PASS** (pre- and post-sprint).
- Corpus L1 runtime **PASS** (pre- and post-sprint).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed; **no** raw URLs; **no** invented bibliographic details.
- **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Human-review documentation sprint only.

**Recommended next sprint:** Sprint **5N-E** — external source verification wave 1 (`de_core_mos2`, `sulfur_element_term_record` priority).

**Files created:**

- `main/data/HUMAN_CANDIDATE_SOURCE_REVIEW_WAVE_1_REPORT.md`
- `main/data/HUMAN_CANDIDATE_SOURCE_REVIEW_MATRIX_WAVE_1.md`
- `main/data/HUMAN_SOURCE_ACCEPTANCE_CRITERIA_WAVE_1.md`
- `main/data/HUMAN_SOURCE_REJECTION_DECISIONS_WAVE_1.md`
- `main/data/HUMAN_SOURCE_REVIEW_NEXT_ACTIONS_WAVE_1.md`
- `main/data/HUMAN_CANDIDATE_SOURCE_REVIEW_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-D entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-28 — External Source Verification Wave 1 Completed

**Decision:** Complete external source verification documentation for the **2** highest-priority human-reviewed candidate-source drafts from Sprint **5N-D**.

**Summary:** Sprint **5N-E** completed external source verification documentation for the two highest-priority human-reviewed candidate-source drafts, `de_core_mos2` and `sulfur_element_term_record`. The sprint classified external verification status, authority class, evidence posture, risks, and next actions without adding source entries, modifying `source_registry.json`, approving claims, modifying claim registries, editing content pages, publishing routes, adding raw URLs where not allowed, or inventing bibliographic details. Source verification remains non-approval, non-source-locking, and non-publication-ready.

**Rationale:** Sprint **5N-D** identified human review status and future registry actions but required external verification to close the naming gap. This sprint documents evidence families, authority requirements, and human verification needs before any source registry proposal or execution — preserving the trust root without fabrication.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `HUMAN_CANDIDATE_SOURCE_REVIEW_WAVE_1_REPORT.md`, `HUMAN_SOURCE_ACCEPTANCE_CRITERIA_WAVE_1.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `CORPUS_LAUNCH_THRESHOLD.md`.

**Sprint 5N-E validation:**

- **2/2** priority drafts covered in verification matrix.
- Route count **126** read from `routes.json` and documented.
- Guardrail runtime **PASS** (pre- and post-sprint).
- Corpus L1 runtime **PASS** (pre- and post-sprint).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed; **no** raw URLs; **no** invented bibliographic details.
- **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. External verification documentation sprint only.

**Recommended next sprint:** Sprint **5N-F** — source registry proposal drafting wave 1 (maximum **1–3** drafts; prioritize `de_core_mos2` after human names DE lexicon candidate).

**Files created:**

- `main/data/EXTERNAL_SOURCE_VERIFICATION_WAVE_1_REPORT.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_MATRIX_WAVE_1.md`
- `main/data/EXTERNAL_SOURCE_AUTHORITY_REVIEW_WAVE_1.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_RISK_REVIEW_WAVE_1.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_NEXT_ACTIONS_WAVE_1.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-E entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Source Registry Proposal Readiness Wave 1 Completed

**Decision:** Complete source registry proposal readiness documentation for `de_core_mos2` and `sulfur_element_term_record` after external source verification.

**Summary:** Sprint **5N-F** completed source registry proposal readiness documentation for `de_core_mos2` and `sulfur_element_term_record` after external source verification. The sprint identified `de_core_mos2` as the only conditional proposal-readiness candidate and kept `sulfur_element_term_record` blocked until a scientific database candidate is named. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, `[SOURCE REQUIRED]` markers remain unresolved, and no page is source-locked or publication-ready.

**Rationale:** Sprint **5N-E** found conditional proposal path for `de_core_mos2` but **0** named verified candidates. Proposal readiness documents gates, criteria, and blockers before any proposal drafting or registry execution — preserving separation between readiness, drafting, execution, approval, and publication.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `EXTERNAL_SOURCE_VERIFICATION_WAVE_1_REPORT.md`, `HUMAN_SOURCE_ACCEPTANCE_CRITERIA_WAVE_1.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `CORPUS_LAUNCH_THRESHOLD.md`.

**Sprint 5N-F validation:**

- **2/2** target drafts covered in readiness matrix.
- `de_core_mos2` — **only conditional** proposal-readiness candidate (`proposal_readiness_conditional`).
- `sulfur_element_term_record` — **blocked** (`needs_scientific_database_candidate_first`).
- Route count **126** read from `routes.json` and documented.
- Guardrail runtime **PASS** (pre- and post-sprint).
- Corpus L1 runtime **PASS** (pre- and post-sprint).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed; **no** raw URLs; **no** invented bibliographic details.
- **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Proposal-readiness documentation sprint only.

**Recommended next sprint:** Sprint **5N-G** — named source candidate intake wave 1 (`de_core_mos2`); parallel database candidate naming for `sulfur_element_term_record`.

**Files created:**

- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_MATRIX_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_DRAFTING_CRITERIA_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_BLOCKERS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-F entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Corpus Production Automation Layer 2 Established

**Decision:** Establish read-only Corpus Production Automation Layer 2 for sovereign-scale corpus growth planning and validation.

**Summary:** Sprint **5O-A** established a read-only Corpus Production Automation Layer 2 for sovereign-scale Bisulfid.com corpus growth. The sprint added dry-run production planning and validation scripts for production waves, internal link graph planning, SEO/indexation planning, multilingual expansion planning, and L2 runtime orchestration. It also documented wave controls, production gates, link graph discipline, SEO/indexation discipline, and multilingual production rules. No routes were added, no content pages were created, no sources were added, no claims were approved, no registries were modified, no routes were published, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Scaling toward **500** governed launch pages and beyond requires repeatable wave planning, gate enforcement, and merge-blocking validation — not ad hoc page generation. L2 complements L1 corpus automation and 5N-B source/claim guardrails without weakening authority.

**Doctrine reference:** `CORPUS_LAUNCH_THRESHOLD.md`, `CORPUS_PRODUCTION_WAVE_MODEL.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`.

**Sprint 5O-A validation:**

- **6** L2 scripts created — stdlib-only, read-only/dry-run.
- L2 production runtime **PASS**; L1 corpus runtime **PASS**; guardrail runtime **PASS**.
- Route count **126**; draft-backed **68**; production can safely proceed: **no**.
- `routes.json`, registries, content pages — **not modified**.
- **0** approved claims; registries **inactive**; all routes `planned`, non-indexable.

**Publication readiness:** **Not ready for publication**. Automation architecture sprint only.

**Recommended next sprint:** Sprint **5O-B** — production dry-run wave planning; parallel **5N-G** named source candidate intake.

**Files created:**

- `scripts/corpus_production_planner_l2.py`
- `scripts/validate_production_wave_plan_l2.py`
- `scripts/validate_internal_link_graph_plan_l2.py`
- `scripts/validate_seo_indexation_plan_l2.py`
- `scripts/validate_multilingual_wave_plan_l2.py`
- `scripts/corpus_production_runtime_l2.py`
- `main/data/CORPUS_PRODUCTION_AUTOMATION_LAYER_2_REPORT.md`
- `main/data/CORPUS_PRODUCTION_AUTOMATION_SCRIPT_REGISTRY.md`
- `main/data/CORPUS_PRODUCTION_WAVE_CONTROL_MODEL.md`
- `main/data/CORPUS_PRODUCTION_GATE_MODEL.md`
- `main/data/CORPUS_PRODUCTION_LINK_GRAPH_MODEL.md`
- `main/data/CORPUS_PRODUCTION_SEO_INDEXATION_MODEL.md`
- `main/data/CORPUS_PRODUCTION_MULTILINGUAL_MODEL.md`
- `main/data/CORPUS_PRODUCTION_AUTOMATION_VALIDATION_REPORT.md`
- `main/data/CORPUS_PRODUCTION_AUTOMATION_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5O-A entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages (except no edits), root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output. Existing L1 automation scripts unchanged except additive L2 siblings.

---

### 2026-05-27 — Production Dry-Run Wave Planning Completed

**Decision:** Complete production dry-run wave planning for a future Route Registration Wave 2 without modifying `routes.json` or creating pages.

**Summary:** Sprint **5O-B** completed a dry-run production planning wave for a future Route Registration Wave 2 without modifying `routes.json` or creating pages. The sprint used the Corpus Production Automation Layer 2 to plan and evaluate a candidate route-registration wave under the 500-page sovereign launch threshold, source/claim gates, internal link graph discipline, SEO/indexation locks, multilingual governance, and anti-thin-content standards. **83** dry-run candidates were identified from the launch cohort blueprint (80–120 band; below preferred 100 because safely eligible EN/DE-first inventory is exhausted under current gates). No routes were added, no content pages were created, no sources were added, no claims were approved, no registries were modified, no routes were published, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5O-A** established L2 read-only production automation. Before Route Registration Wave 2 execution, L2 must be tested against a real planning cohort with manifest, matrix, risk review, and execution blockers — without registry side effects. Wave 1 left **58** missing drafts; registering 83 additional routes now would inflate content debt without source/claim clearance.

**Doctrine reference:** `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`, `CORPUS_PRODUCTION_WAVE_CONTROL_MODEL.md`, `CORPUS_PRODUCTION_GATE_MODEL.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `ROUTE_REGISTRATION_WAVE_1_REPORT.md`.

**Sprint 5O-B validation:**

- Dry-run candidates: **83** (all absent from `routes.json`).
- Language split: **72** `en`, **11** `de`; ar/zh/ja excluded.
- Candidate status: **74** `dry_run_candidate`, **9** `dry_run_candidate_needs_review`.
- Route count **126**; draft-backed **68**; missing drafts **58**.
- L2 production runtime **PASS**; L1 corpus runtime **PASS**; guardrail runtime **PASS**.
- Planner: publication/indexation/sitemap/navigation locks **LOCKED**; `production_can_safely_proceed: no`.
- `routes.json`, registries, content pages — **not modified**.
- **0** approved claims; registries **inactive**; all routes `planned`, non-indexable.

**Publication readiness:** **Not ready for publication**. Dry-run planning sprint only — Route Registration Wave 2 execution **not approved**.

**Recommended next sprint:** Sprint **5N-G** — named source candidate intake (`de_core_mos2`); parallel Draft Wave 1 backlog reduction. **Do not** execute Route Registration Wave 2 or Draft Wave 2 in the next sprint without explicit execution charter and cleared blockers.

**Files created:**

- `main/data/PRODUCTION_DRY_RUN_WAVE_PLANNING_REPORT.md`
- `main/data/ROUTE_REGISTRATION_WAVE_2_DRY_RUN_MANIFEST.md`
- `main/data/ROUTE_REGISTRATION_WAVE_2_CANDIDATE_MATRIX.md`
- `main/data/ROUTE_REGISTRATION_WAVE_2_RISK_REVIEW.md`
- `main/data/ROUTE_REGISTRATION_WAVE_2_EXECUTION_BLOCKERS.md`
- `main/data/PRODUCTION_DRY_RUN_VALIDATION_REPORT.md`
- `main/data/PRODUCTION_DRY_RUN_NEXT_ACTIONS.md`

**Files updated:**

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Named Source Candidate Intake Wave 1 Completed

**Decision:** Complete named source candidate intake documentation for `de_core_mos2` without registry or content modification.

**Summary:** Sprint **5N-G** completed named source candidate intake documentation for `de_core_mos2` while keeping `sulfur_element_term_record` on a separate database-candidate naming track. The sprint preserved the distinction between candidate intake, source approval, registry execution, claim approval, source-locking, and publication readiness. Initial repository-internal finding: **`named_candidate_absent`**. After external human review (patch): intake re-classified to **`named_candidate_requires_external_verification`** with four documented candidate targets — **Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid** (primary DE lexicon), **PubChem — Molybdenum disulfide / CID 14823** (supporting database), **NIST Chemistry WebBook — molybdenum disulphide** (supporting technical data), **Chemie.de Lexikon — Molybdän(IV)-sulfid** (secondary DE support only). All candidates **unapproved**. Registry proposal drafting **blocked until human verification**; registry execution **blocked** (separate sprint). No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-F** made `de_core_mos2` the only conditional proposal-readiness candidate but recorded **named source candidate present: no**. Intake must confirm naming before proposal drafting — without inventing bibliographic details or treating evidence families as named candidates.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SOURCE_REGISTRY_PROPOSAL_READINESS_WAVE_1_REPORT.md`, `EXTERNAL_SOURCE_VERIFICATION_WAVE_1_REPORT.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`.

**Sprint 5N-G validation:**

- Intake target: **`de_core_mos2`** — **`named_candidate_requires_external_verification`** (post-patch; originally **`named_candidate_absent`** repository-internal).
- Named candidate targets documented: **4** (Spektrum primary; PubChem/NIST supporting; Chemie.de secondary) — all **unapproved**.
- `sulfur_element_term_record` — **not advanced**; database-candidate track unchanged.
- Route count **126**; draft-backed **68**; missing drafts **58**.
- L2 production runtime **PASS**; L1 corpus runtime **PASS**; guardrail runtime **PASS**.
- Planner: all locks **LOCKED**; `production_can_safely_proceed: no`.
- `source_registry.json`, `terminology_claims.json`, content — **not modified**.
- **0** approved claims; registries **inactive**; all routes `planned`, non-indexable.

**Publication readiness:** **Not ready for publication**. Named-source-intake documentation sprint only — registry execution **not allowed**.

**Recommended next sprint:** **Human external verification** of documented MoS2 named candidates (`de_core_mos2`). **Do not** proceed to source registry proposal drafting (5N-H) until verification completes; registry editing remains blocked. Parallel: `sulfur_element_term_record` database candidate naming; Draft Wave 1 backlog reduction.

**Files created:**

- `main/data/NAMED_SOURCE_CANDIDATE_INTAKE_WAVE_1_REPORT.md`
- `main/data/NAMED_SOURCE_CANDIDATE_INTAKE_MATRIX_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_ACCEPTANCE_RULES_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_NEXT_ACTIONS_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-G entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — GitHub Actions Governance Workflow Layer Established

**Decision:** Establish read-only GitHub Actions governance CI for merge-time corpus validation.

**Summary:** Sprint **5P-A** established the first GitHub Actions governance workflow layer for Bisulfid.com. The sprint added a read-only Corpus Governance CI workflow that runs existing L1, source/claim guardrail, and L2 production validation scripts on pull requests and manual dispatch. The workflow is governance-only, not deployment automation. It does not publish routes, generate HTML, approve claims, register sources, modify registries, create content pages, use secrets, deploy to GitHub Pages, or integrate Cloudflare. No routes were added, no content pages were created, no sources were added, no claims were approved, no public output was generated, and all publication/indexation locks remain active.

**Rationale:** Scaling toward **500** governed pages requires merge-blocking validation beyond local runs. L1 (**5K**), guardrails (**5N-B**), and L2 (**5O-A**) runtimes must enforce the same discipline on every PR to `main` before deployment or generation automation is considered.

**Doctrine reference:** `CORPUS_PRODUCTION_AUTOMATION_LAYER_2_REPORT.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `GITHUB_ACTIONS_GOVERNANCE_SECURITY_MODEL.md`.

**Sprint 5P-A validation:**

- Workflow: `.github/workflows/corpus-governance-ci.yml` — **Corpus Governance CI**.
- Triggers: `pull_request` → `main`, `workflow_dispatch` only.
- Permissions: `contents: read`; no secrets; no deploy; no artifacts; no package install.
- Scripts: L1 runtime, guardrail runtime, L2 runtime, L2 planner, L0 route registry, L0 content drafts.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README — **not modified**.

**Publication readiness:** **Not ready for publication**. Governance CI sprint only — no deployment.

**Recommended next sprint:** **5N-H prep** — human external verification for `de_core_mos2` named candidates; enable branch protection for Corpus Governance CI.

**Files created:**

- `.github/workflows/corpus-governance-ci.yml`
- `main/data/GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`
- `main/data/GITHUB_ACTIONS_GOVERNANCE_SECURITY_MODEL.md`
- `main/data/GITHUB_ACTIONS_GOVERNANCE_VALIDATION_REPORT.md`
- `main/data/GITHUB_ACTIONS_GOVERNANCE_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5P-A entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, existing automation scripts, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Named Candidate Human Verification Wave 1 Completed

**Decision:** Complete human verification documentation for `de_core_mos2` named candidate sources without registry, claim, or content execution.

**Summary:** Sprint **5N-H** completed human verification documentation for `de_core_mos2` named candidate sources. Spektrum was reviewed as the primary German specialist lexicon candidate (`primary_candidate_verified_for_later_proposal`), while PubChem and NIST were kept as supporting database/technical candidates and Chemie.de was kept as secondary German-language support only. The sprint preserved the distinction between human verification, source approval, source registry execution, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-G** documented named candidate targets requiring external human verification. Controlled human verification must confirm authority role fit before source registry proposal drafting — without treating verification as approval or registry execution.

**Doctrine reference:** `NAMED_SOURCE_CANDIDATE_ACCEPTANCE_RULES_WAVE_1.md`, `NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md`, `doctrine/SOURCE_POLICY.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-H validation:**

- Target: `de_core_mos2` — **1** draft verified.
- Spektrum: **`primary_candidate_verified_for_later_proposal`** — not approved.
- PubChem / NIST: supporting-only; **`rejected_as_primary_german_authority`**.
- Chemie.de: **`secondary_german_support_only`**; **`not_primary_authority`**.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Human verification sprint only — no source-locking.

**Recommended next sprint:** **5N-I prep** — source registry proposal drafting for `de_core_mos2` with human-verified Spektrum bibliographic lines; still no registry execution.

**Files created:**

- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_WAVE_1_REPORT.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_CANDIDATE_AUTHORITY_REVIEW_WAVE_1.md`
- `main/data/SUPPORTING_CANDIDATE_BOUNDARY_REVIEW_WAVE_1.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_RISK_REVIEW_WAVE_1.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_NEXT_ACTIONS_WAVE_1.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-H entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Source Registry Proposal Draft Wave 1 Completed

**Decision:** Complete source registry proposal drafting documentation for `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-I** completed source registry proposal drafting documentation for `de_core_mos2`. Spektrum was drafted as the primary German specialist lexicon proposal candidate for later source registry review, while PubChem and NIST remain supporting database/technical candidates and Chemie.de remains secondary German-language support only. The sprint preserved the distinction between proposal drafting, source registry execution, source approval, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-H** verified Spektrum as **`primary_candidate_verified_for_later_proposal`**. Structured proposal drafting must precede registry execution so human reviewers can assess intended registry role, claim boundaries, and supporting-only discipline before any `source_registry.json` modification.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SOURCE_REGISTRY_PROPOSAL_DRAFTING_CRITERIA_WAVE_1.md`, `NAMED_CANDIDATE_HUMAN_VERIFICATION_WAVE_1_REPORT.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-I validation:**

- Target: `de_core_mos2` — **1** draft proposal.
- Spektrum: **`proposal_draft_primary_candidate`** — not approved; execution **not allowed now**.
- PubChem / NIST: supporting-only proposal boundaries.
- Chemie.de: secondary-only proposal boundary.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Proposal drafting sprint only — no source-locking.

**Recommended next sprint:** **5N-J prep** — source registry execution review with human-verified Spektrum bibliographic fields; still requires separate execution charter.

**Files created:**

- `main/data/SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_DRAFT_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1.md`
- `main/data/SUPPORTING_SOURCE_BOUNDARY_PROPOSAL_DRAFT_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_EXECUTION_BLOCKERS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_DRAFT_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-I entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Source Registry Execution Readiness Wave 1 Completed

**Decision:** Complete source registry execution readiness documentation for `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-J** completed source registry execution readiness documentation for `de_core_mos2`. Spektrum was reviewed as the primary German specialist lexicon source execution candidate for a future `source_registry.json` entry, while PubChem, NIST, and Chemie.de remain bounded supporting candidates. The sprint preserved the distinction between execution readiness, source registry execution, source approval, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-I** drafted Spektrum as **`proposal_draft_primary_candidate`**. Execution readiness must confirm verified vs unverified registry fields before any `source_registry.json` modification — without treating readiness as execution or approval.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1.md`, `SOURCE_REGISTRY_PROPOSAL_EXECUTION_BLOCKERS_WAVE_1.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-J validation:**

- Target: `de_core_mos2` — **1** draft readiness review.
- Spektrum: **`execution_readiness_candidate`**, **`execution_blocked_pending_field_verification`**, **`execution_not_allowed_now`** — not approved.
- PubChem / NIST / Chemie.de: **`supporting_boundary_retained`**, **`not_primary_registry_source_now`**.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Execution readiness sprint only — no source-locking.

**Recommended next sprint:** **5N-K prep** — human bibliographic field verification for Spektrum; then separate execution sprint if readiness clears.

**Files created:**

- `main/data/SOURCE_REGISTRY_EXECUTION_READINESS_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_EXECUTION_READINESS_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_EXECUTION_READINESS_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_ENTRY_FIELD_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_EXECUTION_RISK_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_EXECUTION_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_EXECUTION_READINESS_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-J entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Spektrum Bibliographic Field Verification Wave 1 Completed

**Decision:** Complete bibliographic field verification documentation for the Spektrum candidate associated with `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-K** completed bibliographic field verification documentation for the Spektrum candidate associated with `de_core_mos2`. The sprint identified which governance/source fields are verified for a future registry proposal and which bibliographic fields remain unverified, must stay blank, or require direct source access. The sprint preserved the distinction between bibliographic verification, source registry execution, source approval, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-J** classified Spektrum as **`execution_blocked_pending_field_verification`**. Bibliographic field verification must confirm verified vs unverified registry fields at bibliographic granularity before any `source_registry.json` modification — without treating verification as execution or approval.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SOURCE_REGISTRY_EXECUTION_READINESS_WAVE_1_REPORT.md`, `SPEKTRUM_EXECUTION_READINESS_REVIEW_WAVE_1.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-K validation:**

- Target: `de_core_mos2` — **1** draft field verification.
- Spektrum: **7** governance fields **verified**; **6** bibliographic fields **unverified** — **`execution_blocked_pending_direct_source_access`**, **`execution_not_allowed_now`** — not approved.
- PubChem / NIST / Chemie.de: **`supporting_boundary_retained`**, **`not_primary_registry_source_now`**.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Bibliographic verification sprint only — no source-locking.

**Recommended next sprint:** **5N-L prep** — direct source access bibliographic capture for Spektrum; then separate execution sprint if readiness clears.

**Files created:**

- `main/data/SPEKTRUM_BIBLIOGRAPHIC_FIELD_VERIFICATION_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_BIBLIOGRAPHIC_FIELD_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_FIELD_EVIDENCE_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_FIELD_GAP_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_BIBLIOGRAPHIC_VERIFICATION_RISK_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_BIBLIOGRAPHIC_VERIFICATION_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SPEKTRUM_BIBLIOGRAPHIC_FIELD_VERIFICATION_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-K entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Spektrum Direct Source Access Bibliographic Capture Wave 1 Completed

**Decision:** Complete direct source access bibliographic capture documentation for the Spektrum candidate associated with `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-L** completed direct source access bibliographic capture documentation for the Spektrum candidate associated with `de_core_mos2`. The sprint documented which bibliographic fields were captured through direct source access, which fields remain unavailable or require additional access, and which fields must stay blank rather than be invented. Direct access was **`direct_access_not_available`** in repository artifacts — **0** bibliographic fields captured; **6** remain blank. The sprint preserved the distinction between direct source capture, source registry execution, source approval, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-K** classified Spektrum as **`execution_blocked_pending_direct_source_access`**. Direct source access capture must document verified bibliographic values from direct inspection before any `source_registry.json` modification — without treating capture as execution or approval.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_BIBLIOGRAPHIC_FIELD_VERIFICATION_WAVE_1_REPORT.md`, `SOURCE_REGISTRY_FIELD_GAP_REVIEW_WAVE_1.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-L validation:**

- Target: `de_core_mos2` — **1** draft direct access capture review.
- Spektrum: **`direct_access_not_available`** in repository; **0** bibliographic fields captured; **6** remain blank — **`execution_still_blocked`**, **`execution_not_allowed_now`** — not approved.
- **7** governance fields carry forward verified from 5N-K.
- PubChem / NIST / Chemie.de: **`supporting_boundary_retained`**, **`not_primary_registry_source_now`**.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Direct source access capture sprint only — no source-locking.

**Recommended next sprint:** **5N-M prep** — verified bibliographic artifact capture with human sign-off for Spektrum; then separate execution sprint if readiness clears.

**Files created:**

- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_CAPTURE_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_FIELD_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_EVIDENCE_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_CAPTURED_FIELD_GAP_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_RISK_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-L entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Spektrum Verified Bibliographic Artifact Intake Wave 1 Completed

**Decision:** Establish governed bibliographic artifact intake documentation for the Spektrum candidate associated with `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-M** completed verified bibliographic artifact intake documentation for the Spektrum candidate associated with `de_core_mos2`. The sprint defined required human-provided evidence, intake field matrix, source artifact deposit protocol, and human sign-off checklist. No verified artifact bundle is present in repository — **0** intake fields deposited; **10** required fields missing or awaiting human confirmation. The sprint preserved the distinction between artifact intake, source registry execution, source approval, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-L** documented **`direct_access_not_available`** with **0** bibliographic fields captured. A governed intake layer must define exact evidence requirements before any `source_registry.json` modification — without treating intake as execution or approval.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_DIRECT_SOURCE_ACCESS_CAPTURE_WAVE_1_REPORT.md`, `SPEKTRUM_BIBLIOGRAPHIC_FIELD_VERIFICATION_WAVE_1_REPORT.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-M validation:**

- Target: `de_core_mos2` — **1** artifact intake layer.
- Spektrum: artifact bundle **absent**; **0** intake fields present — **`execution_still_blocked`**, **`execution_not_allowed_now`**, **`source_approval_not_allowed_now`** — not approved.
- **7** governance fields carry forward verified from 5N-K.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Artifact intake sprint only — no source-locking.

**Recommended next step:** Human artifact deposit + sign-off per deposit protocol; then separate registry execution sprint if readiness clears.

**Files created:**

- `main/data/SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_INTAKE_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_FIELD_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_SOURCE_ARTIFACT_DEPOSIT_PROTOCOL_WAVE_1.md`
- `main/data/SPEKTRUM_BIBLIOGRAPHIC_HUMAN_SIGNOFF_CHECKLIST_WAVE_1.md`
- `main/data/SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_RISK_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_INTAKE_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-M entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-30 — Spektrum Human Bibliographic Artifact Review Wave 1 Completed

**Decision:** Complete human bibliographic artifact review documentation for the Spektrum candidate associated with `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-N** completed human bibliographic artifact review for the Spektrum candidate associated with `de_core_mos2`. The repository owner supplied a direct-access bibliographic receipt from the live Spektrum Lexikon der Chemie page. The sprint classified **8** fields as **`verified_from_human_artifact`**, **2** fields as **`not_visible_from_source`** (`publication_date`, `edition_or_version` — remain blank), and copyright 1998 as **`visible_but_policy_sensitive`** rights evidence only — **not** `publication_date`. Posture upgraded to **`execution_candidate_after_artifact_review`**. Preserved: **`source_registry_execution_not_allowed_now`**, **`source_approval_not_allowed_now`**, **`claim_approval_not_allowed_now`**, **`production_can_safely_proceed: no`**. No source entries added, `source_registry.json` was not modified, no claims were approved, content pages were not edited, routes were not published, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-M** defined artifact intake requirements but recorded no human bundle. Human artifact review must evaluate the repository-owner receipt before chartering a separate execution sprint — without treating review as execution or approval.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_INTAKE_WAVE_1_REPORT.md`, `SPEKTRUM_SOURCE_ARTIFACT_DEPOSIT_PROTOCOL_WAVE_1.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-N validation:**

- Target: `de_core_mos2` — **1** human artifact review.
- Human receipt: **8** verified; **2** blank; copyright 1998 rights-only.
- Posture: **`execution_candidate_after_artifact_review`** — execution charter **may proceed**; execution **not allowed now**.
- Local runtimes **PASS**; route count **126**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Human artifact review sprint only — no source-locking.

**Recommended next sprint:** **5N-O prep** — source registry execution charter for `SRC-SPEKTRUM-MOS2-DE` using human-reviewed receipt; blank `publication_date`; documented `access_date` 2026-05-30.

**Files created:**

- `main/data/SPEKTRUM_HUMAN_ARTIFACT_REVIEW_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_HUMAN_ARTIFACT_FIELD_CLASSIFICATION_WAVE_1.md`
- `main/data/SPEKTRUM_HUMAN_ARTIFACT_EXECUTION_CHARTER_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_HUMAN_ARTIFACT_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-N entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.
