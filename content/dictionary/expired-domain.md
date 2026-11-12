---
title: "Expired / aged domain buying"
term_kind: concept
topics: [web-and-advertising]
see_also: [domain, seo, wayback-machine]
summary: "Registering or buying a domain name someone else let go, to reuse the trust and search ranking it built up."
match: ['\bexpired[- ]domains?\b', '\baged domains?\b', '\bestablished domains? (?:is |are |was |were )?bought\b']
sources:
  - title: "Spam policies for Google web search: expired domain abuse"
    url: "https://developers.google.com/search/docs/essentials/spam-policies"
    publisher: "Google Search Central"
    primary: true
  - title: "Expired Registration Recovery Policy"
    url: "https://www.icann.org/en/contracted-parties/consensus-policies/expired-registration-recovery-policy/expired-registration-recovery-policy-28-02-2013-en"
    publisher: "ICANN"
  - title: "Domain drop catching"
    url: "https://en.wikipedia.org/wiki/Domain_drop_catching"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1583.001", topic: "Acquire Infrastructure: Domains",
     url: "https://attack.mitre.org/techniques/T1583/001/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
When the owner of a {{< term "domain" "domain name" >}} stops renewing it, the name eventually becomes free for anyone to register, and old names are also bought and sold directly. A name with years of history keeps its links from other sites and the trust search engines gave it, so it can be refilled with new content that ranks well straight away. Buying one is legal; {{< term "google" >}} treats reusing one mainly to rank low-value content as spam, and attackers sometimes buy expired names because security tools already trust them.
