---
title: "HTTP status codes (200, 401, 403, 404)"
term_kind: concept
topics: [networking]
see_also: [http, api]
summary: "The three-digit number a web server sends back to say how a request went."
match: ['\b(?:status|response) codes?\b', '\b[1-5]xx\b', '\b(?:401|403|404|409)s?\b', '\b(?:an?|with|returns?|answers?|gets?)\s+200\b', '\b200 OK\b']
sources:
  - title: "RFC 9110: HTTP Semantics (section 15, Status Codes)"
    url: "https://www.rfc-editor.org/info/rfc9110/"
    publisher: "IETF"
    primary: true
  - title: "Hypertext Transfer Protocol (HTTP) Status Code Registry"
    url: "https://www.iana.org/assignments/http-status-codes"
    publisher: "IANA"
  - title: "List of HTTP status codes"
    url: "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12.
draft: false
---
Every reply to an {{< term "http" >}} request starts with a three-digit status code. Codes in the 200s mean success, the 300s mean look somewhere else, the 400s mean the request was refused or wrong, and the 500s mean the server itself failed. Common ones are 200 (OK), 401 (you haven't proved who you are), 403 (you have, but you aren't allowed), 404 (nothing there) and 409 (conflicts with the current state). A code is only a summary: some services answer 200 and put the real errors inside the reply, so a program that checks only the code can miss a failure.
