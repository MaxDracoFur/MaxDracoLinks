---
title: "Docker interview questions where the right answer has a version number"
search_phrase: "docker interview questions"
slug: "docker-interview-questions"
url: "/blog/docker-interview-questions"
layout: "blog/single"
series: "hacker"
date: 2026-11-16
draft: true
review_status: "copy-review"
introduces: []
uses: []
summary: "Five of the commonest \"what's the docker command for X\" questions have an answer that changed in a numbered release, and one of them Docker now hides from its own help text. What the question measures, how to answer it without bluffing, and three questions worth asking instead."
cover_image: ""
cover_source: ""
cover_alt: ""
# NOT the INC format, on purpose: there is no incident here. docs/hacker-inc-format.md and the
# quality rule both say the incident-report shape is for a post with a real incident, and the
# evidence labels ("measured", "inferred") belong to those posts, where the format introduces
# them. So this one says plainly when I checked something and where.
#
# FOR MAX, before this can go anywhere:
#   1. The lead needs YOUR interview. Card blog-hacker-docker-recall-interviews asks for one
#      real time a command-recall question caught you out -- no company, no interviewer, no
#      recognisable detail. The paragraph marked MAX'S EXAMPLE is a placeholder and reads as
#      a placeholder on purpose; I am not inventing one for you.
#   2. Cover: pick a photo. The security-themed option already used once is the foil-wrapped
#      dragon head from SecretCon 2025 (stage 265 or 380).
#   3. Dictionary pages for Docker, Docker Compose, BuildKit and Docker Scout are drafts
#      alongside this post and need your approval before a published post may link them.
#
# Every version number and date below was read on 2026-11-16 at Docker's own documentation:
#   docs.docker.com/engine/deprecated/            -- --link, legacy builder
#   docs.docker.com/engine/release-notes/prior-releases/ -- 1.13.0 (2017-01-18) CLI restructure
#   docs.docker.com/reference/cli/docker/container/ls/   -- `docker ps` still an alias
#   docs.docker.com/reference/cli/docker/         -- DOCKER_HIDE_LEGACY_COMMANDS
#   docs.docker.com/compose/migrate/              -- v1 Python vs v2 Go, v1 unmaintained
#   docs.docker.com/desktop/release-notes/        -- scan -> scout in 4.17.0, removed in 4.19.0
---

If you have ever been asked "what's the {{< term "docker" "docker" >}} command for X" in an interview and gone blank,
here is the thing worth knowing: for five of the commonest versions of that question, Docker
changed the answer in a numbered release. One of the old answers is still correct and still
works, and Docker ships a setting that hides it from its own help text. Another has been on
the way out since 2016 and is still there in 2026.

So the question mostly measures when you last typed that command, and which version you learned
on. Below are the five, each checked against Docker's own documentation on 16 November 2026;
then how to answer one honestly without bluffing, and three questions an interviewer can ask
instead that are much harder to fake.

*MAX'S EXAMPLE — placeholder. One real interview where a command-recall question caught him
out, no company or interviewer named.*

## The five answers Docker changed

**"How do you list the running {{< term "container" "containers" >}}?"** Both `docker ps` and `docker container ls` are
right. Docker reorganised its commands in version 1.13, released on 18 January 2017, so that
each one sits under the thing it acts on. The short forms kept working — the reference page for
`docker container ls` still lists `docker ps` as one of its aliases. The twist: the command-line
tool has a setting, `DOCKER_HIDE_LEGACY_COMMANDS`, that hides those short forms from its help
output, and Docker's own reference says that may become the default one day. An interviewer who
calls `docker container ls` wrong is nine years behind; one who calls `docker ps` wrong is
ahead of Docker.

**"What's the Compose command?"** Two different programs with nearly the same name. The older
one is `docker-compose`, written in {{< term "python" >}}; the newer is `docker compose`, written in Go and
built into the main Docker command. Docker's migration page says the first is no longer
maintained and that people should move to the second. Someone whose fingers type the hyphen
learned this before the change; it is not evidence they can't run containers.

**"How do you let two containers talk to each other?"** The old answer was the `--link` option.
It was marked deprecated — Docker's word for "we intend to remove this" — in version 1.10, which
is 2016. Ten years later it still works on networks you create yourself. Version 29.6 added a
warning when it is used on the default network, and removal is currently aimed at version 30.0.
The answer most interviewers are listening for is "put them on a network I created", which is
right, but "`--link`, though it's deprecated" is not wrong, and the person who says the second
thing has probably read the deprecation page.

**"How do you scan an image for known holes?"** The answer was `docker scan`. In Docker Desktop
4.17.0 that was replaced by `docker scout`, and in 4.19.0 the old command was removed outright.
This is the one question on the list where a confidently stale interviewer asks for a command
their own laptop no longer has.

**"What does `docker build` actually use?"** Since version 23.0, building {{< term "linux" >}} images goes
through {{< term "buildkit" >}} by default. The older builder is deprecated and now only does Windows images.
A candidate who describes the old builder's behaviour is describing something that has not been
the default for several versions — and so is an interviewer who expects them to.

Five questions, five answers with a version number attached. None of them tells you whether the
person can get a container running in an unfamiliar codebase on a Tuesday afternoon.

## What the question measures

Recency. It measures whether you typed that command recently enough for it to be in your
fingers, and which version of Docker you were holding when you learned it. That is a real
thing — but it is not the thing the job needs.

The job needs someone who can read the documentation faster than they can guess, work out why a
container exits the moment it starts, and explain what a container actually is — a normal
process on the host, fenced off by features of the operating system's {{< term "kernel" "kernel" >}}, not a small
computer. Any of those is checkable in an interview. None of them is checked by an exact string.

The failure is not that interviewers ask about commands. It is that a miss gets read as proof of
no experience, by someone whose own answer key stopped being updated when they stopped
installing things by hand.

## If you are the candidate

Fluency matters. Do not read this as permission not to learn the commands: someone who has to
look up how to list containers every single time is slower all day, and that shows. What is
worth refusing is the bluff.

When you don't have the string, say what you would do. "I'd run `docker container --help` and
read the verbs" is an answer, and it is the true one, because it is what you will do on the job
at two in the afternoon. Then name the idea the option controls — "I want them on a network I
made, so they can find each other by name" — because that is the part that doesn't change when
the command does. Then offer the story: the container that exited instantly and what the logs
turned out to say. An interviewer who still wants the exact flag after that has told you
something useful about the job.

## Three questions I would rather be asked

I am on the candidate side of the table at the moment, not the hiring side, so take these as
what I would want to be asked rather than advice on running an interview.

**"This container exits immediately. Walk me through finding out why."** The answer shows
whether someone reaches for the logs, whether they know a container stops when its main program
stops, and whether they can tell a crash from a command that simply finished.

**"This image is 1.2 GB. How would you make it smaller, and how would you know it worked?"**
The answer shows whether someone knows an image is built in stacked layers, that deleting a file
in a later layer does not shrink the earlier one, and that the result is something you measure
rather than argue about.

**"What does `--privileged` actually give the program, and when would you refuse to use it?"**
This is the one I would keep if I could only have one. It is a security question dressed as a
Docker question: the answer is about what the fence around a container is made of and which
parts of it that option takes down. It is also very hard to answer from a copied internet
snippet.

None of the three has an answer that will be wrong in two releases' time.

If an interviewer asks you for a string and marks you down for missing it, you have learned
which kind of team you were applying to — which is worth knowing before you take the job.
