# German Nomenclature Source Search Report

## Why This Sprint Exists

Sprint 4A added candidate lexical support for `Sulfid`, `Oxid`, and `Chlorid` as German dictionary forms, but it did not establish a formal German suffix rule.

Sprint 4B searched for stronger German nomenclature support for the `-id` pattern behind the `sulfid_vs_sulfide` draft, with strict limits: candidate sources may only be added if they fit existing governed source categories, and no academic or textbook category may be invented.

## Sources Searched and Evaluated

### FH Münster - Anorganische Nomenklatur

- Potential source ID: `SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR`
- URL: `https://www-backend.fh-muenster.de/ciw/downloads-ciw/personenprofile/juestel/wissenswertes/chemie/Anorganische-Nomenklatur.pdf`
- Observed relevance: German inorganic nomenclature teaching/reference PDF. It states that the following nonmetal atom or ion of binary compounds with negative oxidation number ends in `-id`.
- Evaluation: Useful academic/teaching support, but not DIN, not official German IUPAC, not a regulatory body, and not a peer-reviewed journal article.
- Registry decision: Not added. Category not currently governed.

### Universität Rostock - Materialdesign / Nomenklatur PDF

- Potential source ID: `SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN`
- URL: `https://www.lkv.uni-rostock.de/storages/uni-rostock/Alle_MNF/Chemie_Koeckerling/Materialdesign_12_Nomenklatur.pdf`
- Observed relevance: German university chemistry teaching PDF. It lists `-id` for anions and examples including `Fluorid`, `Chlorid`, `Oxid`, `Sulfid`, `Selenid`, `Nitrid`, `Phosphid`, and `Carbid`.
- Evaluation: Useful academic/teaching support, but not DIN, not official German IUPAC, not a regulatory body, and not a peer-reviewed journal article.
- Registry decision: Not added. Category not currently governed.

### Springer / Jander - Nomenklatur anorganischer Verbindungen

- Potential source ID: `SRC-SPRINGER-JANDER-ANORGANISCHE-NOMENKLATUR-ID`
- URL: `https://link.springer.com/content/pdf/10.1007/978-3-642-71367-5_22.pdf`
- Observed relevance: Book/chapter material states that in binary compounds, the more electropositive component is named first and the more electronegative component receives the ending `-id`.
- Evaluation: Potentially stronger than a web article as textbook/book material, but not DIN, not official German IUPAC, and not a peer-reviewed journal source under the existing registry categories.
- Registry decision: Not added. Book/chapter or textbook source category is not currently governed.

### IUPAC Brief Guide to Nomenclature of Inorganic Chemistry

- Potential source ID: `SRC-IUPAC-BRIEF-GUIDE-INORGANIC-2005`
- URL: `https://iupac.qmul.ac.uk/BriefGuide/inorganic.html`
- Observed relevance: IUPAC English-language inorganic nomenclature context.
- Evaluation: Fits the general IUPAC/chemical nomenclature source family, but it is English-language context only and does not address German `-id` spelling authority. Sprint 4A already added `SRC-IUPAC-INORGANIC-NOMENCLATURE-1971` for cautious English inorganic nomenclature context.
- Registry decision: Not added. No distinct German suffix-rule use was identified, and adding another English IUPAC context source would not close the Sprint 4B gap.

## Source Categories Found

Existing governed source categories in `source_registry.json` are:

- `authoritative_dictionary`
- `chemical_nomenclature_standard`
- `government_scientific_database`
- `regulatory_body`
- `peer_reviewed_journal`
- `industry_publication`
- `market_report`

The evaluated FH Münster and Universität Rostock sources are academic/teaching references. The Springer/Jander source is book/chapter or textbook material. The current registry does not contain a governed source category for academic teaching PDFs, university lecture materials, textbook chapters, or book chapters unless they independently qualify as an existing category such as a formal chemical nomenclature standard or peer-reviewed journal.

No new source category was created.

## Sources Added

No sources were added in Sprint 4B.

The evaluated German sources may be useful future candidates if doctrine adds a governed category for academic teaching sources, textbooks, or book chapters. Under the current source registry categories, adding them would require inventing or stretching a category, so they were left out.

## Sources Not Added and Why

- `SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR`: not added because academic/teaching source category is not currently governed.
- `SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN`: not added because academic/teaching source category is not currently governed.
- `SRC-SPRINGER-JANDER-ANORGANISCHE-NOMENKLATUR-ID`: not added because book/chapter or textbook category is not currently governed.
- `SRC-IUPAC-BRIEF-GUIDE-INORGANIC-2005`: not added because it is English nomenclature context only and would not provide distinct German suffix-rule authority beyond the existing Sprint 4A IUPAC context source.

## Formal German Suffix Rule Source

No authoritative formal German suffix rule source was found in this sprint.

The evaluated German materials provide academic or teaching support for the `-id` ending in certain inorganic naming contexts, but they do not establish a formal DIN rule, official German IUPAC rule, GDCh rule, or equivalent recognized German nomenclature authority.

## Lexical, Academic, and Formal Authority Distinction

Lexical dictionary support:

- Duden sources for `Sulfid`, `Oxid`, and `Chlorid` support individual German lexical forms.
- They do not establish a formal chemical nomenclature rule.

Academic/teaching support:

- FH Münster, Universität Rostock, and Springer/Jander appear relevant to German inorganic nomenclature instruction.
- They may support source review of the `-id` pattern, but their source types are not currently governed in the registry.
- They must not be treated as DIN, official German IUPAC, GDCh, or formal standards authority.

Formal nomenclature authority:

- A formal source would need to be DIN, official German IUPAC, GDCh, or another recognized German chemistry nomenclature authority.
- No such source was identified and added in this sprint.

## Impact on `sulfid_vs_sulfide`

The `sulfid_vs_sulfide` draft remains non-public and still blocked for publication.

Sprint 4B improves the source-search record by identifying likely academic/teaching support and the current source-category gap, but it does not add formal source-locking or approve claims. The page still cannot state a formal universal German `-ide` to `-id` rule.

## Claims Added

No claims were added in Sprint 4B.

Because no new source entries were added, creating a new support claim would leave it without governed source IDs. A source-gap tracking claim was also not added; the gap is recorded in this report and the decision log instead.

## Claims Not Approved

No claims were approved.

Existing claims remain `pending_review`, and claim registries remain inactive. No content wording should be changed and no `[SOURCE REQUIRED]` marker should be removed based on this sprint.

## Remaining Source Gaps

- DIN or official German IUPAC source for the German `-id` naming rule.
- GDCh or equivalent recognized German chemistry authority.
- Governed source-category decision for academic teaching sources, textbooks, or book chapters if they are to be used later.
- Stronger Bisulfid/Bisulfide boundary source.

## Publication Readiness Conclusion

Not ready for publication.

Sprint 4B did not find or add an authoritative formal German suffix rule source. The `sulfid_vs_sulfide` draft remains non-public until formal source-locking, claim approval, and later content review are completed.
