import win32clipboard as w
import win32con


# Version: 1.0.0
# Date: 2020-07-21

# 修改剪贴板内容
# 传入需要的值即可修改剪贴板
# 使用时直接将此函数复制即可，通过传入要写入到剪贴板的字符串来调用
def setClipboard(Str):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, Str)
    w.CloseClipboard()


# 调用测试
setClipboard("Text")
