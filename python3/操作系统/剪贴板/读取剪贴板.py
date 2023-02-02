# 需要导入的库
import win32con
import win32clipboard as w


# -------------------------------------------
# 该函数可以读取剪贴板中的内容，并将读取到的结果返回
# 该功能依赖于win32con和win32clipboard库
# -------------------------------------------

# -------------------------------------------
# Author: 赵慎文
# Version: 1.0.0
# Date: 2020-07-21
# -------------------------------------------

# -------------------------------------------
# 读取剪贴板中的内容
def GetClipboard():
    w.OpenClipboard()
    t = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return t
# -------------------------------------------
# 测试结果
print(GetClipboard())
