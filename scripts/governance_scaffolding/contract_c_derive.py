"""
Contract C — Derived Canonical State: reference specification (pure function).

Sprint: authority-dimension-impl-1 (governance scaffolding).
Baseline: BISULFID_AUTHORITY_DIMENSION_ARCHITECTURE.md (IP-1, IP-2, IP-4, IP-16).

READ-ONLY / UNWIRED. This module is a specification of the derived-state
function. It is NOT imported by build, deploy, sitemap generation, robots,
routes, the release ledger, or any CI production gate. It reads no repository
state. Its only consumer is scripts/governance_scaffolding/contract_c_property_tests.py.

Canonical outputs
-----------------
publication_state ∈ {not_public, public_noindex, public_indexable}
indexation_state  ∈ {noindex, index_approved}          # index_candidate REMOVED (IP-16.1)
"""

# --- Canonical input posture domains -------------------------------------------------

GOVERNANCE = ("planned", "relationship_qualified", "reference_draft", "governed")
EVIDENCE = ("evidence_not_required", "evidence_collecting", "evidence_sufficient", "evidence_locked")
CLAIM = ("claim_not_required", "claim_pending", "claim_approved_narrow", "claim_approved", "claim_forbidden")
VALIDATION = ("not_validated", "validated", "validation_failed")
IG = ("ig_not_required", "ig_not_reviewed", "ig_passed", "ig_failed")
RELEASE = ("not_authorized", "authorized", "withdrawn")
HOLD = ("none", "held")
LEGACY = ("none", "legacy_public_holding")
NON_FACTUAL_CERTIFIED = (False, True)

PUBLICATION_STATES = ("not_public", "public_noindex", "public_indexable")
INDEXATION_STATES = ("noindex", "index_approved")

# Privilege ordering for the monotonic-veto property.
_PUB_RANK = {"not_public": 0, "public_noindex": 1, "public_indexable": 2}
_IDX_RANK = {"noindex": 0, "index_approved": 1}


def privilege_rank(publication_state, indexation_state):
    """Total-order rank of an output pair; higher == more privilege."""
    return (_PUB_RANK[publication_state], _IDX_RANK[indexation_state])


def derive(
    governance,
    evidence,
    claim,
    validation,
    ig,
    release,
    hold="none",
    legacy="none",
    non_factual_class_certified=False,
):
    """Total, deterministic derived-state function (first-match rules R0..R12).

    Every valid combination of canonical inputs returns exactly one
    (publication_state, indexation_state) pair. See IP-1 for the rule listing.
    """
    # R0 — withdrawal overrides everything (including legacy holding).
    if release == "withdrawn":
        return ("not_public", "noindex")

    # RL — migration-only legacy holding (IP-16.2). Never index. Precondition
    # (pre-ratification public AND not a new route) is enforced by the validator,
    # not here; this function only defines the state mapping.
    if legacy == "legacy_public_holding":
        return ("public_noindex", "noindex")

    # R1 — no release authorization.
    if release == "not_authorized":
        return ("not_public", "noindex")

    # R2 — not yet a governed/draft route.
    if governance in ("planned", "relationship_qualified"):
        return ("not_public", "noindex")

    # R3 — validation blocking.
    if validation in ("not_validated", "validation_failed"):
        return ("not_public", "noindex")

    # R4 — claim blocking.
    if claim in ("claim_pending", "claim_forbidden"):
        return ("not_public", "noindex")

    # R5 — evidence still being collected.
    if evidence == "evidence_collecting":
        return ("not_public", "noindex")

    # From here: legacy == none, release == authorized, validation == validated,
    # governance in {reference_draft, governed}, claim in {not_required, approved_narrow, approved},
    # evidence in {not_required, sufficient, locked}.

    # R6 — NEW objects are not public while still drafting (Knowledge-Object-Before-URL, IP-16.2).
    if governance == "reference_draft":
        return ("not_public", "noindex")

    # R7 — no URL before Information-Gain review (IP-16.2).
    if ig == "ig_not_reviewed":
        return ("not_public", "noindex")

    # R8 — IG failure denies an independent URL (IP-16.2).
    if ig == "ig_failed":
        return ("not_public", "noindex")

    # From here: governance == governed, ig in {ig_passed, ig_not_required}.

    # R9 — passed IG + evidence sufficiency, but not yet source-locked -> public, not indexed.
    if evidence == "evidence_sufficient":
        return ("public_noindex", "noindex")

    # R10 — factual indexable path.
    if evidence == "evidence_locked" and claim in ("claim_approved", "claim_approved_narrow"):
        idx = "noindex" if hold == "held" else "index_approved"
        return ("public_indexable", idx)

    # R11 — non-factual certified indexable path (IP-4).
    if evidence == "evidence_not_required" and claim == "claim_not_required" and non_factual_class_certified:
        idx = "noindex" if hold == "held" else "index_approved"
        return ("public_indexable", idx)

    # R12 — SAFE DEFAULT: deny a URL (mixed/contradictory combos). Never a silent public_noindex.
    return ("not_public", "noindex")


def all_input_combinations():
    """Yield every canonical input combination (exhaustive Cartesian product)."""
    for governance in GOVERNANCE:
        for evidence in EVIDENCE:
            for claim in CLAIM:
                for validation in VALIDATION:
                    for ig in IG:
                        for release in RELEASE:
                            for hold in HOLD:
                                for legacy in LEGACY:
                                    for nf in NON_FACTUAL_CERTIFIED:
                                        yield dict(
                                            governance=governance,
                                            evidence=evidence,
                                            claim=claim,
                                            validation=validation,
                                            ig=ig,
                                            release=release,
                                            hold=hold,
                                            legacy=legacy,
                                            non_factual_class_certified=nf,
                                        )


def legacy_holding_allowed(is_new_route, pre_ratification_public):
    """Validator helper (IP-16.2): legacy_public_holding may be assigned ONLY to a
    route that was publicly deployed before Contract C ratification and is NOT newly
    created. This is a governance precondition, separate from the state mapping."""
    return (pre_ratification_public is True) and (is_new_route is False)
