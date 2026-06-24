import socket
import sys
import threading

if len(sys.argv) != 5:
    print("Usage: python client.py <SERVER_IP> <PORT> <ROLE> <TOPIC>")
    sys.exit()

if sys.argv[3] != "SUBSCRIBER" and sys.argv[3] != "PUBLISHER":
    print("Role must be only SUBSCRIBER or PUBLISHER")
    sys.exit()

SERVER_IP = sys.argv[1]
PORT = int(sys.argv[2])
ROLE = sys.argv[3]
TOPIC = sys.argv[4]

GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))
client_socket.send(f"{ROLE}|{TOPIC}".encode())

print(f"{CYAN}======================================{RESET}")
print(f"{CYAN} Connected to server{RESET}")
print(f"{CYAN} Role : {ROLE}{RESET}")
print(f"{CYAN} Topic: {TOPIC}{RESET}")
print(f"{CYAN}======================================{RESET}")

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if message == "":
                break

            print(f"\n{BLUE}[RECEIVED on {TOPIC}]{RESET} {message}")

        except:
            break

if ROLE == "PUBLISHER":
    print(f"{GREEN}Publisher started on topic {YELLOW}{TOPIC}{RESET}")

    while True:
        message = input(f"{YELLOW}Enter message: {RESET}")

        client_socket.send(message.encode())

        if message == "terminate":
            break

        print(f"{GREEN}[SENT]{RESET} {message}")

if ROLE == "SUBSCRIBER":
    print(f"{BLUE}Subscriber started on topic {YELLOW}{TOPIC}{RESET}")

    receive_thread = threading.Thread(target=receive_messages, daemon=True)
    receive_thread.start()

    while True:
        message = input(f"{YELLOW}Enter message: {RESET}")

        client_socket.send(message.encode())

        if message == "terminate":
            break

        print(f"{GREEN}[SENT]{RESET} {message}")

client_socket.close()
print(f"{RED}Disconnected from server.{RESET}")