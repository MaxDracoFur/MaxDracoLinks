---
title: "Redis"
term_kind: tool
topics: [platforms-and-services]
see_also: [postgresql]
summary: "Fast in-memory data store that programs use for caching, queues and short-lived data."
match: ['\bRedis\b']
sources:
  - title: "Redis: Get started"
    url: "https://redis.io/docs/latest/get-started/"
    publisher: "Redis"
    primary: true
  - title: "Redis"
    url: "https://en.wikipedia.org/wiki/Redis"
    publisher: "Wikipedia"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:redis:redis", topic: "the name NVD files Redis vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Aredis%3Aredis"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Redis keeps data in memory rather than on disk, which makes it very fast. Applications use it as a cache, to share small pieces of information between programs, and as a queue of work waiting to be done. It was designed to run inside a trusted network, so a Redis server left reachable from the internet has long been an easy target.
