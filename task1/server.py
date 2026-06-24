import socket
import sys

if len(sys.argv) != 2:
    print("Usage: python server.py <PORT>")
    sys.exit()

PORT = int(sys.argv[1])

# Create a TCP socket using IPv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", PORT))

server_socket.listen(1)
print(f"Server is listening on port {PORT}...")

client_socket, client_address = server_socket.accept()
print(f"Client connected from {client_address}\n")

while True:
    message = client_socket.recv(1024).decode()
    if message == "terminate" :
        print("Client disconnected.")
        break
    print(f"Client says : {message}")

client_socket.close()
server_socket.close()