# UDP套接字编程

## 套接字

不同机器上的进程之间通过套接字（socket）进行通信。如果把进程看成一套房子，那么套接字就好比是门。一个进程想和另一个进程通信时，它需要把信息推出门外，门与门之间可以通过TCP或UDP进行连接，当信息到达另一进程时，打开门，接收信息。

## UDP

UDP协议（用户数据报协议）是面向报文（无连接）的传输协议。无连接也就意味着传输不可靠（出错、丢包不重传），同时它的传输效率相对于TCP来说是很高的。通常应用在对数据准确信要求较低、速度快的领域，比如QQ，在线视频。

![使用UDP的客户-服务器程序](https://img-blog.csdnimg.cn/20200326141718357.png)

client:
```python
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
```

server:
```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
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
```