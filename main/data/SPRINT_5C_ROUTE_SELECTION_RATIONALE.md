# Sprint 5C — Route Selection Rationale

## Executive summary

Sprint **5C** selects **55** proposed `route_id` concepts—**44** English and **11** German—from the Sprint **5A** blueprint (`CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md`) under constraints established by Sprint **5B** (`LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md`, `LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md`). The output is **planning only**: no `routes.json` edits, no new content pages, no publication, no claim activation.

---

## Why these 40–55 concepts were selected first

The cohort prioritizes **trust surfaces** that compound:

1. **Source-governed terminology** — Element, anion, oxo-anion ladder, organosulfur class language, and selected mineral vocabulary establish density without relying on marketing narratives.
2. **German–English chemical language** — `what_is_bisulfid`, orthography and identity boundary pages, and crosswalk infrastructure are the **core differentiation** of bisulfid.com as a sovereign chemical-language asset.
3. **Disambiguation authority** — The bisulfide / hydrosulfide / sulfide triad plus the **bisulfite wall** reduce high-cost user confusion early.
4. **Source / nomenclature governance** — Editors cannot scale pages safely without visible discipline: nomenclature overview, citation primer, teaching-source boundaries, methodology, and internal-linking rules.
5. **Corpus infrastructure** — Index/map and ontology-alignment concepts are included **as planned work** but flagged **defer_until_later_corpus_phase** until hreflang and ontology activation are real.
6. **Industrial document language (bounded)** — A **small** set of Claus / FGD / hydrotreating / logistics / filings vocabulary pages extends the thesis **only** where outlines can ban market, procurement, operations, and compliance-advice drift.

Together, these 55 concepts form a **batch** that can be implemented with **editorial depth** rather than **horizontal sprawl**.

---

## Why not all 300+ concepts should be implemented at once

The **300-page** threshold is a **minimum launch cohort** for the sovereign reference layer—not an instruction to register every blueprint row simultaneously. Parallel mass implementation:

- increases **thin-page** and **list-only glossary** risk (explicitly warned in 5B),
- overwhelms **source_registry** mapping and citation discipline,
- encourages **translation spam** across locales before the EN+DE spine is locked,
- makes **duplicate merge work** (H₂S family, MoS₂/WS₂, bisulfite governance) more expensive after content exists.

Batching proves **quality recipes** (minimum sections, boundaries, internal-link density) before multiplying pages.

---

## Why ar / zh / ja pages remain deferred

Sprint **5B** deferred bulk **`ar_*` / `zh_*` / `ja_*`** mirrors until:

- **English** and **German** hubs are **source-locked**,
- **hreflang** group policy and registry wiring are designed (`multilingual_corpus_map` is flagged **defer** for this reason),
- native-language editorial review capacity exists (no MT-only public pages).

Batch 1 implements **zero** non-Latin/German locales by design.

---

## Why newsletter / acquire do not count toward the sovereign reference corpus

`newsletter` and `acquire` (each mirrored across locales in the blueprint) are **utility / operations** routes. They may exist for product strategy but **must not** be treated as part of the **300 governed chemical-language reference pages** (per 5B accounting). Batch 1 **excludes** them to keep the reference cohort **chemically and lexically coherent**.

---

## Why generic pages were excluded

Pages that read like undifferentiated “intro to chemistry” without binding to the Bisulfid thesis—German–English chemical language, bisulfide/sulfide family, disambiguation, and governed industrial **document language**—were **not** selected as Batch-1 priorities. Breadth rows (e.g. marginal mineral grids, Frasch history vocabulary) were deferred to avoid **coverage without authority**.

---

## Why source-governed terminology pages come first

`SOURCE_POLICY.md` requires that public-tier factual claims map to **`source_registry.json`**. Terminology records are the **atomic unit** of trust: if term pages are shallow or unsourced, every downstream industrial page inherits the same failure mode. Batch 1 therefore **front-loads** term records and gateway bridges that feed the spine.

---

## Why German–English terminology is strategically central

The asset thesis is not “another sulfur blog”; it is **cross-border chemical language infrastructure**. German orthography and English search intent collide precisely around **Bisulfid**, **Sulfid**, **bisulfide**, **hydrosulfide**, and related industrial German usage. Without DE/EN hub pages, the corpus cannot defend **sovereign** positioning in European industrial readership or DE-indexed queries.

---

## Why disambiguation authority pages are foundational

Disambiguation pages are **high leverage**: they prevent systematic misrouting of users and reduce accidental **false chemical claims** caused by conflating bisulfite vs bisulfide families or mis-labeling hydrosulfide chemistry. They are prerequisite to scaling **safe** internal linking.

---

## Why source / nomenclature governance pages are needed before publication

Publication under `QUALITY_GATE.md` requires repeatable editorial behavior: how citations surface, how teaching sources are bounded, how nomenclature disagreements are handled, and how internal links remain **route_id-centric** rather than URL-sprawl. These pages **train** the corpus—even if many remain **non-public** until signoff.

---

## How this batch moves toward the 300-page threshold without weakening quality

- **Sequence, not dilution:** Batch 1 occupies **~55** of **300+** planned reference slots—purposefully **under** the launch threshold to force **depth**.
- **Deferred work stays explicit:** mirrors, safety-heavy substance pages, and merge-cleanups are **not** hidden; they remain blueprint-visible but **out of Batch 1**.
- **300-page minimum remains doctrine:** this sprint **does not** lower the launch threshold; it prepares a **governed slice** that can be repeated in Batch 2, 3, *etc.*, with the same gates.

---

## Cross-reference

- Detailed roster: `main/data/LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md`
- Readiness classification: `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md`
- Architecture / thresholds: `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`, `main/data/CORPUS_LAUNCH_THRESHOLD.md`, `main/data/CORPUS_EXPANSION_MODEL.md`

---

*Sprint 5C — documentation only; no registry or content changes from this rationale.*
