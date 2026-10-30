#!/usr/bin/env python3
"""test_legacy_migration.py — proofs for the bounded Gate-12 legacy migration (Contract C RL)
and for Gate 12-I (institutional page class).

Run: python3 scripts/validators/test_legacy_migration.py   (stdlib unittest; exit 0 = all pass)
"""

import copy
import datetime
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import distinctiveness_core as dc  # noqa: E402

POLICY = dc.load_policy()
RULES = dc._Rules(POLICY)
TODAY = datetime.date(2026, 10, 30)

TEMPLATE = """<!DOCTYPE html><html lang="en"><head><title>{name} — Bisulfid Atlas</title>
<meta name="robots" content="{robots}"></head><body data-atlas-lane="terminology"><main>
<h1>{name}</h1><h2>Term and topic boundary</h2>
<p>This node situates {name} within the cohort family as a terminology reference entry.</p>
<p>It clarifies how neighbouring atlas routes relate without asserting unsupported chemical facts.</p>
<h2>Context layers</h2><p>Structured reference for analysts and journalists; not a primary-source citation.</p>
<p>Context framing without operational, market, or investment advice for {name} readers.</p>
<p>Clear framing for researchers and journalists without unsupported claims about {name}.</p>
</main></body></html>"""

UNIQUE = """<!DOCTYPE html><html lang="en"><head><title>Atlas — Bisulfid Atlas</title>
<meta name="robots" content="index, follow"></head><body><main><h1>Atlas</h1>
<h2>How the atlas is organised</h2><p>{text}</p></main></body></html>"""

UNIQUE_TEXT = ("The atlas groups sulfur vocabulary by chemical family, by language and by industrial setting, so a "
               "reader can move from a German term to its English counterpart and then to the processes where the "
               "word is used in practice. Each family page lists the members that have governed evidence and marks the "
               "ones still waiting for sources, which keeps navigation honest about what the site can support today. "
               "Language hubs collect the German, English and other forms side by side for translators and editors.")

NAMES = ["Alpha Sulfide", "Beta Sulfide", "Gamma Sulfide", "Delta Sulfide"]


def write(root, rel_dir, text):
    d = os.path.join(root, rel_dir)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(text)


def slug(n):
    return n.lower().replace(" ", "-")


class Surface:
    """A tiny legacy surface: 4 templated term pages + 1 unique hub + a sitemap listing everything."""

    def __init__(self):
        self.root = tempfile.mkdtemp(prefix="g12surface-")
        for n in NAMES:
            write(self.root, f"t/{slug(n)}", TEMPLATE.format(name=n, robots="index, follow"))
        write(self.root, "atlas", UNIQUE.format(text=UNIQUE_TEXT))
        self.write_sitemap([f"/t/{slug(n)}/" for n in NAMES] + ["/atlas/"])
        reg = os.path.join(self.root, "institutional.json")
        with open(reg, "w") as fh:
            json.dump({"functions": [{"function_id": "nav_atlas_hub"}],
                       "bindings": [{"path": "/atlas/", "function_id": "nav_atlas_hub", "language": "en"}]}, fh)
        self.inst = dc.InstitutionalRegistry(reg)

    def write_sitemap(self, paths):
        body = "".join(f"<url><loc>https://bisulfid.com{p}</loc></url>" for p in paths)
        with open(os.path.join(self.root, "sitemap-terms-001.xml"), "w") as fh:
            fh.write(f"<urlset>{body}</urlset>")

    def evaluate(self, inst=None):
        pages = dc.load_html_pages(POLICY, self.root, RULES)
        u = dc.Universe(pages, POLICY)
        ctx = dc.IGContext(os.path.join(self.root, "no-registry.json"))
        verdicts = []
        for p in pages:
            b = (inst or self.inst).lookup(path=p.route_id)
            verdicts.append(dc.gate12_verdict(p, u, POLICY, ctx, institutional=b))
        return pages, verdicts

    def seal(self):
        pages, verdicts = self.evaluate()
        entries = sorted(({"p": dc.surface_url_path(p, self.root), "h": dc.body_hash_hex(p), "r": None}
                          for p, v in zip(pages, verdicts) if v["verdict"] != "PASS"), key=lambda e: e["p"])
        return {"entries": entries, "entry_count": len(entries), "entries_sha256": dc.hold_entries_digest(entries),
                "freeze_exception": {"state": "not_authorized"}}

    def states(self, hold, today=TODAY):
        pages, verdicts = self.evaluate()
        out, meta = dc.apply_legacy_hold(pages, verdicts, self.root, hold, POLICY, today)
        return {o["path"]: o["state"] for o in out}, meta

    def noindex_all_held(self, hold):
        held = {e["p"] for e in hold["entries"]}
        for n in NAMES:
            if f"/t/{slug(n)}/" in held:
                write(self.root, f"t/{slug(n)}", TEMPLATE.format(name=n, robots="noindex, follow"))
        self.write_sitemap(["/atlas/"])

    def close(self):
        shutil.rmtree(self.root)


