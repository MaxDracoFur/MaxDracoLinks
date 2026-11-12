---
title: "Kernel"
term_kind: concept
topics: [platforms-and-services]
see_also: [driver, linux, watchdog-timer]
summary: "The core of an operating system, which controls the hardware and runs every other program."
match: ['\bkernels?\b']
sources:
  - title: "The Linux Kernel documentation"
    url: "https://docs.kernel.org/"
    publisher: "The Linux Kernel Organization"
    primary: true
  - title: "Kernel (operating system)"
    url: "https://en.wikipedia.org/wiki/Kernel_(operating_system)"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12.
draft: false
---
The kernel is the central part of an operating system such as {{< term "linux" >}}, {{< term "freebsd" >}} or {{< term "macos" >}}. It talks to the hardware through {{< term "driver" "drivers" >}}, shares out memory and processor time, and decides what each program may do. Every other program asks the kernel for what it needs, so a serious kernel bug can stop the whole machine, called a kernel panic, or hand an attacker full control.
