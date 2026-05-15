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
