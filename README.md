# http2tcp_sample
使用php,把浏览器通过http发送的数据转发到tcp后端
## 说明
服务端软件（如nginx） 监听80端口

tcp服务器 监听8081端口
___

- 在输入框中输入任意数据
- 浏览器中点击“发送”按钮后，通过jquery post函数向tcp.php发送http POST请求，body是输入框中的数据。
- tcp服务器接收到"test"指令后返回"OK"
- 前端接收到"OK",并显示
