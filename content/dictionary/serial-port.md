---
title: "Serial port"
term_kind: concept
topics: [hardware]
see_also: [usb, flipper-zero, shell]
summary: "A simple connection that sends data one bit at a time, often used to control a device by typing commands to it."
match: ['\bserial (?:ports?|consoles?|connections?|lines?)\b', '\bover serial\b']
sources:
  - title: "Linux Serial Console"
    url: "https://www.kernel.org/doc/html/latest/admin-guide/serial-console.html"
    publisher: "The Linux Kernel documentation"
    primary: true
  - title: "Serial port"
    url: "https://en.wikipedia.org/wiki/Serial_port"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A serial port is one of the oldest and simplest ways to connect two devices: data goes down the wire one bit at a time. Today it usually travels over {{< term "usb" >}}, but the idea is the same. Many small gadgets, {{< term "router" "routers" >}} and servers offer a serial console, where you type commands and read replies, which makes it a powerful way in for anyone who can plug into it.
