# Sovereign Reference Corpus Architecture

## Why this sprint exists

Sprint **5A** records Bisulfid.com’s strategic correction: the product is **not** “ship ~300 pages and stop.” The asset is a **large, trusted, academically disciplined, source-governed, multilingual chemical-language reference corpus** aligned to sovereign-grade doctrine. This sprint is **architecture and corpus doctrine only**: it produces planning documents and updates the decision log. **No** corpus pages are drafted here. **No** routes publish. **No** registries change.

## Why weak visibility and placeholder launches are rejected

The owner rejects:

- weak visibility plays,
- placeholder public pages,
- a small “minimum viable” public gate that misrepresents authority,
- undifferentiated generic chemistry sites.

Those patterns destroy **trust** with chemists, translators, editors, compliance users, and analysts—the core audiences who require **reference integrity** over traffic gimmicks.

## 300 pages: minimum launch cohort, not final goal

Three distinct concepts must not be conflated:

| Concept | Definition |
| --- | --- |
| **Minimum public launch cohort** | The **first** public surface Bisulfid.com may show once **≥ 300** pages each meet full launch thresholds (`CORPUS_LAUNCH_THRESHOLD.md`). This is a **floor**, not a destination. |
| **Long-term reference corpus** | The **expandable** body of governed pages intended to grow to **500**, **1,000**, and **3,000+** pages across languages while **strict quality gates** remain in force (`CORPUS_EXPANSION_MODEL.md`). |
| **Full authority system** | The **complete** interplay of `routes`, `sources`, **claims**, **ontology**, **multilingual** alignment, **internal links**, and **Quality Gate**—such that public copy is always traceable to registered authority and corpus roles. |

**Explicit statement:** **300 governed pages is the minimum first-launch threshold. The long-term corpus must be designed to scale far beyond 300 pages while preserving sovereign-grade quality.**

## Strategic corpus thesis

Bisulfid.com becomes a **trusted chemical-language reference system** for:

- chemists,
- chemical terminology editors,
- technical translators,
- chemical industry professionals,
- compliance and documentation teams,
- economic and industrial analysts (for **language, classification, and documentary interpretation**—not fake “market report” copy),
- multilingual scientific reference users.

The corpus is **large, trusted, academically disciplined, source-governed, claim-governed, multilingual, internally linked, expandable, non-generic, non-thin, and sovereign-grade.**

## Long-term authority vision

Over years—not weeks—the system should support:

1. A **dense English spine** (terminology, disambiguation, methodology).
2. A **German identity and nomenclature-origin layer** (not “translations” of English; **Deutsche Lexik** as primary for its domain).
3. **Arabic**, **Chinese**, and **Japanese** **technical reference layers** for industrial and scientific readability in those language communities.
4. **Governance pages** that make sourcing and claim discipline **legible** to external professionals.
5. **Index and map pages** that organize navigation without becoming thin link farms.

## Audience map

| Audience | Primary need from Bisulfid | What we must never become for them |
| --- | --- | --- |
| Chemists | Precise terms, boundaries, nomenclature context | Pop-science blog, unreferenced assertions |
| Terminology editors | Stable records, citations, DE/EN controls | Crowd-sourced ambiguity |
| Technical translators | Language-pair discipline, disambiguation | Untranslated English posing as “localized” |
| Industry professionals | Document language, classification clarity | Procurement playbooks, vendor hype |
| Compliance / documentation | SDS-style **term** context, regulatory **language** framing—not operational safety manuals | Handling instructions, medical advice |
| Industrial / economic analysts | **Lexical** and **sector classification** interpretation | CAGR, market share, acquisition targets without governed methodology |

## Strategic corpus layers (required)

The sovereign corpus includes at least:

1. **Core terminology records** — canonical term pages with boundaries and ontology alignment.
2. **German–English chemical language layer** — explicit cross-language authority framing.
3. **Arabic technical reference layer** — industrial-region accessibility; terminology-first.
4. **Chinese technical reference layer** — scale-aware technical vocabulary records.
5. **Japanese advanced technical reference layer** — precision chemistry language.
6. **Disambiguation authority pages** — triads and near-miss labels (e.g., bisulfide / hydrosulfide / sulfide; bisulfite wall).
7. **Industrial/economic interpretation pages** — clarify *how language is used* in sectors and documents, **without** thin market data.
8. **Source and nomenclature governance pages** — how bisulfid cites and constrains claims.
9. **Methodology / reference system pages** — internal standards for editors and reviewers (may tier non-public).
10. **Index / map pages** — structured entry points; anti-thin rules apply.

## Corpus category architecture — page categories

