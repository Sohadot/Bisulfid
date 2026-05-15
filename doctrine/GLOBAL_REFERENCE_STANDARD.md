# GLOBAL REFERENCE STANDARD

This document governs global reference quality for bisulfid.com.

It is subordinate to `ASSET_THESIS.md` and `PROJECT_DOCTRINE.md`.

---

## What Global Reference Means

bisulfid.com is designed to become a global reference asset.

A global reference asset is:

- Authoritative on its subject matter.
- Verifiable by source.
- Consistent across languages.
- Trusted by industrial, scientific, and procurement readers.
- Designed for depth, not volume.

---

## Global Reference Rules

- No thin multilingual pages.
- No unsourced translated claims.
- No language version contradicts the source registry.
- No translated page publishes without hreflang governance.
- No language layer exists only for SEO volume.

Every language must increase at least one of:

- Public reference value
- Scientific clarity
- Industrial buyer logic
- Safety understanding
- Terminology authority
- Strategic acquisition value

---

## Content Standards

### Depth Over Volume

A single authoritative page is worth more than ten thin pages. Reference depth creates moats. Thin content creates risk.

### Source-Backed Claims

Every factual claim must trace to the source registry. No claim publishes without a verified source entry.

Full policy: `doctrine/SOURCE_POLICY.md`

### Safety Governance

Safety content is published as context, not prescription.

No handling instructions. No dosage advice. No prescriptive thresholds. No medical claims.

### Terminology Precision

Chemical terminology must use the governed ontology as the control system. No term is introduced outside the ontology without doctrine review.

Ontology: `main/data/ontology/sulfur_terms.json`

### Industrial Accuracy

Industrial content must reflect actual procurement language and buyer logic. It does not speculate. It does not use unverified market data.

---

## Prohibited Content

- Thin pages published to fill route coverage.
- Machine-translated pages published without human review.
- Claims without verified source entries.
- Safety thresholds as prescriptive advice.
- Medical or therapeutic claims.
- Competitor targeting.
- Unverified market statistics.
- Bisulfite data presented as bisulfide data.

---

## Reference Page Structure

Every reference page must:

1. Define the term or topic with precision.
2. Establish the source authority.
3. Connect to the terminology ontology.
4. Carry correct language and hreflang markup.
5. Link to related governed pages.
6. Pass all quality gate conditions before publication.

---

## Validation

Reference quality is validated by:

- `validate_content.py`
- `validate_sources.py`
- `validate_claims.py`
- `validate_hreflang.py`
- `validate_translations.py`

All validators must pass before deployment.
