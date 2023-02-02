#!/usr/bin/env python3
import psutil


class SystemInfo:

    @staticmethod
    def memissue():
        print('内存：')
        mem = psutil.virtual_memory()
        # 换算到MB
        memtotal = mem.total / 1024 / 1024
        memused = mem.used / 1024 / 1024
        membaifen = str(mem.used / mem.total * 100) + '%'
        print('%.2fMB' % memused)
        print('%.2fMB' % memtotal)
        print(membaifen)

    @staticmethod
    def cuplist():
        print('磁盘信息：')
        disk = psutil.disk_partitions()
        diskuse = psutil.disk_usage('/')
        # 单位换算为GB
        diskused = diskuse.used / 1024 / 1024 / 1024
        disktotal = diskuse.total / 1024 / 1024 / 1024
        diskbaifen = diskused / disktotal * 100
        print('%.2fGB' % diskused)
        print('%.2fGB' % disktotal)
        print('%.2f' % diskbaifen)


SystemInfo.memissue()
print('*******************')
SystemInfo.cuplist()
