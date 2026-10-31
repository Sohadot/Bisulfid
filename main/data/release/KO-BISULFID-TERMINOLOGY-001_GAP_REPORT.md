# KO-BISULFID-TERMINOLOGY-001 — evidence reuse and remaining gaps

Generated 2026-10-31 from the governed stores. One page; no new framework.

## 1. Reused as-is (valid, not repeated)

| Layer | Status | Record |
|---|---|---|
| Source identity (C1–C8) | 11/11 verified | `main/data/sources/source_registry.json` (Recovery-03) |
| Source-use qualification | 11/11 qualified (narrow) | `source_use_qualification_registry.json` |
| Evidence admission | 15/15 rendered records admitted by `admissible()` for their declared use; 2 boundary records | `main/data/evidence/EVD-TERM-*.json` |
| Verbatim capture (L2) | 43/43 passages, sha256 per artifact (2026-10-30) | `captures/R03_TERMINOLOGY_CAPTURES.json` |
| Claim-to-evidence matching | 11/11 claims matched (narrow approval in an inactive registry; preparer work, not independent review) | `main/data/claims/terminology_claims.json`, `release/claim_dossiers/` |
| Information Gain | structure of route realization verified; ratification pending | `route_realization.check_structure` |

## 2. Completed now (smallest missing technical step)

| Step | Result |
|---|---|
| L3 dated re-fetch (later date) | 2026-10-31: every quoted passage of all 11 sources reproduced verbatim (`captures/TERMINOLOGY_RECAPTURE_2026-10-31.json`). Byte hashes are identical for the DWDS, Spektrum, IUPAC, FH Münster and PubChem artifacts; Merriam-Webster and Duden pages differ in bytes (dynamic HTML) while the quoted passages are unchanged, so their pinned version is capture date + sha256 (L4). This is a technical recapture, not a scientific re-review. |

## 3. Source-lock checklist after reuse

| Source | L1 | L2 | L3 | L4 | L5 | L6 |
|---|---|---|---|---|---|---|
| SRC-DUDEN-SULFID | pass | pass | pass | pass | pass | pending |
| SRC-DWDS-BISULFID | pass | pass | pass | pass | pass | pending |
| SRC-DWDS-HYDROGENSULFID | pass | pass | pass | pass | pass | pending |
| SRC-DWDS-SULFID | pass | pass | pass | pass | pass | pending |
| SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR | pass | pass | pass | pass | pass | pending |
| SRC-IUPAC-RED-BOOK-2005 | pass | pass | pass | pass | pass | pending |
| SRC-MW-BISULFIDE | pass | pass | pass | pass | pass | pending |
| SRC-MW-BISULFITE | pass | pass | pass | pass | pass | pending |
| SRC-MW-DISULFIDE | pass | pass | pass | pass | pass | pending |
| SRC-MW-SULFIDE | pass | pass | pass | pass | pass | pending |
| SRC-SPEKTRUM-SCHWEFELWASSERSTOFF-DE | pass | pass | pass | pass | pass | pending |

## 4. Genuinely missing (not repeatable by the preparer)

| Gap | Who | Smallest action |
|---|---|---|
| Independent nomenclature/lexicography review | a named human reviewer, not the preparer | review `release/review_packets/KO-BISULFID-TERMINOLOGY-001.md` and record verdicts in `release/reviews/KO-BISULFID-TERMINOLOGY-001.json` |
| L6 source-lock signatures (11 sources) | source registry owner | sign L1–L6 per source in `sources/source_lock_records.json` (L1–L5 now pass for all 11) |
| Claim activation (11 claims) | owner | signed record in `release/owner_acts.json` |
| AMD-IG-R03-001 ratification | owner | ratify in `ig_governance_policy.json` |
| Release authorization | owner | signed record in `release/owner_acts.json` |

## 5. Human review found in the repository

None for this object: `release/reviews/KO-BISULFID-TERMINOLOGY-001.json` has no review, `sources/source_lock_records.json` has no record, and the only older human sign-off artifact touching these sources (`SPEKTRUM_BIBLIOGRAPHIC_HUMAN_SIGNOFF_CHECKLIST_WAVE_1.md`) is marked "not completed". Nothing was inferred or reused as a review.
