---
route_id: what_is_bisulfid
language: en
status: draft
publication_status: non_public
source_status: pending_source_review
claim_status: no_claims_approved
indexable: false
in_sitemap: false
generated: false
---

# What Is Bisulfid?

Bisulfid is the central term of this asset. It is not simply a chemical name — it is an architectural decision, a nomenclature boundary, and the governing identifier of bisulfid.com.

---

## Domain Thesis vs Chemical Definition

This asset uses the term Bisulfid in two related but distinct senses:

1. **As a chemical term** — Bisulfid is the German-form spelling of the compound more commonly written as bisulfide in English. The two spellings refer to the same underlying chemical entity. The German form drops the final E in accordance with German chemical nomenclature conventions. [SOURCE REQUIRED] for formal nomenclature authority citations.

2. **As an asset identifier** — Within bisulfid.com, Bisulfid is the name of the asset itself: the domain, the reference framework, and the governed terminology system built around this compound and its spelling boundary.

A domain thesis is not the same as a chemical definition. The asset makes no claim to be an authoritative chemistry reference. It makes a claim to be a governed reference asset built around a precisely chosen term.

---

## The Center Node

Within the terminology ontology (`main/data/ontology/sulfur_terms.json`), bisulfid is the center node. All other terms — bisulfide, bisulfite, sulfid, sulfide, and related compounds — are positioned relative to it.

This is an architectural choice, not a chemical hierarchy. The center-node position reflects the domain thesis, not any claim of chemical primacy.

---

## Disambiguation: Bisulfid vs Bisulfite

**Bisulfid** (or bisulfide) and **bisulfite** are distinct chemical compounds. They are not interchangeable.

- Bisulfide relates to the HS⁻ ion (hydrogen sulfide anion) or sulfide-based compounds. [SOURCE REQUIRED]
- Bisulfite relates to the HSO₃⁻ ion (hydrogen sulfite anion). [SOURCE REQUIRED]

Confusion between these two is a documented pattern in informal usage. This asset does not conflate them. Any claim that treats bisulfide data as applicable to bisulfite, or vice versa, is blocked under `doctrine/SOURCE_POLICY.md`.

---

## German-Form Spelling Boundary

The spelling Bisulfid — without the final E — marks the boundary between the English and German chemical naming conventions for this compound family. This boundary is explained in detail in the planned page `bisulfid_vs_bisulfide`.

---

## Source Validation Requirement

This page contains claims about chemical nomenclature and compound identity that require source validation before public publication.

Specifically:

- The characterisation of German vs English nomenclature conventions [SOURCE REQUIRED]
- The ion assignments for bisulfide and bisulfite [SOURCE REQUIRED]
- Any further chemical detail added in future drafts [SOURCE REQUIRED]

No claim on this page is approved for publication until corresponding entries exist in `main/data/sources/source_registry.json` and the relevant claim registry.

---

## Planned Internal Links

- `bisulfid_vs_bisulfide` — The Missing Letter explained
- `sulfid_vs_sulfide` — broader spelling pattern
- `bisulfide_hydrosulfide_sulfide` — bisulfide, hydrosulfide, and sulfide disambiguation
- `german_english_chemical_terms` — German-English chemical nomenclature context
- `glossary` — full term glossary
- `sources` — source discipline

---

*This page is a draft. It is non-public. It may not be cited, linked, or treated as published content until its route passes the Quality Gate.*
