import sys
import socket
from datetime import datetime


#Define our targets (IPs will be the arguments passed)
target = None
if(len(sys.argv) > 1):
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4
else:
    print("Invalid No of Arguments.")
    sys.exit()

print('-' * 30)
print("Scanning Targets: \n" + target)
print("Time Started" + str(datetime.now()))
print('-' * 30)


my_socket = None
result = None
try:
    #scan for ports 50 to 85
    for port in range(50, 85):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = my_socket.connect_ex((target, port)) #returns an error code
        #checking the port
        if(result == 0):
            print("Port {} is open".format(port))
        my_socket.close() #close our connection
except socket.gaierror:
    print("Error! Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("Error! Could not connect to server")
    sys.exit()


