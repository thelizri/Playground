import tkinter
from tkinter import BOTH, StringVar, END

#Define root window
root = tkinter.Tk()
root.title("Terminal Chat")
root.geometry("800x450")
root.resizable(0, 0)

#Define colors
root_color = "#7289da"
input_color = "#1e2124"
output_color = "#424549"
red = "#ff0000"
green = "#00ff00"
blue = "#0000ff"
white = "#ffffff"
root.config(bg=root_color)

#Define functions
def send_message():
	'''Send the user's message to the output frame'''
	message_label = tkinter.Label(output_frame, text=message_entry.get(), fg=text_color.get(), bg=output_color, font=("Helvetica", 12))
	message_label.pack()

	message_entry.delete(0, END)

#Define GUI layout

#Define frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
output_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
input_frame.pack(padx=10, pady=10)

#Define widgets
message_entry = tkinter.Entry(input_frame, text="Enter message here", width=30, font=("Helvetica", 12))
send_button = tkinter.Button(input_frame, text="Send", command=send_message, bg=output_color, fg=white)
message_entry.grid(row=0, column=0, columnspan=3, padx=(20,10), pady=10)
send_button.grid(row=0, column=3, padx=10, pady=10, ipadx=20)

text_color = StringVar()
text_color.set(red)
red_button = tkinter.Radiobutton(input_frame, text="Red", variable=text_color, value=red, bg=input_color, fg=red, activebackground=input_color)
green_button = tkinter.Radiobutton(input_frame, text="Green", variable=text_color, value=green, bg=input_color, fg=green, activebackground=input_color)
blue_button = tkinter.Radiobutton(input_frame, text="Blue", variable=text_color, value=blue, bg=input_color, fg=blue, activebackground=input_color)
red_button.grid(row=1, column=0)
green_button.grid(row=1, column=1)
blue_button.grid(row=1, column=2)

output_label = tkinter.Label(output_frame, text="---Messages---", fg=white, bg=output_color, font=("Helvetica bold", 18))
output_label.pack(pady=15)

#Run the window's main loop
root.mainloop()