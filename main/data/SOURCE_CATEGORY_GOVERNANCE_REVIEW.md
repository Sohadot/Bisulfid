# Source Category Governance Review

## Why This Review Exists

Sprint 4B found useful German academic, teaching, and book/chapter sources for the inorganic `-id` naming pattern, but those sources were not added to `source_registry.json` because the current governed source categories do not explicitly cover academic teaching PDFs, university lecture materials, textbook chapters, or technical educational references.

Sprint 4C reviews whether Bisulfid should later add a controlled category for those source types. This sprint does not implement a new category, does not change `SOURCE_POLICY.md`, does not change `source_registry.json`, does not add sources, and does not add or approve claims.

## Current Governed Source Categories

The current source registry categories are:

- `authoritative_dictionary`
- `chemical_nomenclature_standard`
- `government_scientific_database`
- `regulatory_body`
- `peer_reviewed_journal`
- `industry_publication`
- `market_report`

These categories favor formal authority, institutional traceability, and source types that can be scoped with clear limits.

## Source Gap Discovered in Sprint 4B

Sprint 4B evaluated German university teaching PDFs and Springer/Jander book/chapter material relevant to the `-id` ending in inorganic naming. These sources appeared useful for source-search context, but they were not DIN, official German IUPAC, GDCh, regulatory, government scientific database, authoritative dictionary, market report, industry publication, or peer-reviewed journal sources.

The gap is not a lack of interesting evidence. The gap is governance: the registry does not yet define whether instructional chemistry sources can be admitted, how they should be labeled, and what they may or may not support.

## Source Type Distinctions

### Authoritative Dictionary

An authoritative dictionary supports lexical existence, spelling, meaning, and usage boundaries for a term. It can support statements such as Duden recording `Sulfid`, `Oxid`, or `Chlorid` as German lexical entries. It does not establish a formal chemical nomenclature rule.

### Chemical Nomenclature Standard

A chemical nomenclature standard supports formal naming rules where directly stated. IUPAC, DIN, or recognized official nomenclature publications may support formal nomenclature claims if the source is directly applicable to the language and rule being claimed.

### Government Scientific Database

A government scientific database supports chemical identity, formula, registry, synonym, or database context where directly stated. It does not by itself support market, safety, medical, or formal language-rule claims.

### Regulatory Body

A regulatory body supports regulatory classification, legal status, or compliance context where directly stated. It must not be converted into general science, market, or medical advice beyond its scope.

### Peer-Reviewed Journal

A peer-reviewed journal can support scientific findings, methods, or domain-specific claims when directly relevant. It usually does not function as a formal nomenclature authority unless the article itself is a recognized standards or nomenclature publication.

### Industry Publication

An industry publication can support observed commercial or technical usage, but it has lower authority for formal definitions and must not support safety, medical, market, or procurement claims without stronger qualified sources.

### Academic Teaching Reference

An academic teaching reference includes university lecture PDFs, course handouts, institutional teaching notes, and instructional chemistry materials. It can be useful for understanding how concepts are taught, but it is secondary and should not be treated as a formal standard.

### Textbook Reference

A textbook reference or publisher-hosted book chapter can provide structured educational synthesis and may be more stable than a web page. It is still generally secondary instructional authority, not a formal standards source unless the work is itself an official standard.

## Evaluated Category Options

### `academic_teaching_reference`

- Strategic value: High for recording university-level educational support discovered during source searches.
- Trust level: Medium when institution, author, date, and context are identifiable.
- Risk level: Medium to high if used as formal authority.
- Permitted uses: Candidate support for draft explanations, source-search reports, and cautious educational context where directly stated.
- Prohibited uses: Formal DIN/IUPAC/GDCh rule claims, claim approval alone, route publication alone, market claims, safety advice, medical claims, procurement claims, and acquisition claims.
- Public claim support: Should not approve public claims alone.
- Draft/source-search support: Suitable for source-search and gap-analysis support.
- Stronger source requirement: Should require a stronger formal source before publication of formal rule language.
- Asset risk: Could weaken the asset if low-quality course materials are admitted too broadly.

### `technical_educational_reference`

- Strategic value: Medium; broader than academic sources and may cover institutional technical explainers.
- Trust level: Variable, depending on publisher and review context.
- Risk level: High because the category name could become too broad.
- Permitted uses: Internal source-search context and cautious draft support only.
- Prohibited uses: Formal authority claims, standalone public claim approval, market, safety, medical, procurement, and acquisition claims.
- Public claim support: Not alone.
- Draft/source-search support: Yes, if tightly documented.
- Stronger source requirement: Required for publication.
- Asset risk: Broad wording could invite weak educational pages into the registry.

### `textbook_reference`

