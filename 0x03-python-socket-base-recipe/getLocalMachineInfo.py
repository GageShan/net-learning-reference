# get localhost

import socket
def getLocalInfo():
	hostname = socket.gethostname()
	ip = socket.gethostbyname(hostname)
	print("hostname:" + hostname)
	print("ip:" + ip)

if __name__ == "__main__":
	getLocalInfo()
