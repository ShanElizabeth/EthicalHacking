#!/bin/python3

import sys
import socket
from datetime import datetime

#Define target
#take arg, python3 scanner.py <192.0.0.1> (arg1)

if len(sys.argv) ==2:
	target=socket.gethostbyname(sys.argv[1]) #dns service incase of .com or string
else:
	print('Invalid amt of args\n Synatx: python3 scanner.py <ip>')
	sys.exit()


#Add banner to the 
print('_'*50)
print("Scanning target "+target)
print("Time started : " +str(datetime.now()))
print('_'*50)

try: 
	for port in range (50,85):
		si = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #stop hanging move on if not open after 1 sec		
		result= si.connect_ex((target,port)) #Returns error
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		si.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("\nHostname cannot be reached")
	sys.exit()

except socket.error:
	print("\nServer down")
	sys.exit()

