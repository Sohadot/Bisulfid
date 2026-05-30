# Spektrum Source Registry Field Mapping — Wave 1

**Sprint:** 5N-O  
**Scope:** Human-reviewed receipt → `SRC-SPEKTRUM-MOS2-DE` registry row  
**Date:** 2026-05-30

| receipt / governance field | registry field | value inserted | omitted / blank |
| --- | --- | --- | --- |
| proposed_source_id | `source_id` | `SRC-SPEKTRUM-MOS2-DE` | — |
| source_title | `title` | Molybdän(IV)-sulfid - Lexikon der Chemie | — |
| author_or_organization | `author_or_organization` | Lexikon der Chemie editorial and authorial team; Fachkoordination: Hans-Dieter Jakubke and Ruth Karcher; Redaktion: Sabine Bartels, Ruth Karcher, Sonja Nagel | — |
| publisher | `publisher` | Spektrum Akademischer Verlag, Heidelberg | — |
| publication_date | `publication_date` | — | **Omitted** — not visible; copyright 1998 not used |
| copyright_year | `risk_notes` | Rights evidence only (1998) | Not `publication_date` |
| url_or_doi | `url` | https://www.spektrum.de/lexikon/chemie/molybdaen-iv-sulfid/5985 | — |
| edition_or_version | — | — | **Omitted** — not visible |
| page_or_entry_citation | `notes` | entry: Molybdän(IV)-sulfid, in Lexikon der Chemie | — |
| access_date | `notes` | Access date 2026-05-30 | — |
| authority_class | `category` | `authoritative_dictionary` | — |
| language | `language` | `de` | — |
| route_relationship | `notes` / `use_for` | Route scope: de_core_mos2; use_for lists MoS2 DE lexicon scope | — |
| claim_boundary_scope | `use_for` / `do_not_use_for` | Scoped terminology; forbidden uses listed | — |
| rights_or_license_posture | `risk_notes` / `notes` | Bibliographic reference only; no full text copied | — |
| verification_note | `last_reviewed` / `notes` | 2026-05-30; Sprint 5N-N human review basis | — |
| execution posture | `status` | `seeded` | Not `verified` |
| source-lock posture | `source_lock_status` | `candidate` | Not `locked` |

**Registry file-level:** `status` remains **`inactive`**.

**No other registry rows modified.**
