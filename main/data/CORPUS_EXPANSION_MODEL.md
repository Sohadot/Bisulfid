# Corpus Expansion Model — Sovereign Reference System

## Purpose

This document defines how Bisulfid.com grows from a **minimum public launch cohort** into a **large multilingual chemical-language reference corpus** without sacrificing sovereign-grade quality. **Growth is permitted only while quality gates remain strict.** Volume is an output of discipline, not a target decoupled from authority.

## Expansion horizons (conceptual scale)

| Horizon | Approximate scale | Role | Quality posture |
| --- | --- | --- | --- |
| **Launch cohort** | **≥ 300** governed reference pages | First public surface: minimum authority threshold | Highest scrutiny; zero thin pages; no public `[SOURCE REQUIRED]`; every page has a defined corpus role |
| **Authority layer** | **~500** pages | Strong cross-linking; disambiguation and multilingual bridges mature | Same gates as launch; additional multilingual pairs must each pass language-specific review |
| **Deep reference corpus** | **~1,000** pages | Specialist terminology, industrial interpretation, methodology depth | Batch creation with mandatory sampling audit; pruning rules active |
| **Multilingual industrial/scientific system** | **3,000+** pages (long-term) | Full Arabic, Chinese, Japanese, German layers with English spine | Anti–translation-spam rules; hub-and-spoke linking; optional tiered publication (some layers non-public longer) |

**Critical clarification:** **300 pages is not the final goal.** It is the **minimum governed page count** required before **any** public launch. The architecture expects **substantially larger** corpora over time if quality stays sovereign-grade.

## Expansion rules (non-negotiable)

1. **No orphan concepts:** Every proposed page must map to a future `route_id`, `content_file`, corpus category, and internal-linking cluster before build work begins.
2. **No route invention in content sprints:** Routes are added only in dedicated routing/registry sprints aligned with this architecture.
3. **No page without a role:** Each page declares one primary corpus role (terminology record, disambiguation authority, methodology, index hub, etc.).
4. **No thinning:** Pages below minimum substance thresholds (see `CORPUS_LAUNCH_THRESHOLD.md`) cannot enter the public cohort.
5. **No generic chemistry blog voice:** Explainers must remain terminology- and source-governed; narrative flourish does not substitute for authority.
6. **Multilingual growth ≠ translation spam:** New language pages are **controlled terminology records** with explicit `use_for` / `do_not_use_for` source alignment—not bulk machine translation of English.
7. **Industrial/economic interpretation ≠ market report:** Interpretation pages clarify *language*, *classification*, and *documentary context* for analysts; they do not host CAGR, market share, or procurement guidance unless independently governed elsewhere under SOURCE_POLICY.
8. **Safety-adjacent pages remain non-manuals:** Expansion must not turn safety-context pages into handling instructions or emergency procedures.

## Page quality gates (summary)

Detailed criteria live in `CORPUS_LAUNCH_THRESHOLD.md`. In short:

- Minimum content depth per category (anti-thin).
- Zero unresolved public `[SOURCE REQUIRED]` markers.
- Source-locked claims for every factual statement that is not pure internal methodology.
- Internal link graph: no broken required links; each public page has a declared cluster role.

## Source-locking requirements

- Every public factual claim traces to `main/data/sources/source_registry.json` per `doctrine/SOURCE_POLICY.md`.
- Category-appropriate sources only; `academic_teaching_reference` remains **candidate** and cannot stand alone for formal regulative or normative public claims.
- No raw URLs in public copy unless governed by source policy and internal linking rules.

## Claim approval gates

- Claim registries remain **inactive** until a dedicated activation sprint under `doctrine/QUALITY_GATE.md`.
- No page publishes with **unapproved** claims in scope for that page’s `required_claim_groups`.
- High `risk_level` routes (safety-adjacent, substance-specific industrial pages) require **explicit** launch eligibility review even when claims are approved.

## Multilingual scaling rules

1. **English** is the global **spine** for hreflang grouping and ontology alignment—not the only intellectual authority; German holds **identity and nomenclature-origin** privilege for Deutsche chemische Lexik.
2. Each language layer maintains **parallel terminology records**: definitions, cautions, and boundaries may legitimately **differ** from English where target-language standard works demand it.
3. **Translation memory tools** may assist drafting but **cannot** be the authority; human terminology editor sign-off required per batch.
4. **Expansion rate cap (recommended):** do not add more than **N** new public language pages per batch without audit (N set by ops; architecture default is conservative).
5. **Hub pages** per language (`/ar/reference-map/`, etc. in future routes) prevent orphan clusters.

## Internal linking density rules

- **Core terminology hub:** minimum inbound links from sibling terminology pages at launch (as declared in blueprint clusters).
- **Disambiguation pages:** must link to every canonical term record they disambiguate.
- **Index/map pages:** outbound only to governed routes; no dead `route_id` references.
- **No “link stuffing”:** links must serve corpus navigation, not SEO manipulation.

## Anti-thin-content rules

- Single-definition pages are allowed **only** if they meet minimum structured sections (scope, boundaries, source posture, related terms)—not a one-sentence stub.
- Lists without prose rationale are disallowed for public launch.
- “See Wikipedia” patterns are disallowed as content.

## Anti-generic-content rules

- Ban educational-blog tone (“In today’s world…”, undifferentiated explainer churn).
- Ban undifferentiated “chemistry 101” unless explicitly framed as **internal methodology** or **editor training** (non-public tiers).
- Every page ties back to **sulfur chemical language**, **bisulfide/sulfide family**, **German–English boundary**, or **documented governance** scope.

## Pruning rules for weak page concepts

Remove or merge a page concept when:

1. It duplicates another `route_id` role without distinct corpus purpose.
2. It cannot be source-supported at any approved category within 24 months (park as **non-public** or drop).
3. It invites generic SEO treatment rather than reference discipline.
4. It conflicts with safety/medical/procurement blocks in SOURCE_POLICY.
5. It fails internal link clustering (cannot attach to a hub without forced edges).

**Merged pages** must document redirect strategy *in routing sprints* (out of scope for passive architecture files).

## Relationship to other docs

- `SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md` — thesis, layers, audiences, strategy.
- `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` — ≥300 proposed launch-cohort concepts (blueprint only; not `routes.json`).
- `CORPUS_LAUNCH_THRESHOLD.md` — explicit launch and no-go conditions.

## Sprint 5A note

This model was **authored in Sprint 5A** as architecture-only documentation. **No** routes were published; **no** content files were created; **no** registries were modified.
