# get remote machine info
import socket
def getRemoteMachineInfo():
	domain = "www.github.com"
	try:
		ip = socket.gethostbyname(domain)
		print("%s'ip is %s" %(domain,ip))
	except socket.error as err_msg:
		print("%s: %s" %(domain,err_msg))

if __name__ == '__main__':
	getRemoteMachineInfo()
