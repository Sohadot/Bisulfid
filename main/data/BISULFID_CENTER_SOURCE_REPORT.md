# Bisulfid Center Node Source Report — Sprint 3B

**Date:** 2026-05-16  
**Branch:** claude/sprint-3b-bisulfid-center-source-lock  
**Governed by:** doctrine/SOURCE_POLICY.md

---

## Why This Sprint Exists

Sprint 3 seeded 8 candidate sources and assigned `source_ids` to 8 ontology terms. The `bisulfid` center node — the conceptual and linguistic anchor of bisulfid.com — was explicitly identified in the Sprint 3 source registry seed report as having no source_ids, and was flagged as the highest-priority remaining source gap. Sprint 3B addresses that gap.

The `bisulfid` term is architecturally central: every route, every claim, and every language layer points back to this node. Without at least candidate source support, the center node has no source foundation at all. Sprint 3B seeds the minimum candidate support while being honest about what that support does and does not establish.

---

## Sources Searched or Evaluated

### Search scope

- **Authoritative dictionaries**: Duden was searched for a 'Bisulfid' entry (as opposed to 'Sulfid', which was found in Sprint 3). No direct Duden entry for 'Bisulfid' was identified as available for seeding in this sprint. A Duden entry for 'Bisulfid' remains the highest-priority future source target.
- **IUPAC Gold Book**: Reviewed for a direct 'bisulfide' or 'bisulfid' entry. The IUPAC Gold Book entry found in Sprint 3 covers 'hydrosulfides', not 'bisulfide/bisulfid' as a direct headword. No IUPAC entry directly for 'bisulfid' (German form) was identified.
- **German chemical databases and regulatory sources**: No government scientific database or German regulatory entry directly under 'Bisulfid' was identified for seeding in this sprint.
- **Wikipedia**: Excluded per governance rules. Not used as a source.
- **AI summaries**: Excluded per governance rules. Not used as a source.
- **Commercial and technical German-language sources**: A Badger Meter German-language technical page was identified as directly using the term 'Bisulfid' in the context of water-quality sulfur monitoring: *Messung von Bisulfid und Schwefelwasserstoff im Wasser*. This source uses 'Bisulfid und Schwefelwasserstoff (HS⁻ / H₂S)' in a German technical context.
- **Patent records**: Patent usage was considered but not added in this sprint. Patents are usage evidence only and not authoritative terminology standards. No clean, directly relevant patent page was identified as sufficiently stable and clear for seeding.

### Stronger sources not found in this sprint

No authoritative dictionary, nomenclature standard, regulatory body, government scientific database, or peer-reviewed journal entry directly for the term 'Bisulfid' (German form) was identified for seeding in this sprint. The Badger Meter source is the only candidate source added.

---

## Source Selected

**SRC-BADGER-BISULFID-H2S**

| Field | Value |
|---|---|
| source_id | SRC-BADGER-BISULFID-H2S |
| category | industry_publication |
| publisher | Badger Meter |
| title | Messung von Bisulfid und Schwefelwasserstoff im Wasser |
| url | https://www.badgermeter.com/de-de/parameter-zur-uberwachung-der-wasserqualitat/hs-h2s/ |
| language | de |
| status | seeded |
| source_lock_status | candidate |
| last_reviewed | 2026-05-16 |

---

## Source Category and Limitations

**Category:** `industry_publication`

This is the weakest source category in the registry hierarchy. It is below:
- authoritative_dictionary
- chemical_nomenclature_standard
- government_scientific_database
- regulatory_body
- peer_reviewed_journal

**What this source establishes:**
- Observed German technical usage of the term 'Bisulfid' in a water-quality / sulfur-monitoring context.
- A plausible connection between 'Bisulfid' and 'HS⁻ / H₂S' terminology as used by a German-language technical publisher.

**What this source does NOT establish:**
- Formal German nomenclature authority for 'Bisulfid'.
- That 'Bisulfid' is the preferred or IUPAC-standard German form.
- Final equivalence between Bisulfid and hydrosulfide.
- Any safety, handling, or exposure guidance.
- Any market data.
- Any procurement or regulatory authority.

---

## Whether Bisulfid Remains Candidate or Verified

**Bisulfid status: `planned` (candidate source support only)**

Bisulfid is NOT marked verified. The term status remains `planned`. The source added is a commercial technical source in the lowest-priority source category. It supports observed German technical usage only. It does not provide dictionary, nomenclature standard, regulatory, or academic authority for the term.

The bisulfid center node remains under-sourced relative to the standard required for publication. No [SOURCE REQUIRED] markers may be removed based on this source alone.

---

## Ontology Update Made

**File:** `main/data/ontology/sulfur_terms.json`

- `bisulfid.source_ids`: updated from `[]` to `["SRC-BADGER-BISULFID-H2S"]`
- `bisulfid.status`: remains `"planned"` (unchanged)
- `bisulfid.notes`: updated to append: *"Center node source support remains candidate. Current source supports German technical usage only; stronger dictionary, nomenclature, regulatory, or academic source still required."*

All other terms unchanged.

---

## Claim Update Made

**File:** `main/data/claims/terminology_claims.json`

New claim added:

| Field | Value |
|---|---|
| claim_id | CLM-TERM-BISULFID-001 |
| claim_type | terminology |
| status | pending_review |
| statement | Bisulfid appears as a German technical usage term in sulfur/water-quality monitoring context. |
| source_ids | [SRC-BADGER-BISULFID-H2S] |
| risk_level | medium |

The claim carries `status: pending_review`. It was not approved. The claim registry `status` field remains `inactive`.

**Prohibited uses recorded on claim:**
- formal nomenclature authority
- safety instructions
- market claims
- medical claims
- industrial procurement claims
- public proof of preferred German IUPAC spelling

---

## Why No Market Data Was Added

This sprint is a source-locking sprint for the ontology center node only. Market data (production statistics, trade volumes, pricing, Gulf/Morocco/China data) was not in scope and was not added. `market_claims.json` was not modified. The blocked source use `market_statistics_without_verified_source` remains in force.

---

## Why No Route or Publication State Changed

No route was published. No route status, indexable, in_sitemap, or in_navigation value was changed. All routes remain `planned`. The source registry `status` remains `inactive`. No claim was approved. No content page was modified. No [SOURCE REQUIRED] marker was removed. The site remains in full prelaunch, non-public state.

---

## Remaining Source Gap

The bisulfid center node still requires a stronger authoritative source. Priority order for future source sprints:

1. **Duden — Bisulfid**: An authoritative German dictionary entry directly under 'Bisulfid' would be the highest-quality source available. Search for this entry first in any future source sprint.
2. **IUPAC Gold Book or IUPAC nomenclature standard**: A direct IUPAC entry for bisulfide (English form) or bisulfid (German form) would provide nomenclature authority.
3. **German regulatory or government database**: A German-language government scientific database (e.g., BfR, GESTIS, BAuA) or European chemical regulatory entry directly using 'Bisulfid' would qualify as a stronger source.
4. **Peer-reviewed journal or academic reference**: A journal article or academic chemical reference that directly names and defines 'Bisulfid' as a German chemical term.
5. **Further commercial/technical sources**: Additional German-language commercial or technical sources using 'Bisulfid' could supplement the Badger Meter source but would not replace the need for a tier-1 authoritative source.

Until a tier-1 source is found and locked, the bisulfid center node remains `planned` with candidate source support only, and no [SOURCE REQUIRED] markers may be removed from the `what_is_bisulfid` or `bisulfid_vs_bisulfide` draft pages.
