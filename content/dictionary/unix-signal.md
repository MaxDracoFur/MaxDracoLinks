---
title: "Signal (SIGTERM, SIGKILL)"
term_kind: concept
topics: [programming-and-ai]
see_also: [daemon, exit-code, kubernetes]
summary: "A short notice the operating system sends a running program, such as a request to stop."
match: ['\bSIG(?:TERM|KILL|INT|HUP|STOP|CHLD)\b', '\bsignal handlers?\b', '\bhandles? (?:one|a|the) signal\b']
sources:
  - title: "signal.h (POSIX.1-2024)"
    url: "https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/signal.h.html"
    publisher: "The Open Group / IEEE"
    primary: true
  - title: "Signal (IPC)"
    url: "https://en.wikipedia.org/wiki/Signal_(IPC)"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
On Unix-like systems such as {{< term "linux" >}} and {{< term "macos" >}}, a signal is a numbered notice the system delivers to a running program. SIGTERM politely asks a program to shut down, and the program can catch it to finish its work and exit cleanly. SIGKILL ends it at once and cannot be caught. Tools like {{< term "kubernetes" >}} send SIGTERM first and SIGKILL after a grace period, so a program that ignores SIGTERM is always stopped the slow, hard way.