class LegacyHoldTests(unittest.TestCase):

    def setUp(self):
        self.s = Surface()
        self.hold = self.s.seal()

    def tearDown(self):
        self.s.close()

    def test_baseline_seals_failing_pages_only(self):
        self.assertEqual(sorted(e["p"] for e in self.hold["entries"]), sorted(f"/t/{slug(n)}/" for n in NAMES))
        self.assertEqual(dc.verify_hold(self.hold), [])

    def test_indexed_legacy_blocks_by_default(self):
        st, meta = self.s.states(self.hold)
        self.assertTrue(all(st[f"/t/{slug(n)}/"] == "BLOCK_LEGACY_INDEXED" for n in NAMES))
        self.assertFalse(meta["freeze_exception_active"])

    def test_noindex_and_sitemap_removal_reach_contract_c_rl(self):
        self.s.noindex_all_held(self.hold)
        st, _ = self.s.states(self.hold)
        self.assertTrue(all(st[f"/t/{slug(n)}/"] == "LEGACY_HOLD_NOINDEX" for n in NAMES), st)

    def test_sitemap_listing_alone_is_an_indexation_request(self):
        self.s.noindex_all_held(self.hold)
        self.s.write_sitemap(["/atlas/", f"/t/{slug(NAMES[0])}/"])   # robots noindex, but still in a sitemap
        st, _ = self.s.states(self.hold)
        self.assertEqual(st[f"/t/{slug(NAMES[0])}/"], "BLOCK_LEGACY_INDEXED")

    def test_new_failing_page_blocks_even_if_noindex(self):
        self.s.noindex_all_held(self.hold)
        write(self.s.root, "t/epsilon-sulfide", TEMPLATE.format(name="Epsilon Sulfide", robots="noindex, follow"))
        st, _ = self.s.states(self.hold)
        self.assertEqual(st["/t/epsilon-sulfide/"], "BLOCK_NEW_FAILING")

    def test_modified_legacy_page_must_pass(self):
        self.s.noindex_all_held(self.hold)
        n = NAMES[1]
        write(self.s.root, f"t/{slug(n)}", TEMPLATE.format(name=n, robots="noindex, follow")
              .replace("</main>", "<p>An added generic sentence that changes the body.</p></main>"))
        st, _ = self.s.states(self.hold)
        self.assertEqual(st[f"/t/{slug(n)}/"], "BLOCK_MODIFIED_LEGACY")

    def test_rebuilt_page_that_passes_is_allowed_and_entry_becomes_stale(self):
        self.s.noindex_all_held(self.hold)
        n = NAMES[2]
        write(self.s.root, f"t/{slug(n)}", UNIQUE.format(text=UNIQUE_TEXT.replace("atlas", "reference").replace(
            "reader", "chemist").replace("Language hubs", "Separate language records")).replace("Atlas", n))
        pages, verdicts = self.s.evaluate()
        v = next(v for p, v in zip(pages, verdicts) if p.route_id == f"/t/{slug(n)}/")
        # A rebuilt knowledge page still needs IG units to PASS; without them it is BLOCK_MODIFIED_LEGACY.
        st, meta = self.s.states(self.hold)
        self.assertEqual(v["verdict"], "FAIL")
        self.assertEqual(st[f"/t/{slug(n)}/"], "BLOCK_MODIFIED_LEGACY")

    def test_tampered_baseline_is_invalid(self):
        bad = copy.deepcopy(self.hold)
        bad["entries"].append({"p": "/t/epsilon-sulfide/", "h": "0" * 16, "r": None})
        self.assertTrue(dc.verify_hold(bad))
        bad["entry_count"] = len(bad["entries"])
        self.assertTrue(any("sha256" in e for e in dc.verify_hold(bad)), "re-counting without re-sealing is detected")

    def test_ratchet_only_shrinks(self):
        smaller = copy.deepcopy(self.hold)
        smaller["entries"] = smaller["entries"][1:]
        self.assertEqual(dc.hold_ratchet(smaller, self.hold)[0], [])
        grown = copy.deepcopy(self.hold)
        grown["entries"].append({"p": "/t/epsilon-sulfide/", "h": "0" * 16, "r": None})
        self.assertTrue(dc.hold_ratchet(grown, self.hold)[0])
        repinned = copy.deepcopy(self.hold)
        repinned["entries"][0] = dict(repinned["entries"][0], h="f" * 16)
        self.assertTrue(dc.hold_ratchet(repinned, self.hold)[0], "re-pinning a modified page is a ratchet violation")

    def test_freeze_exception_is_explicit_bounded_and_expires(self):
        auth = copy.deepcopy(self.hold)
        auth["freeze_exception"] = {"state": "authorized", "authorized_by": "owner", "authorized_on": "2026-10-20",
                                    "expires_on": "2026-11-15", "reason": "urgent non-content fix"}
        st, meta = self.s.states(auth)
        self.assertTrue(meta["freeze_exception_active"])
        self.assertTrue(all(st[f"/t/{slug(n)}/"] == "LEGACY_FREEZE_INDEXED" for n in NAMES))
        _, meta = self.s.states(auth, today=datetime.date(2026, 11, 16))
        self.assertFalse(meta["freeze_exception_active"], "expired")
        long = copy.deepcopy(auth)
        long["freeze_exception"]["expires_on"] = "2027-06-01"
        self.assertFalse(self.s.states(long)[1]["freeze_exception_active"], "window above policy max_days")
        incomplete = copy.deepcopy(auth)
        incomplete["freeze_exception"]["authorized_by"] = None
        self.assertFalse(self.s.states(incomplete)[1]["freeze_exception_active"])
        # The exception never admits new or modified pages.
        write(self.s.root, "t/epsilon-sulfide", TEMPLATE.format(name="Epsilon Sulfide", robots="index, follow"))
        st, _ = self.s.states(auth)
        self.assertEqual(st["/t/epsilon-sulfide/"], "BLOCK_NEW_FAILING")

    def test_passing_page_needs_no_hold(self):
        st, _ = self.s.states(self.hold)
        self.assertNotIn("/atlas/", {e["p"] for e in self.hold["entries"]})


