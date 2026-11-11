---
title: "syslog"
term_kind: technology
summary: "The standard way computers and network devices send log messages to a log server."
match: ['\bsyslog\b']
sources:
  - title: "RFC 5424: The Syslog Protocol"
    url: "https://www.rfc-editor.org/rfc/rfc5424"
    publisher: "IETF"
    primary: true
  - title: "RFC 5426: Transmission of Syslog Messages over UDP"
    url: "https://www.rfc-editor.org/rfc/rfc5426"
    publisher: "IETF"
  - title: "RFC 5425: TLS Transport Mapping for Syslog"
    url: "https://www.rfc-editor.org/rfc/rfc5425"
    publisher: "IETF"
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first; health is checked daily.
draft: true
---
Syslog is a simple format and protocol for log messages: each message has a timestamp, the host that sent it, how serious it is, and the text. It started on BSD Unix in the 1980s and is now an IETF standard. Devices can keep syslog locally or send it over the network to a central log server, classically over UDP port 514, or over TLS when the messages need protecting.

## Why it's on this site

My firewall and other boxes send their logs to a log server on my network with syslog, so I can search everything in one place.
