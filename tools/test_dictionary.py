"""The Max dictionary rule, pinned. Run: python3 -m unittest tools/test_dictionary.py"""

import os
import sys
import tempfile
import unittest
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
import dictionary as D  # noqa: E402

NOW = datetime(2026, 11, 11, 12)
TERM = """---
title: "OPNsense"
term_kind: tool
summary: "Firewall software."
match: ['\\bOPNsense\\b']
topics: [networking]
sources:
  - {title: "OPNsense", url: "https://opnsense.org/", primary: true}
draft: %s
---
OPNsense is a firewall.
"""


class Site:
    def __init__(self, term_draft="false"):
        self.dir = tempfile.mkdtemp()
        for d in ("blog", "dictionary"):
            os.makedirs(os.path.join(self.dir, "content", d))
        os.makedirs(os.path.join(self.dir, "content", "dictionary", "topics"))
        self.topic("networking")
        self.term("opnsense", TERM % term_draft)

    def topic(self, slug, draft="false", body="How machines talk to each other."):
        with open(os.path.join(self.dir, "content", "dictionary", "topics", slug + ".md"), "w") as fh:
            fh.write(f"---\ntitle: {slug.title()}\ndraft: {draft}\n---\n{body}\n")

    def term(self, slug, text):
        with open(os.path.join(self.dir, "content", "dictionary", slug + ".md"), "w") as fh:
            fh.write(text)

    def post(self, name, body="", **fm):
        fm.setdefault("date", "2026-11-01")
        lines = ["---"] + [f"{k}: {v}" for k, v in fm.items()] + ["---", body]
        with open(os.path.join(self.dir, "content", "blog", name + ".md"), "w") as fh:
            fh.write("\n".join(lines))

    def problems(self, publish=True):
        terms = D.load_terms(os.path.join(self.dir, "content", "dictionary"))
        posts = D.load_posts(os.path.join(self.dir, "content", "blog"))
        topics = D.load_topics(os.path.join(self.dir, "content", "dictionary"))
        return D.check(posts, terms, NOW, publish, topics=topics)


class Posts(unittest.TestCase):
    def test_unlinked_mention_refused(self):
        s = Site()
        s.post("p", "My OPNsense box.")
        _, posts = s.problems()
        self.assertIn("without linking", posts["p.md"][0])

    def test_shortcode_first_mention_passes(self):
        s = Site()
        s.post("p", 'My {{< term "opnsense" >}} box. OPNsense again, unlinked, is fine.')
        self.assertEqual(s.problems(), ({}, {}))

    def test_shortcode_with_own_text(self):
        s = Site()
        s.post("p", 'My {{< term "opnsense" "firewall OS" >}}. Later OPNsense.')
        self.assertEqual(s.problems(), ({}, {}))

    def test_markdown_link_counts(self):
        s = Site()
        s.post("p", "My [OPNsense](/dictionary/opnsense/) box.")
        self.assertEqual(s.problems(), ({}, {}))

    def test_first_mention_must_be_the_link(self):
        s = Site()
        s.post("p", 'OPNsense first.\n\nThen {{< term "opnsense" >}}.')
        _, posts = s.problems()
        self.assertIn("first mention", posts["p.md"][0])

    def test_code_urls_headings_comments_ignored(self):
        s = Site()
        s.post("p", "## OPNsense heading\n\n`opnsense` and https://opnsense.org/x\n\n"
                    "```\nOPNsense log\n```\n<!-- OPNsense -->\n[docs](https://docs.opnsense.org/)")
        self.assertEqual(s.problems(), ({}, {}))

    def test_link_to_missing_page_refused(self):
        s = Site()
        s.post("p", '{{< term "pfsense" >}}')
        _, posts = s.problems()
        self.assertIn("has no page", posts["p.md"][0])

    def test_link_to_draft_page_refused_when_publishing(self):
        s = Site(term_draft="true")
        s.post("p", 'My {{< term "opnsense" >}} box.')
        _, posts = s.problems(publish=True)
        self.assertIn("still a draft", posts["p.md"][0])
        _, posts = s.problems(publish=False)
        self.assertEqual(posts, {})

    def test_draft_posts_only_checked_in_plan(self):
        s = Site()
        s.post("p", "OPNsense", draft="true")
        self.assertEqual(s.problems(publish=True), ({}, {}))
        self.assertIn("p.md", s.problems(publish=False)[1])

    def test_future_post_not_checked_when_publishing(self):
        s = Site()
        s.post("p", "OPNsense", date="2027-02-08")
        self.assertEqual(s.problems(publish=True), ({}, {}))


