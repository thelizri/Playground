import threading

def function1():
	for i in range(100):
		print(" ONE ")

def function2():
	for i in range(100):
		print(" TWO ")

def function3():
	for i in range(100):
		print(" THREE ")

#Create threads
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)

#Starts the threads
t1.start()
t2.start()
t3.start()

#Pauses the main program until the threads have completed executing
t1.join()
t2.join()
t3.join()

print("Executed all threads")