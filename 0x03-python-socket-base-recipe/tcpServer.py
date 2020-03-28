# tcp-server

import socket
import sys
import argparse

host = 'localhost'
port = 8385
backlog = 5
buffsize = 2048

def tcp_server():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	server_address = (host,port)
	sock.bind(server_address)
	sock.listen(backlog)
	
	while True:
		print("waiting to receive message")
		client,address = sock.accept()
		data = client.recv(buffsize)
		if data:
			print("receive : %s" % data.decode())
			data = input("send:")
			client.send(data.encode())
		client.close()

if __name__ == '__main__':
	tcp_server()
