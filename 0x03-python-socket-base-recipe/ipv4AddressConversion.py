# inet_aton convert '192.168.0.1' to 32-bit packed binary format
# inet_ntoa convert 32-bit packed binary format to '192.168.0.1' 

import socket
from binascii import hexlify

def convert_ipv4_address():
	for ip_addr in ['127.0.0.1','192.168.142.128']:
		packed_ip = socket.inet_aton(ip_addr)
		unpacked_ip = socket.inet_ntoa(packed_ip)
		print("%s = %s = %s" %(ip_addr,hexlify(packed_ip),unpacked_ip))

if __name__ == '__main__':
	convert_ipv4_address()
