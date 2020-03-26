# with port find service 
import socket
def findServiceName():
	protocolName = "tcp"
	for port in [80,25]:
		serviceName = socket.getservbyport(port,protocolName)
		print("%s:%s" %(port,serviceName))
	serviceName = socket.getservbyport(53,'udp')
	print("9999:%s" %(serviceName))

if __name__ == "__main__":
	findServiceName()
