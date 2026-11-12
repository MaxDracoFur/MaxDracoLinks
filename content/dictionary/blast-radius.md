---
title: "Blast radius"
term_kind: concept
topics: [security-operations]
see_also: [single-point-of-failure, high-availability]
summary: "How much else breaks or is exposed when one part of a system fails or is compromised."
match: ['\bblast radius\b']
sources:
  - title: "REL10-BP03 Use bulkhead architectures to limit scope of impact"
    url: "https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_use_bulkhead.html"
    publisher: "Amazon Web Services"
    primary: true
  - title: "Blast radius"
    url: "https://en.wikipedia.org/wiki/Blast_radius"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Borrowed from explosives, "blast radius" in computing means how far the damage spreads when one thing goes wrong: a machine dies, a change is bad, or a password leaks. A small blast radius means the problem stays contained to one part; a large one means many other things go down or are exposed with it. Engineers shrink it by splitting systems into separate pieces and giving each piece only the access it needs.
