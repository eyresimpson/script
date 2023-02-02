import pyautogui

# 等待3秒，让用户可以移动鼠标到需要操作的窗口
pyautogui.PAUSE = 3

# 打开浏览器并访问登录页面
pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('chrome')
pyautogui.hotkey('enter')
pyautogui.typewrite('https://www.example.com/login')
pyautogui.hotkey('enter')

# 在登录页面输入用户名和密码
pyautogui.typewrite('username')
pyautogui.hotkey('tab')
pyautogui.typewrite('password')
pyautogui.hotkey('enter')
