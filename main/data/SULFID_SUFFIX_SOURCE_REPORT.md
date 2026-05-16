# Sulfid Suffix Source Report

## Why This Sprint Exists

Sprint 3C identified `sulfid_vs_sulfide` as the most blocked English draft page because it referenced German-English spelling examples that were not yet supported by registered source entries or scoped claims.

The missing support centered on:

- Oxide/Oxid lexical comparison.
- Chloride/Chlorid lexical comparison.
- A possible IUPAC/DIN suffix standard for the German `-id` pattern.

Sprint 4A adds candidate source support for the German lexical examples used by the draft while avoiding any claim that a formal universal German `-ide` to `-id` rule has been source-locked.

## Sources Evaluated

- `SRC-DUDEN-SULFID` — existing Duden lexical source for `Sulfid`.
- `SRC-DUDEN-OXID` — Duden lexical source candidate for `Oxid`.
- `SRC-DUDEN-CHLORID` — Duden lexical source candidate for `Chlorid`.
- `SRC-IUPAC-INORGANIC-NOMENCLATURE-1971` — IUPAC / Pure and Applied Chemistry nomenclature material for English inorganic nomenclature context only.

No Wikipedia source, AI summary, market source, safety source, or industrial procurement source was used.

## Sources Added

- `SRC-DUDEN-OXID`
  - Category: `authoritative_dictionary`
  - Status: `seeded`
  - Source lock status: `candidate`
  - Use: German lexical support for `Oxid` as a cautious spelling-comparison example.

- `SRC-DUDEN-CHLORID`
  - Category: `authoritative_dictionary`
  - Status: `seeded`
  - Source lock status: `candidate`
  - Use: German lexical support for `Chlorid` as a cautious spelling-comparison example.

- `SRC-IUPAC-INORGANIC-NOMENCLATURE-1971`
  - Category: `chemical_nomenclature_standard`
  - Status: `seeded`
  - Source lock status: `candidate`
  - Use: English inorganic nomenclature context only where directly supported.

All new source entries include `use_for`, `do_not_use_for`, and `risk_notes` arrays. No source was marked final, locked, approved, or public-ready.

## Formal German Suffix Rule Source

No formal German suffix rule source was found in this sprint.

The Duden entries support individual German lexical forms (`Sulfid`, `Oxid`, `Chlorid`). They do not, by themselves, establish a formal German chemical nomenclature rule or a universal suffix transformation rule.

The IUPAC 1971 source was added only as English nomenclature context. It must not be used as German spelling authority or as proof of German suffix compression.

## Lexical Support vs Nomenclature Authority

The Duden sources can support cautious wording that presents `Sulfid`, `Oxid`, and `Chlorid` as documented German lexical forms.

They cannot support public wording that says German chemical nomenclature universally converts English `-ide` forms to German `-id` forms.

A formal nomenclature authority would require a stronger German-language source, such as a DIN standard, a German-language IUPAC nomenclature source, or another authoritative educational or standards source that directly states the rule.

## Claims Added

- `CLM-TERM-OXID-001` — pending_review lexical claim for `Oxid`.
- `CLM-TERM-CHLORID-001` — pending_review lexical claim for `Chlorid`.
- `CLM-TERM-GERMAN-ID-PATTERN-001` — pending_review cautious lexical comparison-set claim for `Sulfid`, `Oxid`, and `Chlorid`.
- `CLM-TERM-ENGLISH-IDE-CONTEXT-001` — pending_review English `-ide` nomenclature context claim.

No claim was approved.

## Why No Claims Were Approved

All new claims remain `pending_review` because Sprint 4A only adds candidate source support.

The German lexical examples are supported as dictionary entries, not as a formal nomenclature standard. The broader suffix-pattern claim remains medium risk until a stronger German nomenclature source is identified and reviewed.

The English IUPAC context source does not close the German suffix-rule gap.

## Why No Content Pages Were Modified

Content pages were intentionally left unchanged because this sprint only registers candidate source and claim support.

No `[SOURCE REQUIRED]` markers were removed. No draft wording was changed. No route was published, indexed, added to the sitemap, or generated as public HTML.

## Remaining Gaps

- Formal German nomenclature source.
- DIN or German-language IUPAC suffix rule, if available.
- Stronger source for the Bisulfid/Bisulfide boundary.
- Claim approval review after stronger source-locking is completed.

## Publication Readiness Conclusion

Not ready for publication.

The `sulfid_vs_sulfide` draft now has better candidate support for the Oxide/Oxid and Chloride/Chlorid examples, but it still lacks a formal German suffix-rule source. The page remains blocked for public release until stronger nomenclature source-locking is completed and claims are reviewed under the source policy.
