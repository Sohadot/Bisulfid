# BISULFID Reference Exchange v1 — portable knowledge, not a content farm

**Publisher:** Sohadot (sohadot.com)  
**State:** internal governed pilot; no public URL, API or dataset license conferred.  
**Initial object:** `KO-BISULFID-TERMINOLOGY-001` (English/German terminology).

## Why this exists

BISULFID's long-term value must survive changes in search engines, AI models and interface technologies. The durable asset is a source-bounded relationship between **claims, admitted evidence, source identifiers, qualified uses and scientific uncertainty**. HTML is one presentation, this exchange JSON is another; neither substitutes for the underlying provenance.

The executable pilot exports **11 approved but owner-inactive terminology claims**, with **13 bound evidence uses from 11 sources**, from the *existing* governed stores. Its evidence links retain the third-party sources' published URLs, source IDs, retrieval dates and use-qualification IDs. The bundle deliberately omits raw captures and verbatim source excerpts. A `documentary_verified` label means D1–D7 passed under the adopted internal policy, **not** that independent human peer review occurred.

## Contract

- File: `bisulfid_terminology.v1.json`; schema version `1.0.0`.
- Core fields: `publisher`, `reference`, `publication`, `verification`, `rights`, `exclusions`, `provenance`, `claims[]`.
- Each claim contains a stable ID, an authored statement and evidence edges with identifiers and retrievable source URLs. **Database synonym, dictionary sense and IUPAC recommendation are not interchangeable.**
- The pilot is **not an open publication** of the research object. Its intended canonical URL may already resolve as a legacy page; that is not publication of this drafted version.
- The `rights` field conveys **no new license** to reuse third-party texts, source captures, trademarks or proprietary material. Any future licensing decision must distinguish BISULFID-owned transformations from third-party rights, existing repository license terms, and per-source restrictions.
- No API hosting, paid AI inference or external service is necessary. Plain versioned JSON remains parseable by ordinary applications and AI agents without a particular vendor.

## Reproduce and test

```bash
python scripts/interoperability/export_reference_v1.py --check
python scripts/interoperability/test_export_reference_v1.py
# Explicit regeneration after editing the authoritative evidence/claim records:
python scripts/interoperability/export_reference_v1.py --write
```

The exporter **fails closed** if D1–D7 cease to pass, claim text/bindings drift, a source URL is unqualified, evidence becomes unrendered, or owner acts change. It does not promote MoS₂ or other unapproved objects merely because files exist.

## Reference Explorer — offline pilot

The reference exchange now has a usable local query interface, requiring only Python's standard library. It does not call an AI provider or any external network service.

```bash
python scripts/interoperability/reference_explorer_v1.py --summary --format text
python scripts/interoperability/reference_explorer_v1.py --term bisulfide --format text
python scripts/interoperability/reference_explorer_v1.py --claim-id CLM-TERM-BISULFIDE-EN-SENSE-001
python scripts/interoperability/reference_explorer_v1.py --source-id SRC-MW-BISULFIDE
python scripts/interoperability/reference_explorer_v1.py --evidence-id EVD-TERM-MW-BISULFIDE
python scripts/interoperability/reference_explorer_v1.py --sources --format text
python scripts/interoperability/test_reference_explorer_v1.py
```

It returns the claim, source identity, retrieval date, and evidence qualification. Whole-term Unicode matching avoids treating similar chemical words as interchangeable. Every JSON result discloses the staged-only state, verification limits and ungranted licensing rights. Malformed inputs or changed rights and authorization status are rejected.

These commands demonstrate search and reverse provenance tracing internally; they do not establish customer demand, market adoption or revenue. No public API, deployment, scientific sign-off or dataset license is implied.

## What would justify the next investment?

Demonstrable use: a researcher can trace a claim to a source; a multilingual specialist can distinguish ambiguous terms; a legitimate integrator can consume consistent IDs and revisions. Validate these use cases before building an API, subscriptions or a database server. A future public export would require its **own** rights review, explicit publisher authorization, route/indexation decision and CI validation. Do not expose this pilot under `site/public` or advertise it as a public API now.

**Search strategy:** continue human-first SEO for genuinely useful pages, but measure branded/direct use, provenance reuse and qualified institutional interest separately from organic clicks. AI interoperability is an additional channel, not an excuse for thin pages or invented machine-readable claims.
