---
title: "Regular expression (regex)"
term_kind: concept
topics: [programming-and-ai, data-formats]
see_also: [redaction]
summary: "A compact pattern language for finding text of a given shape, such as any run of digits."
match: ['\bregex(?:es|p|ps)?\b', '\bregular expressions?\b']
sources:
  - title: "Regular Expressions (POSIX Base Definitions, chapter 9)"
    url: "https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html"
    publisher: "The Open Group"
    primary: true
  - title: "Regular expression"
    url: "https://en.wikipedia.org/wiki/Regular_expression"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A regular expression, or regex, describes a pattern of text rather than exact words: for example, "the word key, then a space, then any run of letters and digits". Programs use them to search, check and rewrite text, from checking a form field to finding secrets in logs. Most languages and tools support them, but each has its own dialect, so a regex written for one tool may need adjusting before it works in another.