- Strategic value: Medium to high for stable publisher-hosted chemistry explanations.
- Trust level: Medium to high when publisher, edition, authors, and chapter context are clear.
- Risk level: Medium if limited to reputable publishers and identifiable editions.
- Permitted uses: Candidate educational context, comparison support, and source-search reports.
- Prohibited uses: Formal standards authority unless the textbook reproduces or cites an official standard and the official standard is separately sourced.
- Public claim support: Possibly for cautious educational claims after review, but not for formal rule claims alone.
- Draft/source-search support: Yes.
- Stronger source requirement: Required before formal nomenclature publication.
- Asset risk: Lower than broad educational references if restricted to reputable publishers, but still weaker than formal standards.

### `educational_chemistry_reference`

- Strategic value: Medium; clear domain scope.
- Trust level: Variable.
- Risk level: Medium to high because it can include many source qualities.
- Permitted uses: Candidate chemistry education context and internal source-search documentation.
- Prohibited uses: Formal authority, safety, medical, market, procurement, and acquisition claims.
- Public claim support: Not alone for formal or high-risk claims.
- Draft/source-search support: Yes.
- Stronger source requirement: Required for publication of formal rule language.
- Asset risk: Could dilute source discipline if not limited by institution, author, date, and review context.

## Should Academic Teaching References Be Allowed?

Recommendation: allow only later, if a narrow governed category is created with strict safeguards.

Academic teaching references are useful for source discovery and educational context, especially when a university chemistry department publishes a directly relevant document. They should not be treated as formal nomenclature authority, and they should not approve public claims alone.

## Should Textbook References Be Allowed?

Recommendation: allow later under a narrower category or sub-scope than general educational references.

Textbooks and publisher-hosted book chapters can be strategically useful because they are often authored, edited, and stable. They still remain secondary instructional sources. They may support cautious educational context, but formal nomenclature claims still require DIN, official IUPAC German, GDCh, or equivalent authority.

## Should University Teaching PDFs Be Allowed?

Recommendation: allow later only for source-search and candidate support unless paired with stronger formal sources.

University teaching PDFs can explain nomenclature patterns clearly, but they vary in review depth, version control, and long-term availability. They should require institution, author or department, date or access date, course/context, URL, and risk notes.

## Risks of Expanding Source Categories

- Overclaiming authority by treating instructional material as standards material.
- Treating teaching material as a formal DIN, IUPAC, or GDCh rule.
- Making public claims before source-locking is complete.
- Weakening scientific credibility through overuse of secondary educational sources.
- Opening the registry to low-quality course notes, unsourced explainers, or unstable PDFs.
- Creating category drift where convenience sources replace authoritative sources.

## Benefits of Controlled Expansion

- Better documentation of source-search work when formal sources are hard to find.
- More transparent distinction between candidate instructional support and formal authority.
- Ability to preserve useful leads without approving claims prematurely.
- Better governance for draft pages that need cautious educational context.
- Clearer audit trail for why a source was considered but not source-locking authority.

## Recommended Decision

Recommendation: **B. Add a narrow category later**, but only after a separate doctrine or registry implementation sprint.

The preferred future category name is `academic_teaching_reference` if the intent is limited to university and institutional teaching material. If textbooks are included, `textbook_reference` should be a separate category or explicit sub-scope rather than being hidden inside a broad educational category.

Do not add a broad `technical_educational_reference` category without tighter controls. It is too easy to stretch and could weaken the asset if used as a catch-all for convenient sources.

## Proposed Safeguards

If a future category is approved, it should include these safeguards:

- Candidate only by default.
- Cannot approve claims alone.
- Cannot prove formal nomenclature authority.
- Must be paired with stronger source for publication of formal rules.
- Must include publisher or institution, author or department where available, date or access date, URL, and teaching or textbook context.
- Must include `use_for`, `do_not_use_for`, and `risk_notes` arrays.
- Must not support market, safety, medical, procurement, or acquisition claims.
- Must not remove `[SOURCE REQUIRED]` markers by itself.
- Must not be used to publish routes by itself.
- Must be scoped to the exact statement directly supported by the source.

## What Must Not Change Yet

- Do not change `SOURCE_POLICY.md`.
- Do not change `source_registry.json` categories.
- Do not add academic teaching or textbook sources yet.
- Do not add or approve claims based on these source types yet.
- Do not modify content pages or remove `[SOURCE REQUIRED]` markers.
- Do not publish routes or activate sitemap/navigation/indexation state.

## Publication Readiness Conclusion

Not ready for publication.

Sprint 4C is a governance review only. It does not close the formal German nomenclature source gap, does not approve claims, and does not make `sulfid_vs_sulfide` public-ready.

## Recommended Next Sprint

Sprint 4D should decide whether to implement a narrow governed category.

Recommended Sprint 4D path:

- Review `SOURCE_POLICY.md` and `source_registry.json` category taxonomy together.
- If approved, add a narrow `academic_teaching_reference` category with explicit safeguards.
- Consider a separate `textbook_reference` category only if publisher-hosted chemistry textbooks are intended to be governed differently from university teaching PDFs.
- Do not add sources in the same sprint unless the category implementation and validation rules are complete.
- Keep all new category usage candidate-only until a later source-locking sprint.
