---
title: "Remote console (KVM over IP)"
term_kind: thing
topics: [hardware, networking]
see_also: [lan, tunnel]
summary: "A small device that lets someone see a computer's screen and use its keyboard and mouse over the network."
match: ['\bKVM[- ]over[- ]IP\b', '\bIP[- ]KVMs?\b', '\bremote[- ]consoles?\b']
sources:
  - title: "PiKVM documentation"
    url: "https://docs.pikvm.org/"
    publisher: "PiKVM"
    primary: true
  - title: "KVM switch"
    url: "https://en.wikipedia.org/wiki/KVM_switch"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1219.003", topic: "Remote Access Tools: Remote Access Hardware",
     url: "https://attack.mitre.org/techniques/T1219/003/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A KVM-over-IP device (KVM stands for keyboard, video, mouse) plugs into a computer's screen output and {{< term "usb" "USB" >}} port and puts them on the network. Someone elsewhere can then watch the screen and type as if they were sitting at the machine, even while it starts up or when its own software has crashed. That makes it very handy for fixing servers, and also very powerful: anyone who can reach the device has the computer, so it needs the same protection as the machine itself.
