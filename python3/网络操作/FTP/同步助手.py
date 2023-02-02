# 正向同步/仅写同步（控制端——>被控端）
# 反向同步/仅读同步（控制端<——被控端）
# 双向同步/读写同步（控制端<——>被控端）
# 同步主函数
import time

import paramiko
from watchdog.events import *
from watchdog.observers import Observer


class Sync:
    # 破晓
    # 人间世
    # 构造函数，必须为其提供需要的参数
    def __init__(self, ip, port, user, passwd):
        self.__server_ip = ip
        self.__server_port = port
        self.__user = user
        self.__passwd = passwd

    transport = paramiko.Transport(("192.168.5.128", 22))  # 获取Transport实例
    transport.connect(username="root", password="    ")  # 建立连接
    # 创建sftp对象，SFTPClient是定义怎么传输文件、怎么交互文件
    sftp = paramiko.SFTPClient.from_transport(transport)
    # 要同步的地址字典，其结构为字典格式，Key为远程路径，Value为本地路径
    # 该路径会被循环检查
    __sync = {}
    # 本地同步文件路径
    __local = []
    # 远程服务器地址
    __server_ip = ''
    # 远程服务器端口，一般不用改，默认即是22
    __server_port = 22
    # 远程服务器用户名
    __user = 'root'
    # 远程服务器密码
    __passwd = '    '

    # 增加巡查列表项
    def addsync(self, local, net):
        self.__local.append(local)
        self.__sync.update({local: net})

    # # 正向同步入口
    # def positive(self):
    #     pass
    #
    # # 反向同步入口
    # def reverse(self):
    #     pass
    #
    # # 双向同步入口
    # def bothway(self):
    #     pass

    # 巡查器,判断文件是否被修改，并做出针对性应对手段
    def start(self, local, net):
        print(local + net)
        observer = Observer()
        event_handler = FileEventHandler()
        observer.schedule(event_handler, local, True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    # 下载文件
    def download(self, net, local):
        self.sftp.get(net, local)

    def downloads(self, LocalFile, RemoteFile):  # 下载当个文件
        file_handler = open(LocalFile, 'wb')
        print(file_handler)
        self.sftp.get(RemoteFile, LocalFile)  # 下载目录中文件
        file_handler.close()
        return True

    # 上传文件
    def update(self, local, net):
        self.sftp.put(local, net)

    # 获取文件列表
    def getlist(self, net):
        pass


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            # 创建目录
            print("directory created:{0}".format(event.src_path))
        else:
            # 创建文件
            print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            # 删除目录
            print("directory deleted:{0}".format(event.src_path))
        else:
            # 删除文件
            print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            # 修改目录
            print("directory modified:{0}".format(event.src_path))
        else:
            # 修改文件
            print("file modified:{0}".format(event.src_path))

    def passed(self, types):
        pass


if __name__ == "__main__":
    s = Sync('192.168.5.128', '22', 'root', '    ')
    s.addsync(r'E:\\test', '/root/test')
    # s.start(r'E:\\test', '/root/test')
    # 4000 2600 1000 1000
    s.downloads(r'E:\\test\\mk.txt', '/root/test/mk.txt')
