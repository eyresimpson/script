import http.server
import socketserver

# 设置端口号
PORT = 8099

# 创建 HTTP 请求处理程序
Handler = http.server.SimpleHTTPRequestHandler

# 创建一个服务器
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    # 输出提示信息
    print("serving at port", PORT)
    # 以阻塞模式处理请求
    httpd.serve_forever()
