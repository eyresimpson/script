import wmi
import xlwings as xw


# 使用注意：
# 在运行前一定要保存wps中正在进行的工作，程序启动后会强行关闭wps
# 此模块的优势：
# 运行速度较快，仅慢于Win32Api
# 几乎不需要考虑兼容性问题（Office/WPS）
# 此模块的劣势
# 使用前必须关闭WPS（保存可能失败）
# 在执行时会独占WPS程序
class X_Excel:
    application = None
    # 最好不要改动，否则可能出现各种Bug
    wb = None
    path = ''

    # 构造函数
    def __init__(self, path, isVisible=False, addBook=False, displayAlerts=False, ScreenUpdating=False):
        # 结束掉wps的进程
        self.exitWPS()
        # visible这里设置为不显示界面，如果为True会在前台显示调用
        # add_book指的是是否增加新的工作表，一般修改的话直接设为False即可
        self.application = xw.App(visible=isVisible, add_book=addBook)
        # 最好不要改动，否则可能出现各种Bug
        self.application.display_alerts = displayAlerts
        self.application.screen_updating = ScreenUpdating
        # 路径赋值（保存可能用到）
        self.path = path
        # 打开文档
        self.wb = self.application.books.open(path)

    # ------------------------------------------------------------
    # Excel操作
    # ------------------------------------------------------------

    # 保存文件到硬盘
    # 默认保存到原文件，但有可能出现只读异常
    def save(self, file=' '):
        if file == ' ':
            file = self.path
        self.wb.save(file)

    # 关闭表格，以防止其他对象打开时出现问题
    # 如果需要可以调用，但通常该对象销毁时会自动调用
    def exit(self):
        self.wb.close()
        self.application.quit()
        self.exitWPS()

    # ------------------------------------------------------------
    # 数据表操作
    # ------------------------------------------------------------

    # 清空整个工作表（不是整个文件）
    def cleanSheet(self, sheet='Sheet1'):
        self.wb.sheets[sheet].clear()

    # ------------------------------------------------------------
    # 数据行操作
    # ------------------------------------------------------------

    # 获取整行

    # ------------------------------------------------------------
    # 数据列操作
    # ------------------------------------------------------------

    # 获取整列

    # ------------------------------------------------------------
    # 单元格操作
    # ------------------------------------------------------------

    # 为单元格赋值
    def putCell(self, location, val, sheet="Sheet1"):
        self.wb.sheets[sheet].range(location).value = val

    # 单元格填充颜色
    def fillColor(self, R, G, B, cell, sheet='Sheet1'):
        self.wb.sheets[sheet][cell].color = (R, G, B)

    # 为单元格添加超链接
    def hyperlink(self, cell, text, linkto, sheet='Sheet1'):
        self.wb.sheets[sheet][cell].add_hyperlink(linkto, text, '点击传送')

    # ------------------------------------------------------------
    # 系统操作
    # ------------------------------------------------------------

    def exitWPS(self):
        c = wmi.WMI()
        try:
            # et是wps表格的进程名，wps中表格的部分会崩溃，因此需要预先保存数据
            for process in c.Win32_Process(name="et.exe"):
                # 打印结束的进程
                print(process.ProcessId, process.Name)
                # 结束进程
                process.Terminate()
        except:
            pass


# ------------------------------------------------------------
# 主入口
# ------------------------------------------------------------
if __name__ == '__main__':
    # 本类的使用方法：
    # 实例化对象，并传入要打开的文件路径
    excel = X_Excel(r"C:\Users\Tsos2\Desktop\FillColor.xlsx", isVisible=False, displayAlerts=False,
                    ScreenUpdating=False)
    # 调用功能函数
    # excel.hyperlink('A1', 'sss', 'www.baidu.com')

    # 保存文件，如果为空，则视为修改；如果有数据，则视为另存为
    excel.save()
    # 必须调用这个方法，否则可能造成wps打不开文件的现象
    excel.exit()
