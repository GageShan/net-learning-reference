import socket

SEND_BUFF_SIZE = 4096
RECV_BUFF_SIZE = 4096

def modify_buff_size():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
	print("before buffsize = %s" % bufsize)

	sock.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY,1)
	sock.setsockopt(
		socket.SOL_SOCKET,
		socket.SO_SNDBUF,
		SEND_BUFF_SIZE)
	
	sock.setsockopt(
		socket.SOL_SOCKET,
		socket.SO_RCVBUF,
		RECV_BUFF_SIZE)

	bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
	print("after buffsize = %s" % bufsize)

if __name__ == '__main__':
	modify_buff_size()
