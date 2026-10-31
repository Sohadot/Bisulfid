# Release-01A — terminology reference: publication readiness, evidence and SEO

**Owner:** Sohadot (sohadot.com)  
**Prepared:** 2026-10-31  
**Branch:** `release-01/terminology-release-readiness` (stacked on `release-01/pr-e`)  
**Knowledge Object:** `KO-BISULFID-TERMINOLOGY-001`  
**Existing canonical route:** `/bisulfid-vs-bisulfide/`  
**Decision status:** DRAFT — no claim activation, IG ratification, release approval, merge or deployment.

## Evidence and scientific integrity

- `DOCUMENTARY-VERIFICATION@1.0.0` was adopted by Sohadot on 2026-10-31.
- The object's stored documentary evaluation is `documentary_verified`, with 11/11 narrowly approved terminology claims, 11/11 sources meeting L1–L5, 15 admitted evidence records, 13 valid information-gain units and no independent human peer-review claim.
- Individual source locks remain candidates: **0 signed human L6 source locks**. The owner-adopted policy accepts the documentary pathway for this low-risk informational KO only; `evidence_locked` and `validated` are accepted documentary postures, **not** claims of human signatures.
- `CLM-TERM-BISULFID-001` (general German industry usage) remains pending and unbound. The reference's boundary disclosure was narrowed from "some German industry pages" to a single captured observation, without generalizing it into accepted German usage.
- The candidate and staged manifest have been synchronized with the approved documentary pathway. The remaining authorization blockers are independent and explicit.

## Search and reader-value audit (read-back of the staged HTML)

- The page answers the actual comparison question immediately; the title is **Bisulfid vs Bisulfide: Meanings, IUPAC Names, German Usage**.
- Unique meta description is 136 characters, with the relevant institutions and terminology; one descriptive H1; self-canonical `https://bisulfid.com/bisulfid-vs-bisulfide/`.
- `DefinedTermSet` JSON-LD contains 5 source-bounded terms; its existence does **not** guarantee a Google rich result.
- 15 evidence-row anchors and 34 intra-page evidence references were present; no missing evidence-anchor target in the staged HTML on inspection. Reader-facing claims link to source records and external primary/authoritative sources.
- The page distinguishes dictionary sense, chemical-database synonym, IUPAC nomenclature and German lexicography rather than implying equivalence. The supported/open/not-inferable synthesis is retained.
- Internal methodology and source-guidance links remain. The link calling the unready MoS₂ legacy surface a governed scientific reference was **withheld** until that reference is actually approved and released. No new hreflang is invented for the non-equivalent German legacy page.
- Four same-task legacy duplicates remain **consolidation obligations**, not executable redirects or noindex actions. They must not be changed until the destination is index-approved and per-URL decisions receive real authority.
- Avoid thin translated surfaces, templated near-duplicates, invented expertise, unsupported structured data, rankings or traffic claims. Google Search guidance prioritizes substantive original value and correct canonicalization, not output volume.

**Important staging distinction:** The staged HTML's robots meta currently reads `index, follow` because the current publication authority resolves the sealed *legacy URL's* status quo for rendering. This **does not** grant the proposed governed replacement an indexation entitlement. The staged `release.json` still derives `not_public/noindex`; `apply_release.py` must refuse an unauthorized copy to `site/public`. Do not deploy the staged HTML or treat its meta tag as proof of approval.

## Separate Sohadot decisions outstanding — in order

1. **Claim activation:** Explicitly authorize exactly the 11 KO-bound, narrowly approved claims in `main/data/release/owner_acts.json`; exclude `CLM-TERM-BISULFID-001`. A genuine representative/owner identity and date are required by the current publication authority; no artificial signature.
2. **IG route realization:** Separately decide whether to ratify `AMD-IG-R03-001` revision 2 in `main/data/information_gain/ig_governance_policy.json`. This allows the new reference to **replace the same existing URL**, not create sibling URLs, and retains the four consolidation obligations.
3. **Release authorization:** Only after the preceding requirements and full release QA pass, separately authorize the exact knowledge object and staged artifact.
4. **Merge/deploy:** Distinct decisions, following chain integrity, GitHub CI and live-site preflight. Neither is covered by the other three acts.

**Dependency:** The staged English and German homepages refer to both governed references, including the incomplete MoS₂ scientific object. **Do not launch those homepages alongside the terminology reference** unless their independent dependencies and R11 certifications are actually satisfied.

## Verification provenance and unresolved work

The repository read-back confirmed JSON parseability, the 15/34 evidence anchor relationship, one H1, existing canonical/title/description and source links, and consistency between the candidate and staged manifest. Added regression checks cover documentarily accepted postures, truthful source-lock reporting and separation from owner acts.

**Not yet run on this exact branch:** canonical renderer `--check`, isolated full suite, GitHub CI and a served-surface deployment dry run. Do not report them as PASS or claim publication readiness until executed.

Once the runtime checks pass, present the three precise owner decisions above for real approval. No more general governance redesign is required; prioritize original, technically rigorous reference content and measured consolidation after the first legitimate release.
