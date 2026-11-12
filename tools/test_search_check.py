"""Pins tools/search_check.py. Run: python3 -m unittest tools/test_search_check.py"""
import os
import sys
import unittest
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(__file__))
import search_check as S  # noqa: E402

NOW = datetime(2026, 11, 11, 23, tzinfo=timezone.utc)
HEAD = "path,slug,title,date,expiryDate,publishDate,draft,permalink,kind,section\n"
ZERO = "0001-01-01T00:00:00Z"


def row(path, url, draft="false", pub="2026-11-01T00:00:00Z", exp=ZERO):
    return f"{path},,T,{pub},{exp},{pub},{draft},https://maxdraco.com{url},page,blog\n"


class SearchCheck(unittest.TestCase):
    def hidden(self, *rows):
        return S.hidden_paths(HEAD + "".join(rows), NOW)

    def test_draft_future_expired_are_hidden(self):
        h = self.hidden(row("a.md", "/blog/a/", draft="true"),
                        row("b.md", "/blog/b/", pub="2027-02-08T00:00:00Z"),
                        row("c.md", "/blog/c/", exp="2026-01-01T00:00:00Z"),
                        row("d.md", "/blog/d/"))
        self.assertEqual(sorted(h), ["/blog/a/", "/blog/b/", "/blog/c/"])

    def test_leaked_draft_refused(self):
        h = self.hidden(row("x.md", "/blog/embargoed/", draft="true"))
        out = S.problems({"pages": [{"u": "/blog/embargoed/"}]}, h, lambda u: True)
        self.assertEqual(len(out), 1)
        self.assertIn("draft", out[0])

    def test_unbuilt_url_refused_and_clean_index_passes(self):
        self.assertTrue(S.problems({"pages": [{"u": "/gone/"}]}, {}, lambda u: False))
        self.assertEqual(S.problems({"pages": [{"u": "/blog/d/"}]}, {}, lambda u: True), [])


if __name__ == "__main__":
    unittest.main()
