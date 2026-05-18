# Batch 1A Source and Claim Boundary Review (Sprint 5F)

## Why this sprint exists

Sprint **5E** produced **non-public** Markdown bodies for the five Batch **1A** methodology routes. Those drafts are intentional **governance and editorial inventory**: they explain corpus posture, linking discipline, Quality Gate expectations, and German methodology boundaries without publishing routes, wiring `internal_links.json`, approving claims, or completing source-locking.

Sprint **5F** is a **report-only** governance review. It maps **source requirement level**, **claim boundaries**, **German authority boundaries**, **internal-link readiness**, and **publication blockers** so later sprints can execute source mapping, claim work, and linking batches with explicit scope—**without** treating these drafts as publication-ready today.

**Sprint 5F did not modify** content pages, `routes.json`, `internal_links.json`, claim or source registries, or any other forbidden surface.

---

## Files reviewed (read-only)

| Path | Role in review |
| --- | --- |
| `main/data/routes.json` | Route metadata, `content_file`, `status`, `risk_level`, `required_claim_groups` |
| `main/data/ROUTE_PLANNING_BATCH_1A_REPORT.md` | Batch 1A planning context |
| `main/data/BATCH_1A_NON_PUBLIC_DRAFT_CREATION_REPORT.md` | Sprint 5E scope and preflight |
| `main/content/en/pages/corpus-methodology.md` | `corpus_methodology_overview` draft |
| `main/content/en/pages/internal-linking-discipline.md` | `internal_linking_discipline` draft |
| `main/content/en/pages/quality-gate.md` | `quality_gate_public_explainer` draft |
| `main/content/de/pages/corpus-map.md` | `de_method_corpus_map` draft |
| `main/content/de/pages/translator-playbook.md` | `de_method_translator_playbook` draft |
| `doctrine/SOURCE_POLICY.md` | Approved source categories, academic-teaching constraints, blocked patterns |
| `main/data/sources/source_registry.json` | Baseline: no new sources required for this sprint |
| `main/data/claims/terminology_claims.json` | Baseline: registry inactive; illustrative future claim surface |
| `DECISION_LOG.md` | Prior sprint decisions (5D, 5E) |

---

## Five-draft summary table

| route_id | content_file | lang | Route status (registry) | Draft status (frontmatter) | Primary corpus role | Source requirement level | Claim risk level (assessment) | Source-locking needs | Claim-boundary needs | Internal-link readiness | Publication blockers (summary) | Relative publication proximity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `corpus_methodology_overview` | `main/content/en/pages/corpus-methodology.md` | en | `planned` | `draft` / `non_public` | Methodology / operating model for the sovereign corpus | **Medium–high** | **Low–medium** | Lock **300-page** / gate language to doctrine or sources; clear **2×** `[SOURCE REQUIRED]` | Keep meta-only; no implied approved corpus facts | **Low** (lists targets; no graph edges) | Markers; planned route; no link graph | **Mid** after markers cleared and doctrine cites added |
| `internal_linking_discipline` | `main/content/en/pages/internal-linking-discipline.md` | en | `planned` | `draft` / `non_public` | Editorial rules for route_id-centric linking | **Medium** | **Low** | Cite link-density rules from doctrine | Process-only; avoid metric claims without doctrine | **Low** (no `internal_links.json` yet) | Marker; planned route | **Closest** for *process-only* readiness; needs doctrine tie-in |
| `quality_gate_public_explainer` | `main/content/en/pages/quality-gate.md` | en | `planned` | `draft` / `non_public` | Public-oriented explainer of gate concepts (still non-public) | **Medium–high** | **Low–medium** | Sync enumerated gates to `QUALITY_GATE.md`; clear **2×** marker clusters | Must not invent gate conditions | **Low** | Markers; **owner review** per route notes | **Mid** if strict doctrine derivative |
| `de_method_corpus_map` | `main/content/de/pages/corpus-map.md` | de | `planned` | `draft` / `non_public` | DE corpus map / methodology bridge | **High** | **Medium** | Thresholds and DE/EN interface lines registry-backed | Reinforce teaching vs normative split; no DIN/IUPAC-DE authority | **Low** | Markers; DE editorial pass; planned route | **Substantial** governance |
| `de_method_translator_playbook` | `main/content/de/pages/translator-playbook.md` | de | `planned` | `draft` / `non_public` | DE translator / editor playbook fragment | **High** | **Medium** | Per-term IUPAC/teaching citations if any line goes public | **`terminology_claims` group**; block universal suffix / equiv. claims | **Low** | Markers; `required_claim_groups`; planned route | **Substantial** (registry coupling) |

**Registry note:** All five routes use `risk_level: "low"` in `routes.json`; this sprint’s **content-level** assessment still elevates **source and claim attention** where chemistry language, German identity layer, or `terminology_claims` coupling appears—consistent with `SOURCE_POLICY.md` (candidate teaching sources cannot carry normative public wording alone).

---

## Page-by-page: source requirement assessment

### `corpus_methodology_overview`

