import win32com.client


# -------------------------------------------
# 通过win32api的方式仅限于win平台，并且极有可能
# 和wps版本，excel版本存在各种不兼容问题，如果需
# 要迁移到其他的平台，一定要检查此处的配置
# -------------------------------------------
# 在对WPS进行操作时，可能造成WPS闪烁（重新打开）
# WPS的各种版本间是不兼容的，比如个人版和企业版
# -------------------------------------------

class W_Excel:
    # -------------------------------------------
    # 构造函数，必须传入Excel文件路径，可以传入Excel中
    # 的表名称（默认打开Sheet1）
    # -------------------------------------------
    def __init__(self, file, sheet='Sheet1'):
        self.xlApp = win32com.client.Dispatch('Excel.Application')
        self.xlBook = self.xlApp.Workbooks.Open(file)
        self.sheet = self.xlBook.Worksheets(sheet)
        # self.xlBook.SendMail('tsos201@outlook.com')

    # -------------------------------------------
    # 该函数可以关闭打开的文件
    # -------------------------------------------
    def close(self):  # 关闭文件
        self.xlBook.Close(SaveChanges=0)
        del self.xlApp

    def getRow(self, row):
        # return self.wb.Rows(row).Value
        return self.sheet.Rows(row)

    def getCell(self, row, col):  # 获取单元格的数据
        return self.sheet.Cells(row, col).Value

    def setCell(self, row, col, value):  # 设置单元格的数据
        self.sheet.Cells(row, col).Value = value

    def setCellformat(self, row, col):  # 设置单元格的数据
        self.sheet.Cells(row, col).Font.Size = 15  # 字体大小
        self.sheet.Cells(row, col).Font.Bold = True  # 是否黑体
        self.sheet.Cells(row, col).Name = "Arial"  # 字体类型
        self.sheet.Cells(row, col).Interior.ColorIndex = 3  # 表格背景
        self.sheet.Cells(row, col).BorderAround(1, 4)  # 表格边框
        self.sheet.Rows(3).RowHeight = 30  # 行高
        self.sheet.Cells(row, col).HorizontalAlignment = -4131  # 水平居中xlCenter
        self.sheet.Cells(row, col).VerticalAlignment = -4160  #

    def deleteRow(self, row):
        self.sheet.Rows(row).Delete()  # 删除行
        self.sheet.Columns(row).Delete()  # 删除列

    def getRange(self, row1, col1, row2, col2):  # 获得一块区域的数据，返回为一个二维元组
        """return a 2d array (i.e. tuple of tuples)"""
        return self.sheet.Range(self.sheet.Cells(row1, col1), self.sheet.Cells(row2, col2)).Value

    def addPicture(self, pictureName, Left, Top, Width, Height):  # 插入图片
        """Insert a picture in wb"""
        self.sheet.Shapes.AddPicture(pictureName, 1, 1, Left, Top, Width, Height)

    # 调用时必须指定新创建的工作表名称，可选传入插入的位置（在当前表之前/之后）
    # 如果在之前创建新表，则将location设为Before，否则设为After或不填该值
    # 另外会覆盖已经存在的表（比如一个excel表中有abc三个表，当执行
    # copySheet(b,'d')时，会将c表覆盖为d表，如果希望继续复制，可以通过循环调用
    # Next属性即可选中新创建的表
    def copySheet(self, Name, location='After'):  # 复制工作表
        if location == 'After' or location == 'after':
            self.sheet.Copy(None, self.sheet)
        else:
            if location == 'Before' or location == 'before':
                self.sheet.Copy(self.sheet)
            else:
                print("复制函数的请求参数非法，请检查参数是否正确")
        self.sheet.Next.Name = Name

    def inserRow(self, row):
        self.sheet.Rows(row).Insert(1)


if __name__ == '__main__':
    excel = W_Excel(r'C:\\Users\\Tsos2\\Desktop\\5sd5gsz中间库.xlsx', '20201013')
    # print(excel.getRow(2))
    excel.copySheet('20201020')
    # excel.inserRow(10)
