"""tools/title_check.py: a post's title carries a phrase a reader would actually search for.

Why (Max 2026-11-12, after the Furby post went live): its title said exactly what the post shows
and drew readers from Telegram and direct links, but no search traffic at all in its first week
(measured 11-12: 17 human pageviews, 0 from a search engine). Nobody searches "Furby fan site
Mayan ruins"; they search "AdSense publisher ID". "Let's keep that in mind for the next post /
add it to the style/quality checks."

Requirements:
- A post that will publish (not draft, date not in the future), dated on or after 2026-11-13,
  sets `search_phrase` in front matter: the words a stranger would type to find it, 2 to 6 words.
- Its title contains that phrase (case, punctuation and extra spaces ignored).
- The title doesn't open like a listicle ("10 ... Tricks", "7 Ways ..."): the brand rule is no
  BuzzFeed hooks (memory feedback_maxdraco_brand_content).
- Older posts are untouched. `plan` lists drafts too and never fails.
"""
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "title_check.py")


class TitleCheck(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.root, "content", "blog"))

    def post(self, title, phrase=None, date="2026-11-20", draft=False, name="a.md"):
        fm = f'---\ntitle: "{title}"\ndate: {date}\ndraft: {"true" if draft else "false"}\n'
        if phrase is not None:
            fm += f'search_phrase: "{phrase}"\n'
        open(os.path.join(self.root, "content", "blog", name), "w").write(fm + "---\nbody\n")

    def run_tool(self, mode="check"):
        return subprocess.run([sys.executable, TOOL, mode, "--root", self.root, "--now", "2026-12-01"],
                              capture_output=True, text=True)

    def test_title_with_its_search_phrase_passes(self):
        self.post("One AdSense publisher ID, two unrelated sites", "AdSense publisher ID")
        self.assertEqual(self.run_tool().returncode, 0)

    def test_phrase_match_ignores_case_and_punctuation(self):
        self.post("Why your ads.txt file names who gets paid", "ads txt file")
        self.assertEqual(self.run_tool().returncode, 0)

    def test_missing_search_phrase_refuses(self):
        self.post("A Furby fan site, a Mayan ruins guide, and one ad account")
        r = self.run_tool()
        self.assertEqual(r.returncode, 1)
        self.assertIn("search_phrase", r.stdout)

    def test_title_without_the_phrase_refuses(self):
        self.post("A Furby fan site, a Mayan ruins guide, and one ad account", "AdSense publisher ID")
        r = self.run_tool()
        self.assertEqual(r.returncode, 1)
        self.assertIn("AdSense publisher ID", r.stdout)

    def test_phrase_must_be_two_to_six_words(self):
        for phrase in ("AdSense", "how to find every site that shares one AdSense publisher ID"):
            with self.subTest(phrase=phrase):
                self.setUp()
                self.post(f"x {phrase} x", phrase)
                self.assertEqual(self.run_tool().returncode, 1)

    def test_listicle_title_refuses(self):
        for title in ("10 Furry Furby AI Fanfic SEO Tricks", "7 Ways Your AdSense Publisher ID Leaks",
                      "Top 5 AdSense publisher ID lookups"):
            with self.subTest(title=title):
                self.setUp()
                self.post(title, "AdSense publisher ID" if "AdSense" in title else "Furby")
                r = self.run_tool()
                self.assertEqual(r.returncode, 1)
                self.assertIn("listicle", r.stdout)

    def test_number_in_title_is_fine_when_not_a_listicle(self):
        self.post("Two sites, one AdSense publisher ID, since 2025", "AdSense publisher ID")
        self.assertEqual(self.run_tool().returncode, 0)

    def test_post_before_rule_untouched(self):
        self.post("A Furby fan site, a Mayan ruins guide, and one ad account", date="2026-11-12T07:00:00-06:00")
        self.assertEqual(self.run_tool().returncode, 0)

    def test_undated_post_counts_as_before_the_rule(self):
        """Same as cover_check: an undated post was written before the rule (content/blog/1.md)."""
        fm = '---\ntitle: "old note"\ndraft: false\n---\nbody\n'
        open(os.path.join(self.root, "content", "blog", "1.md"), "w").write(fm)
        self.assertEqual(self.run_tool().returncode, 0)

    def test_draft_and_future_not_checked(self):
        self.post("no phrase here", draft=True, name="a.md")
        self.post("no phrase either", date="2027-01-01", name="b.md")
        self.assertEqual(self.run_tool().returncode, 0)

    def test_plan_lists_drafts_and_never_fails(self):
        self.post("no phrase here", draft=True)
        r = self.run_tool("plan")
        self.assertEqual(r.returncode, 0)
        self.assertIn("a.md", r.stdout)


if __name__ == "__main__":
    unittest.main()
