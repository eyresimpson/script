# coding=utf-8
import os

import paramiko


class Ssh:
    client = None

    def __init__(self, ip, port, username, keyfile):
        # TODO：修改为通过密钥的方式连接
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pKeyfile = os.path.expanduser(keyfile)  # 定义key路径
        pKey = paramiko.RSAKey.from_private_key_file(pKeyfile)
        # pKey=paramiko.DSSKey.from_private_key_file(pKeyfile,password='061128')   # DSSKey方式 password是key的密码
        self.client.connect(hostname=ip, port=port, username=username, pkey=pKey)

    def __del__(self):
        self.client.close()

    def command(self, remote_cmd):
        stdin, stdout, stderr = self.client.exec_command('%s' % remote_cmd, get_pty=True)
        # stdin, stdout, stderr = client.exec_command(remote_cmd,get_pty=True)
        result = stdout.read().decode('utf-8')
        return result


ssh = Ssh("192.168.33.56", 22, "root", r"C:\Users\Tsos2\TineAine.txt")
print(ssh.command("pwd"))