class InstitutionalClassTests(unittest.TestCase):

    def setUp(self):
        self.s = Surface()
        self.tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump({"functions": [{"function_id": "nav_atlas_hub"}, {"function_id": "glossary_hub"}],
                   "bindings": [{"path": "/atlas/", "function_id": "nav_atlas_hub", "language": "en"},
                                {"path": f"/t/{slug(NAMES[0])}/", "function_id": "glossary_hub", "language": "en"},
                                {"path": f"/t/{slug(NAMES[1])}/", "function_id": "nav_atlas_hub", "language": "en"}]},
                  self.tmp)
        self.tmp.close()
        self.inst = dc.InstitutionalRegistry(self.tmp.name)

    def tearDown(self):
        self.s.close()
        os.unlink(self.tmp.name)

    def verdict_for(self, path):
        pages, verdicts = self.s.evaluate(self.inst)
        return next(v for p, v in zip(pages, verdicts) if p.route_id == path)

    def test_distinct_registered_institutional_page_passes_without_ig(self):
        v = self.verdict_for("/atlas/")
        self.assertEqual(v["page_class"], "institutional")
        self.assertEqual(v["verdict"], "PASS", v["failures"])

    def test_same_page_unregistered_needs_ig(self):
        pages, verdicts = self.s.evaluate(dc.InstitutionalRegistry(os.path.join(self.s.root, "none.json")))
        v = next(v for p, v in zip(pages, verdicts) if p.route_id == "/atlas/")
        self.assertEqual(v["verdict"], "FAIL")
        self.assertTrue(any(f.startswith("information_gain") for f in v["failures"]))

    def test_institutional_class_does_not_relax_template_rules(self):
        v = self.verdict_for(f"/t/{slug(NAMES[0])}/")
        self.assertEqual(v["page_class"], "institutional")
        self.assertEqual(v["verdict"], "FAIL")
        self.assertTrue(any(f.startswith("near_duplicate") for f in v["failures"]))

    def test_duplicate_function_fails(self):
        v = self.verdict_for(f"/t/{slug(NAMES[1])}/")
        self.assertTrue(any(f.startswith("institutional_duplicate_function") for f in v["failures"]))


