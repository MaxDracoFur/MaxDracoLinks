---
title: "WireGuard"
term_kind: protocol
topics: [networking, cryptography]
summary: "Simple, fast, modern VPN protocol and software."
match: ['\bWireGuard\b']
sources:
  - title: "WireGuard"
    url: "https://www.wireguard.com/"
    publisher: "WireGuard"
    primary: true
  - title: "WireGuard: Next Generation Kernel Network Tunnel (whitepaper)"
    url: "https://www.wireguard.com/papers/wireguard.pdf"
    publisher: "Jason A. Donenfeld"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:wireguard:wireguard", topic: "the name NVD files WireGuard vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Awireguard%3Awireguard"}
  - {standard: attack, clause: "T1133", topic: "External Remote Services",
     url: "https://attack.mitre.org/techniques/T1133/"}
  - {standard: sp800-53, clause: "AC-17", topic: "Remote Access",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AC-17"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-11). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
WireGuard is a {{< term "vpn" >}}: it creates an encrypted tunnel between devices so they can reach each other as if they were on the same network. It is deliberately small, with a fixed set of modern cryptography and no options to choose between. Each device has a key pair, and each side lists the public keys it will accept. It runs over {{< term "udp" >}} and stays silent to anything that doesn't present a valid key.
