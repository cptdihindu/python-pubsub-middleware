import socket
import sys
import threading

if len(sys.argv) != 4:
    print("Usage: python client.py <SERVER_IP> <PORT> <ROLE>")
    sys.exit()

if sys.argv[3] != "SUBSCRIBER" and sys.argv[3] != "PUBLISHER":
    print("Role must be only SUBSCRIBER or PUBLISHER")
    sys.exit()

SERVER_IP = sys.argv[1]
PORT = int(sys.argv[2])
ROLE = sys.argv[3]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))
client_socket.send(ROLE.encode())

print_lock = threading.Lock()

GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

def show_prompt():
    print(f"{YELLOW}> {RESET}", end="", flush=True)

def print_received(message):
    with print_lock:
        print(f"\n{BLUE}[RECEIVED]{RESET} {message}")
        show_prompt()

def print_sent(message):
    with print_lock:
        print(f"{GREEN}[YOU]{RESET} {message}")

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if message == "":
                break

            print_received(message)

        except:
            break

print(f"{CYAN}Connected to server as {ROLE}.{RESET}")

if ROLE == "PUBLISHER":
    print(f"{GREEN}Publisher mode started. Type messages below.{RESET}")

    while True:
        show_prompt()
        message = input()

        client_socket.send(message.encode())

        if message == "terminate":
            break

        print_sent(message)

if ROLE == "SUBSCRIBER":
    print(f"{BLUE}Subscriber mode started. Waiting for publisher messages.{RESET}")

    receive_thread = threading.Thread(target=receive_messages, daemon=True)
    receive_thread.start()

    while True:
        show_prompt()
        message = input()

        client_socket.send(message.encode())

        if message == "terminate":
            break

        print_sent(message)

client_socket.close()
print(f"{RED}Disconnected from server.{RESET}")