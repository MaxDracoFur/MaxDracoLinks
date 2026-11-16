"""tools/jargon_check.py: posts are written in plain words, for someone outside the field.

Max, 2026-11-15, after killing the venue-licence post: "can we have a no jargon rule". That post
said "(my account)" at a reader who had never been told what the label meant, called a sentence of
ordinance "the trap", and sold itself as "the two-minute check".

Three things this can check mechanically. The fourth and biggest one -- is this written for someone
who doesn't already know? -- is a judgement, and stays a person's job.

1. EVIDENCE LABELS belong to the hacker INC posts, where the format explains them. Anywhere else
   "(measured 11-05)", "(inferred)", "(my account)" are our shorthand leaking at a reader.
2. OUR OWN PROCESS WORDS never belong in a post at all: lane test, INC format, front matter,
   cover_source, the rotation, copy review. They are how the site is made, not what it says.
3. HYPE HEADINGS: "The trap in ...", "The two-minute check", "What nobody tells you". A heading
   states what the section shows, or it instructs. It does not sell.

Warn-level by design: the wording is always Max's, so this flags and never blocks.
"""
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "jargon_check.py")


class JargonCheck(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.root, "content", "blog"))

    def post(self, body, series="cds", name="a.md", draft=False):
        fm = f'---\ntitle: "t"\ndate: 2026-11-20\ndraft: {"true" if draft else "false"}\nseries: "{series}"\n---\n'
        open(os.path.join(self.root, "content", "blog", name), "w").write(fm + body)

    def run_tool(self, mode="check"):
        return subprocess.run([sys.executable, TOOL, mode, "--root", self.root, "--now", "2026-12-01"],
                              capture_output=True, text=True)

    def flags(self, body, **kw):
        self.post(body, **kw)
        return self.run_tool().stdout

    # 1. evidence labels
    def test_evidence_labels_are_flagged_outside_hacker_posts(self):
        for label in ("*(measured 11-05)*", "*(inferred)*", "*(my account)*", "*(from my notes)*"):
            with self.subTest(label=label):
                self.setUp()
                self.assertIn("evidence label", self.flags(f"The disc is round. {label}"))

    def test_evidence_labels_are_fine_in_a_hacker_post(self):
        self.assertNotIn("evidence label", self.flags("Two sites share an ID. *(measured 11-05)*",
                                                      series="hacker"))

    # 2. our own process words
    def test_process_words_are_flagged_in_any_post(self):
        for word in ("the lane test", "INC format", "front matter", "cover_source", "copy review"):
            with self.subTest(word=word):
                self.setUp()
                self.assertIn("our own word", self.flags(f"This post passes {word} easily.",
                                                         series="hacker"))

    # 3. hype headings
    def test_hype_headings_are_flagged(self):
        for head in ("## The trap in the capacity test",
                     "## The two-minute check",
                     "## What nobody tells you about discs",
                     "## The secret to grading"):
            with self.subTest(head=head):
                self.setUp()
                self.assertIn("heading sells", self.flags(head + "\n\nBody."))

    def test_a_plain_heading_passes(self):
        out = self.flags("## Take two minutes to check before you book\n\nBody.")
        self.assertNotIn("heading sells", out)

    def test_a_plain_post_is_clean(self):
        out = self.flags("I looked the venue up before booking it. Here is how, and what it misses.")
        self.assertEqual(out.strip().splitlines()[-1].strip().endswith("plain words"), True, out)

    # behaviour
    def test_it_warns_and_never_blocks(self):
        self.post("Rubbish. *(my account)*")
        r = self.run_tool()
        self.assertEqual(r.returncode, 0, "jargon is a warning: the wording is Max's")

    def test_plan_covers_drafts_too(self):
        self.post("A draft. *(my account)*", draft=True)
        self.assertIn("evidence label", self.run_tool("plan").stdout)

    def test_check_ignores_drafts(self):
        self.post("A draft. *(my account)*", draft=True)
        self.assertNotIn("evidence label", self.run_tool("check").stdout)


if __name__ == "__main__":
    unittest.main()
