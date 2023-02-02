# coding=utf-8
import os

# 在此处粘贴要遍历的目录路径
path = r'C:\\Users\\Tsos2\\'


# DFS遍历函数
# 需要传入一个字符串类型的遍历地址
def DFS(file_dir):
    # 进行循环遍历
    for root, dirs, files in os.walk(file_dir):
        # # 输出当前所在的目录，以及当前目录包含的文件和文件夹
        # print('当前目录:', root)
        # # 输出当前目录下所有的目录名

        # print('目录:', dirs)
        # # 输出当前目录下所有的文件名
        # print('文件:', files)
        if len(files) == 0:
            # 有目录没文件
            print('当前目录是：' + str(root) + '，其中包含目录有' + str(dirs) + '，但并不包含文件')
        else:
            if len(dirs) == 0:
                # 有文件没目录
                print('当前目录是：' + str(root) + '，当前目录不包含目录' + '，但包含的文件为：' + str(files))
            else:
                # 都有
                print('当前目录是：' + str(root) + '，其中包含目录有' + str(dirs) + '，其中包含文件有：' + str(files))


DFS(path)
