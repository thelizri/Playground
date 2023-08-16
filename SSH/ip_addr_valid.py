import sys

#Will check that the ip addresses are valid
# In other words, that they're in the correct format and don't contain these reserved addresses
# Loopback, multicast, broadcast, link-local, reserved-for-future use

def ip_addr_valid(ip_list):
	
	for ip in ip_list:
		octet_list = ip.split(".")

		if len(octet_list) != 4:
			print("Incorrectly formatted ip: "+ip)
			sys.exit()

		for octet in octet_list:
			if not octet.isdigit():
				 print("Incorrectly formatted ip: "+ip)
				 sys.exit()

		check_octet(octet_list)

	return True

def check_octet(octet_list):
	octet_numbers = [int(octet) for octet in octet_list]
	if octet_numbers[0] > 223: print("Error: contains reserved ip address"); sys.exit()
	if octet_numbers[0] == 127: print("Error: contains reserved ip address"); sys.exit()
	if octet_numbers[0] == 169 and octet_numbers[1] == 254: print("Error: contains reserved ip address"); sys.exit()
	for octet in octet_numbers:
		if octet < 0 or octet > 255: print("Error: octet in ip goes outside allowed range (0-255)"); sys.exit()
	return True