#Chat Server Side
import socket

#Define the constants we will use in the project
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024
IPV4 = socket.AF_INET
TCP = socket.SOCK_STREAM

#Create and bind the socket
server_socket = socket.socket(IPV4, TCP)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()
print("Server has been started")

#Accept incoming connection
client_socket, client_address = server_socket.accept()
client_socket.send("You are connected to the server".encode(ENCODER))

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
server_socket.close()