# http2tcp_sample
## 说明
服务端软件（如nginx） 监听80端口
python http服务 监听81端口
tcp服务器 监听8080端口
___

- 浏览器中点击“开始”按钮后，通过js fetch函数向81端口发送http GET请求，uri作为请求的指令。
- python http服务接收到数据后，读取uri并转发到8080端口的tcp服务器
- tcp服务器接收到指令后返回"OK"
- 前端接收到"OK"
