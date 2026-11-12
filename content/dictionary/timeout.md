---
title: "Timeout"
term_kind: concept
topics: [networking, programming-and-ai]
see_also: [tarpit, socket, health-check]
summary: "A limit on how long a program waits for something before it gives up."
match: ['\btimeouts? (?:set|configured|error)\b', '\b(?:connect|connection|read|per-read|socket|overall|total|request) timeouts?\b']
sources:
  - title: "socket: Notes on socket timeouts"
    url: "https://docs.python.org/3/library/socket.html"
    publisher: "Python Software Foundation"
    primary: true
  - title: "Timeout (computing)"
    url: "https://en.wikipedia.org/wiki/Timeout_(computing)"
    publisher: "Wikipedia"
classification:
  - {standard: cwe, clause: "CWE-1088", topic: "Synchronous Access of Remote Resource without Timeout",
     url: "https://cwe.mitre.org/data/definitions/1088.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A timeout is a limit on how long a program will wait, for a connection to open, for the next piece of data, or for a whole request to finish, before it stops and reports an error. Without one, a program talking to a slow or broken server can hang forever. Different timeouts cover different phases, so a limit on each step does not protect against a server that answers just often enough to keep resetting it.
