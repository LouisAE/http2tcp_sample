from http.server import BaseHTTPRequestHandler,HTTPServer
from os.path import dirname,abspath
import socket
dirs = dirname(abspath(__file__))
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.log_message(self.path)
        self.send_response(200)
        self.send_header('Content-type', 'text/plaintext')
        #允许跨域
        self.send_header('Access-Control-Allow-Origin',"*")
        self.end_headers()

        #tcp客户端
        tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #连接服务器
        serverAddr = ('127.0.0.1',8080)
        tcpClientSocket.connect(serverAddr)

        #发送数据
        #去除路径开头的斜杠
        sendData = self.path[1:].encode()

        if len(sendData)>0:
            tcpClientSocket.send(sendData)  

        #接收数据
        recvData = tcpClientSocket.recv(1024)
        #关闭套接字
        tcpClientSocket.close()

        self.wfile.write(recvData)
        return


with HTTPServer(("127.0.0.1",81),handler) as s:
    s.serve_forever()

