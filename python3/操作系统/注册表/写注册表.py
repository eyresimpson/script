import winreg

# 打开注册表项
registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\MyApp", 0, winreg.KEY_WRITE)

# 创建注册表值
winreg.SetValueEx(registry_key, "MyValue", 0, winreg.REG_SZ, "MyValueData")

# 关闭注册表项
winreg.CloseKey(registry_key)
