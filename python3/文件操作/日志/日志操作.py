# coding=utf-8
# ---------------------------------------------------------------------------------------------------------------

# 经典日志操作类
# 本类没有什么自定义的成分，所以使用非常简单
# 如果希望自定义，请使用“定制日志.py”

# ---------------------------------------------------------------------------------------------------------------

# -----------------------------------
# 本次改动

# DO:确立了日志的基本结构
# DO:增加了控制台打印时不同日志的颜色
# -----------------------------------

# -----------------------------------
# 下一次改进

# TODO:优化语句
# TODO:增加本地文件日志
# TODO:增加远程日志功能
# -----------------------------------

import datetime


# 具象化
class ILog:
    def __init__(self):
        pass

    def printDate(self):
        print(datetime.datetime.now().date())

    def printTime(self):
        print(datetime.datetime.now().time().strftime("%H:%M:%S"))

    def printDateTime(self):
        print("---------------------------------------------------")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("---------------------------------------------------")

    def printError(self, Code, Message):
        self.printObject("Error", Code, Message, color="red")

    def printWarring(self, Code, Message):
        self.printObject("Warring", Code, Message, color="yellow")

    def printMessage(self, Code, Message):
        self.printObject("Message", Code, Message, color="green")

    def printObject(self, OType, OCode, OMessage, color="None"):
        # print("\n")
        # self.printDateTime()
        # print(OType + ": " + str(OCode) + " Message " + OMessage)
        if color == "red":
            print("\033[31m" + OType + ": " + str(OCode) + " Message " + OMessage + "\033[0m")
        elif color == "green":
            print("\033[32m" + OType + ": " + str(OCode) + " Message " + OMessage + "\033[0m")
        elif color == "yellow":
            print("\033[33m" + OType + ": " + str(OCode) + " Message " + OMessage + "\033[0m")


# 仅用于测试，不要试图通过此入口调用
if __name__ == '__main__':
    log = ILog()
    log.printError(102, "系统无法连接到服务器，请检查您的网络是否正常")
    log.printError(103, "系统无法访问本地文件系统，请检查系统是否具有运行权限")
    log.printWarring(22, "未识别的通讯符，本次链接可能被服务器拒绝")
    log.printMessage(1, "通讯链路建立成功，系统配置同步完成")
    log.printMessage(1, "信息流传递完成")
