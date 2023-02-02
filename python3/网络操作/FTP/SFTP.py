import paramiko

# 远程服务器登录IP和端口
transport = paramiko.Transport(("192.168.5.128", 22))
# 远程服务器用户名和密码
transport.connect(username="username", password="passwd")
# 创建sftp
sftp = paramiko.SFTPClient.from_transport(transport)
# 文件上传
sftp.put("E:/aaa.ico", "/www/aaa.ico")
# 文件下载
sftp.get("/root/a.sh", "E:/a.py")
# 关闭SFTP的链接
transport.close()