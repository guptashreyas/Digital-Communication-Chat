# Digital Communication Chat

A simple **two-way chat application** built **just for fun** while learning basic networking concepts.  
This project demonstrates the **foundation of digital communication** using Python: messages are encoded into **binary format**, transmitted over a TCP socket, and decoded back to text on the receiver side.

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
```
2. **Run the server:**
```bash
python server.py
```
3. **Run the client (in another terminal):**
```bash
python client.py
```
4. **Start chatting!**
```
 Client types a message → sent in binary → server decodes and replies.
 Server types a reply → sent in binary → client decodes.
```

## Example

[CLIENT] Enter message: Hello Server

[SERVER] Decoded: Hello Server

[SERVER] Enter reply: Hello Client

[CLIENT] Decoded: Hello Client


## License

This project is open-source and available under the MIT License.

## Author

Shreyas Gupta
