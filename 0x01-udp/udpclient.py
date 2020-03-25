from socket import *
serverName = '192.168.142.128'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
while True:
	message = input("send:")
	if message == "__":
		break
	clientSocket.sendto(message.encode(),(serverName,serverPort))
	modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
	print("receive:" + modifiedMessage.decode())
clientSocket.close()
