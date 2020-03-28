# tcp-client

import socket
import sys

host = 'localhost'
port = 8385

def tcp_client():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address = (host,port)
	sock.connect(server_address)
	
	try:
		message = input("send:")
		sock.sendall(message.encode())
		data = sock.recv(2048)
		print("received: %s" % data.decode())
	except socket.error as e:
		print("socket error %s" % str(e))
	except Exception as e:
		print("other exception %s" % str(e))
	finally:
		print("Closing connection to the server")
		sock.close()
if __name__ == '__main__':
	tcp_client()
		