Each category below specifies purpose, audience, claims, sources, prohibitions, linking role, publication criteria, and launch eligibility. **“Public at launch”** still requires passing **all** thresholds in `CORPUS_LAUNCH_THRESHOLD.md`; many categories default to **non-public until source-locked**.

| Category | Purpose | Expected audience | Acceptable claim types | Source requirements | Prohibited content | Internal linking role | Publication criteria | Launch: public allowed when |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Core terminology record** | Canonical controlled term | Editors, translators, chemists | Terminology + cautious science identity | Dictionary, IUPAC, gov DBs per SOURCE_POLICY | Generic defs; invented suffix rules | Terminology hub spokes | All markers resolved; claims approved | Source-locked + low/medium risk |
| **DE–EN chemical language** | Cross-language boundary truth | Translators, bilingual editors | Terminology, comparative orthography | Duden-class + IUPAC-context appropriately | Teaching PDF as sole formal authority | Bridge between EN spine and DE layer | DE+EN sources registered | Each language claim locked |
| **Arabic technical layer** | AR terminology authority | AR-region technical readers | Terminology; cautious substance labels | AR technical standards, peer refs where applicable | Machine-translation spam | AR cluster hub | AR source posture defined | Source-locked AR |
| **Chinese technical layer** | ZH terminology authority | CN industrial readers | Terminology; cautious labels | CN standard works, governed refs | Bulk EN→ZH without review | ZH cluster hub | ZH source posture defined | Source-locked ZH |
| **Japanese technical layer** | JP precision chemistry language | JP lab/industry readers | Terminology; IUPAC-JP alignment where used | JP standard refs | Tutorial blog voice | JP cluster hub | JP source posture defined | Source-locked JP |
| **Disambiguation authority** | Resolve near-miss terms | All professional audiences | Terminology + scope delimiters | Strong nomenclature + glossary discipline | Collapsing bisulfite into bisulfide | Central triangulation node | Linked from all confused terms | High scrutiny; medium risk ok if bounded |
| **Industrial/economic interpretation** | Document & sector **language** | Analysts, compliance, PMs | **Narrow** industry_claims if any | Industry pubs with methodology | CAGR, market share, acquisition targets | Connects terminology to sector vocabulary | Claims approved; no thin lists | Often **non-public until** industry claims mature |
| **Safety context (non-manual)** | Awareness & vocabulary | Professionals needing framing | safety_claims only, non-prescriptive | Regulatory + verified refs | Handling steps; dosage; emergency procedures | Links **out** to specialist safety systems | Explicitly non-manual review | Usually **non-public until** safety review program |
| **Governance / sources** | Transparency of evidence | Editors, auditors, scientists | Meta claims about policy | N/A for facts; cites doctrine | Raw URL dumps outside policy | Nexus for “why we cite” | Doctrine-aligned | Public when registry has verified entries |
| **Methodology / system** | How corpus is built | Internal editors | Non-factual process statements | Doctrine | Assertions about chemicals without sources | Support node for reviewer training | Often **non-public** early | Owner discretion |
| **Index / map** | Navigation scaffolding | All | None or definitional only | N/A | Thin auto-generated grids | Receives links; bounded outbound | Structured sections required | Public only if non-thin |

## Multilingual architecture

**Languages in scope:** English (global base), German (identity and terminology-origin), Arabic (strategic accessibility / industrial-region reference), Chinese (industrial scale), Japanese (advanced technical chemistry language).

**Why multilingual pages are strategic**

- Chemical commerce and regulation are **multilingual**; searchers arrive in **wrong-language** orthographies (e.g., Bisulfid vs bisulfide class).
- Technical translators need **paired records**, not paragraph substitutes.

**Why multilingual pages must not be simple translations**

- Authorities and acceptable term forms **differ by language community**.
- German **-id** orthography, Arabic script chemical naming conventions, Chinese standard names, and Japanese katakana/IUPAC interplay each require **local discipline**.

**Controlled terminology records**

- Each language page states: scope, boundaries, **what it does not claim**, markers until locked, and links to **hreflang siblings** as future routes permit.

**Connection to source governance**

- Each language layer uses SOURCE_POLICY categories valid for that page’s claims; **no language skips** the registry.

**Scaling beyond 300 without translation spam**

- Hub-and-spoke cluster limits,
- Batch caps and audits (`CORPUS_EXPANSION_MODEL.md`),
- Pruning weak concepts,
- Disallowing MT-only pages for public tiers.

## Academic and reference authority standard

Bisulfid.com must remain **usable as serious reference infrastructure** by:

- chemists,
- chemical industry professionals,
- technical translators,
- terminology editors,
- compliance and documentation teams,
- economists and industrial analysts (for **language, classification, and documentary framing**—not counterfeit “market intelligence”).

**Out of scope by design — the corpus must not become:**

