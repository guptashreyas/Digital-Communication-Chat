# Digital Communication Chat

A simple **two-way chat application** demonstrating the **foundation of digital communication** using Python.  
This project encodes messages into **binary format**, transmits them over a TCP socket, and decodes them back to text on the receiver side.

---

## Features
- **Two-way communication:** Both client and server can send and receive messages.
- **Digital communication demonstration:** Messages are converted to binary (digital signals) before transmission.
- **Simple and lightweight:** No external dependencies, runs on Python’s standard library.

---

## Project Structure
- `server.py` → The server script. Waits for client connection, receives binary messages, decodes, and allows server replies.
- `client.py` → The client script. Connects to the server, sends messages in binary, and receives replies.
- `README.md` → Project documentation.

---

## How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/<your-username>/Digital-Communication-Chat.git
cd Digital-Communication-Chat

    Run the server:

python server.py

    Run the client (in another terminal):

python client.py

    Start chatting!

        Client types a message → sent in binary → server decodes and replies.

        Server types a reply → sent in binary → client decodes.

Example

[CLIENT] Enter message: Hello Server
[SERVER] Decoded: Hello Server
[SERVER] Enter reply: Hello Client
[CLIENT] Decoded: Hello Client

Requirements

    Python 3.x

    No external libraries required

License

This project is open-source and available under the MIT License

.
Author

Shreyas Gupta