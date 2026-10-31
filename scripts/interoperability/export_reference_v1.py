#!/usr/bin/env python3
"""Build the non-public BISULFID Reference Exchange v1 pilot from governed inputs.

This is an interoperable *draft* data product, NOT an API, public release, dataset
license or substitute for source verification. Use --check in CI to catch drift.
No third-party passages or captured artifacts are redistributed.
"""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"
KO_ID = "KO-BISULFID-TERMINOLOGY-001"
OUTPUT = DATA / "interoperability" / "bisulfid_terminology.v1.json"
REQUIRED_CHECKS = {f"D{i}" for i in range(1, 8)}


def read(relative_path):
    with (DATA / relative_path).open(encoding="utf-8") as handle:
        return json.load(handle)


def build(*, dossier=None, registry=None, evaluation=None, claims_store=None, owner_acts=None):
    dossier = dossier if dossier is not None else read("release/claim_dossiers/" + KO_ID + ".json")
    registry = registry if registry is not None else read("knowledge_objects/knowledge_object_registry.json")
    evaluation = evaluation if evaluation is not None else read("release/documentary_verification/" + KO_ID + ".json")
    claims_store = claims_store if claims_store is not None else read("claims/terminology_claims.json")
    owner_acts = owner_acts if owner_acts is not None else read("release/owner_acts.json")

    ko = next((item for item in registry["knowledge_objects"]
               if item["knowledge_object_id"] == KO_ID), None)
    if ko is None or dossier["knowledge_object_id"] != KO_ID:
        raise ValueError("missing or mismatched governed knowledge object")
    if not (evaluation.get("knowledge_object_id") == KO_ID
            and evaluation.get("policy_adopted") is True
            and evaluation.get("policy_status") == "adopted"
            and evaluation.get("verification_level") == "documentary_verified"
            and evaluation.get("independently_human_reviewed") is False
            and evaluation.get("risk_class") == "low_risk_informational"
            and not evaluation.get("failures")):
        raise ValueError("documentary evaluation is not eligible for exchange")
    checks = evaluation.get("checks", {})
    if {k[:2] for k, v in checks.items() if v == "pass"} != REQUIRED_CHECKS:
        raise ValueError("not all D1–D7 checks passed")

    # Never infer public release or claim activation from approved registry entries.
    if owner_acts.get("claim_activations") or owner_acts.get("release_authorizations"):
        raise ValueError("pilot requires re-assessment if owner acts change")

    authored = {claim["claim_id"]: claim for claim in claims_store["claims"]}
    outcomes = {item["claim_id"]: item for item in evaluation["claim_outcomes"]}
    expected = ko["claim_ids"]
    if len(expected) != 11 or len(expected) != len(set(expected)):
        raise ValueError("pilot claim IDs changed")
    by_id = {item["claim_id"]: item for item in dossier["claims"]}
    if set(expected) != set(by_id) or set(expected) != set(outcomes):
        raise ValueError("dossier, evaluation and registry claim sets disagree")

    claims = []
    for claim_id in expected:
        item, store, check = by_id[claim_id], authored.get(claim_id), outcomes[claim_id]
        if not store or item["status_in_store"] != "approved" or store.get("status") != "approved":
            raise ValueError(f"{claim_id}: claim is not approved in the registry")
        if store.get("claim_type") != "terminology" or check["outcome"] != "documentary_verified":
            raise ValueError(f"{claim_id}: unsupported type or evaluation")
        if not item.get("statement") or item["statement"] != store.get("statement"):
            raise ValueError(f"{claim_id}: statement differs from the source registry")
        evidence = []
        for ev in item["evidence"]:
            url = ev.get("url", "")
            parsed = urlparse(url)
            if parsed.scheme != "https" or not parsed.netloc:
                raise ValueError(f"{claim_id}: invalid source URL")
            if (not ev.get("rendered_on_page")
                    or ev.get("source_status") != "verified"
                    or ev.get("review_posture") != "evidence_verified"
                    or not ev.get("qualification_id")
                    or not ev.get("admitted_for")):
                raise ValueError(f"{claim_id}: unqualified, pending or unrendered evidence")
            evidence.append({
                "evidence_id": ev["evidence_id"],
                "source_id": ev["source_id"],
                "publisher": ev["publisher"],
                "source_url": url,
                "retrieved_on": ev["retrieval_date"],
                "use_qualification_id": ev["qualification_id"],
                "admitted_for": ev["admitted_for"],
                "source_lock_status": ev["source_lock_status"],
            })
        if not evidence:
            raise ValueError(f"{claim_id}: no bound evidence")
        if (set(x["evidence_id"] for x in evidence) != set(check["evidence_ids"])
                or set(x["source_id"] for x in evidence) != set(check["sources"])):
            raise ValueError(f"{claim_id}: evidence bindings differ from verification")
        claims.append({
            "claim_id": claim_id,
            "claim_type": "terminology",
            "registry_status": "approved_not_owner_activated",
            "statement": item["statement"],
            "verification_level": "documentary_verified",
            "evidence": evidence,
        })

    return {
        "format": "BISULFID Reference Exchange",
        "schema_version": "1.0.0",
        "publisher": {"name": "Sohadot", "website": "https://sohadot.com"},
        "reference": {
            "knowledge_object_id": KO_ID,
            "language": "en",
            "topic": "English/German chemical terminology",
            "intended_canonical_url": "https://bisulfid.com/bisulfid-vs-bisulfide/",
            "disclosure": "Recorded chemical names and source usage are not automatically equivalent or recommended IUPAC names.",
        },
        "publication": {
            "state": "staged_not_public",
            "owner_claim_activation": False,
            "release_authorized": False,
            "public_api_available": False,
            "note": "This exchange bundle is an internal development artifact and does not make the linked reference publicly authorized.",
        },
        "verification": {
            "policy": "DOCUMENTARY-VERIFICATION@1.0.0",
            "level": "documentary_verified",
            "independent_human_peer_review": False,
            "assertion": "Automated documentary verification of cited evidence, not external peer review.",
            "checks": {key: checks[key] for key in sorted(checks)},
        },
        "rights": {
            "bundle_license": "not_granted",
            "external_materials": "Third-party source material retains its own copyright and licensing terms.",
            "no_republished_source_extracts": True,
            "commercial_reuse": "Requires explicit rights review and separate owner licensing decision.",
        },
        "exclusions": {
            "unverified_german_industry_usage": True,
            "safety_medical_industrial_advice": True,
            "knowledge_objects_other_than_pilot": True,
        },
        "provenance": {
            "claims_registry": "main/data/claims/terminology_claims.json",
            "claim_dossier": "main/data/release/claim_dossiers/" + KO_ID + ".json",
            "documentary_evaluation": "main/data/release/documentary_verification/" + KO_ID + ".json",
            "knowledge_registry": "main/data/knowledge_objects/knowledge_object_registry.json",
            "source_captures_redistributed": False,
        },
        "claims": claims,
    }


def serialize(payload):
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Regenerate internal reference exchange JSON")
    mode.add_argument("--check", action="store_true", help="Fail if output differs from governed inputs")
    args = parser.parse_args()
    result = serialize(build())
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != result:
            print("STALE: internal reference exchange pilot; run --write")
            return 1
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(result, encoding="utf-8")
    print("BISULFID reference exchange: 11 documentary-verified claims, staged only; no public release")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
