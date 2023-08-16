#UDP Server Side

import socket

#Creating server socket using IPv4 (AF_INET) and UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Get ip address
hostname=socket.gethostname()   
ipv4=socket.gethostbyname(hostname)

#Bind our socket to an ip and a port
server_socket.bind((ipv4, 12345))

#UDP is connectionless, so we don't have to listen or wait for a connection
message, address = server_socket.recvfrom(1024)

print(message.decode("utf-8"))
print(f"From address: {address}")

server_socket.close()