---
title: "GraphQL"
term_kind: protocol
topics: [programming-and-ai]
see_also: [api, json, http-status-code]
summary: "A query language for APIs in which the client asks for exactly the data it wants in one request."
match: ['\bGraphQL\b']
sources:
  - title: "GraphQL specification"
    url: "https://spec.graphql.org/"
    publisher: "GraphQL Foundation"
    primary: true
  - title: "GraphQL"
    url: "https://en.wikipedia.org/wiki/GraphQL"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12.
draft: false
---
GraphQL is a way of asking an {{< term "api" >}} for data. Instead of a separate address for each kind of thing, there is one, and each request is a query naming exactly the fields it wants; the answer comes back as {{< term "json" "JSON" >}} in the same shape. It was created at Facebook and is now an open specification. A GraphQL reply can report success overall while carrying a list of errors inside it, so a program has to read that list to know whether it really got what it asked for.
