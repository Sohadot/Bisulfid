# Terminology Reference Spine Boundary Review

## Why this sprint exists

Sprint 4J introduced the first **non-public terminology reference spine** (`glossary`, `sulfur_compounds`, `bisulfide_hydrosulfide_sulfide`) and reduced missing English `content_file` drafts from **14** to **11**. Sprint 4K is a **read-only boundary review**: it checks that these drafts behave as **sovereign-grade reference infrastructure** (terminology-first, governance-first) and do not drift toward generic chemistry articles, implicit claim approval, source overreach, market or safety copy, or publication readiness. **No new pages** are created; **no content pages** were modified in this sprint.

## Files reviewed (read-only)

- `main/content/en/pages/glossary.md`
- `main/content/en/pages/sulfur-compounds.md`
- `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md`
- `main/data/TERMINOLOGY_REFERENCE_SPINE_BATCH_1_REPORT.md`
- `main/data/ENGLISH_DRAFT_INVENTORY_REVIEW.md`
- `main/data/routes.json`
- `main/data/internal_links.json`
- `main/data/claims/terminology_claims.json`
- `main/data/sources/source_registry.json` *(registry path on disk; not `main/data/source_registry.json`)*
- `main/data/ontology/sulfur_terms.json`
- `DECISION_LOG.md`

## Summary of Sprint 4J outputs (baseline)

- Three English drafts at governed `content_file` paths, with required frontmatter (`draft`, `non_public`, `indexable` / `in_sitemap` false, `en` layer).
- `glossary.md`: controlled terminology chamber with a 14-term draft table and explicit lexical vs chemical vs candidate vs **no approved claims** framing.
- `sulfur-compounds.md`: sulfur terminology scope map with grouped lanes, teaching vs formal authority separation, and bisulfite called out as **not** the bisulfide/hydrosulfide lane.
- `bisulfide-hydrosulfide-sulfide.md`: triad disambiguation draft with bisulfite boundary, "what this page does not claim," and "source and claim status" sections.
- `TERMINOLOGY_REFERENCE_SPINE_BATCH_1_REPORT.md`: documents spine intent, 14/3/11 missing-draft math, and no publication recommendation.

## Route and publication state review

From `routes.json` (unchanged in this sprint), for `glossary`, `sulfur_compounds`, and `bisulfide_hydrosulfide_sulfide`:

- `status`: **planned**
- `indexable`: **false**
- `in_sitemap`: **false**
- `language`: **en**

The three markdown drafts consistently state they are **non-public**, **not published**, **not indexable**, **not** in the sitemap, **not** approved for public use, and **not publication-ready**. No conflict with route records was identified that would require content edits in this sprint.

## Page role review

| Route | Expected role | Review finding |
| --- | --- | --- |
| `glossary` | Controlled terminology chamber | **Passes** - rules table, chamber framing, explicit rejection of generic glossary and textbook depth. |
| `sulfur_compounds` | Sulfur terminology scope map | **Passes** - explicit scope-map purpose, grouped vocabulary lanes, non-goals list. |
| `bisulfide_hydrosulfide_sulfide` | Disambiguation authority **draft** | **Passes** - states it is not final authority; separates triad from safety pages; preserves bisulfite boundary. |

## Claim boundary review

- **`terminology_claims.json`** remains **`status: inactive`**. Individual claims (for example `CLM-TERM-001`, `CLM-TERM-002`) remain **`pending_review`**; **none** are verified or approved for publication.
- Spine drafts use **draft-level** and **candidate** language throughout; they state **no claim is approved** on-page.
- **`[SOURCE REQUIRED]`** remains dense and appropriate: factual lines that would read as public-grade are not offered without markers.
- **Spine drafts do not** remove or satisfy markers on **other** pages (stated explicitly in `glossary.md` and `bisulfide-hydrosulfide-sulfide.md`).

**Draft-level only (examples):** chamber operating rules; illustrative scope clusters; scope-map "lanes"; disambiguation "draft slots" and open questions.

