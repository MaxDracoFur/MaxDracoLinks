"""tools/cover_check.py: every published post has a cover (Max 2026-11-12: "we need at least 1
image for the CD album like cover").

Requirements: a post that will publish (not draft, date not in the future) and is dated on or
after the rule (2026-11-12) needs `cover_image`, and that file must exist under assets/ or static/;
otherwise `check` exits 1. Older published posts without one are warned about, not refused.
Drafts are reported by `plan` and never fail it.
"""
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "cover_check.py")


class CoverGate(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.root, "content", "blog"))
        os.makedirs(os.path.join(self.root, "assets", "res", "covers"))
        open(os.path.join(self.root, "assets", "res", "covers", "ok.jpg"), "wb").write(b"x")

    def post(self, name, date, draft=False, cover=None):
        fm = f'---\ntitle: t\ndate: {date}\ndraft: {"true" if draft else "false"}\n'
        if cover is not None:
            fm += f'cover_image: "{cover}"\n'
        open(os.path.join(self.root, "content", "blog", name), "w").write(fm + "---\nbody\n")

    def run_tool(self, mode="check"):
        return subprocess.run([sys.executable, TOOL, mode, "--root", self.root, "--now", "2026-12-01"],
                              capture_output=True, text=True)

    def test_new_post_with_existing_cover_passes(self):
        self.post("a.md", "2026-11-20", cover="/res/covers/ok.jpg")
        self.assertEqual(self.run_tool().returncode, 0)

    def test_new_post_without_cover_refuses(self):
        self.post("a.md", "2026-11-20")
        r = self.run_tool()
        self.assertEqual(r.returncode, 1)
        self.assertIn("a.md", r.stderr)

    def test_cover_file_must_exist(self):
        self.post("a.md", "2026-11-20", cover="/res/covers/missing.jpg")
        r = self.run_tool()
        self.assertEqual(r.returncode, 1)
        self.assertIn("missing.jpg", r.stderr)

    def test_old_post_without_cover_only_warns(self):
        self.post("old.md", "2025-01-01")
        r = self.run_tool()
        self.assertEqual(r.returncode, 0)
        self.assertIn("old.md", r.stderr)

    def test_undated_published_post_is_legacy_and_only_warns(self):
        os.makedirs(os.path.join(self.root, "content", "blog"), exist_ok=True)
        open(os.path.join(self.root, "content", "blog", "u.md"), "w").write("---\ntitle: t\n---\nbody\n")
        r = self.run_tool()
        self.assertEqual(r.returncode, 0)
        self.assertIn("u.md", r.stderr)

    def test_drafts_and_future_posts_are_not_checked(self):
        self.post("d.md", "2026-11-20", draft=True)
        self.post("f.md", "2027-06-01")
        self.assertEqual(self.run_tool().returncode, 0)

    def test_plan_lists_drafts_without_failing(self):
        self.post("d.md", "2026-11-20", draft=True)
        r = self.run_tool("plan")
        self.assertEqual(r.returncode, 0)
        self.assertIn("d.md", r.stderr)


if __name__ == "__main__":
    unittest.main()
