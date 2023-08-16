#Client Side GUI Chat Room
import socket, threading, tkinter
from tkinter import DISABLED, VERTICAL, END, NORMAL

#Define Colors
black = "#010101"
light_green = "#1fc742"
light_blue = "#7289DA"
red = "#ff0000"
green = "#00ff00"
blue = "#0000ff"
white = "#ffffff"

#Define Fonts
my_font = ("SimSun", 14)

#Define Socket Constants
ENCODER = "utf-8"
BYTE_SIZE = 1024
IPV4 = socket.AF_INET
TCP = socket.SOCK_STREAM
client_socket = None

#Define Window
root = tkinter.Tk()
root.title("Terminal Chat")
root.iconbitmap("icon.ico")
root.geometry("900x600")
root.resizable(0, 0)
root.config(bg=black)

#Define Functions
def connect():
	'''Connect to a server given ip/port'''
	global client_socket
	NAME = name_entry.get()
	DEST_IP = ip_entry.get()
	DEST_PORT = port_entry.get()

	if NAME and DEST_IP and DEST_PORT:
		my_listbox.insert(END, f"{NAME} is waiting to connect to ip {DEST_IP} at port {DEST_PORT}...")
		client_socket = socket.socket(IPV4, TCP)
		client_socket.connect((DEST_IP, int(DEST_PORT)))

		verify_connection(NAME)
	else:
		my_listbox.insert(END, "Insufficient information to connection...")


def verify_connection(name):
	'''Verify that the connection is valid'''
	global client_socket

	#Server should pass a "NAME" flag
	flag = client_socket.recv(BYTE_SIZE).decode(ENCODER)

	if flag == "NAME":
		client_socket.send(name.encode(ENCODER))
		message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

		if message:
			my_listbox.insert(END, message)

			#Change button entry states
			connect_button.config(state=DISABLED)
			name_entry.config(state=DISABLED)
			ip_entry.config(state=DISABLED)
			port_entry.config(state=DISABLED)

			disconnect_button.config(state=NORMAL)
			input_entry.config(state=NORMAL)
			send_button.config(state=NORMAL)

			#Create a thread to continously receive messages from the server
			receive_thread = threading.Thread(target=receive_message)
			receive_thread.start()
		else:
			my_listbox.insert(END, "No confirmation message was received")
			my_listbox.insert(END, "Closing connection")
			client_socket.close()
	else:
		my_listbox.insert(END, "Connection was denied")
		my_listbox.insert(END, "Closing connection")
		client_socket.close()


def disconnect():
	'''Disconnect from the server'''
	client_socket.close()

	#Change button entry states
	connect_button.config(state=NORMAL)
	name_entry.config(state=NORMAL)
	ip_entry.config(state=NORMAL)
	port_entry.config(state=NORMAL)

	disconnect_button.config(state=DISABLED)
	input_entry.config(state=DISABLED)
	send_button.config(state=DISABLED)

	my_listbox.insert(END, "Disconnecting from server")

def send_message():
	'''Send a message to be broadcast on the server'''
	try:
		message = input_entry.get()
		input_entry.delete(0, END)
		if message:
			client_socket.send(message.encode(ENCODER))
	except:
		disconnect()

def receive_message():
	'''Receive a message from the server'''
	while True:
		try:
			message = client_socket.recv(BYTE_SIZE).decode(ENCODER)
			if message:
				my_listbox.insert(END, message)
		except:
			client_socket.close()
			my_listbox.insert(END, "You have left the chatroom")
			break

#Define GUI Layout
info_frame = tkinter.Frame(root, bg=black)
output_frame = tkinter.Frame(root, bg=black)
input_frame = tkinter.Frame(root, bg=black)

info_frame.pack()
output_frame.pack(pady=10)
input_frame.pack()

#Info Frame Layout
name_label = tkinter.Label(info_frame, text="Client Name:", font=my_font, fg=light_green, bg=black)
name_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
ip_label = tkinter.Label(info_frame, text="Host IP:", font=my_font, fg=light_green, bg=black)
ip_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
port_label = tkinter.Label(info_frame, text="Port Num:", font=my_font, fg=light_green, bg=black)
port_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font, width=10)
connect_button = tkinter.Button(info_frame, text="Connect", font=my_font, bg=light_green, borderwidth=5, width=10, command=connect)
disconnect_button = tkinter.Button(info_frame, text="Disconnect", font=my_font, bg=light_green, borderwidth=5, width=10, command=disconnect,state=DISABLED)

name_label.grid(row=1, column=0, padx=5, pady=10)
name_entry.grid(row=1, column=1, padx=5, pady=10)
ip_label.grid(row=0, column=0, padx=5, pady=10)
ip_entry.grid(row=0, column=1, padx=5, pady=10)
port_label.grid(row=0, column=2, padx=5, pady=10)
port_entry.grid(row=0, column=3, padx=5, pady=10)
connect_button.grid(row=1, column=2, padx=5, pady=10)
disconnect_button.grid(row=1, column=3, padx=5, pady=10)

#Output Frame Layout
my_scrollbar = tkinter.Scrollbar(output_frame, orient=VERTICAL)
my_listbox = tkinter.Listbox(output_frame, width=80, height=20, borderwidth=3, bg=black, fg=light_green, font=my_font, yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_listbox.yview)

my_listbox.grid(row=0, column=0, pady=2)
my_scrollbar.grid(row=0, column=1, sticky="NS")

#Input Frame Layout
input_entry = tkinter.Entry(input_frame, width=45, borderwidth=3, font=my_font, state=DISABLED)
send_button = tkinter.Button(input_frame, text="Send",width=10, borderwidth=5, font=my_font, bg=light_green, state=DISABLED, command=send_message)

input_entry.grid(row=0, column=0, pady=2, padx=5)
send_button.grid(row=0, column=1, pady=2, padx=5)

#Run the window's main loop
root.mainloop()