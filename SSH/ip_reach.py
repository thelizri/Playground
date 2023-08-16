import sys
import subprocess

#Checking IP reachability
def ip_reach(iplist):

	for ip in iplist:
		#Runs ping on the command line
		ping_reply = subprocess.call('ping %s -n 2' % (ip), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL) 

		if ping_reply == 0:
			print("{} is reachable".format(ip))
		else:
			print('{} is not reachable'.format(ip))
			sys.exit()
            
