# Academic Teaching Source Registration Report

## Why This Sprint Exists

Sprint 4D implemented `academic_teaching_reference` as a governed candidate-only category for university and academic instructional sources.

Sprint 4E uses that new category to register selected German academic teaching references for the inorganic `-id` nomenclature pattern. The sprint adds candidate source support only. It does not approve claims, publish routes, modify content pages, or remove `[SOURCE REQUIRED]` markers.

## Category Used

- `academic_teaching_reference`

This category is candidate-only. It may support source-search review, draft-page review, and cautious educational terminology context where directly stated. It is not formal nomenclature authority and cannot approve claims alone.

## Sources Evaluated

### FH Münster - Anorganische Nomenklatur

- Source ID: `SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR`
- URL: `https://www-backend.fh-muenster.de/ciw/downloads-ciw/personenprofile/juestel/wissenswertes/chemie/Anorganische-Nomenklatur.pdf`
- Category fit: Fits `academic_teaching_reference` as a German university/applied-sciences teaching or instructional chemistry reference.
- Registration decision: Registered as a seeded candidate source.

### Universität Rostock - Materialdesign / Nomenklatur

- Source ID: `SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN`
- URL: `https://www.lkv.uni-rostock.de/storages/uni-rostock/Alle_MNF/Chemie_Koeckerling/Materialdesign_12_Nomenklatur.pdf`
- Category fit: Fits `academic_teaching_reference` as a German university teaching or instructional chemistry reference.
- Registration decision: Registered as a seeded candidate source.

### Springer / Jander - Nomenklatur anorganischer Verbindungen

- Potential source ID: `SRC-SPRINGER-JANDER-ANORGANISCHE-NOMENKLATUR-ID`
- URL: `https://link.springer.com/content/pdf/10.1007/978-3-642-71367-5_22.pdf`
- Category fit: Not clearly governed by `academic_teaching_reference`.
- Registration decision: Not registered in Sprint 4E.

Springer/Jander appears to be textbook or book-chapter material rather than a university teaching PDF or academic department instructional handout. Because Sprint 4D did not create a `textbook_reference` category and the current policy does not clearly govern publisher-hosted textbook chapters under `academic_teaching_reference`, this source was left out.

## Sources Registered

- `SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR`
- `SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN`

Both sources were registered with:

- `category: academic_teaching_reference`
- `status: seeded`
- `source_lock_status: candidate`
- `last_reviewed: "2026-05-16"`
- `use_for`
- `do_not_use_for`
- `risk_notes`

## Sources Not Registered and Why

- `SRC-SPRINGER-JANDER-ANORGANISCHE-NOMENKLATUR-ID` was not registered because textbook or book-chapter material is not clearly governed by the current `academic_teaching_reference` category.

No Wikipedia source, AI summary, market source, safety source, medical source, procurement source, or acquisition source was registered.

## How Each Registered Source Is Limited

The FH Münster and Universität Rostock sources may support:

- Candidate academic teaching support for German inorganic nomenclature context.
- Cautious explanation of `-id` endings where directly stated.
- Source-search support for `sulfid_vs_sulfide` and `german_english_chemical_terms` drafts.

They must not support:

- Formal DIN rule claims.
- Official German IUPAC authority claims.
- Universal suffix transformation claims.
- Final claim approval by themselves.
- Market data.
- Safety advice.
- Medical claims.
- Industrial procurement claims.
- Acquisition claims.
- Removal of `[SOURCE REQUIRED]` markers by themselves.
- Route publication by themselves.

## Academic Teaching Support vs Formal Nomenclature Authority

Academic teaching references can help document how nomenclature concepts are taught in educational contexts. They are useful for draft review and source-search context.

They do not establish formal nomenclature authority. They are not DIN, not official German IUPAC, not GDCh, and not a recognized formal nomenclature standard. Any public claim that sounds formal or normative still requires stronger authority.

## Claims Added

- `CLM-TERM-GERMAN-ID-ACADEMIC-001`

This claim is `pending_review` only. It links only to the academic teaching sources registered in this sprint.

`CLM-TERM-GERMAN-ID-FORMAL-GAP-001` was not added. The formal source gap is documented in this report and prior Sprint 4B/4C/4D reports, and adding a source-gap claim was not necessary for the source registration step.

## Why No Claims Were Approved

No claims were approved because academic teaching references are candidate-only by policy and cannot approve claims alone.

The new claim remains `pending_review`, and the claim registry remains inactive.

## Why No Routes Were Published

No routes were published because candidate academic teaching sources do not source-lock formal public claims by themselves.

All routes remain planned, non-indexable, and excluded from the sitemap.

## Why No Content Pages Were Modified

No content pages were modified because this sprint only registers candidate sources and a pending-review claim.

No `[SOURCE REQUIRED]` markers were removed. Any content update must wait for a later content/source-locking sprint.

## Remaining Source Gaps

- DIN or official German IUPAC source for the German `-id` naming rule.
- GDCh or equivalent recognized German chemistry authority.
- Stronger Bisulfid/Bisulfide boundary source.
- Clear governance for textbook or book-chapter sources if Springer/Jander is to be registered later.

## Publication Readiness Conclusion

Not ready for publication.

Sprint 4E improves candidate academic teaching support for source review, but it does not establish formal German nomenclature authority, approve claims, publish routes, or make `sulfid_vs_sulfide` public-ready.

## Recommended Next Sprint

Sprint 4F should perform a source-to-claim alignment review for the German `-id` pattern now that dictionary, English IUPAC context, and academic teaching candidate support exist.

The next sprint should still avoid claim approval unless a formal DIN, official German IUPAC, GDCh, or equivalent source is found and registered.
