#!/usr/bin/env python3
"""Offline, machine-readable claim and evidence explorer for the BISULFID v1 pilot.

No network, AI API, telemetry, search engine or database service is required.
A result documents a draft reference's evidence; it is not a publication approval.
"""
import argparse
from datetime import date
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "main/data/interoperability/bisulfid_terminology.v1.json"
DOCUMENTARY_CHECKS = {f"D{i}" for i in range(1, 8)}


class ExplorerError(ValueError):
    """Input bundle is not an eligible, rights-aware reference exchange pilot."""


def normalize(text):
    return unicodedata.normalize("NFKC", text).casefold()


def term_present(phrase, text):
    """Match a whole term/phrase, never 'sulfid' within 'bisulfide'."""
    q = normalize(phrase).strip()
    if not q:
        return False
    return re.search(r"(?<!\w)" + re.escape(q) + r"(?!\w)", normalize(text)) is not None


def validate(bundle):
    if bundle.get("format") != "BISULFID Reference Exchange" or bundle.get("schema_version") != "1.0.0":
        raise ExplorerError("unsupported reference-exchange format or version")
    if bundle.get("publisher", {}).get("name") != "Sohadot":
        raise ExplorerError("unexpected publisher")
    if bundle.get("reference", {}).get("knowledge_object_id") != "KO-BISULFID-TERMINOLOGY-001":
        raise ExplorerError("pilot only supports the verified terminology knowledge object")
    pub = bundle.get("publication", {})
    if (pub.get("state") != "staged_not_public" or pub.get("public_api_available") is not False
            or pub.get("owner_claim_activation") is not False or pub.get("release_authorized") is not False):
        raise ExplorerError("changed publication authority: revalidate against governed stores")
    ver = bundle.get("verification", {})
    if (ver.get("policy") != "DOCUMENTARY-VERIFICATION@1.0.0"
            or ver.get("level") != "documentary_verified"
            or ver.get("independent_human_peer_review") is not False):
        raise ExplorerError("verification or independent-review posture has changed")
    checks = ver.get("checks", {})
    if not isinstance(checks, dict) or {key[:2] for key, val in checks.items() if val == "pass"} != DOCUMENTARY_CHECKS:
        raise ExplorerError("not all documentary D1–D7 checks passed")
    rights = bundle.get("rights", {})
    if (rights.get("bundle_license") != "not_granted"
            or rights.get("no_republished_source_extracts") is not True):
        raise ExplorerError("rights posture changed; separate licensing review required")
    if not bundle.get("exclusions", {}).get("unverified_german_industry_usage"):
        raise ExplorerError("unverified German usage cannot be implicitly admitted")

    claims = bundle.get("claims")
    if not isinstance(claims, list) or len(claims) != 11:
        raise ExplorerError("pilot claim count changed; a new governed release is required")
    seen_claims, seen_evidence = set(), {}
    for claim in claims:
        cid = claim.get("claim_id")
        if not isinstance(cid, str) or not cid or cid in seen_claims:
            raise ExplorerError("empty or duplicate claim ID")
        seen_claims.add(cid)
        if (claim.get("claim_type") != "terminology"
                or claim.get("registry_status") != "approved_not_owner_activated"
                or claim.get("verification_level") != "documentary_verified"
                or not isinstance(claim.get("statement"), str)
                or not claim["statement"].strip()):
            raise ExplorerError(f"{cid}: unqualified claim")
        evidence = claim.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            raise ExplorerError(f"{cid}: missing evidence")
        local_ids = set()
        for edge in evidence:
            eid, sid = edge.get("evidence_id"), edge.get("source_id")
            if not isinstance(eid, str) or not eid or eid in local_ids or not isinstance(sid, str) or not sid:
                raise ExplorerError(f"{cid}: invalid or duplicate evidence ID")
            local_ids.add(eid)
            if eid in seen_evidence and seen_evidence[eid] != sid:
                raise ExplorerError(f"{eid}: inconsistent source identity")
            seen_evidence[eid] = sid
            url = edge.get("source_url", "")
            if not isinstance(url, str):
                raise ExplorerError(f"{eid}: URL is not text")
            parts = urlsplit(url)
            if parts.scheme != "https" or not parts.netloc or parts.username or parts.password:
                raise ExplorerError(f"{eid}: unsafe source URL")
            try:
                date.fromisoformat(edge["retrieved_on"])
            except (KeyError, TypeError, ValueError):
                raise ExplorerError(f"{eid}: missing or invalid retrieval date") from None
            if any(not isinstance(edge.get(k), str) or not edge[k].strip()
                   for k in ("publisher", "use_qualification_id", "admitted_for", "source_lock_status")):
                raise ExplorerError(f"{eid}: incomplete source provenance")
            if any(k in edge for k in ("verbatim_or_fields", "source_fulltext", "capture")):
                raise ExplorerError(f"{eid}: raw or verbatim third-party capture must not be exported")
    return bundle


