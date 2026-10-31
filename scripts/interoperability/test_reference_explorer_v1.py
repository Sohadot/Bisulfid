#!/usr/bin/env python3
"""No-cost contract tests: the reference explorer must remain useful and fail closed."""
import copy
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reference_explorer_v1 as ex  # noqa: E402


class ReferenceExplorerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundle = ex.load()

    def test_summary_is_reproducible_and_not_a_public_api(self):
        r = ex.search(self.bundle, "summary")
        self.assertEqual(r["summary"]["claims"], 11)
        self.assertEqual(r["summary"]["evidence_edges"], 13)
        self.assertEqual(r["summary"]["unique_sources"], 11)
        self.assertEqual(r["publication"]["state"], "staged_not_public")
        self.assertFalse(r["publication"]["public_api_available"])
        self.assertEqual(r["rights"]["bundle_license"], "not_granted")

    def test_exact_word_distinguishes_bisulfide_from_bisulfite(self):
        self.assertTrue(ex.term_present("bisulfide", "bisulfide"))
        self.assertFalse(ex.term_present("bisulfide", "bisulfite"))
        self.assertFalse(ex.term_present("sulfid", "bisulfide"))
        self.assertFalse(ex.term_present("sulfid", "Bisulfid"))
        self.assertEqual(ex.search(self.bundle, "term", "bisulfite")["matched_claims"], 1)

    def test_german_terms_are_case_insensitive_and_unicode_safe(self):
        r = ex.search(self.bundle, "term", "HYDROGENSULFID")
        self.assertGreaterEqual(r["matched_claims"], 1)
        self.assertEqual(ex.normalize("Ｂｉｓｕｌｆｉｄ"), "bisulfid")

    def test_claim_id_exact_lookup(self):
        cid = self.bundle["claims"][0]["claim_id"]
        r = ex.search(self.bundle, "claim-id", cid)
        self.assertEqual(r["matched_claims"], 1)
        self.assertEqual(r["claims"][0]["claim_id"], cid)
        self.assertEqual(ex.search(self.bundle, "claim-id", cid.lower())["matched_claims"], 0)

    def test_source_reverse_lookup_preserves_provenance(self):
        sid = self.bundle["claims"][0]["evidence"][0]["source_id"]
        r = ex.search(self.bundle, "source-id", sid)
        self.assertGreaterEqual(r["matched_claims"], 1)
        self.assertTrue(any(e["source_id"] == sid for c in r["claims"] for e in c["evidence"]))
        self.assertFalse(r["verification"]["independent_human_peer_review"])

    def test_evidence_id_lookup(self):
        eid = self.bundle["claims"][0]["evidence"][0]["evidence_id"]
        r = ex.search(self.bundle, "evidence-id", eid)
        self.assertEqual(r["matched_claims"], 1)
        self.assertEqual(r["claims"][0]["evidence"][0]["evidence_id"], eid)

    def test_sources_are_deduplicated_and_sorted(self):
        r = ex.search(self.bundle, "sources")
        self.assertEqual(len(r["sources"]), 11)
        ids = [s["source_id"] for s in r["sources"]]
        self.assertEqual(ids, sorted(set(ids)))
        self.assertTrue(all(s["claim_ids"] and s["source_urls"] for s in r["sources"]))

    def test_unknown_term_or_source_yields_empty_noninvented_result(self):
        self.assertEqual(ex.search(self.bundle, "term", "never-specified-term")["claims"], [])
        self.assertEqual(ex.search(self.bundle, "source-id", "SRC-UNREGISTERED")["claims"], [])

    def test_text_and_machine_json_are_consistent(self):
        r = ex.search(self.bundle, "term", "bisulfite")
        self.assertIn("not human peer review", ex.as_text(r))
        self.assertIn(r["claims"][0]["claim_id"], ex.as_text(r))
        self.assertEqual(json.loads(json.dumps(r))["matched_claims"], 1)

    def test_cli_json_summary(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            status = ex.main(["--summary", "--format", "json"])
        self.assertEqual(status, 0)
        self.assertEqual(json.loads(buf.getvalue())["summary"]["claims"], 11)

    def test_cli_plain_text_term(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            status = ex.main(["--term", "bisulfide", "--format", "text"])
        self.assertEqual(status, 0)
        self.assertIn("staged reference", buf.getvalue())
        self.assertIn("CLM-TERM-BISULFIDE-EN-SENSE-001", buf.getvalue())

    def test_publisher_or_publication_tampering_blocks(self):
        b = copy.deepcopy(self.bundle)
        b["publication"]["public_api_available"] = True
        with self.assertRaises(ex.ExplorerError):
            ex.validate(b)
        b = copy.deepcopy(self.bundle)
        b["publisher"]["name"] = "Unsanctioned"
        with self.assertRaises(ex.ExplorerError):
            ex.validate(b)

    def test_unlicensed_third_party_extract_rejected(self):
        b = copy.deepcopy(self.bundle)
        b["claims"][0]["evidence"][0]["verbatim_or_fields"] = ["unlicensed source quote"]
        with self.assertRaises(ex.ExplorerError):
            ex.validate(b)

    def test_source_identity_and_retrieval_must_be_valid(self):
        b = copy.deepcopy(self.bundle)
        b["claims"][0]["evidence"][0]["source_url"] = "http://example.org/"
        with self.assertRaises(ex.ExplorerError):
            ex.validate(b)
        b = copy.deepcopy(self.bundle)
        b["claims"][0]["evidence"][0]["retrieved_on"] = "not-a-date"
        with self.assertRaises(ex.ExplorerError):
            ex.validate(b)

    def test_failing_documentary_check_rejected(self):
        b = copy.deepcopy(self.bundle)
        b["verification"]["checks"]["D7_risk"] = "fail"
        with self.assertRaises(ex.ExplorerError):
            ex.validate(b)

    def test_legacy_or_pending_claim_rejected(self):
        b = copy.deepcopy(self.bundle)
        b["claims"][0]["registry_status"] = "pending"
        with self.assertRaises(ex.ExplorerError):
            ex.validate(b)
        b = copy.deepcopy(self.bundle)
        b["claims"].append(copy.deepcopy(b["claims"][0]))
        with self.assertRaises(ex.ExplorerError):
            ex.validate(b)

    def test_no_mos2_claim_admission(self):
        b = copy.deepcopy(self.bundle)
        b["reference"]["knowledge_object_id"] = "KO-MOS2-SCIENTIFIC-001"
        with self.assertRaises(ex.ExplorerError):
            ex.validate(b)


if __name__ == "__main__":
    unittest.main(verbosity=2)
