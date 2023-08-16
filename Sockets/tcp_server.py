#TCP Server Side

import socket

#Creating server socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Get ip address
hostname=socket.gethostname()   
ipv4=socket.gethostbyname(hostname)

#Bind our socket to an ip and a port
server_socket.bind((ipv4, 12345))

#Put socket into listening mode
server_socket.listen()

try:
	client_socket, client_address = server_socket.accept() #Will wait until it receives a connection
	print(type(client_socket))
	print(client_socket)
	print(type(client_address))
	print(client_address)

	print(f"Connected to {client_address}\n")

	#Send a message to the client
	client_socket.send("You are connected".encode("utf-8"))

except KeyboardInterrupt:
	print("Oh! you pressed CTRL + C.")
	print("Program interrupted.")

finally:
	print("Closing socket")
	server_socket.close()