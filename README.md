# Nagle's Algorithm and Its Impact on TCP/IP

This project demonstrates the impact of **Nagle’s Algorithm** on TCP/IP communication using a simple **client-server model** with **Flask** and **sockets**.

## Description

- A **Flask client** sends multiple small packets to a **TCP server**.
- The client can toggle **Nagle’s algorithm** (`TCP_NODELAY`).
- The round-trip time (RTT) is measured to analyze the effect of enabling/disabling Nagle’s algorithm.

## Features

- Simulates packet transmission over TCP
- Measures response time with and without Nagle’s algorithm
- Simple Flask web interface

## Installation

1. **Clone the Repository**
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd nagle-tcp-experiment