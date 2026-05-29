# Source Registry Execution Readiness Matrix — Wave 1

**Sprint:** 5N-J  
**Scope:** `de_core_mos2` — four candidate/boundary sources  
**Date:** 2026-05-29

| candidate_target | related_route_id | candidate role | execution readiness classification | proposed registry status later | fields verified | fields unverified | execution allowed now | source approval allowed now | claim approval allowed now | publication-ready | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid | de_core_mos2 | Primary German specialist lexicon | execution_readiness_candidate; execution_blocked_pending_field_verification; execution_not_allowed_now; source_approval_not_allowed_now | `verified` (future, if execution clears) | `source_id` label; `category`; `language`; role fit; route relationship; claim boundary limits (governance) | `author_or_organization`; `publisher`; `publication_date`; `url`/`doi`; edition/page citation | no | no | no | no | Primary execution candidate; blocked until human bibliographic verification |
| PubChem — Molybdenum disulfide / CID 14823 | de_core_mos2 | Supporting database | supporting_boundary_retained; not_primary_registry_source_now; not_claim_approval_source_now; not_publication_ready_source_now | optional supporting row (future) | candidate identity; CID reference label; supporting role boundary | full registry bibliographic fields if row added later | no | no | no | no | Database identity support only; not DE lexical primary |
| NIST Chemistry WebBook — molybdenum disulphide | de_core_mos2 | Supporting technical data | supporting_boundary_retained; not_primary_registry_source_now; not_claim_approval_source_now; not_publication_ready_source_now | optional supporting row (future) | candidate identity; technical role boundary | full registry bibliographic fields if row added later | no | no | no | no | Technical data support only |
| Chemie.de Lexikon — Molybdän(IV)-sulfid | de_core_mos2 | Secondary German support | supporting_boundary_retained; not_primary_registry_source_now; not_claim_approval_source_now; not_publication_ready_source_now | optional secondary row (future) | candidate identity; secondary role boundary | full registry bibliographic fields if row added later | no | no | no | no | Secondary cross-check only; not primary |

*Rows: 4*

**Parallel blocked track:** `sulfur_element_term_record` — not in matrix; separate database-candidate track; not advanced.

**Matrix notes:**

- **fields verified** = governance-verified only unless human confirmed bibliographic value in repository artifacts (none for Spektrum bibliographic lines).
- **execution allowed now: no** for all rows.
- Spektrum may reach **`execution_ready_after_field_verification`** after human bibliographic verification sprint — not in 5N-J.
