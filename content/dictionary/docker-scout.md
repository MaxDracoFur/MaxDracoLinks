---
title: "Docker Scout"
term_kind: tool
topics: [security-operations]
see_also: [docker, container, vulnerability, cve]
summary: "Docker's tool for listing the known security holes in an image; it replaced the older `docker scan` command."
match: ['\bDocker Scout\b', '\bdocker scout\b', '\bdocker scan\b']
sources:
  - title: "Docker Scout"
    url: "https://docs.docker.com/scout/"
    publisher: "Docker, Inc."
    primary: true
  - title: "Docker Desktop release notes"
    url: "https://docs.docker.com/desktop/release-notes/"
    publisher: "Docker, Inc."
# Copy review: Claude drafted this entry (2026-11-16) for the post docker-interview-questions
# (card blog-hacker-docker-recall-interviews). NOT yet approved by Max.
draft: true
---
An image is built out of other people's software, and some of that software has publicly known flaws. Docker Scout reads an image, works out what is inside it, and lists the known flaws it can find, each with the published identifier that describes it. It replaced an earlier command called `docker scan`: Docker Desktop 4.17.0 announced the replacement and 4.19.0 removed the old command, so a machine with a recent {{< term "docker" >}} no longer has `docker scan` at all.
