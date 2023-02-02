# coding:utf-8
import winreg

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"键值")
# 获取该键的所有键值，因为没有方法可以获取键值的个数，所以只能用这种方法进行遍历
try:
    i = 0
    while 1:
        # EnumValue方法用来枚举键值，EnumKey用来枚举子键
        name, value, type = winreg.EnumValue(key, i)
        print(repr(name), value)
        i += 1
except WindowsError:
    print('error')
