---
title: "Socket"
term_kind: concept
topics: [networking, programming-and-ai]
see_also: [network-port, tcp, timeout]
summary: "The handle a program uses to send and receive data over a network connection."
match: ['\bsockets?\b']
sources:
  - title: "socket: create an endpoint for communication (POSIX.1-2024)"
    url: "https://pubs.opengroup.org/onlinepubs/9799919799/functions/socket.html"
    publisher: "The Open Group / IEEE"
    primary: true
  - title: "Network socket"
    url: "https://en.wikipedia.org/wiki/Network_socket"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A socket is what a program opens to talk over a network, or to another program on the same machine. It is one end of a connection: the program writes data into it and reads replies out of it, and the operating system handles the rest. Each open connection uses its own socket, which is why a server's capacity is often counted in sockets.
