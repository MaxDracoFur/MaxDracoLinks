---
title: "Polling"
term_kind: concept
topics: [programming-and-ai, networking]
see_also: [webhook, websocket, race-condition]
summary: "Checking something over and over on a timer to see whether it has changed, instead of waiting to be told."
match: ['\bpoll(?:s|ed|ing|er|ers)?\b']
sources:
  - title: "RFC 6202: Known Issues and Best Practices for the Use of Long Polling and Streaming in Bidirectional HTTP"
    url: "https://www.rfc-editor.org/info/rfc6202/"
    publisher: "IETF"
    primary: true
  - title: "Polling (computer science)"
    url: "https://en.wikipedia.org/wiki/Polling_(computer_science)"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Polling means a program asks the same question again and again: is there new data, is the link still up, has anything changed? It is simple and dependable but wasteful, and when two programs poll the same thing at once they can get in each other's way. The alternative is to be told when something happens, as with a {{< term "webhook" >}}.
