"""The concept-sequencing rule, pinned. Run: python3 -m unittest tools/test_concepts.py"""

import os
import sys
import tempfile
import textwrap
import unittest
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
import concepts as C  # noqa: E402

NOW = datetime(2026, 11, 5, 12)
CONCEPTS = """
badgescope:
  what: the rig
  match: ['\\bbadgescope\\b']
"""


class Site:
    def __init__(self):
        self.dir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.dir, "content", "blog"))
        with open(os.path.join(self.dir, "concepts.yaml"), "w") as fh:
            fh.write(CONCEPTS)

    def post(self, name, body="", **fm):
        lines = ["---"] + [f"{k}: {v}" for k, v in fm.items()] + ["---", body]
        with open(os.path.join(self.dir, "content", "blog", name + ".md"), "w") as fh:
            fh.write("\n".join(lines))

    def problems(self, drafts=False):
        return C.check(C.load_posts(os.path.join(self.dir, "content", "blog")),
                       C.load_concepts(os.path.join(self.dir, "concepts.yaml")),
                       NOW, drafts=drafts)


class Rule(unittest.TestCase):
    def setUp(self):
        self.s = Site()

    def test_undeclared_jargon_is_refused(self):
        self.s.post("a", "I built badgescope.", date="2026-11-01")
        self.assertIn("without declaring", self.s.problems()["a.md"][0])

    def test_use_without_an_intro_is_refused(self):
        self.s.post("a", "badgescope again", date="2026-11-01", uses="[badgescope]")
        self.assertIn("no earlier published post", self.s.problems()["a.md"][0])

    def test_intro_must_be_earlier_not_same_time(self):
        self.s.post("intro", "badgescope is", date="2026-11-01", introduces="[badgescope]")
        self.s.post("later", "badgescope", date="2026-11-01", uses="[badgescope]")
        self.assertIn("later.md", self.s.problems())

    def test_earlier_published_intro_passes(self):
        self.s.post("intro", "badgescope is", date="2026-10-01", introduces="[badgescope]")
        self.s.post("later", "BadgeScope", date="2026-11-01", uses="[badgescope]")
        self.assertEqual(self.s.problems(), {})

    def test_a_draft_intro_does_not_count_for_publishing(self):
        self.s.post("intro", "badgescope is", date="2026-10-01",
                    introduces="[badgescope]", draft="true")
        self.s.post("later", "badgescope", date="2026-11-01", uses="[badgescope]")
        self.assertIn("later.md", self.s.problems())
        # ...but in plan mode the sequence is complete.
        self.assertEqual(self.s.problems(drafts=True), {})

    def test_future_dated_intro_does_not_count(self):
        self.s.post("intro", "badgescope is", date="2026-12-01", introduces="[badgescope]")
        self.s.post("later", "badgescope", date="2026-11-01", uses="[badgescope]")
        self.assertIn("later.md", self.s.problems())

    def test_drafts_are_not_checked_when_publishing(self):
        self.s.post("wip", "badgescope", date="2026-11-01", draft="true")
        self.assertEqual(self.s.problems(), {})

    def test_unknown_concept_is_refused(self):
        self.s.post("a", "x", date="2026-11-01", uses="[nope]")
        self.assertIn("not in concepts.yaml", self.s.problems()["a.md"][0])

    def test_toml_front_matter(self):
        with open(os.path.join(self.s.dir, "content", "blog", "t.md"), "w") as fh:
            fh.write("+++\ndate = '2026-11-01T00:00:00-05:00'\ndraft = false\n+++\nbadgescope\n")
        self.assertIn("t.md", self.s.problems())

    def test_cli_exit_codes(self):
        self.s.post("a", "badgescope", date="2026-11-01")
        self.assertEqual(C.main(["check", "--root", self.s.dir]), 1)
        self.assertEqual(C.main(["plan", "--root", self.s.dir]), 0)


if __name__ == "__main__":
    unittest.main()
