# 自动化工具包
import pyautogui
import win32con
import win32gui
import win32print


# 要继承这个类
class Flow:
    # 操作器单元
    operation = None

    def __init__(self, operationType="Windows"):
        if operationType == "Windows":
            self.operation = WindowsOperation()
        if operationType == "Linux":
            self.operation = LinuxOperation()
        if operationType == "Command":
            self.operation = CommandOperation()

    # 重写此方法
    def mainFlow(self):
        # 在此处开始编写您的代码
        pass

    # 可以重写此方法以测试功能
    def testFlow(self):
        pass


# Windows操作器
# @Author   Tineaine
# @Version  1.0.0
# 注意，此版本仅对Windows10进行过测试，在其他平台应用前务必进行测试
class WindowsOperation:
    resolution = None
    mouse = None

    def get_real_resolution(self):
        hDC = win32gui.GetDC(0)
        # 横向分辨率
        w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
        # 纵向分辨率
        h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
        return w, h

    def __init__(self):
        # 获取屏幕分辨率
        self.resolution = self.get_real_resolution()

    # 使鼠标移动到指定的坐标
    # 参数（x坐标，y坐标，移动时间：默认为0）
    def move_to_point(self, point_x, point_y, time_l=0):
        pyautogui.moveTo(point_x, point_y, time_l)

    # 使鼠标移动到屏幕的指定百分比
    def move_to_percentage(self, percentage_x, percentage_y, time_l=0):
        real_point_x = self.resolution[0] * percentage_x
        real_point_y = self.resolution[1] * percentage_y
        self.move_to_point(real_point_x, real_point_y, time_l)

    # 根据像素进行模拟点击
    def click_with_point(self, point_x, point_y, move_time=0, key="left"):
        self.move_to_point(point_x, point_y, move_time)
        pyautogui.click(button=key)

    # 根据像素比（百分比）进行模拟点击
    # 无论x轴还是y轴都绝对不能大于1
    def click_with_percentage(self, percentage_x, percentage_y, move_time=0, key="left"):
        # 首先将百分比转为分辨率
        real_point_x = self.resolution[0] * percentage_x
        real_point_y = self.resolution[1] * percentage_y
        self.click_with_point(real_point_x, real_point_y, move_time, key=key)

    # 获取鼠标所在坐标
    def get_mouse_point(self):
        currentMouseX, currentMouseY = pyautogui.position()
        return currentMouseX, currentMouseY

    # 获取鼠标所在屏幕百分比
    def get_mouse_percentage(self):
        real_point_x, real_point_y = self.get_mouse_point()
        return real_point_x / self.resolution[0], real_point_y / self.resolution[1]

    def get_point_color(self, point_x, point_y):
        return pyautogui.screenshot().getpixel((point_x, point_y))

    def get_percentage_color(self, percentage_x, percentage_y):
        real_point_x = self.resolution[0] * percentage_x
        real_point_y = self.resolution[1] * percentage_y
        return self.get_point_color(real_point_x, real_point_y)


# Linux操作器
class LinuxOperation:
    pass


# 命令操作器
class CommandOperation:
    pass


if __name__ == '__main__':
    from pywinauto import Desktop, Application

    Application().start('explorer.exe "C:\\Program Files"')

    # connect to another process spawned by explorer.exe
    # Note: make sure the script is running as Administrator!
    app = Application(backend="uia").connect(path="explorer.exe", title="Program Files")

    app.ProgramFiles.set_focus()
    common_files = app.ProgramFiles.ItemsView.get_item('Common Files')
    common_files.right_click_input()
    app.ContextMenu.Properties.invoke()

    # this dialog is open in another process (Desktop object doesn't rely on any process id)
    Properties = Desktop(backend='uia').Common_Files_Properties
    Properties.print_control_identifiers()
    Properties.Cancel.click()
    Properties.wait_not('visible')  # make sure the dialog is closede_keys("pywinauto Works!", with_spaces=True)
