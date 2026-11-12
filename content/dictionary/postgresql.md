---
title: "PostgreSQL (Postgres)"
term_kind: tool
topics: [platforms-and-services]
see_also: [redis, least-privilege]
summary: "Free, open-source database that stores data in tables and answers queries written in SQL."
match: ['\bPostgres(?:QL)?\b']
sources:
  - title: "About PostgreSQL"
    url: "https://www.postgresql.org/about/"
    publisher: "PostgreSQL Global Development Group"
    primary: true
  - title: "PostgreSQL"
    url: "https://en.wikipedia.org/wiki/PostgreSQL"
    publisher: "Wikipedia"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:postgresql:postgresql", topic: "the name NVD files PostgreSQL vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Apostgresql%3Apostgresql"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
PostgreSQL, usually called Postgres, is a free, {{< term "open-source" >}} database. Programs store their data in it as tables and ask for it back in the SQL query language. One Postgres server can hold many separate databases, each with its own users and permissions, so several applications can share it without seeing each other's data.
