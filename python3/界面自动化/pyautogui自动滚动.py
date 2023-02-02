import pyautogui

# 注意很多情况下此程序会受到各种中文输入法的影响，导致enter键无法使用/失效/输入错乱，可可考虑切换为英文状态

# 等待3秒，让用户可以移动鼠标到需要操作的窗口
pyautogui.PAUSE = 3

# 访问一个长页面
pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('msedge')
pyautogui.hotkey('enter')
pyautogui.typewrite('https://www.zhihu.com/')
pyautogui.hotkey('enter')

# 滚动页面
for i in range(100):
    pyautogui.hotkey('pagedown')
