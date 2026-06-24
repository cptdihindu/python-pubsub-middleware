# Python Pub/Sub Middleware Using Sockets

A socket-based Publish/Subscribe middleware implementation built in Python for the Middleware Architectures assignment.

This project demonstrates how clients communicate through a middleware server using TCP sockets. It starts with a basic client-server model, then extends into publishers, subscribers, concurrent clients, and topic-based message filtering.

---

## Overview

In this system, the server acts as the **middleware broker** between clients.

Publishers do not directly communicate with subscribers. Instead:

```text
Publisher Client -> Middleware Server -> Subscriber Client
```

The server receives messages from publishers and forwards them to the correct subscribers.

---

## Features

- TCP socket-based client-server communication
- Command Line Interface support
- Multiple concurrent client connections
- Publisher and subscriber client roles
- Topic-based message filtering
- Clean terminal output with colored messages
- Client termination using the `terminate` keyword

---

## Technologies Used

- Python 3
- TCP sockets
- Threading
- Command Line Interface

No external Python libraries are required.

---

## Project Structure

```text
.
├── task1/
│   ├── server.py
│   └── client.py
│
├── task2/
│   ├── server.py
│   └── client.py
│
├── task3/
│   ├── server.py
│   └── client.py
│
└── README.md
```

---

## Task 1: Basic Client-Server Application

Task 1 implements a basic TCP client-server socket application.

### What It Does

- Starts a server on a given port
- Starts a client using server IP and port
- Allows the client to send messages to the server
- Displays client messages on the server terminal
- Terminates the client when the user types `terminate`

### Run Server

```bash
python server.py 5000
```

### Run Client

```bash
python client.py 127.0.0.1 5000
```

### Example Flow

```text
Client types: Hello server
Server displays: Client says: Hello server
```

---

## Task 2: Publishers and Subscribers

Task 2 extends Task 1 by adding multiple concurrent clients and role-based communication.

### What It Does

- Supports multiple clients at the same time
- Each client connects as either a `PUBLISHER` or `SUBSCRIBER`
- Publisher messages are forwarded to all subscribers
- Publisher messages are not sent to other publishers
- Server displays all client activities

### Run Server

```bash
python server.py 5000
```

### Run Publisher Client

```bash
python client.py 127.0.0.1 5000 PUBLISHER
```

### Run Subscriber Client

```bash
python client.py 127.0.0.1 5000 SUBSCRIBER
```

### Example Flow

```text
Publisher sends: Hello subscribers
Subscriber receives: Hello subscribers
```

---

## Task 3: Topic-Based Publish/Subscribe Middleware

Task 3 improves the Pub/Sub system by adding topic-based filtering.

### What It Does

- Each publisher publishes messages under a topic
- Each subscriber subscribes to a specific topic
- Messages are delivered only to subscribers of the same topic
- Multiple publishers and subscribers can connect under different topics

### Run Server

```bash
python server.py 5000
```

### Run Subscriber for `TOPIC_A`

```bash
python client.py 127.0.0.1 5000 SUBSCRIBER TOPIC_A
```

### Run Publisher for `TOPIC_A`

```bash
python client.py 127.0.0.1 5000 PUBLISHER TOPIC_A
```

### Run Subscriber for `TOPIC_B`

```bash
python client.py 127.0.0.1 5000 SUBSCRIBER TOPIC_B
```

### Example Flow

```text
Publisher TOPIC_A sends: Hello Topic A
Subscriber TOPIC_A receives: Hello Topic A
Subscriber TOPIC_B does not receive the message
```

---

## How Topic Filtering Works

The server stores subscribers by topic using a dictionary-like structure:

```text
TOPIC_A -> Subscriber 1, Subscriber 2
TOPIC_B -> Subscriber 3
```

When a publisher sends a message on `TOPIC_A`, the server forwards it only to subscribers registered under `TOPIC_A`.

---

## Running on the Same Computer

For local testing, use:

```text
127.0.0.1
```

This IP address refers to the same computer.

Example:

```bash
python client.py 127.0.0.1 5000 PUBLISHER TOPIC_A
```

---

## Running on Different Computers

To run clients from another computer on the same network:

1. Start the server on one computer.
2. Find the server computer's local IP address.
3. Use that IP address when starting the client.

Example:

```bash
python client.py 192.168.1.10 5000 SUBSCRIBER TOPIC_A
```

Make sure the server port is allowed through the firewall.

---

## Terminating a Client

Any client can disconnect by typing:

```text
terminate
```

The client will close its socket connection and exit.

---

## Requirements

- Python 3 installed
- Terminal or command prompt
- No external dependencies

Check Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Important Concepts Demonstrated

- Client-server architecture
- Middleware broker architecture
- TCP socket communication
- Concurrent client handling using threads
- Publisher/subscriber pattern
- Topic-based message routing
- Command line arguments
- Basic distributed communication concepts

---

## Assignment Context

This project was developed for the Middleware Architectures module assignment. The goal is to demonstrate the design and implementation of a simple Publish/Subscribe middleware using socket programming concepts.