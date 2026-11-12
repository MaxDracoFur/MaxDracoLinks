---
title: "Watchdog (timer)"
term_kind: concept
topics: [hardware]
see_also: [kernel, firmware, health-check]
summary: "A timer that restarts a computer automatically if its software stops checking in."
match: ['\bwatchdogs?(?: timers?)?\b']
sources:
  - title: "The Linux Watchdog driver API"
    url: "https://docs.kernel.org/watchdog/watchdog-api.html"
    publisher: "The Linux Kernel documentation"
    primary: true
  - title: "watchdog(4)"
    url: "https://man.freebsd.org/cgi/man.cgi?query=watchdog&sektion=4"
    publisher: "FreeBSD"
  - title: "Watchdog timer"
    url: "https://en.wikipedia.org/wiki/Watchdog_timer"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A watchdog is a countdown timer, usually built into the hardware, that the running system must reset regularly. If the software freezes and stops resetting it, the timer runs out and restarts the machine. It turns a silent hang into a reboot, which is better for unattended devices like {{< term "router" "routers" >}}, though it also means the moment of the freeze can go unrecorded.
