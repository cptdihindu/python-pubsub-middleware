import socket
import sys

if len(sys.argv) != 3:
    print("Usage: python client.py <SERVER_IP> <PORT>")
    sys.exit()

SERVER_IP = sys.argv[1]
PORT = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))
print("Connected to server.")

while True:
    message = input("Enter message: ")
    client_socket.send(message.encode())

    if message == "terminate":
        break

client_socket.close()