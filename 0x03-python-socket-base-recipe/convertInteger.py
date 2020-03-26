# htonl ---from host to network long 32-bit 1234-->3523477504
# ntohl ---from network to host long 32-bit 
# htons ---from host to network short 16-bit 1234-->53764
# ntohs ---from network to host short 16-bit
import socket
from binascii import hexlify
def convert_integer():
	data = 1234
	print("%s=%s=%s" %(data,(socket.htonl(data)),(socket.ntohl(data))))
	print("%s=%s=%s" %(data,(socket.htons(data)),(socket.ntohs(data))))

if __name__ == "__main__":
	convert_integer()
