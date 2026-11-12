---
title: "ZeroTier"
term_kind: tool
topics: [networking, platforms-and-services]
see_also: [tailscale, vpn, headscale]
summary: "Service and software that joins devices anywhere into one private virtual network."
match: ['\bZeroTier\b']
sources:
  - title: "ZeroTier documentation"
    url: "https://docs.zerotier.com/"
    publisher: "ZeroTier"
    primary: true
  - title: "ZeroTier"
    url: "https://en.wikipedia.org/wiki/ZeroTier"
    publisher: "Wikipedia"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:zerotier:zerotierone", topic: "the name NVD files ZeroTier One vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Azerotier%3Azerotierone"}
  - {standard: attack, clause: "T1133", topic: "External Remote Services",
     url: "https://attack.mitre.org/techniques/T1133/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
ZeroTier links devices in different places into one private, {{< term "encryption" "encrypted" >}} network, as if they were plugged into the same switch. A controller decides which devices may join; most people use ZeroTier's hosted controller, though it can be {{< term "self-hosting" "self-hosted" >}}. Like {{< term "tailscale" >}}, whoever runs the controller can add members to the network, so they are part of who can get in.
