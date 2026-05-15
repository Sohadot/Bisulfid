# SOURCE POLICY

This document governs claims and sources for bisulfid.com.

It is subordinate to `ASSET_THESIS.md` and `PROJECT_DOCTRINE.md`. It takes precedence over all content, SEO, and language policies where claims intersect.

---

## Core Rule

> No source entry = no published claim.

Every factual claim requires a verified entry in:

`main/data/sources/source_registry.json`

---

## Approved Source Categories

- Authoritative dictionaries and encyclopedias.
- IUPAC and chemical nomenclature standards.
- Government scientific databases.
- Regulatory bodies (national and international).
- Peer-reviewed journals.
- Industry publications with named publisher and date.
- Market reports with verified publisher, date, and methodology.

---

## Source Registry Format

Each source entry must include:

- `source_id` — unique identifier
- `title`
- `author_or_organization`
- `publisher`
- `publication_date` (or access date for databases)
- `url` or `doi` (where applicable)
- `category` (from approved categories above)
- `linked_claims` — array of claim IDs sourced to this entry

---

## Claim Registry

All published claims are registered in:

`main/data/claims/claim_registry.json`

Each claim entry links to its source entry. A claim without a source entry may not be registered. A registered claim that loses its source must be removed from publication until an alternative source is verified.

---

## Permanently Blocked Content

The following may never be published regardless of source:

- Market statistics without a verified source with publisher, date, and methodology.
- Bisulfite data used as bisulfide data.
- Safety thresholds as prescriptive advice.
- Medical or therapeutic claims.
- Chemical handling instructions.
- Dosage advice.
- Competitor targeting language.
- Company names as acquisition targets in public pages.

---

## AI and Tool Use

- AI tools may assist in source identification and content drafting.
- AI-generated text is not a source.
- AI-generated summaries of sources are not sources.
- All claims must trace to the original source, not to an AI summary of it.

---

## Review and Dispute

If a source is later found to be unreliable, all claims linked to that source are removed from publication until alternative sources are verified.

No source dispute is resolved by removing the requirement for sourcing.

---

## Validation

Source coverage is validated by:

- `validate_sources.py`
- `validate_claims.py`

Gate 04 of the Quality Gate requires zero unsourced published claims.
