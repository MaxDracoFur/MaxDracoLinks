---
title: "Scheduled job (cron)"
term_kind: concept
topics: [platforms-and-services]
see_also: [daemon, kubernetes, exit-code]
summary: "A task a computer runs automatically on a timetable, such as every five minutes or every night."
match: ['\b(?:small|backup|nightly|frequent|scheduled) jobs?\b', '\bcron ?jobs?\b', '\bcron\b']
sources:
  - title: "crontab (POSIX.1-2024)"
    url: "https://pubs.opengroup.org/onlinepubs/9799919799/utilities/crontab.html"
    publisher: "The Open Group / IEEE"
    primary: true
  - title: "cron"
    url: "https://en.wikipedia.org/wiki/Cron"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1053", topic: "Scheduled Task/Job",
     url: "https://attack.mitre.org/techniques/T1053/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A scheduled job is a task a computer runs by itself on a timetable: a backup every night, a check every five minutes. On Unix-like systems the classic tool for this is cron, and {{< term "kubernetes" >}} has its own CronJob. Because nobody watches a scheduled job run, its failures are easy to miss unless it reports them somewhere. Attackers also add scheduled jobs of their own, to keep a foothold that restarts itself.
