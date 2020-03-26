# gettimeout,settimeout
import socket
def socket_timeout():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("default timeout :%s" % s.gettimeout())
	s.settimeout(100)
	print("current timeout :%s" % s.gettimeout())

if __name__ == "__main__":
	socket_timeout()
