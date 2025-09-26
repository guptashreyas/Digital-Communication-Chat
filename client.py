import socket

def binary_to_text(binary_str):
    chars = [chr(int(b, 2)) for b in binary_str.split()]
    return ''.join(chars)

def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

HOST = '127.0.0.1'  # Change to server IP if needed
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[CLIENT] Connected to server.")
    while True:
        msg = input("[CLIENT] Enter message: ")
        binary_msg = text_to_binary(msg)
        s.sendall(binary_msg.encode())

        data = s.recv(1024).decode()
        decoded = binary_to_text(data)
        print(f"[SERVER] {decoded}")
