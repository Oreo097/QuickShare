import socket

hello="helloworld"
print(len(hello))


port =4000
HOST=bytes('192.168.31.255',encoding = "utf8")
addr=(HOST,port)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(bytes(hello,encoding = "utf8"),addr)