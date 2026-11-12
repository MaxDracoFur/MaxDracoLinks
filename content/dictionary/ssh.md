---
title: "SSH"
term_kind: protocol
topics: [networking, identity-and-access]
summary: "Encrypted protocol for logging in to and running commands on another computer."
match: ['\bSSH\b']
sources:
  - title: "RFC 4251: The Secure Shell (SSH) Protocol Architecture"
    url: "https://www.rfc-editor.org/rfc/rfc4251"
    publisher: "IETF"
    primary: true
  - title: "OpenSSH"
    url: "https://www.openssh.com/"
    publisher: "OpenBSD project"
classification:
  - {standard: attack, clause: "T1021.004", topic: "Remote Services: SSH",
     url: "https://attack.mitre.org/techniques/T1021/004/"}
  - {standard: attack, clause: "T1098.004", topic: "SSH Authorized Keys",
     url: "https://attack.mitre.org/techniques/T1098/004/"}
  - {standard: cpe, clause: "cpe:2.3:a:openbsd:openssh", topic: "the name NVD files OpenSSH vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Aopenbsd%3Aopenssh"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: true
---
SSH (Secure Shell) lets you log in to another computer over the network and run commands on it, with the whole session encrypted. It replaced older tools such as Telnet that sent passwords in plain text. You can sign in with a password or, more safely, with a key pair: the server keeps your public key and you keep the private one. OpenSSH is the version almost every Linux and Mac system ships.
