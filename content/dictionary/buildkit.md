---
title: "BuildKit"
term_kind: tool
topics: [platforms-and-services]
see_also: [docker, container]
summary: "The engine Docker uses to build images, and since version 23.0 the default one for Linux images."
match: ['\bBuildKit\b']
sources:
  - title: "BuildKit"
    url: "https://docs.docker.com/build/buildkit/"
    publisher: "Docker, Inc."
    primary: true
  - title: "Docker Engine deprecated features"
    url: "https://docs.docker.com/engine/deprecated/"
    publisher: "Docker, Inc."
# Copy review: Claude drafted this entry (2026-11-16) for the post docker-interview-questions
# (card blog-hacker-docker-recall-interviews). NOT yet approved by Max.
draft: true
---
When you ask {{< term "docker" "Docker" >}} to build an image, something has to read the build instructions and do the work. BuildKit is the newer of the two things that can: it can do independent steps at the same time, skip work it has already done, and keep build-time secrets out of the finished image. Docker made it the default for {{< term "linux" >}} images in version 23.0 and marked the older builder as on its way out, so a build today usually goes through BuildKit whether or not anyone asked for it.
