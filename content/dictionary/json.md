---
title: "JSON"
term_kind: format
topics: [data-formats]
see_also: [api, graphql]
summary: "A simple text format for structured data that people can read and almost every programming language can handle."
match: ['\bJSON\b']
sources:
  - title: "RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format"
    url: "https://www.rfc-editor.org/info/rfc8259/"
    publisher: "IETF"
    primary: true
  - title: "Introducing JSON"
    url: "https://www.json.org/"
    publisher: "json.org"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12.
draft: false
---
JSON (JavaScript Object Notation) is a plain-text way of writing structured data: lists go in square brackets and named fields in curly braces, as in `{"name": "value"}`. Almost every programming language can read and write it, so it is the usual format for data passed between programs, especially by web {{< term "api" "APIs" >}}. It is only a format: a program reading JSON from outside still has to check that what arrived is what it expected.
