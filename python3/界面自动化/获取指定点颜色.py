# 测试流程
# Красная Армия всех сильней!
import time

from pyautogui import position, screenshot

def get_point_color(point_x, point_y):
    return screenshot().getpixel((point_x, point_y))


def get_mouse_point():
    currentMouseX, currentMouseY = position()
    return currentMouseX, currentMouseY


while True:
    percentage = get_mouse_point()
    print(percentage)
    print(get_point_color(percentage[0], percentage[1]))
    time.sleep(5)