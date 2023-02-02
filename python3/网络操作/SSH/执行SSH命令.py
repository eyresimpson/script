#!/usr/bin/python
# ssh
import os

import paramiko

host = '192.168.66.53'
user = 'root'
s = paramiko.SSHClient()
s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
privatekeyfile = os.path.expanduser(r'C:/Users/Tsos2/Desktop/TineAine.txt')  # 定义key路径
mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
# mykey=paramiko.DSSKey.from_private_key_file(privatekeyfile,password='061128')   # DSSKey方式 password是key的密码
s.connect(host, 22, user, pkey=mykey, timeout=5)

# 接受用户输入，并向用户返回结果
while True:
    cmd = input("请输入命令行：")
    if cmd == "exit":
        break
    cmd = cmd + "> runCache"
    s.exec_command(cmd)
    stdin, stdout, stderr = s.exec_command("cat runCache")
    cmd_result = stdout.read().decode('utf-8')

    # print(ssh.command("ping " + Host + " -q -f -c 5 > outCatch.txt"))
    # 从临时文件中获取数据 range(5)
    # result = ssh.command("sed -n '4, 4p' outCatch.txt")
    print(cmd_result)
s.close()
