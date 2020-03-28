import socket

def test_socket_modes():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setblocking(0)
	s.bind(("127.0.0.1", 0))
	
	socket_address = s.getsockname()
	print("trivial server launched on socket %s " % str(socket_address))
	while True:
		s.listen(1)

if __name__ == '__main__':
	test_socket_modes()
