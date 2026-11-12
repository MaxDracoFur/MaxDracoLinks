---
title: "BotFather"
term_kind: tool
topics: [platforms-and-services]
see_also: [telegram, access-token]
summary: "Telegram's official bot for creating Telegram bots and managing their tokens."
match: ['\bBotFather\b']
sources:
  - title: "Telegram Bot Features: BotFather"
    url: "https://core.telegram.org/bots/features"
    publisher: "Telegram"
    primary: true
  - title: "From BotFather to 'Hello World'"
    url: "https://core.telegram.org/bots/tutorial"
    publisher: "Telegram"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
BotFather is itself a bot inside {{< term "telegram" >}}, run by Telegram, and it is the only way to make a new Telegram bot. You chat with it to create a bot, change its name or picture, and get the bot's {{< term "access-token" "token" >}}, the secret a program uses to act as that bot. If a token leaks, BotFather is also where you revoke it and issue a new one.