- a safety manual or emergency playbook,
- a medical or therapeutic resource,
- a procurement guide or vendor directory,
- a market report (CAGR, share, price forecasts) without governed methodology,
- a casual education blog,
- a low-quality AI-generated glossary,
- a mass page generator that prizes count over source-backed claims.

Reference discipline is enforced through **SOURCE_POLICY**, **claim registries**, **ontology alignment**, and **Quality Gate** publication—never through volume alone.

## Academic and reference authority standard

Bisulfid.com must remain **usable as serious reference infrastructure** by:

- chemists,
- chemical industry professionals,
- technical translators,
- terminology editors,
- compliance and documentation teams,
- economists and industrial analysts (for **language, classification, and documentary framing**—not counterfeit “market intelligence”).

**Out of scope by design — the corpus must not become:**

- a safety manual or emergency playbook,
- a medical or therapeutic resource,
- a procurement guide or vendor directory,
- a market report (CAGR, share, price forecasts) without governed methodology,
- a casual education blog,
- a low-quality AI-generated glossary,
- a mass page generator that prizes count over source-backed claims.

Reference discipline is enforced through **SOURCE_POLICY**, **claim registries**, **ontology alignment**, and **Quality Gate** publication—never through volume alone.

## Source and claim governance model (summary)

- **Sources:** `main/data/sources/source_registry.json` is the gate for factual public copy (`doctrine/SOURCE_POLICY.md`).
- **Claims:** Claim registries remain **inactive** until deliberately activated; no publication while required claims are pending or unapproved.
- **Ontology:** Terms move to verified public use only with coordinated registry + content alignment.

## Internal linking model

- **Clusters** (see blueprint): `terminology_spine`, `gateway`, `multilingual_de`, `multilingual_ar`, `multilingual_zh`, `multilingual_ja`, `disambiguation`, `governance`, `industrial_interpretation`, `safety_context`, `index_map`.
- **Density rules:** Hubs accept bounded inbound edges; disambiguation pages must link to all canonical records they separate.
- **No broken public graph** at launch.

## Publication readiness model

Stages:

1. **Blueprint** (Sprint 5A) — concepts only.
2. **Route registration** — future sprint; align `routes.json`.
3. **Draft** — non-public, markers on.
4. **Source-lock** — registry verification.
5. **Claim approval** — governed activation.
6. **Quality Gate** — publication + indexation **only** if all thresholds pass.

## Batch creation strategy

- Work in **vertical slices** (e.g., DE terminology batch, AR hub batch), not horizontal “300 thin stubs.”
- Each batch ends with **sampled audit** and **link-graph check**.
- High-risk routes batched separately with specialist review.

## Quality scaling strategy

- Gates tighten proportionally to **claim risk** and **language complexity**.
- **Anti-thin** and **anti-generic** rules are enforced at batch boundaries, not “fixed later.”

## Validation strategy

- Validator suite + human editor review for:
  - markers,
  - link targets,
  - claim/registry alignment,
  - multilingual drift.

## Launch strategy

- **No public launch** until `CORPUS_LAUNCH_THRESHOLD.md` is satisfied at **≥ 300** pages.
- Launch is **authority-first**; SEO tactics subordinate to doctrine.

## Risks

| Risk | Mitigation |
| --- | --- |
| Launching early | Reputational collapse with professional users; maintain hard no-go conditions. |
| 300 weak pages | Same as failure; enforce anti-thin + marker + claim gates. |
| Scaling past 300 without governance | Translation spam, registry drift; use expansion caps, pruning, audits. |
| Safety drift | Keep safety pages non-manual; repeated compliance review. |

## Why no routes were published (Sprint 5A)

Sprint 5A is **doctrine and architecture only** per charter. **No** `routes.json` edits. **No** `status: published`. **No** indexation flags toggled.

## Why no content pages were created (Sprint 5A)

Corpus drafting is intentionally deferred. This sprint establishes **what** must exist before drafting at scale.

## Artifacts produced (Sprint 5A)

- `SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md` (this file)
- `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` — **≥ 300** proposed page concepts (**blueprint only**)
- `CORPUS_EXPANSION_MODEL.md`
- `CORPUS_LAUNCH_THRESHOLD.md`
- `DECISION_LOG.md` — sprint record appended

## Recommended next sprint

1. **Routing cohort sprint:** Register a **first multilingual route slice** (e.g., German terminology mirror routes + Arabic hub shell) strictly aligned to this blueprint—**without** publishing.
2. **OR** focused **English** draft completion sprint for highest hub-demand routes still missing bodies—under non-public constraints.
3. **Parallel:** Claim-registry activation planning sprint (if owner approves)—still **no** publication until thresholds met.

---

*Sprint 5A — architecture only. No registries modified. No public HTML generated.*
