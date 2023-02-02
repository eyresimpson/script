# Linux下需要的依赖
import os
# Windows下需要的依赖
import wmi

# 需要结束的进程名称
processName = "MarkText.exe"
# windows环境情况下结束进程


c = wmi.WMI()

# for process in c.Win32_Process ():   这里枚举所有进程
# #   print process.ProcessId, process.Name
#     print process.Name, "\n"
try:
    for process in c.Win32_Process(name=processName):
        # print(process.ProcessId, process.Name)
        process.Terminate()
except:
    print("已结束程序的执行！")
# Linux环境下结束进程


# tmp = os.popen("ps -af").read()
# # 读取系统上所有的进程
# gzclient_count = tmp.count('gzclient')
# if gzclient_count > 0:
#     # 如果有正在运行的gaclient进程
#     os.system("killall -9 gzclient")
