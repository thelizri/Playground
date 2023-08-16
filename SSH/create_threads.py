import threading

def create_threads(iplist, function):

	threads = []

	for ip in iplist:
		th = threading.Thread(target = function, args = (ip,))   #args is a tuple with a single element
		th.start()
		threads.append(th)

	for th in threads:  #Tells main program to pause until all threads have finished executing
		th.join()
