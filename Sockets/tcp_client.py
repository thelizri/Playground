#TCP Client Side

import socket

#Creating client socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Get ip address
hostname=socket.gethostname()   
ipv4=socket.gethostbyname(hostname)

#Connect to server
client_socket.connect((ipv4, 12345))

#Read message from server. Specify max size of segment
message = client_socket.recv(1024)
message = message.decode("utf-8")
print(message)

client_socket.close()