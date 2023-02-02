import ctypes

user32 = ctypes.WinDLL('user32')
user32.ChangeDisplaySettingsW.argtypes = (ctypes.c_void_p, ctypes.c_int32)
user32.ChangeDisplaySettingsW.restype = ctypes.c_int32

disp_device = None

result = user32.EnumDisplayDevicesW(None, 0, ctypes.byref(disp_device), 0)

if result == 0 or disp_device is None:
    print("Error: could not retrieve display device")
    exit(1)

devmode = ctypes.c_void_p()

result = user32.EnumDisplaySettingsW(disp_device.DeviceName, -1, ctypes.byref(devmode))

if result == 0:
    print("Error: could not retrieve display settings")
    exit(1)

devmode.PelsWidth = 1024
devmode.PelsHeight = 768

result = user32.ChangeDisplaySettingsW(disp_device.DeviceName, 0)

if result != 0:
    print("Error: could not change display settings")
    exit(1)

print("Display resolution changed to 1024x768")
