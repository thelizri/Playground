import socket, threading

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
print(f"Server has been started at ip {HOST_IP} on port {HOST_PORT}\n")

#Two lists to store all the clients
client_socket_list = []
client_name_list = []

def broadcast(message):
	try:
		for client in client_socket_list:
			client.send(message)
	except:
		print("Could not broadcast message")

def receive_message(client):
	while True:
		try:
			#Get name of client
			index = client_socket_list.index(client)
			name = client_name_list[index]

			#Receive message
			message = client.recv(BYTE_SIZE).decode(ENCODER)

			#Format message
			message = f"{name}: {message}".encode(ENCODER)
			broadcast(message)
		except:
			#Get name of client
			index = client_socket_list.index(client)
			name = client_name_list[index]

			#Remove from lists
			client_socket_list.remove(client)
			client_name_list.remove(name)
			client.close()

			#Broadcast that client has left the server
			broadcast(f"{name} has left the server".encode(ENCODER))
			break


def connect_client():
	while True:
		try:
			#Accept any incoming connection
			client_socket, client_address = server_socket.accept()
			print(f"\nClient {client_address} has connected to the server")

			#Promt the client for a NAME
			client_socket.send("NAME".encode(ENCODER))
			client_name = client_socket.recv(BYTE_SIZE).decode(ENCODER)

			#Append socket and name to list
			client_socket_list.append(client_socket)
			client_name_list.append(client_name)

			#Send status updates
			print(f"Name of new client is {client_name}\n")
			client_socket.send(f"Welcome to the server {client_name}\n".encode(ENCODER))
			broadcast(f"Everyone, {client_name} has joined the chat room...\n".encode(ENCODER))

			#Start a thread for the new client
			client_thread = threading.Thread(target=receive_message, args=(client_socket,))
			client_thread.start()
		except:
			print("Incoming connection failed")
			break

#Start the server
server_thread = threading.Thread(target=connect_client)
server_thread.start()

while True:
	message = input("")
	if message == "quit":
		server_socket.close()
		for socket in client_socket_list:
			socket.close()
		break
	else:
		print("Type 'quit' to stop server")

print("Server has shutdown")