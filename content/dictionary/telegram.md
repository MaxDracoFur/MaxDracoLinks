---
title: "Telegram (and Bot API)"
term_kind: tool
topics: [platforms-and-services]
see_also: [botfather, access-token, polling]
summary: "A messaging app whose Bot API lets programs run accounts that read and send messages."
match: ['\bTelegram\b']
sources:
  - title: "Telegram Bot API"
    url: "https://core.telegram.org/bots/api"
    publisher: "Telegram"
    primary: true
  - title: "Telegram (software)"
    url: "https://en.wikipedia.org/wiki/Telegram_(software)"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1102", topic: "Web Service",
     url: "https://attack.mitre.org/techniques/T1102/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Telegram is a cloud-based messaging app for phones and computers, used for private chats, groups and public channels. Its Bot {{< term "api" "API" >}} lets a program run a bot account: the program proves who it is with a secret {{< term "access-token" "token" >}} and either asks Telegram for new messages ({{< term "polling" >}}) or has them pushed to it by a {{< term "webhook" >}}. Anyone who holds a bot's token can act as that bot, so the token has to be guarded like a password.
