#Chat Client Side
import socket

#Define the constants we will use in the project
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024
IPV4 = socket.AF_INET
TCP = socket.SOCK_STREAM

#Create socket and connect to server
client_socket = socket.socket(IPV4, TCP)
client_socket.connect((DEST_IP, DEST_PORT))

#Send/Receive messages
while True:
	message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

	if message == "quit":
		client_socket.send("quit".encode(ENCODER))
		print("\nEnding the chat...Goodbye!!!")
		break
	else:
		print(f"\n{message}")
		message = input("Message: ")
		client_socket.send(message.encode(ENCODER))

#Shutdown socket
client_socket.close()
