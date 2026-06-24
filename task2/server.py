import socket
import sys
import threading

if len(sys.argv) != 2:
    print("Usage: python server.py <PORT>")
    sys.exit()

PORT = int(sys.argv[1])

subscribers = []

def handle_client(client_socket, client_address):
    role = client_socket.recv(1024).decode()
    print(f"{role} connected from {client_address}")

    if role == "SUBSCRIBER":
        subscribers.append(client_socket)
        print("Subscriber added to subscriber list.")

    while True:
        message = client_socket.recv(1024).decode()

        if message == "terminate":
            print(f"{role} disconnected from {client_address}")
            break
        
        print(f"{role} says: {message}")

        if role == "PUBLISHER":
            for subscriber in subscribers:
                subscriber.send(message.encode())

    if role == "SUBSCRIBER":
        subscribers.remove(client_socket)
    
    client_socket.close()

# Create a TCP socket using IPv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", PORT))

server_socket.listen(5)
print(f"Server is listening on port {PORT}...")

while True:
    client_socket, client_address = server_socket.accept()

    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )
    client_thread.start()
