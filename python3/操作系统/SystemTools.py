# 对windows适用的工具类
import os

import win32api
import win32clipboard as w
import win32con
import win32gui
import win32print


class Windows:
    # 读取当前剪贴板中的内容
    def getClipboard(self):
        w.OpenClipboard()
        t = w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
        return t

    # 写入剪贴板的内容
    def setClipboard(self, Str):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, Str)
        w.CloseClipboard()

    def getRealResolution(self):
        hDC = win32gui.GetDC(0)
        # 横向分辨率
        w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
        # 纵向分辨率
        h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
        return w, h

    # # 获取默认分辨率（可能被缩放）
    def getScreenSize(self):
        w = win32api.GetSystemMetrics(0)
        h = win32api.GetSystemMetrics(1)
        return w, h

    # ----------------------------------------------------------------
    # 获取环境变量
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # 设置永久的环境变量
    # variableType：类型，True代表系统变量，False代表用户变量
    # key：键，如JAVA_HOME、PATH都可以被称为一个键值
    # value：值，如C://Program/，代表键的值
    # ！！！！！！！！！！！！注意！！！！！！！！！！！！
    #       没有重名的键会新建，有重名的键会替换
    #       没有重名的键会新建，有重名的键会替换
    #       没有重名的键会新建，有重名的键会替换
    # ！！！！！！！！！！！！注意！！！！！！！！！！！！
    # 也就是说如果你想修改Path的值，一定要先get到旧值
    # 再添加新值，否则Path的所有内容都会被覆盖
    # ！！！！！！！！！！！！！！！！！！！！！！！！！！
    # ----------------------------------------------------------------
    # 开发者：Tine Aine
    # 版本号：1.0.0
    # 维护日期：2020年11月2日14:21:42
    # ----------------------------------------------------------------
    def setPerpetualEnvironmentVariable(self, variableType, key, value):
        if variableType:
            # 需要管理员权限才能正常执行
            command = r"setx %s %s /m" % (key, value)
        else:
            command = r"setx %s %s" % (key, value)
        os.system(command)
        # print(command)

    def setTemporaryEnvironmentVariable(self, variableType, key, value):
        pass

    def getEnvironmentVariable(self, key):
        return os.getenv(key)

    # 获取系统环境信息
    # HOMEPATH，    当前用户主目录
    # TEMP          临时目录路径
    # PATHEXT       可执行文件
    # SYSTEMROOT    系统主目录
    # LOGONSERVER   机器名
    # PROMPT        设置提示符
    #
    def getSystemEnvironmentInformation(self, information):
        return os.environ[information]


# 对Linux适用的工具类
class Linux:
    pass


if __name__ == '__main__':
    windows = Windows()
    # windows.setPerpetualEnvironmentVariable(True, "MIUI12", "C://System32/Library/")

    text = windows.getEnvironmentVariable("JAVA_HOME")
    print(text)
