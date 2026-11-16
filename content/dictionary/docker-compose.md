---
title: "Docker Compose"
term_kind: tool
topics: [platforms-and-services]
see_also: [docker, container]
summary: "Docker's tool for describing several containers in one file and starting them together."
match: ['\bDocker Compose\b', '\bdocker-compose\b', '\bdocker compose\b']
sources:
  - title: "Docker Compose"
    url: "https://docs.docker.com/compose/"
    publisher: "Docker, Inc."
    primary: true
  - title: "Migrate to Compose v2"
    url: "https://docs.docker.com/compose/migrate/"
    publisher: "Docker, Inc."
# Copy review: Claude drafted this entry (2026-11-16) for the post docker-interview-questions
# (card blog-hacker-docker-recall-interviews). NOT yet approved by Max.
draft: true
---
An application is rarely one program: a website might be a web server, a database and a cache. Docker Compose lets you write all of them down in a single file and start or stop the lot with one command. It exists in two versions with confusingly similar names. The original, written in {{< term "python" >}}, is run as `docker-compose` with a hyphen; Docker's own migration page says it is no longer maintained. The replacement, written in Go and built into the main {{< term "docker" "Docker" >}} command, is run as `docker compose` with a space.