- **High-confidence as doctrine/process (no external source needed for the posture):** Separation of route planning, drafts, source-locking, claim approval, and launch; rejection of thin SEO-only pages as a *design principle*; plain `route_id` inventory without hyperlinks.
- **Requires source-locking or explicit doctrine citation before public tier:** The **“300-page”** minimum cohort framing; references to “candidate doctrinal and planning documents” and gate language—currently flagged **`[SOURCE REQUIRED]`**.
- **Internal consistency:** Draft correctly states registries inactive and no approved claims.

### `internal_linking_discipline`

- **Doctrine/process:** Links as governance infrastructure; `route_id → route_id` mental model; prohibition on assuming publication from registry presence; hub / spine / support vocabulary.
- **Requires later source-locking:** **Link density** and quantitative/qualitative editorial rules—“future iterations may cite doctrine” is explicitly **`[SOURCE REQUIRED]`**.

### `quality_gate_public_explainer`

- **Doctrine/process:** “Planned ≠ published”; gates must pass together; markers must not ship as final copy; weak placeholder launch rejected.
- **Requires source-locking:** **Exact Quality Gate enumeration** restatement against `doctrine/QUALITY_GATE.md`—**`[SOURCE REQUIRED]`** on detailed criteria and the precise list/numbering of conditions.

German pages — see **German draft boundary assessment** below.

---

## Page-by-page: claim-boundary assessment

| route_id | Claim families touched | Boundary posture in draft | Residual risk |
| --- | --- | --- | --- |
| `corpus_methodology_overview` | Governance meta; corpus scale narrative | Explicitly no claim approval; inactive registries | Threshold numbers and “failure mode” wording could be read as empirical without sources |
| `internal_linking_discipline` | None substantive (process) | No live link graph; no publication assumption | Low if link-density rules stay cited from doctrine only |
| `quality_gate_public_explainer` | Meta (eligibility) | No claim approval; no bypass | Mis-sync with `QUALITY_GATE.md` would create false eligibility narrative |
| `de_method_corpus_map` | DE/EN terminology identity; teaching vs normative authority | Strong disclaimers on DIN / official German IUPAC | Any future public tightening needs terminology_claims + stronger sources |
| `de_method_translator_playbook` | Suffix families; disambiguation list; IUPAC/teaching split | Disclaims universal suffix rule; no procurement/safety/market | `required_claim_groups` includes **`terminology_claims`**—future publication must not skip registry |

**Permanently blocked classes (from `SOURCE_POLICY.md`) remain irrelevant to these drafts**—the pages correctly avoid market, safety, medical, procurement, acquisition, and formal DIN/“official German IUPAC rule” *as positive authority*. Any future sentence that sounds **normative** in German still requires **non–academic-teaching** authority per policy.

---

## German draft boundary assessment

Applicable to **`de_method_corpus_map`** and **`de_method_translator_playbook`**.

| Boundary | Evidence in drafts | Sprint 5F judgment |
| --- | --- | --- |
| **German lexical authority** | DE forms (`Sulfid`, `Bisulfid`) framed as identity/disambiguation layer, not as dictionary proof | **Consistent** with “lexical ≠ systematic authority” discipline; public tier still needs registry-backed examples |
| **Academic teaching source boundary** | Both drafts: teaching = **Kandidat** only; cannot replace norms | **Aligned** with `academic_teaching_reference` constraints in `SOURCE_POLICY.md` |
| **DIN / official German IUPAC non-claim** | Explicit **keine** formal DIN / **keine** behauptete offizielle deutsche IUPAC-Normativität / Verbindlichkeit | **Pass**—no false authority claims |
| **Translation-risk boundary** | MT without review insufficient; DE pages “editorisch eigenständig” | **Pass** as process doctrine |
| **No universal suffix-transformation boundary** | Translator playbook: **keine** universelle Suffix-Transformationsregel | **Pass**—matches policy prohibition on universal suffix claims without stronger sources |
| **Bisulfid / Bisulfide / Sulfid / Sulfide / Hydrosulfide / Bisulfite** | Named in playbook disambiguation list; corpus-map points to specialist routes | **Appropriate as worklist** only; **no** chemical equivalence or handling claims—**consistent** |

---

## Source categories likely needed later

When these pages move toward public eligibility (not now), expect combinations of:

- **Doctrine-internal** locks (canonical quotations or synchronized restatement from `doctrine/QUALITY_GATE.md`, `PROJECT_DOCTRINE.md`, linking doctrine).
- **IUPAC / nomenclature standards** (for any sentence that reads like a systematic naming rule—not yet asserted as final public copy).
- **Authoritative lexical references** (for DE/EN surface-form discussions if presented as more than editorial hypothesis).
- **Peer-reviewed or standards-adjacent** material only where **non-teaching** authority is required.
- **`academic_teaching_reference`** strictly as **candidate support** alongside the disclaimers already drafted—never as sole authority for normative German chemistry wording.

---

## Claims likely needed later

