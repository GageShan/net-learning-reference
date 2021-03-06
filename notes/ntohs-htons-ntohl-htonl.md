
了解这4个方法之前，先说说大端字节序（BE，big-endian）和小端字节序（LE，little-endian）。

BE：将高序字节存储在起始地址

LE：将低序字节存储在起始地址

![](https://img-blog.csdnimg.cn/20200327170947550.png)

```python
ntohs  网络字节序转换成主机字节序 s-->16-bit
htons  主机字节序转换成网络字节序 s-->15-bit
ntohl  网络->主机 l-->32-bit
htonl  主机->网络 l-->32-bit
```

通常主机字节序（x86机器）是按照小端字节序来存储的，网络字节序是按照大端字节序来存储的。在网络通信过程中，这就有必要对主机和网络字节序相互转换。

拿一个例子来说。

a = 1234（十进制）-------> 0x00--00--04--d2（十六进制）

如果a是按大端字节序存储，即a = 0x00--00--04--d2 （高序字节在前面）

否则，a = 0xd2--04--00--00（低序字节在前面）

ntohl(a) --> 网络字节序转换成主机字节序 --> 大端字节序转换成小端字节序 --> 0xd2040000

htonl(a) --> 主机字节序转换成网络字节序 --> 小端字节序转换成大端字节序 --> 0xd2040000