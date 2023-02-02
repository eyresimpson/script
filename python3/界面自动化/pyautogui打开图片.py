import pyautogui

# 等待3秒，让用户可以移动鼠标到需要操作的窗口
pyautogui.PAUSE = 3

# 在文件管理器中找到图片文件并点击打开
pyautogui.hotkey('winleft', 'e')
pyautogui.typewrite('pictures')
pyautogui.hotkey('enter')
pyautogui.typewrite('my_picture.jpg')
pyautogui.hotkey('enter')
