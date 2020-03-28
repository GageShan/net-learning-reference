import socket
import sys

def reuseSocketAddr():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
	print("old_state : %s" % old_state)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	new_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
	print("new_state : %s" % new_state)

	local_port = 8282
	
	srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	srv.bind(('',local_port))
	srv.listen(1)
	
	print("listening on port %s" % local_port)

	while True:
		try:
			connection,addr = srv.accept()
			print("connected by %s:%s" % (addr[0],addr[1]))
		except KeyboardInterrupt:
			break
		except socket.error as e:
			print("error %s" % e)

if __name__ == '__main__':
	reuseSocketAddr()