**May be supported later by candidate / lexicon / chemical sources (when source-locked per policy):** DE **-id** surface forms for pattern illustration; cautious EN chemical label alignment where `source_registry.json` and claims permit (for example entries tied to hydrosulfide / sodium salt identity **only** within each source's `use_for`).

**Still needs stronger formal authority for publication-grade German regulatory / systematic claims:** any line that would assert **DIN**, **official German IUPAC**, or **national standards body** binding for public copy - not asserted today; remains future work.

**Must remain blocked (until explicit governance + sources):** treating academic PDFs as formal nomenclature authority; approving terminology without registry workflow; public-first phrasing on spine pages; collapsing **bisulfite** into sulfide-anion vocabulary.

## Source boundary review

Findings refer to **categories and examples** in `main/data/sources/source_registry.json` (read-only):

- **Duden / `authoritative_dictionary`:** suitable **later** for **lexical** existence and spelling-form discussion for German **-id** entries (for example sulfid, oxid, chlorid) **within** each source's registered `use_for` / `do_not_use_for` - not automatic proof for every English sentence on the spine.
- **`academic_teaching_reference`:** suitable **later** for **candidate teaching context** only (how a term is introduced in class), per `SOURCE_POLICY.md` constraints - **must not** stand in for DIN or official German IUPAC authority.
- **IUPAC / PubChem / NIST-class entries (where present):** may support **English chemical nomenclature or identity context** only where the registry entry explicitly allows and the claim pipeline locks - spine drafts correctly avoid asserting lock today.
- **DIN / official German IUPAC / GDCh-equivalent:** still **needed** for any future public claim that German **systematic** or **regulatory** authority requires a specific string; spine drafts **do not** claim that lock.

**Confirmed:** No spine draft treats teaching material as formal authority; several explicitly separate teaching support from authority (`sulfur-compounds.md`, `glossary.md` distinctions).

## Bisulfite disambiguation boundary review

- `glossary.md` table row for **Bisulfite** and boundary notes on bisulfide / sulfide rows.
- `sulfur-compounds.md` bisulfide/hydrosulfide group explicitly **not** the bisulfite family.
- `bisulfide-hydrosulfide-sulfide.md` §8 and §9 - **not** interchangeable with triad; **not** subsumed into triad.

`main/data/ontology/sulfur_terms.json` includes `not_to_be_confused_with` references such as **`bisulfite_disambiguation`** on relevant terms - consistent with draft boundary discipline (ontology **not** modified in this sprint).

## Generic content drift review

**No material drift** detected toward:

- encyclopedic systematic chemistry tutorials
- blog-style narrative
- undifferentiated "explainer" voice without governance scaffolding

Spine pages repeatedly anchor on **internal infrastructure** (chamber, scope map, disambiguation draft) and **Quality Gate / registry** deferrals.

## Safety, market, procurement exclusion review

- **Safety:** Disambiguation and scope pages **deflect** handling, exposure, and emergency duties; `bisulfide_hydrosulfide_sulfide` points high-risk routes to separate planned pages without absorbing them.
- **Market / procurement / acquisition:** **Non-goals** listed on `sulfur-compounds.md`; no market data, CAGR, trade statistics, procurement advice, or acquisition targeting in spine drafts.
- **Medical:** No medical claims identified in spine drafts.

## Internal reference role review

- **References:** Spine drafts use **`route_id`** backticks and plain text only; **no** raw URLs; **no** markdown public links that assume published targets.
- **Broken public links:** None introduced (planned routes only).
- **Fit in linking spine:** `internal_links.json` shows **`glossary`** as a **hub** (many groups link to it); **`sulfur_compounds`** connects gateway layer to **`sodium_bisulfide`** and **`glossary`**; **`bisulfide_hydrosulfide_sulfide`** links toward **`what_is_bisulfid`**, **`sodium_bisulfide`**, **`sulfur_safety_context`**, **`glossary`**, **`sources`**. This matches "terminology spine first, specialized drafts later."

**Suggested next draft connections (from remaining 11, inventory-consistent):**

1. `what_is_sulfur` - public-gateway alignment with scope map placeholder.
2. `sulfur_uses` - completes gateway pair with `sulfur_compounds` in link graph.
3. `sodium_bisulfide` - **high** `risk_level` in `routes.json`; only with explicit sprint authorization and safety doctrine.

## Statements that may later be source-locked (non-exhaustive)

- German lexical rows for Sulfid / Disulfid / Oxid / Chlorid where Duden (or successor) entries align with registry rules.
- Hydrosulfide / sodium salt **identity** language where IUPAC Gold Book / PubChem entries match allowed `use_for`.

## Statements that still require stronger authority

- Any future public sentence tying **German commercial** branding to **official systematic** German authority.
- Cross-language "universal suffix rule" as a verified fact.

## Statements that must remain blocked (until governance clears)

- Removing **`[SOURCE REQUIRED]`** from spine pages without claim approval.
- Using spine copy as **approved** public glossary output while registries are **inactive**.

## `[SOURCE REQUIRED]` markers that must remain

- All table rows and cluster bullets that describe chemical scope, authority class, or public-readiness without a locked claim chain.
- Publication blocker sections that premise future registry alignment.

## Why no claims were approved

Claim registries are **inactive**; Sprint 4K is **report-only**; no claim workflow was run.

## Why no routes were published

`routes.json` unchanged; all routes **planned**; no Quality Gate publication path executed.

## Why no content pages were created

Out of scope - boundary review only.

## Why no content pages were modified

No blocking governance inconsistency was found between drafts and `routes.json` / registry posture that required an emergency edit; **prefer report-only** per sprint charter.

## Remaining missing English draft count

**11** (per Sprint 4J / Sprint 4I inventory): `what_is_sulfur`, `sulfur_uses`, `sodium_bisulfide`, `disulfide_bonds`, `industrial_sulfur_systems`, `sulfur_safety_context`, `hydrogen_sulfide_risk`, `sds_and_sulfur_terms`, `protein_disulfide_structure`, `molybdenum_disulfide`, `newsletter`.

## Recommended next sprint

- **4L option A:** Controlled draft-creation sprint for **`what_is_sulfur`** (gateway coherence with `sulfur_compounds`), **or**
- **4L option B:** **`sulfur_uses`** to close the gateway pair, **or**
- **4L option C:** Source-locking sprint mapping specific spine table rows to **`terminology_claims.json`** entries - still **without** approving claims until registries activate under doctrine.

## Publication readiness conclusion

**Not ready for publication.** Spine drafts are **non-public reference infrastructure** only; 11 English routes still lack bodies; claims and ontology terms remain **unpublished** / **inactive** or **planned** per registry files.

## Sprint 4K change scope

**Created:** `main/data/TERMINOLOGY_REFERENCE_SPINE_BOUNDARY_REVIEW.md` (this report).

**Updated:** `DECISION_LOG.md`.

**Not modified:** `routes.json`, `internal_links.json`, sitemap/navigation/hreflang/translation JSON, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, all content pages, templates, root `README.md`, packages, workflows, generated HTML.
