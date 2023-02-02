import os
import time


class OpenCME:

    @staticmethod
    def restore(type, f1, f2, f3, chars=1):
        print("-----------------------------------------------")
        print("解混淆开始时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        if type == "cme_1":
            size = int(os.path.getsize(f2)) + int(os.path.getsize(f3))

            fs1 = open(f1, 'wb+')
            fs2 = open(f2, 'rb')
            fs3 = open(f3, 'rb')

            # index = 0
            # while index <= size:
            #     if index % 2 == 0:
            #         fs1.write(fs2.read(1))
            #     else:
            #         fs1.write(fs3.read(1))
            #     index += 1

            index = 0
            while index < size:
                fs1.write(fs2.read(chars)[::-1])
                fs1.write(fs3.read(chars)[::-1])
                index += chars * 2
            print("解混淆结束时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            print("-----------------------------------------------")
            fs1.close()
            fs2.close()
            fs3.close()

    # 开始执行
    @staticmethod
    def execute(type, f1, f2, f3):
        print("-----------------------------------------------")
        print("混淆开始时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        size = int(os.path.getsize(f1))
        print("文件大小：" + str(size))
        # 2.进行混淆
        if type == "cme_1":
            # 打开文件
            fs1 = open(f1, 'rb')
            fs2 = open(f2, 'wb+')
            fs3 = open(f3, 'wb+')

            index = 0
            while index < size:
                fs2.write(fs1.read(1))
                fs3.write(fs1.read(1))
                index += 2
            print("混淆结束时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            print("-----------------------------------------------")
            fs1.close()
            fs2.close()
            fs3.close()

    # 开始执行
    @staticmethod
    def execute2(type, f1, f2, f3, chars=1):
        print("-----------------------------------------------")
        print("混淆开始时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        size = int(os.path.getsize(f1))
        print("文件大小：" + str(size))
        # 2.进行混淆
        if type == "cme_1":
            # 打开文件
            fs1 = open(f1, 'rb')
            fs2 = open(f2, 'wb+')
            fs3 = open(f3, 'wb+')

            index = 0
            while index < size:
                fs2.write(fs1.read(chars)[::-1])
                fs3.write(fs1.read(chars)[::-1])
                index += chars * 2
            print("混淆结束时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            print("-----------------------------------------------")
            fs1.close()
            fs2.close()
            fs3.close()

# 简单文件混淆
# 这些算法并非为了加密，而是为了保护用户的文件不被审查，cme系列的文件不要太小，且文件尽可能通过压缩工具先进行压缩（过大的文件会造成运算慢）
if __name__ == '__main__':
    # cme(Cut Minimum Equal)：最小公平切割，将文件平均切分，一份文件被分为偶数个文件
    #   cme_1：根据奇数位和偶数位直接切分，每个奇数位的字节放在一个文件中，每个偶数位的字节被放在另一个文件中，一般用于较为简单的筛查
    #   cme_r：随机位切分，随机将半数的字节置于另外的一个文件中，并生成一份用于恢复的Key，一般用于较为严格的检查，适用于安全的客户端
    #   cme_rs：随机群分，随机将一定百分比的字节放在一份文件中，并生成一份用于恢复的Key，cme—r的变种，会生成更多的文件，一般用于更为严格的检查，适用于安全的客户端
    type = "cme_1"
    # source_file = r"A:\Temp\\Download.rar"
    source_file = r"C:\Users\aine\Pictures\2021\2021-03-13\IMG_0015.JPG"
    restore_file = r"A:\Temp\\IMG_0004.jpg"
    target_1 = r"A:\Temp\\opt.k1"
    target_2 = r"A:\Temp\\opt.k2"
    # 切分，最大相似值越大，混淆和解混淆的速度越快，但效果便越差
    OpenCME.execute2(type, source_file, target_1, target_2, 3)
    # 还原，注意，最大相似值在混淆和解混淆时必须一致
    OpenCME.restore(type, restore_file, target_1, target_2, 3)
