---
title: "Linux distribution (Debian, Ubuntu, Alpine)"
term_kind: tool
topics: [platforms-and-services]
see_also: [linux, container]
summary: "A complete operating system built around the Linux kernel, such as Debian, Ubuntu or Alpine."
match: ['\bDebian\b', '\bUbuntu\b', '\bAlpine\b', '\bdistros?\b']
sources:
  - title: "About Debian"
    url: "https://www.debian.org/intro/about"
    publisher: "Debian"
    primary: true
  - title: "About Ubuntu"
    url: "https://ubuntu.com/about"
    publisher: "Canonical"
  - title: "About Alpine Linux"
    url: "https://alpinelinux.org/about/"
    publisher: "Alpine Linux"
  - title: "Linux distribution"
    url: "https://en.wikipedia.org/wiki/Linux_distribution"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A distribution (or "distro") takes the {{< term "linux" >}} {{< term "kernel" "kernel" >}} and adds everything else a working system needs: a package manager, system tools and thousands of ready-built programs. Debian is a long-running volunteer project, Ubuntu is a popular system built on Debian by the company Canonical, and Alpine is a very small one often used inside {{< term "container" "containers" >}}. Each distribution builds and patches its own packages, so the same program can have a security flaw in one distribution's version and not in another's.