def load():
    with BUNDLE.open(encoding="utf-8") as handle:
        return validate(json.load(handle))


def sources(bundle):
    result = {}
    for claim in bundle["claims"]:
        for edge in claim["evidence"]:
            sid = edge["source_id"]
            if sid not in result:
                result[sid] = {
                    "source_id": sid, "publisher": edge["publisher"],
                    "source_urls": [], "claim_ids": [], "evidence_ids": [],
                }
            row = result[sid]
            for k, v in (("source_urls", edge["source_url"]),
                         ("claim_ids", claim["claim_id"]),
                         ("evidence_ids", edge["evidence_id"])):
                if v not in row[k]:
                    row[k].append(v)
    for row in result.values():
        for k in ("source_urls", "claim_ids", "evidence_ids"):
            row[k].sort()
    return sorted(result.values(), key=lambda r: r["source_id"])


def search(bundle, mode, value=None):
    validate(bundle)
    if mode not in {"term", "claim-id", "source-id", "evidence-id", "sources", "summary"}:
        raise ExplorerError("unsupported query mode")
    if mode in {"term", "claim-id", "source-id", "evidence-id"}:
        if not isinstance(value, str) or not value.strip():
            raise ExplorerError("query is required")
        value = value.strip()
    found = []
    for claim in bundle["claims"]:
        if mode == "term":
            keep = term_present(value, claim["statement"])
        elif mode == "claim-id":
            keep = claim["claim_id"] == value
        elif mode == "source-id":
            keep = any(e["source_id"] == value for e in claim["evidence"])
        elif mode == "evidence-id":
            keep = any(e["evidence_id"] == value for e in claim["evidence"])
        else:
            keep = False
        if keep:
            found.append(claim)
    result = {
        "format": "BISULFID Reference Explorer",
        "schema_version": "1.0.0",
        "query": {"mode": mode, "value": value if value is not None else None},
        "knowledge_object_id": bundle["reference"]["knowledge_object_id"],
        "verification": {
            "level": bundle["verification"]["level"],
            "independent_human_peer_review": False,
        },
        "publication": bundle["publication"],
        "rights": bundle["rights"],
        "matched_claims": len(found),
        "claims": found,
    }
    if mode in ("sources", "summary"):
        srcs = sources(bundle)
        result["claims"] = []
        result["matched_claims"] = 0
        result["sources"] = srcs if mode == "sources" else []
        if mode == "summary":
            result["summary"] = {
                "claims": len(bundle["claims"]),
                "evidence_edges": sum(len(c["evidence"]) for c in bundle["claims"]),
                "unique_sources": len(srcs),
                "source_lock_posture": "documentary L1–L5 acceptance; no human L6 signatures asserted",
            }
    return result


def as_text(result):
    parts = [
        f"BISULFID Reference Explorer: {result['query']['mode']} {result['query']['value'] or ''}".strip(),
        "Status: internal staged reference | documentary checks only | not human peer review",
        "Rights: no public reuse or commercial license granted",
    ]
    if "summary" in result:
        parts.append(json.dumps(result["summary"], ensure_ascii=False, sort_keys=True))
    elif result["query"]["mode"] == "sources":
        for s in result["sources"]:
            parts.append(f"{s['source_id']} | {s['publisher']} | {len(s['claim_ids'])} claims")
    else:
        parts.append(f"Matches: {result['matched_claims']}")
        for claim in result["claims"]:
            parts.append(f"\n{claim['claim_id']}\n{claim['statement']}")
            for edge in claim["evidence"]:
                parts.append(f"  {edge['evidence_id']} -> {edge['source_id']} [{edge['publisher']}] {edge['source_url']}")
    return "\n".join(parts) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--term", metavar="TERM", help="Whole-word, case-insensitive term/phrase in claim text")
    modes.add_argument("--claim-id", metavar="ID", help="Exact claim ID")
    modes.add_argument("--source-id", metavar="ID", help="Find claims citing this source ID")
    modes.add_argument("--evidence-id", metavar="ID", help="Find claims bound to this evidence record")
    modes.add_argument("--sources", action="store_true", help="List sources and reverse evidence edges")
    modes.add_argument("--summary", action="store_true", help="Report verified pilot coverage and limits")
    parser.add_argument("--format", choices=["json", "text"], default="json")
    args = parser.parse_args(argv)
    mode = next((k for k in ("term", "claim_id", "source_id", "evidence_id")
                 if getattr(args, k) is not None), None)
    if mode is None:
        mode = "sources" if args.sources else "summary"
        value = None
    else:
        value = getattr(args, mode)
        mode = mode.replace("_", "-")
    try:
        result = search(load(), mode, value)
    except (ExplorerError, OSError, json.JSONDecodeError) as exc:
        parser.exit(2, f"REFERENCE EXPLORER REFUSED: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json" else as_text(result), end="" if args.format == "text" else "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
