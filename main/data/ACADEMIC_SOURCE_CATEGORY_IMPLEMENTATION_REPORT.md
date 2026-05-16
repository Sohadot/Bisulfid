# Academic Source Category Implementation Report

## Why This Sprint Exists

Sprint 4B found useful German academic, teaching, and book/chapter sources for the inorganic `-id` pattern, but those sources were not added because the source registry did not govern academic teaching or instructional chemistry references.

Sprint 4C reviewed the category gap and recommended a narrow future category with strict safeguards. Sprint 4D implements that governance category only. It does not add source entries, claims, content changes, or publication state.

## Decision Inherited from Sprint 4C

Sprint 4C recommended that Bisulfid may add a narrow controlled category later, rather than a broad educational catch-all. It specifically preferred a focused `academic_teaching_reference` category with candidate-only behavior and safeguards against treating teaching material as formal nomenclature authority.

Sprint 4D implements that recommendation.

## Category Implemented

Exact category name:

- `academic_teaching_reference`

Definition:

A source produced by a recognized university, academic department, instructor, or educational chemistry program for teaching or instructional purposes. It may support candidate terminology context, classroom-level nomenclature explanation, or source-search review, but it is not a formal nomenclature standard and cannot independently approve public claims.

## What the Category Permits

`academic_teaching_reference` may support:

- Candidate terminology context.
- Source-search support.
- Draft-page review support.
- Cautious educational explanation where directly stated.
- Support for identifying terms requiring stronger source-locking.

Any source added under this category in a future sprint must include institution or publisher, title, URL, language, last reviewed date, `use_for`, `do_not_use_for`, and `risk_notes`.

## What the Category Forbids

`academic_teaching_reference` must not support:

- Formal nomenclature authority.
- DIN rule claims.
- Official IUPAC German rule claims.
- Universal suffix transformation claims.
- Final claim approval by itself.
- Market data.
- Safety advice.
- Medical claims.
- Industrial procurement claims.
- Acquisition claims.
- Removal of `[SOURCE REQUIRED]` markers by itself.
- Publication readiness by itself.

It also cannot mark ontology terms verified, cannot support route publication by itself, and must be paired with a stronger source for any public claim that sounds formal, normative, regulatory, medical, safety-related, market-related, or procurement-related.

## Why No Sources Were Added

No source entries were added in Sprint 4D because this sprint implements governance only.

FH Münster, Universität Rostock, Springer/Jander, and similar sources require a later candidate-source sprint where each source can be reviewed, scoped, and added with `status: seeded`, `source_lock_status: candidate`, and explicit `use_for`, `do_not_use_for`, and `risk_notes` arrays.

## Why No Claims Were Added

No claims were added because no source entries were added and no source-to-claim review was performed in this sprint.

Adding claims before registering and scoping specific candidate sources would weaken the source governance chain.

## Why No Claims Were Approved

No claims were approved because `academic_teaching_reference` is candidate-only by design and cannot approve claims alone.

Existing claims remain pending review. Claim registries remain inactive.

## Why No Routes Were Published

No routes were published because a category implementation does not source-lock claims, approve claims, remove `[SOURCE REQUIRED]` markers, or make draft pages public-ready.

All routes remain planned, non-indexable, and excluded from sitemap publication.

## Future Handling of FH Münster / Rostock / Springer-Jander Sources

The new category gives future sprints a governed place to evaluate university teaching PDFs and instructional chemistry material without overstating authority.

- FH Münster may be considered later as an `academic_teaching_reference` if the source is reviewed directly and scoped as educational support only.
- Universität Rostock may be considered later as an `academic_teaching_reference` if the source is reviewed directly and scoped as educational support only.
- Springer/Jander should be evaluated carefully. If treated as instructional textbook material, it may need either `academic_teaching_reference` or a future separate `textbook_reference` category. Sprint 4D does not add a textbook category.

None of these sources should be used as formal DIN, official German IUPAC, GDCh, or equivalent nomenclature authority unless the source itself is a recognized formal authority.

## Remaining Source Gaps

- DIN or official German IUPAC source for the German `-id` naming rule.
- GDCh or equivalent recognized German chemistry authority.
- Stronger Bisulfid/Bisulfide boundary source.

## Publication Readiness Conclusion

Not ready for publication.

Sprint 4D adds governance capacity only. It does not add sources, approve claims, publish routes, modify content pages, or close the formal German nomenclature source gap.

## Recommended Next Sprint

Sprint 4E should evaluate one or more candidate academic teaching sources under the new category, starting with the sources documented in Sprint 4B.

Recommended constraints for Sprint 4E:

- Add only candidate source entries that fit `academic_teaching_reference`.
- Keep every added source `status: seeded` and `source_lock_status: candidate`.
- Add `use_for`, `do_not_use_for`, and `risk_notes` arrays to every new source.
- Add only pending-review claims if source support justifies them.
- Do not approve claims, publish routes, modify content pages, or remove `[SOURCE REQUIRED]` markers.
