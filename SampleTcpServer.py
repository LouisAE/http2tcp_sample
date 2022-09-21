#!/bin/python3 
import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 8080   

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#服务器监听的ip和端口号
server.bind((bind_ip,bind_port))

print("[*] Listening on %s:%d" % (bind_ip,bind_port))

#最大连接数
server.listen(5)

#接收客户端数据
def handle_client(client_socket):

    request = client_socket.recv(1024)
    
    
    #输出接收到的请求
    print("[*] Received: %s" % request)
    #收到开启指令时，向客户端返回OK
    if request.decode("utf-8") == "start":
        client_socket.send("OK".encode())
    else:
        pass
     
    client_socket.close()

while True:

    #等待客户连接，连接成功后，将socket对象保存到client，将细节数据等保存到addr
    client,addr = server.accept()

    print("[*] Acception connection from %s:%d" % (addr[0],addr[1]))

    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
