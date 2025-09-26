import socket

def binary_to_text(binary_str):
    # Convert 8-bit binary chunks back to text
    chars = [chr(int(b, 2)) for b in binary_str.split()]
    return ''.join(chars)

def text_to_binary(text):
    # Convert text to 8-bit binary
    return ' '.join(format(ord(char), '08b') for char in text)

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVER] Listening on {HOST}:{PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"[SERVER] Connected by {addr}")
        while True:
            # Receive message from client
            data = conn.recv(1024).decode()
            if not data:
                break
            message = binary_to_text(data)
            print(f"[CLIENT] {message}")

            # Server sends reply
            reply = input("[SERVER] Enter reply: ")
            binary_reply = text_to_binary(reply)
            conn.sendall(binary_reply.encode())
