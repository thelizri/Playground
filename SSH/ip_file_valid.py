import sys
import os.path

#Checks that the file exists, and then reads its contents
def ip_file_valid():

	#Get the file path from the user
	ip_file = input("Enter the path of the file containing the ip addresses: \n")

	#Checks if the file exist
	if not os.path.exists(ip_file):
		print("File could not be found")
		sys.exit()

	#Opens the file in reading mode
	selected_ip_file = open(ip_file, "r")

	#Makes sure we're reading from the beginning of the file
	selected_ip_file.seek(0)

	#Gets a list of strings with the ip addresses
	ip_list = [row.strip() for row in selected_ip_file]
	
	#Closes the file
	selected_ip_file.close()

	return ip_list