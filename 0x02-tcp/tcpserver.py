from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(55555) # 监听来自客户端的请求，参数为最大连接数
print("the server is ready to receive")
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(2048).decode()
	print("receive:" + sentence)
	sentence = input("send:")
	connectionSocket.send(sentence.encode())
	connectionSocket.close()
serverSocket.close()
	

