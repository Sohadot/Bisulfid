# main/content/en/

English is the source layer for bisulfid.com.

All files in this directory are drafts. File presence does not equal publication.

## Publication Governance

Publication is governed by `main/data/routes.json`. A page may not be considered public
until its corresponding route has `status: published` in routes.json AND all 11 Quality
Gate conditions defined in `doctrine/QUALITY_GATE.md` have passed.

## Source and Claim Governance

Factual claims in these drafts are governed by:

- `main/data/sources/source_registry.json` — no source entry = no approved claim.
- `main/data/claims/` — claim registries remain inactive and empty.

Draft pages may contain `[SOURCE REQUIRED]` markers where future verification is needed.
These markers indicate that a claim has not yet been source-locked and must not be
treated as verified.

## Draft Status

- All pages in this directory carry `status: draft` and `publication_status: non_public`.
- No draft may be indexed, linked, or presented as public content until Quality Gate passes.
- `indexable: false` and `in_sitemap: false` are required on all drafts.

## Language Role

English is the source layer. It defines the canonical term meanings and content structure
that other language layers (DE, AR, ZH, JA, FR, ES) will reference and translate from.
The German identity layer (DE) and Arabic market-chain layer (AR) carry distinct strategic
roles defined in `doctrine/MULTILINGUAL_POLICY.md`.
