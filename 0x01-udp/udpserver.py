from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('192.168.142.128',serverPort))
print("the server is ready to receive")
while True:
	message,clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode()
	print("receive:" + modifiedMessage)
	message = input('send:')
	if message == "__":
		break
	serverSocket.sendto(message.encode(),clientAddress)
serverSocket.close()
