import socket
import sys
import threading

if len(sys.argv) != 2:
    print("Usage: python server.py <PORT>")
    sys.exit()

PORT = int(sys.argv[1])

subscribers = {}

GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

def handle_client(client_socket, client_address):
    client_info = client_socket.recv(1024).decode()
    role, topic = client_info.split("|")

    print(f"{CYAN}[CONNECTED]{RESET} {role} from {client_address} on topic {YELLOW}{topic}{RESET}")

    if role == "SUBSCRIBER":
        if topic not in subscribers:
            subscribers[topic] = []

        subscribers[topic].append(client_socket)
        print(f"{BLUE}[SUBSCRIBER ADDED]{RESET} Topic: {YELLOW}{topic}{RESET}")

    while True:
        message = client_socket.recv(1024).decode()

        if message == "terminate":
            print(f"{RED}[DISCONNECTED]{RESET} {role} from {client_address} on topic {YELLOW}{topic}{RESET}")
            break

        print(f"{GREEN}[MESSAGE]{RESET} {role} on {YELLOW}{topic}{RESET}: {message}")

        if role == "PUBLISHER":
            if topic in subscribers:
                for subscriber in subscribers[topic]:
                    subscriber.send(message.encode())

    if role == "SUBSCRIBER":
        subscribers[topic].remove(client_socket)

        if len(subscribers[topic]) == 0:
            del subscribers[topic]

    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", PORT))

server_socket.listen(5)

print(f"{CYAN}======================================{RESET}")
print(f"{CYAN} Pub/Sub Middleware Server Started{RESET}")
print(f"{CYAN} Listening on port {PORT}{RESET}")
print(f"{CYAN}======================================{RESET}")

while True:
    client_socket, client_address = server_socket.accept()

    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )

    client_thread.start()