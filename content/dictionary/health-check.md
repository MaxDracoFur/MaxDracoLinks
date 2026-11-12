---
title: "Health check (readiness check)"
term_kind: concept
topics: [logging-and-monitoring]
see_also: [high-availability, timeout, metrics]
summary: "An automatic test that asks a running service whether it is working, so a broken one can be restarted or taken out of use."
match: ['\b(?:health|readiness|liveness) checks?\b', '\b(?:readiness|liveness) probes?\b']
sources:
  - title: "Liveness, Readiness, and Startup Probes"
    url: "https://kubernetes.io/docs/concepts/workloads/pods/probes/"
    publisher: "Kubernetes"
    primary: true
  - title: "Configure Liveness, Readiness and Startup Probes"
    url: "https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/"
    publisher: "Kubernetes"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12.
draft: false
---
A health check is a small automatic test that a monitoring system runs against a service again and again, such as asking it to answer a web request. A readiness check asks whether the service is ready to take work; a liveness check asks whether it is still running at all. {{< term "kubernetes" >}}, for example, stops sending work to a copy that fails its readiness check and restarts one that fails its liveness check. A health check is only as good as what it tests: one that only checks that the service answers can stay green while the service does nothing useful.
