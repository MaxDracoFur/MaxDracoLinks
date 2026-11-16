---
title: "Docker"
term_kind: tool
topics: [platforms-and-services]
see_also: [container, docker-compose, kubernetes]
summary: "The most widely used tool for building and running containers, and the command-line program people mean when they say \"docker\"."
match: ['\bDocker\b(?! Compose| Scout| Desktop| Hub)', '\bdocker ps\b', '\bdocker build\b']
sources:
  - title: "Docker Docs"
    url: "https://docs.docker.com/"
    publisher: "Docker, Inc."
    primary: true
  - title: "Docker Engine deprecated features"
    url: "https://docs.docker.com/engine/deprecated/"
    publisher: "Docker, Inc."
  - title: "SP 800-190, Application Container Security Guide"
    url: "https://csrc.nist.gov/pubs/sp/800/190/final"
    publisher: "NIST"
# Copy review: Claude drafted this entry (2026-11-16) for the post docker-interview-questions
# (card blog-hacker-docker-recall-interviews). NOT yet approved by Max.
# Sources: Docker's own documentation first. Version facts in the body were read there 2026-11-16.
draft: true
---
Docker builds and runs {{< term "container" "containers" >}}: it packages a program with everything it needs into an image, and starts that image as a running program fenced off from the rest of the machine. Most people meet it as a command you type — `docker build` to make an image, `docker run` to start one — and that command is also where its history shows. Docker has been through many numbered releases since 2013, and old ways of doing a thing usually keep working for years after a new one arrives, which is why two people can give different correct answers to the same question about it.
