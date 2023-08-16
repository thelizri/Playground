import socket, threading

#Define the constants we will use in the project
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024
IPV4 = socket.AF_INET
TCP = socket.SOCK_STREAM

#Create socket
client_socket = socket.socket(IPV4, TCP)
client_socket.connect((DEST_IP, DEST_PORT))

def send_message():
	while True:
		try:
			message = input("")
			if message == "quit":
				client_socket.close()
				break
			else:
				client_socket.send(message.encode(ENCODER))
		except:
			client_socket.close()
			break

def receive_message():
	while True:
		try:
			message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

			if message == "NAME":
				#Send back username
				name = input("What is your username?  ")
				client_socket.send(name.encode(ENCODER))

				#Start thread for sending messages
				send_thread = threading.Thread(target=send_message)
				send_thread.start()
			else:
				print(message)
		except:
			client_socket.close()
			print("You have left the chat room...")
			break

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()