class Pages(unittest.TestCase):
    def test_primary_source_first(self):
        s = Site()
        s.term("x", TERM.replace("primary: true", "primary: false") % "false")
        pages, _ = s.problems()
        self.assertTrue(any("primary" in p for p in pages["x.md"]))

    def test_http_source_refused(self):
        s = Site()
        s.term("x", (TERM % "false").replace("https://opnsense.org/", "http://opnsense.org/"))
        self.assertTrue(any("not https" in p for p in s.problems()[0]["x.md"]))

    def test_lookaround_refused_for_re2(self):
        s = Site()
        s.term("x", (TERM % "false").replace("\\bOPNsense\\b", "OPN(?=sense)"))
        self.assertTrue(any("RE2" in p for p in s.problems()[0]["x.md"]))

    def test_draft_page_not_validated_when_publishing(self):
        s = Site()
        s.term("x", "---\ntitle: x\ndraft: true\n---\n")
        self.assertEqual(s.problems(publish=True)[0], {})
        self.assertIn("x.md", s.problems(publish=False)[0])

    def test_published_term_under_draft_index_refused(self):
        s = Site()
        terms = D.load_terms(os.path.join(s.dir, "content", "dictionary"))
        pages, _ = D.check([], terms, NOW, True, index_draft=True)
        self.assertIn("_index.md", pages)

    def test_seed_pages_are_valid(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        terms = D.load_terms(os.path.join(root, "content", "dictionary"))
        for t in terms.values():
            self.assertEqual(D.page_problems(t, D.load_topics(os.path.join(root, "content", "dictionary")), terms),
                             [], t["file"])


class Sources(unittest.TestCase):
    def test_sources_doc_marks_primary(self):
        s = Site()
        doc = D.sources_doc(D.load_terms(os.path.join(s.dir, "content", "dictionary")))
        self.assertEqual(doc["sources"], [{"url": "https://opnsense.org/", "term": "opnsense",
                                           "title": "OPNsense", "primary": True}])

    def test_classification_urls_are_checked_too(self):
        s = Site()
        s.term("tls", TLS % ("https://attack.mitre.org/techniques/T1557/"))
        doc = D.sources_doc(D.load_terms(os.path.join(s.dir, "content", "dictionary")))
        row = [r for r in doc["sources"] if r["term"] == "tls" and not r["primary"]][0]
        self.assertEqual((row["url"], row["standard"], row["clause"]),
                         ("https://attack.mitre.org/techniques/T1557/", "attack", "T1557"))


TLS = """---
title: "TLS"
term_kind: protocol
summary: "Encryption in transit."
match: ['\\bTLS\\b']
topics: [networking]
sources:
  - {title: "RFC 8446", url: "https://www.rfc-editor.org/rfc/rfc8446", primary: true}
classification:
  - {standard: attack, clause: T1557, topic: Adversary-in-the-Middle, url: "%s"}
draft: true
---
TLS encrypts connections.
"""


class Classification(unittest.TestCase):
    def problems(self, entry, body="TLS encrypts connections."):
        s = Site()
        text = TLS.replace("  - {standard: attack, clause: T1557, topic: Adversary-in-the-Middle, url: \"%s\"}",
                           entry).replace("TLS encrypts connections.", body)
        s.term("tls", text)
        return D.page_problems(D.load_terms(os.path.join(s.dir, "content", "dictionary"))["tls"])

    def test_canonical_urls_pass(self):
        for e in ['  - {standard: attack, clause: T1557, topic: x, url: "https://attack.mitre.org/techniques/T1557/"}',
                  '  - {standard: attack, clause: T1686.002, topic: x, url: "https://attack.mitre.org/techniques/T1686/002/"}',
                  '  - {standard: attack, clause: M1037, topic: x, url: "https://attack.mitre.org/mitigations/M1037/"}',
                  '  - {standard: cwe, clause: CWE-319, topic: x, url: "https://cwe.mitre.org/data/definitions/319.html"}',
                  '  - {standard: capec, clause: CAPEC-94, topic: x, url: "https://capec.mitre.org/data/definitions/94.html"}',
                  '  - {standard: cpe, clause: "cpe:2.3:a:grafana:loki", topic: x, url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Agrafana%3Aloki"}',
                  '  - {standard: sp800-53, clause: AU-6(3), topic: x, url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AU-06(03)"}']:
            self.assertEqual(self.problems(e), [], e)

    def test_wrong_url_unknown_standard_bad_id(self):
        self.assertIn("url should be", self.problems(
            '  - {standard: cwe, clause: CWE-319, topic: x, url: "https://example.com/319"}')[0])
        self.assertIn("is not one of", self.problems(
            '  - {standard: owasp, clause: A01, topic: x, url: "https://owasp.org/"}')[0])
        self.assertIn("not a valid", self.problems(
            '  - {standard: attack, clause: T15, topic: x, url: "https://attack.mitre.org/"}')[0])
        self.assertIn("needs", self.problems('  - {standard: attack, clause: T1557}')[0])

    def test_no_why_section(self):
        self.assertTrue(any("Why it's on this site" in p for p in self.problems(
            '  - {standard: attack, clause: T1557, topic: x, url: "https://attack.mitre.org/techniques/T1557/"}',
            body="TLS encrypts.\n\n## Why it's on this site\n\nBecause.")))


class Taxonomy(unittest.TestCase):
    def test_kind_must_be_in_vocabulary(self):
        s = Site()
        s.term("x", (TERM % "false").replace("term_kind: tool", "term_kind: technology"))
        self.assertTrue(any("term_kind" in p for p in s.problems()[0]["x.md"]))

    def test_term_needs_a_topic(self):
        s = Site()
        s.term("x", (TERM % "false").replace("topics: [networking]\n", ""))
        self.assertTrue(any("topics" in p for p in s.problems()[0]["x.md"]))

    def test_unknown_topic_refused(self):
        s = Site()
        s.term("x", (TERM % "false").replace("[networking]", "[networking, cooking]"))
        self.assertTrue(any("cooking" in p for p in s.problems()[0]["x.md"]))

    def test_published_term_under_draft_topic_refused(self):
        s = Site()
        s.topic("networking", draft="true")
        self.assertTrue(any("draft" in p for p in s.problems()[0]["opnsense.md"]))
        self.assertNotIn("opnsense.md", s.problems(publish=False)[0])

    def test_see_also_must_exist_and_not_be_self_or_draft(self):
        s = Site()
        s.term("x", (TERM % "false").replace("topics: [networking]", "topics: [networking]\nsee_also: [nope, x]"))
        out = s.problems()[0]["x.md"]
        self.assertTrue(any("nope" in p for p in out))
        self.assertTrue(any("itself" in p for p in out))
        s.term("y", TERM % "true")
        s.term("x", (TERM % "false").replace("topics: [networking]", "topics: [networking]\nsee_also: [y]"))
        self.assertTrue(any("draft" in p for p in s.problems()[0]["x.md"]))

    def test_topic_page_needs_a_description(self):
        s = Site()
        s.topic("networking", body="")
        self.assertIn("topics/networking.md", s.problems()[0])

    def test_seed_topics_are_valid(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        d = os.path.join(root, "content", "dictionary")
        topics, terms = D.load_topics(d), D.load_terms(d)
        self.assertTrue(topics)
        for t in terms.values():
            self.assertEqual(D.page_problems(t, topics, terms), [], t["file"])


UDP = """---
title: "UDP"
term_kind: protocol
topics: [networking]
summary: "Datagrams."
match: ['\\bUDP\\b']
sources:
  - {title: "RFC 768", url: "https://www.rfc-editor.org/rfc/rfc768", primary: true}
draft: false
---
%s
"""


class CrossLinks(unittest.TestCase):
    """Max 2026-11-11: you should be able to traverse the terms, so a page that names another
    term links its first mention, exactly like a post."""

    def site(self, opnsense_body):
        s = Site()
        s.term("opnsense", (TERM % "false").replace("OPNsense is a firewall.", opnsense_body))
        s.term("udp", UDP % "UDP sends datagrams.")
        return s

    def test_page_naming_another_term_unlinked_refused(self):
        pages, _ = self.site("OPNsense can send syslog over UDP.").problems()
        self.assertIn("names UDP without linking it", pages["opnsense.md"][0])

    def test_page_linking_another_term_passes(self):
        s = self.site('OPNsense can send syslog over {{< term "udp" >}}.')
        self.assertEqual(s.problems(), ({}, {}))

    def test_page_naming_itself_needs_no_link(self):
        s = self.site("OPNsense is a firewall. OPNsense again.")
        self.assertEqual(s.problems(), ({}, {}))

    def test_published_page_linking_draft_page_refused(self):
        s = self.site('Over {{< term "udp" >}}.')
        s.term("udp", (UDP % "UDP.").replace("draft: false", "draft: true"))
        pages, _ = s.problems()
        self.assertIn("still a draft", pages["opnsense.md"][0])

    def test_seed_pages_link_each_other(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        d = os.path.join(root, "content", "dictionary")
        pages, _ = D.check([], D.load_terms(d), NOW, publish=False, topics=D.load_topics(d))
        self.assertEqual(pages, {})


class Candidates(unittest.TestCase):
    """Max 2026-11-11: "scan my site for terms that should be linked". Report-only: names the
    site uses that no dictionary page, concept or reviewed not-a-term entry covers."""

    def run_on(self, body, not_terms=()):
        s = Site()
        s.post("p", body)
        terms = D.load_terms(os.path.join(s.dir, "content", "dictionary"))
        docs = {"p.md": D.load_posts(os.path.join(s.dir, "content", "blog"))[0]["body"]}
        return {w: files for w, _, files in D.candidates(docs, terms, [], set(not_terms))}

    def test_unpaged_names_reported(self):
        got = self.run_on("Postgres talks to Redis over a VPN.")
        self.assertEqual(set(got), {"Postgres", "Redis", "VPN"})

    def test_paged_term_not_reported(self):
        self.assertNotIn("OPNsense", self.run_on('My {{< term "opnsense" >}} box. OPNsense again.'))

    def test_ordinary_words_and_reviewed_not_terms_dropped(self):
        got = self.run_on("Look here. Then look again, Read it and read it. My PC runs.",
                          not_terms={"PC"})
        self.assertEqual(got, {})

    def test_plurals_fold_and_hyphenated_names_kept_whole(self):
        got = self.run_on("One VLAN, two VLANs, on Wi-Fi.")
        self.assertEqual(set(got), {"VLAN", "Wi-Fi"})

    def test_code_and_links_ignored(self):
        self.assertEqual(self.run_on("Run `Redis` or see [x](https://Prometheus.io/)."), {})

    def test_own_concepts_not_reported(self):
        s = Site()
        terms = D.load_terms(os.path.join(s.dir, "content", "dictionary"))
        got = D.candidates({"p.md": "My badgescope rig, Badgescope again."}, terms,
                           [r"\bbadgescope\b"], set())
        self.assertEqual(got, [])


class AutoLink(unittest.TestCase):
    """`dictionary.py link` wraps each term's first unlinked mention, so the rule is cheap to follow."""

    def terms(self):
        s = Site()
        s.term("udp", UDP % "UDP.")
        return D.load_terms(os.path.join(s.dir, "content", "dictionary"))

    def test_wraps_first_mention_only_keeping_its_text(self):
        body, skipped = D.autolink("OPNsense and udp. More OPNsense.", self.terms())
        self.assertEqual(body, '{{< term "opnsense" >}} and {{< term "udp" "udp" >}}. More OPNsense.')
        self.assertEqual(skipped, [])

    def test_leaves_linked_code_and_self_alone(self):
        text = 'See {{< term "opnsense" >}}. `UDP` here, then UDP.'
        body, _ = D.autolink(text, self.terms(), self_slug="udp")
        self.assertEqual(body, text)

    def test_mention_inside_link_text_is_skipped_not_nested(self):
        body, skipped = D.autolink("[my OPNsense notes](https://example.com/)", self.terms())
        self.assertEqual(body, "[my OPNsense notes](https://example.com/)")
        self.assertIn("opnsense", skipped[0])

    def test_url_paths_are_not_mentions(self):
        s = Site()
        s.post("p", 'The docs say "GET /opnsense/api/v1/status". Then {{< term "opnsense" >}}.')
        self.assertEqual(s.problems(), ({}, {}))

    def test_result_passes_the_check(self):
        terms = self.terms()
        body, _ = D.autolink("UDP first, OPNsense second, UDP again.", terms)
        self.assertEqual(D.post_problems({"body": body}, terms, False), [])


if __name__ == "__main__":
    unittest.main()
