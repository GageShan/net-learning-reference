# TCP套接字编程

tcp与udp不同，tcp是面向连接，也就是说，在客户端和服务器能够相互通信之前，它们之间需要先握手和创建一个tcp连接。三次握手，即已创建了一个欢迎套接字（按照房子和门的说法，就是创建了一个欢迎之门），欢迎套接字是所有要与服务器通信的客户端的起始接触点。当客户端与服务器握手之后，客户端开始发送消息，这就会使得服务器创建一个连接套接字，它是专门对客户进行连接的新生成的套接字，发送消息通过连接套接字完成。

注意：使用tcp套接字通信并不需要为每一个分组附上目的地址，客户程序只需要将要发送的消息送入tcp连接即可。

![tcp客户服务器流程](https://img-blog.csdnimg.cn/20200326163350495.png)

client：

```python
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
```

server:

```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5) # 监听来自客户端的请求，参数为最大连接数
print("the server is ready to receive")
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(2048).decode()
	print("receive:" + sentence)
	sentence = input("send:")
	connectionSocket.send(sentence.encode())
	connectionSocket.close()
serverSocket.close()
```





