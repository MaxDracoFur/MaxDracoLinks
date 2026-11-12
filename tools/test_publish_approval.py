"""tools/publish_approval.py: a post publishes only with Max's own approval of that exact content
(Max 2026-11-12, after three hacker posts went live on an agent's reading of "3 today" and were
pulled the same morning: "yes, fix the gate").

Requirements:
- `check` refuses (exit 1) a post that will publish (not draft, date not in the future), dated on or
  after 2026-11-12, unless approvals.json holds an entry for its slug whose hashes match the post's
  content and its cover file now. Any edit to the text or the cover after approval voids it.
- The hash ignores `date` and `draft`, so scheduling an approved post doesn't void it.
- `review_status: approved` in front matter counts for nothing (an agent can write it).
- A post dated on or after 2026-11-13 also needs `cover_source: stage:<path>`: a photo of Max's
  exported by the stage app, not a made-up title card.
- `approve` refuses without a controlling terminal: an agent's shell has none, so it can't approve
  by piping "y" in. Max runs it himself.
- Older posts are untouched. Drafts never fail `check`.
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "publish_approval.py")
sys.path.insert(0, HERE)


class ApprovalGate(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.root, "content", "blog"))
        os.makedirs(os.path.join(self.root, "assets", "res", "covers"))
        self.cover = os.path.join(self.root, "assets", "res", "covers", "a.jpg")
        open(self.cover, "wb").write(b"photo-1")

    def post(self, date="2026-11-20", draft=False, body="body\n", source="stage:maxdraco-hack/2026-11-12/a.jpg",
             extra=""):
        fm = (f'---\ntitle: t\nslug: "a"\ndate: {date}\ndraft: {"true" if draft else "false"}\n'
              f'cover_image: "/res/covers/a.jpg"\n')
        if source:
            fm += f'cover_source: "{source}"\n'
        open(os.path.join(self.root, "content", "blog", "a.md"), "w").write(fm + extra + "---\n" + body)

    def approve_now(self):
        """Write the entry the way `approve` would, without the terminal step."""
        import publish_approval as pa
        pa.record(self.root, "a", via="test")

    def run_tool(self, *args):
        return subprocess.run([sys.executable, TOOL, *args, "--root", self.root, "--now", "2026-12-01"],
                              capture_output=True, text=True, stdin=subprocess.DEVNULL)

    def test_unapproved_published_post_refuses(self):
        self.post()
        r = self.run_tool("check")
        self.assertEqual(r.returncode, 1)
        self.assertIn("a.md", r.stderr)

    def test_approved_post_passes(self):
        self.post()
        self.approve_now()
        self.assertEqual(self.run_tool("check").returncode, 0)

    def test_frontmatter_review_status_is_not_approval(self):
        self.post(extra='review_status: "approved"\n')
        self.assertEqual(self.run_tool("check").returncode, 1)

    def test_text_edit_after_approval_voids_it(self):
        self.post()
        self.approve_now()
        self.post(body="body, edited after approval\n")
        self.assertEqual(self.run_tool("check").returncode, 1)

    def test_cover_swap_after_approval_voids_it(self):
        self.post()
        self.approve_now()
        open(self.cover, "wb").write(b"a different picture")
        self.assertEqual(self.run_tool("check").returncode, 1)

    def test_scheduling_does_not_void_approval(self):
        self.post(date="2027-01-01", draft=True)
        self.approve_now()
        self.post(date="2026-11-25", draft=False)
        self.assertEqual(self.run_tool("check").returncode, 0)

    def test_draft_never_fails(self):
        self.post(draft=True)
        self.assertEqual(self.run_tool("check").returncode, 0)

    def test_future_post_not_checked(self):
        self.post(date="2027-06-01")
        self.assertEqual(self.run_tool("check").returncode, 0)

    def test_post_before_rule_untouched(self):
        self.post(date="2026-10-01")
        self.assertEqual(self.run_tool("check").returncode, 0)

    def test_new_post_needs_stage_photo_cover(self):
        self.post(source="")
        self.approve_now()
        r = self.run_tool("check")
        self.assertEqual(r.returncode, 1)
        self.assertIn("cover_source", r.stderr)

    def test_created_cover_refused_from_photo_rule(self):
        self.post(source="created: title card")
        self.approve_now()
        self.assertEqual(self.run_tool("check").returncode, 1)

    def test_post_dated_11_12_keeps_created_cover(self):
        self.post(date="2026-11-12T07:00:00-06:00", source="")
        self.approve_now()
        self.assertEqual(self.run_tool("check").returncode, 0)

    def test_approve_refuses_without_terminal(self):
        self.post(draft=True)
        r = subprocess.run([sys.executable, TOOL, "approve", "a", "--root", self.root],
                           input="a\ny\n", capture_output=True, text=True, start_new_session=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("terminal", r.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.root, "approvals.json")))

    def test_approve_works_at_a_real_terminal(self):
        """Bug 2026-11-12: open('/dev/tty', 'r+') raises io.UnsupportedOperation ("not seekable",
        an OSError subclass) on a real macOS terminal, so `approve` told Max he had no terminal.
        Run it under a pseudo-terminal as its controlling terminal (what Terminal.app gives)."""
        import pty
        import time
        self.post(draft=True)
        pid, fd = pty.fork()
        if pid == 0:
            os.execv(sys.executable, [sys.executable, TOOL, "approve", "a", "--root", self.root])
        out, sent, deadline = b"", False, time.time() + 20
        while time.time() < deadline:
            try:
                chunk = os.read(fd, 4096)
            except OSError:
                break
            if not chunk:
                break
            out += chunk
            if not sent and b"Type the slug" in out:
                os.write(fd, b"a\n")
                sent = True
        _, status = os.waitpid(pid, 0)
        self.assertEqual(os.waitstatus_to_exitcode(status), 0, out.decode(errors="replace"))
        self.assertIn("a", json.load(open(os.path.join(self.root, "approvals.json"))))


if __name__ == "__main__":
    unittest.main()
