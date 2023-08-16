#UDP Client Side

import socket

#Creating client socket using IPv4 (AF_INET) and UDP (SOCK_DGRAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Get ip address
hostname=socket.gethostname()   
ipv4=socket.gethostbyname(hostname)

#Message
message = "Hello world!! UDP for the win!!!".encode("utf-8")

#Connect to server
client_socket.sendto(message, (ipv4, 12345))


client_socket.close()