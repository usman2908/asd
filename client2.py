
import socket               # Import socket module

s = socket.socket()         
host = socket.gethostname()
port = 5188            # Reserve a port for your service.

s.connect((host, port))

while True:
	data = s.recv(1024)
	if not data:
		break
	else:
		print data
	
	data=raw_input()
	if not data:
		break
	else:
		s.sendall(data)
		
		
s.close()                    # Close the socket when done