- **None approved or introduced in Sprint 5F.**

For **`de_method_translator_playbook`**, `routes.json` already flags **`terminology_claims`** as a **required claim group** for future publication. That implies: selective, low-risk terminology claims (or expanded draft scope reduced to pure process-only language) before any public route flip—**registry remains inactive today**.

---

## Statements that can remain doctrine/process statements

- Planning vs publication separation; `planned` routes are not live.
- Internal links as governance graph intent; `internal_links.json` is the eventual implementation layer.
- Rejection of placeholder launch and marker-stripping without review.
- DE editorial independence and anti–machine-translation-default posture.
- Teaching sources as **candidate-only**; no DIN / no official German IUPAC authority **as asserted norm** (negative boundaries).

---

## Statements requiring source-locking if published as factual or enumerative

- **300-page** threshold wording and provenance of “minimum launch cohort” language.
- **Quality Gate** detailed condition list and numbering (must match doctrine).
- **Link-density** rules when stated as concrete editorial requirements.
- **DE/EN collision** examples and any future “how we translate X” lines beyond generic discipline.
- **Per-term** system assignment (bisulfite vs bisulfide family, etc.) when stated as more than a cautious worklist.

---

## Statement classes that must remain blocked from public wording until stronger authority exists

- **Universal suffix transformation** EN→DE (playbook already blocks this).
- **Formal DIN compliance** claims or **official German IUPAC** “binding” readings.
- **Chemical equivalence** across languages or salts without dedicated science claims + sources.
- **Market, procurement, safety, medical** expansions (drafts correctly avoid; must not creep in during hardening).

---

## Internal linking readiness

| Dimension | Status |
| --- | --- |
| `internal_links.json` | **Unchanged**; correct for current posture |
| Draft cross-references | **Plain `route_id` only**—safe, non-navigable |
| Graph coherence for public tier | **Not ready**—targets are largely planned; edges would be aspirational |
| Methodology interlinks | Sensible *future* hub: `corpus_methodology_overview` ↔ `internal_linking_discipline` ↔ `quality_gate_public_explainer` ↔ DE methodology pair |

**Recommendation (future sprint, not 5F):** Add **planned** edges only under an explicit linking batch, after target routes have eligible copy.

---

## Publication blocker matrix

Legend: **B** = blocker present until resolved.

| Blocker | corpus_methodology | internal_linking | quality_gate | de_corpus_map | de_translator_playbook |
| --- | --- | --- | --- | --- | --- |
| **`[SOURCE REQUIRED]` markers** | B | B | B | B | B |
| Route `status: planned` | B | B | B | B | B |
| `indexable` / `in_sitemap` false | B | B | B | B | B |
| Claim registries inactive | B (meta narrative references) | — | B (meta) | B | B (incl. `terminology_claims` group) |
| Owner / editorial gates (route notes) | Editorial signoff | Editorial signoff | Owner review | Editorial + DE pass | Editorial + terminology alignment |
| Internal link graph not public-ready | B | B | B | B | B |
| Quality Gate not satisfied globally | B | B | B | B | B |

---

## Pages closest to future publication readiness (relative, not approval)

**Closer (still not publication-ready):**

1. **`internal_linking_discipline`** — Mostly process; lowest chemistry-factual surface. Remaining gap: cite link-density doctrine explicitly and clear the single **`[SOURCE REQUIRED]`**.
2. **`quality_gate_public_explainer`** — Strong structural alignment with gate narrative; must become a **strict derivative** of `doctrine/QUALITY_GATE.md` and clear markers.

**Requiring substantial additional governance:**

3. **`corpus_methodology_overview`** — Scale and doctrine-crosswalk sentences need locking.
4. **`de_method_corpus_map`** — DE/EN interface + identity layer needs sources and DE editorial completion.
5. **`de_method_translator_playbook`** — Highest **claim-registry coupling** (`terminology_claims`); disambiguation list must not harden into public rules without claims.

**This sprint does not approve publication for any route and does not recommend public launch.**

---

## Sprint 5F governance confirmations

| Topic | Confirmation |
| --- | --- |
| Why no content pages were modified | Sprint charter: **report-only** review; edits would preempt source-locking workflow |
| Why no routes were published | All routes remain **`planned`**; Quality Gate and registry posture unchanged |
| Why no claims were approved | Registries **inactive**; drafts explicitly disclaim approval |
| Why **`[SOURCE REQUIRED]`** markers remain | Factual/doctrinal restatements are not yet registry-backed |
| Publication readiness conclusion | **Not ready for publication** |
| Recommended next sprint | **Sprint 5G (or equivalent):** (1) Editorial hardening: replace markers with doctrine-synchronized text **or** scoped source additions in `source_registry` *in a dedicated sprint that explicitly allows registry edits*; (2) Optional **`internal_links.json`** batch for methodology cluster only, **planned** edges; (3) For `de_method_translator_playbook`, terminology **source mapping** and claim scoping before any publication discussion |

---

*Sprint 5F — governance report only. No registry or content mutations.*
