from socket import *
serverName = '192.168.142.128'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:
	sentence = input("send:")
	if sentence == "__":
		break
	clientSocket.send(sentence.encode())
	modifiedMessage = clientSocket.recv(2048)
	print("receive:" + modifiedMessage.decode())
clientSocket.close()
