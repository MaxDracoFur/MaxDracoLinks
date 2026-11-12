---
title: "Driver (device driver)"
term_kind: concept
topics: [hardware]
see_also: [kernel, firmware, usb]
summary: "Software that lets an operating system control one particular kind of hardware."
match: ['\bdrivers?\b']
sources:
  - title: "Chapter 9. Writing FreeBSD Device Drivers"
    url: "https://docs.freebsd.org/en/books/arch-handbook/driverbasics/"
    publisher: "FreeBSD Project"
    primary: true
  - title: "What is a driver?"
    url: "https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/what-is-a-driver-"
    publisher: "Microsoft"
  - title: "Device driver"
    url: "https://en.wikipedia.org/wiki/Device_driver"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A driver is the piece of software that lets an operating system talk to one particular kind of hardware, such as a network adapter, a disk or a printer. The rest of the system asks for general things like "send this data", and the driver turns that into the exact commands the chip understands, often working around the chip's known quirks along the way. Drivers usually run inside the {{< term "kernel" >}} with full control of the machine, so a bug in one can crash the whole system or open a security hole.
