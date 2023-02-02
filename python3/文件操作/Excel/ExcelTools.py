# Excel 工具箱


# 本类提供了两种调用
import win32com.client
# 不得不用xlrd进行读取，win32调api的方式会读到很多的None
# 未来可能会尝试排除这个故障

# 我也不想把这个功能类写的这么麻烦，但确实没办法实现
import wmi
import xlrd


# 主要是pandas数据操作比较强大，所以就牺牲一点空间来获取便捷了

class S:
    # 主应用程序对象
    win32Application = None
    # 工作簿对象
    win32Workbook = None
    xlrdWorkbook = None
    # 工作表对象
    win32Worksheet = None
    xlrdWorksheet = None
    # 系统重载指示器
    reloadIndex = 0

    # 运行与加载参数
    # 当前读取的文件路径
    filePath = ""
    # 当前读取的表名
    sheetName = ""
    # 是否可见
    visible = False
    # 是否静音
    enableSound = False
    # 屏幕更新
    screenUpdating = False
    # 是否全屏
    displayFullScreen = False

    # 当前表行数
    rowCount = None
    # 当前表列数
    colCount = None

    # 构造
    def __init__(self, path, sheet, visible=False, enableSound=False, screenUpdating=False, displayFullScreen=False):
        try:
            self.filePath = path
            self.sheetName = sheet
            # win32初始化
            try:
                self.win32Application = win32com.client.Dispatch('Excel.Application')
            except:
                print("ERROR—100：初始化应用程序发现异常，请检查当前计算机中是否安装了WPS或者Office，详情请参照参考手册")
            self.win32Application.Visible = visible
            self.win32Application.enableSound = enableSound
            self.win32Application.screenUpdating = screenUpdating
            self.win32Application.displayFullScreen = displayFullScreen

            try:
                self.win32Workbook = self.win32Application.Workbooks.Open(path)
            except:
                print("ERROR-101：打开文件失败，请检查文件是否存在，或用户是否具有相关权限")
            try:
                self.win32Worksheet = self.win32Workbook.Worksheets(sheet)
            except:
                print("ERROR-102：打开表失败，请检查目标文件中是否存在指定的表")
            # xlrd
            try:
                self.xlrdWorkbook = xlrd.open_workbook(path)
            except:
                print("ERROR-103：读取文件失败，请检查文件是否存在，或用户是否具有相关权限")
            try:
                self.xlrdWorksheet = self.xlrdWorkbook.sheet_by_name(sheet)
            except:
                print("ERROR-104：读取表失败，请检查目标文件中是否存在指定的表")

            # 为类属性赋值
            # 行数
            self.rowCount = self.xlrdWorksheet.nrows
            # 列数
            self.colCount = self.xlrdWorksheet.ncols
        except:
            if self.reloadIndex == 0:
                self.reloadIndex += 1
                self.exitWPS()
                self.__init__(path, sheet)

    # 析构
    def __del__(self):
        try:
            self.win32Workbook.Close()
            self.win32Application.Quit()
        except:
            try:
                self.exitWPS()
            except:
                pass

    def exitWPS(self):
        # wmi对象
        c = wmi.WMI()
        try:
            # et是wps表格的进程名，wps中表格的部分会崩溃，因此需要预先保存数据
            for process in c.Win32_Process(name="et.exe"):
                print("ET进程被终止，返回的消息为：")
                # 打印结束的进程
                print(process.ProcessId, process.Name)
                # 结束进程
                process.Terminate()
        except:
            pass

    # 程序操作 ------------------------------------------------------------------------------------------
    # 暂时废弃，因为可以直接调用win32的API，没必要过度封装，如有需要可以根据API文档直接调用属性或方法
    # 文档操作 ------------------------------------------------------------------------------------------

    # 保存
    def save(self):
        # 直接保存，没什么好说的
        self.win32Workbook.Save()
        print("文件修改已保存！")
        # 注意，xlrd仅负责读取，没有任何写入的操作，因此不能保存
        # self.xlrdWorkbook.save()

    # 另存为
    def saveAs(self, fileName, fileFormat=51):
        # 注意，保存格式要按照API的文档进行，如果不填就是API的默认值
        # 枚举 参照随带的API手册简明版或官方的完整版
        try:
            self.win32Workbook.SaveAs(Filename=fileName, FileFormat=fileFormat)
            print("文件被另存到：", fileName)
        except:
            print("另存为失败，目标文件可能已存在，或您对目标目录没有读写权限！")

    # 切换文件/表格
    # 一般来说，切换文件（Workbook)表名也会发生改变，一定要注意这一点
    def workChange(self, path=".", sheet="."):
        if path == ".":
            path = self.filePath
        if sheet == ".":
            sheet = self.sheetName
        # 修改类对象中的值
        self.filePath = path
        self.sheetName = sheet
        # 重新生成需要的内容(win32)
        self.win32Application = win32com.client.Dispatch('Excel.Application')
        self.win32Workbook = self.win32Application.Workbooks.Open(self.filePath)
        self.win32Worksheet = self.win32Workbook.Worksheets(self.sheetName)
        # 重新生成需要的内容(xlrd)
        self.xlrdWorkbook = xlrd.open_workbook(self.filePath)
        self.xlrdWorksheet = self.xlrdWorkbook.sheet_by_name(self.sheetName)
        # 为类属性赋值
        # 行数
        self.rowCount = self.xlrdWorksheet.nrows
        # 列数
        self.colCount = self.xlrdWorksheet.ncols

    # 复制表格

    # 删除表格

    # 重命名表格

    # 打印工作表
    def printOut(self, copies=1, ignorePrintAreas=False):
        try:
            self.win32Worksheet.PrintOut(Copies=copies, IgnorePrintAreas=ignorePrintAreas)
        except:
            print("打印异常，请关注是否人为取消或打印机拒绝打印！")

    # 区域操作 ------------------------------------------------------------------------------------------
    #
    # 行操作 --------------------------------------------------------------------------------------------

    # 获取整行
    def getRows(self, Row):
        try:
            return self.xlrdWorksheet.row_values(Row)
        except:
            print("通过xlrd获取行失败，请检查是否越界（从1开始）")

    # 写出整列
    def putRows(self):
        pass

    # 设置指定行的高度
    # 秋色说不尽，月落叶有霜
    # 如果pounds的值为auto，那么会根据内容自动设置（自适应）
    def setRowHeight(self, row, pounds):
        if pounds == 'auto' or pounds == 'Auto':
            self.win32Worksheet.Rows(row).AutoFit()
        else:
            self.win32Worksheet.Rows(row).RowHeight = pounds

    # 设置所有行的高度
    # 如果pounds的值为auto，那么会根据内容自动设置（自适应）
    def setRowsHeight(self, pounds):
        if pounds == 'auto' or pounds == 'Auto':
            self.win32Worksheet.Rows.AutoFit()
        else:
            self.win32Worksheet.Rows.RowHeight = pounds

    # 列操作 --------------------------------------------------------------------------------------------

    # 获取整列
    def getCol(self, col):
        return self.xlrdWorksheet.col_values(col)

    # 写出整列
    def putCol(self):
        pass

    # 设置指定列的宽度
    # 如果pounds的值为auto，那么会根据内容自动设置（自适应）
    def setColWidth(self, col, pounds):
        if pounds == 'auto' or pounds == 'Auto':
            self.win32Worksheet.Columns(col).AutoFit()
        else:
            self.win32Worksheet.Columns(col).ColumnWidth = pounds

    # 设置所有列的宽度
    # 如果pounds的值为auto，那么会根据内容自动设置（自适应）
    def setColsWidth(self, pounds):
        if pounds == 'auto' or pounds == 'Auto':
            self.win32Worksheet.Columns.AutoFit()
        else:
            self.win32Worksheet.Columns.ColumnWidth = pounds

    # 列筛选
    def setAutoFilter(self):
        self.win32Worksheet.EnableAutoFilter = True
        print(self.win32Worksheet.AutoFilter.Creator)

    # 界面操作 ------------------------------------------------------------------------------------------

    # 单元格操作 -----------------------------------------------------------------------------------------

    # 读取单元格(xlrd)
    # 输入（行，列）
    # 行和列的下标从1开始（注意不是从0）
    def getCell_x(self, row, col):
        return self.xlrdWorksheet.cell(row - 1, col - 1).value

    # 读取单元格(win32)
    # 输入（行，列）
    # 行和列的下标从1开始（注意不是从0）
    def getCell_w(self, row, col):
        return self.win32Worksheet.Cells(row, col)

    # 写出单元格
    def putCell(self, row, col, val):
        self.win32Worksheet.Cells(row, col).Value = val


if __name__ == '__main__':
    # S.getRows(Am.Workbooks.Open(r'C:\Users\Tsos2\Desktop\raw_1.xlsx').Worksheets('20200912'), 1)
    sss = S(r'C:\Users\Tsos2\Desktop\raw_1.xlsx', '20200912', visible=True, screenUpdating=True)
    sss.win32Application.Dialogs.Item(127).Show()
    # sss.setAutoFilter()
    # sss.putCell(10, 10, '123')
    # sss.setRowsHeight('Auto')
    # sss.setColsWidth("Auto")
    # sss.save()
    # sss.printOut()
    # sss.win32Application.Dialogs.Item(188).Show()
    # sss.win32Application.Dialogs.Item(188).Show(None, None, True)
    # sss.saveAs(r"c:\Users\Tsos2\Desktop\raw_1.xlsx")
    # print(sss.getRows(5))
    # sss.workChange(sheet='20200824')
    # print(sss.getRows(5))
    # sss.workChange(path =r'C:\Users\Tsos2\Desktop\raw_2.xlsx',sheet='Sheet2')
    # print(sss.getRows(6))