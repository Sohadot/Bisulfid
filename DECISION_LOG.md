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
