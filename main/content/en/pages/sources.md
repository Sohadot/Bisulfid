---
route_id: sources
language: en
status: draft
publication_status: non_public
source_status: pending_source_review
claim_status: no_claims_approved
indexable: false
in_sitemap: false
generated: false
---

# Sources

bisulfid.com operates under strict source discipline. No claim is published without a corresponding source entry in the registry.

---

## The Governing Principle

No source entry = no published claim.

Every factual claim that appears on a public-facing page of bisulfid.com must have a corresponding entry in `main/data/sources/source_registry.json`. If no source entry exists for a claim, that claim may not appear on a published page.

---

## Current Registry Status

The source registry is not populated yet.

`main/data/sources/source_registry.json` exists as a governed structure but contains no source entries. Draft content across the site contains `[SOURCE REQUIRED]` markers where claims await source-locking.

Draft content is not public evidence. The existence of a draft page does not mean the claims on that page are verified, approved, or ready for publication.

---

## Source Categories

The source registry will eventually include sources from the following categories:

- **Chemical nomenclature authorities** — IUPAC, DIN, and other recognised bodies that govern compound naming conventions.
- **Industrial reference databases** — verified industry data relevant to sulfur compounds.
- **Scientific literature** — peer-reviewed publications where relevant to terminology claims.
- **Regulatory bodies** — official sources where regulatory claims are made. Note: safety thresholds, handling instructions, and dosage or exposure data are outside the scope of this asset entirely.
- **Commercial and market data** — verified market data from credentialled sources. Note: unsourced market statistics are blocked.

---

## What Is Blocked

The following source types are permanently blocked under `doctrine/SOURCE_POLICY.md`:

- **Unsourced market statistics** — any numerical market claim that cannot be traced to a credentialled data provider.
- **Bisulfite data presented as bisulfide data** — the two compounds are distinct; conflating their data is a structural error.
- **Safety thresholds presented as advice** — this asset does not publish handling instructions, exposure limits, or safety guidance of any kind.
- **Medical or therapeutic claims** — no claim about health effects, therapeutic use, or medical application is permitted.
- **Handling instructions** — chemical handling guidance is outside the scope of this asset.
- **AI-generated summaries as sources** — AI outputs are not primary sources. No AI summary may be cited as evidence for a factual claim.

---

## Draft Content Is Not Public Evidence

Pages in `main/content/en/pages/` with `publication_status: non_public` are internal drafts. They are:

- Not indexed.
- Not linked from any published navigation.
- Not part of the sitemap.
- Not treated as evidence for any claim on any other page.

The existence of a draft page does not mean the asset has published the claims it contains.

---

## Planned Internal Links

- `what_is_bisulfid` — Bisulfid as the central term
- `glossary` — governed sulfur terminology glossary
- `home` — return to gateway

---

*This page is a draft. It is non-public. It may not be cited, linked, or treated as published content until its route passes the Quality Gate.*
