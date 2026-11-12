---
title: "Daemon (background service)"
term_kind: concept
topics: [platforms-and-services]
see_also: [linux, macos, scheduled-job]
summary: "A program that runs in the background, with no window, waiting to do its job."
match: ['\bdaemons?\b', '\bbackground services?\b', '\bsystem services?\b']
sources:
  - title: "daemon(7)"
    url: "https://www.freedesktop.org/software/systemd/man/latest/daemon.html"
    publisher: "freedesktop.org (systemd)"
    primary: true
  - title: "Daemon (computing)"
    url: "https://en.wikipedia.org/wiki/Daemon_(computing)"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1543", topic: "Create or Modify System Process",
     url: "https://attack.mitre.org/techniques/T1543/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A daemon (pronounced "demon") is a program that starts in the background and keeps running without anyone watching it, such as the service that syncs the clock or handles printing. On {{< term "linux" >}} and {{< term "macos" >}}, the operating system starts them and restarts them if they stop. Because they run all the time, often with more access than an ordinary app, attackers like to add their own daemon to keep a foothold on a machine.
