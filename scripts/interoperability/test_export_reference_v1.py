#!/usr/bin/env python3
"""Regression tests for the technology-neutral and non-public reference exchange pilot."""
import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import export_reference_v1 as exp  # noqa: E402


class ReferenceExchangeTests(unittest.TestCase):
    def setUp(self):
        self.dossier = exp.read("release/claim_dossiers/" + exp.KO_ID + ".json")
        self.registry = exp.read("knowledge_objects/knowledge_object_registry.json")
        self.evaluation = exp.read("release/documentary_verification/" + exp.KO_ID + ".json")
        self.claims = exp.read("claims/terminology_claims.json")
        self.acts = exp.read("release/owner_acts.json")

    def run_build(self, **changes):
        inputs = dict(dossier=copy.deepcopy(self.dossier),
                      registry=copy.deepcopy(self.registry),
                      evaluation=copy.deepcopy(self.evaluation),
                      claims_store=copy.deepcopy(self.claims),
                      owner_acts=copy.deepcopy(self.acts))
        inputs.update(changes)
        return exp.build(**inputs)

    def test_pilot_has_eleventraceable_claims_and_no_public_authority(self):
        p = self.run_build()
        self.assertEqual(len(p["claims"]), 11)
        self.assertEqual(sum(len(x["evidence"]) for x in p["claims"]), 13)
        self.assertEqual(p["publication"]["state"], "staged_not_public")
        self.assertFalse(p["publication"]["public_api_available"])
        self.assertFalse(p["publication"]["release_authorized"])
        self.assertFalse(p["publication"]["owner_claim_activation"])
        self.assertFalse(p["verification"]["independent_human_peer_review"])
        self.assertTrue(p["rights"]["no_republished_source_extracts"])
        self.assertTrue(p["exclusions"]["unverified_german_industry_usage"])

    def test_no_capture_bytes_or_source_verbatim_passages_are_redistributed(self):
        p = self.run_build()
        for claim in p["claims"]:
            self.assertEqual(claim["registry_status"], "approved_not_owner_activated")
            for e in claim["evidence"]:
                self.assertTrue(e["source_url"].startswith("https://"))
                self.assertNotIn("verbatim_or_fields", e)
                self.assertNotIn("capture", e)
                self.assertNotIn("source_fulltext", e)

    def test_unverified_or_unsupported_claim_is_rejected(self):
        c = copy.deepcopy(self.claims)
        next(x for x in c["claims"] if x["claim_id"] == self.dossier["claims"][0]["claim_id"])["status"] = "pending"
        with self.assertRaisesRegex(ValueError, "not approved"):
            self.run_build(claims_store=c)

    def test_claim_text_drift_is_rejected(self):
        d = copy.deepcopy(self.dossier)
        d["claims"][0]["statement"] += " UNSOURCED ADDITION"
        with self.assertRaisesRegex(ValueError, "differs"):
            self.run_build(dossier=d)

    def test_source_retrieval_must_have_an_admissible_https_locator(self):
        d = copy.deepcopy(self.dossier)
        d["claims"][0]["evidence"][0]["url"] = "http://example.org/unqualified"
        with self.assertRaisesRegex(ValueError, "invalid source URL"):
            self.run_build(dossier=d)

    def test_evidence_that_is_not_rendered_is_rejected(self):
        d = copy.deepcopy(self.dossier)
        d["claims"][0]["evidence"][0]["rendered_on_page"] = False
        with self.assertRaisesRegex(ValueError, "unqualified"):
            self.run_build(dossier=d)

    def test_evidence_binding_mismatch_is_rejected(self):
        d = copy.deepcopy(self.dossier)
        d["claims"][0]["evidence"][0]["evidence_id"] = "EVD-FAKE"
        with self.assertRaisesRegex(ValueError, "bindings differ"):
            self.run_build(dossier=d)

    def test_failed_documentary_qualification_never_exports(self):
        e = copy.deepcopy(self.evaluation)
        e["checks"]["D7_risk"] = "fail"
        with self.assertRaisesRegex(ValueError, "D1–D7"):
            self.run_build(evaluation=e)

    def test_other_knowledge_object_not_exported(self):
        d = copy.deepcopy(self.dossier)
        d["knowledge_object_id"] = "KO-MOS2-SCIENTIFIC-001"
        with self.assertRaisesRegex(ValueError, "mismatched"):
            self.run_build(dossier=d)

    def test_changed_owner_acts_force_release_reassessment(self):
        acts = copy.deepcopy(self.acts)
        acts["claim_activations"].append({"fake": "fixture"})
        with self.assertRaisesRegex(ValueError, "owner acts"):
            self.run_build(owner_acts=acts)

    def test_generated_file_is_bit_for_bit_reproducible(self):
        data = exp.serialize(self.run_build())
        self.assertTrue(exp.OUTPUT.is_file())
        self.assertEqual(exp.OUTPUT.read_text(encoding="utf-8"), data)
        parsed = json.loads(data)
        self.assertEqual(parsed["publisher"]["name"], "Sohadot")


if __name__ == "__main__":
    unittest.main(verbosity=2)