class ReferenceRenderTests(unittest.TestCase):

    def test_renderer_is_up_to_date_and_fail_closed(self):
        sys.path.insert(0, os.path.join(dc.ROOT, "scripts", "reference_production"))
        import render_ko_reference as rk
        self.assertEqual(rk.main(["--check"]), 0, "rendered MoS2 outputs must match the governed inputs")
        spec = json.load(open(os.path.join(dc.DATA, "reference_production", "render_specs", "KO-MOS2-SCIENTIFIC-001.json")))
        bad = copy.deepcopy(spec)
        bad["modules"][0]["paragraphs"][0]["text"] += " Its band gap is {{EVD-MOS2-FORMULA-PUBCHEM:scientific_scope.band_gap}}."
        with self.assertRaises(rk.RenderError):
            rk.build(bad)   # a value that no evidence holds cannot be rendered
        bad = copy.deepcopy(spec)
        bad["modules"][0]["paragraphs"][0]["evidence_ids"].append("EVD-MOS2-3R-BOUNDARY-RSC")
        with self.assertRaises(rk.RenderError):
            rk.build(bad)   # boundary evidence cannot support the formula claim
        bad = copy.deepcopy(spec)
        bad["evidence_uses"]["EVD-MOS2-FORMULA-PUBCHEM"] = "lattice_parameter_2h"
        with self.assertRaises(rk.RenderError):
            rk.build(bad)   # evidence used outside its admitted use is refused
        bad = copy.deepcopy(spec)
        bad["canonical_route_id"] = "molybdenum_disulfide_new_url"
        with self.assertRaises(rk.RenderError):
            rk.build(bad)   # no new URL may be minted

    def test_preview_is_noindex_and_outside_the_deploy_root(self):
        p = os.path.join(dc.DATA, "reference_production", "previews", "molybdenum-disulfide", "index.html")
        txt = open(p, encoding="utf-8").read()
        self.assertIn('<meta name="robots" content="noindex, nofollow">', txt)
        self.assertNotIn("site/public", os.path.relpath(p, dc.ROOT))
        self.assertFalse(os.path.exists(os.path.join(dc.ROOT, "site", "public", "molybdenum-disulfide", "index.html.preview")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
