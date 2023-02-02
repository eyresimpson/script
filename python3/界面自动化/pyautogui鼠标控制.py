import pyautogui

# 获取屏幕的宽度和高度
screen_width, screen_height = pyautogui.size()

# 计算鼠标移动的目标位置
x = screen_width / 2
y = screen_height / 2

# 移动鼠标到目标位置
pyautogui.moveTo(x, y)
