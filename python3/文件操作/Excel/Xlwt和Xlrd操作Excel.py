import xlrd


# 如果需要对Xls文件进行操作，使用xlwt和xlrd实现
# 也可以打开xlsx文件，当然也允许在excel或wps打开的情况下进行操作
# 但通常不建议这样做
class Excel_Xls:
    # Excel表格文件的路径
    _path = ''
    # Excel文件中要打开的表路径
    _sheet = ''
    # 存储读取到的文件
    _file = None
    # 存储读取到的表格
    _table = None

    # 初始化函数，将会在此处打开Excel文件，必须为其提供打开的文件路径，可选提供要打开的表
    def __init__(self, path, sheet=0):
        self._path = path
        self._sheet = sheet
        try:
            # 打开文件
            excel = xlrd.open_workbook(self._path, formatting_info=True)
        except:
            print("没有找到 " + self._path + " ，请检查该文件是否存在")
        self._file = excel
        # 找不到表（表不存在）异常捕获
        try:
            sheets = excel.sheet_by_index(sheet)
            self._table = sheets
            # print(sheets.row_values(2))
        except:
            print("没有找到指定的表，请检查要打开的表是否存在，是否为空")

    # 读取整行
    def getRow(self, row):
        try:
            return self._table.row_values(row)
        except:
            print("未发现该行数据，可能是数据表中不存在该数据，或文件打开错误")

    # 读取整列
    def getCol(self, col):
        try:
            return self._table.col_values(col)
        except:
            print("未发现该行数据，请检查该行是否存在，或打开的文件是否正确")

    # 读取单元格
    def getCell(self, row, col):
        try:
            cell = self._table.cell(row, col)
            cell_value = cell.value
            if cell.ctype in (2, 3) and int(cell_value) == cell_value:
                cell_value = int(cell_value)
            return cell_value
        except:
            print("该单元格似乎不存在，请检查输入和正在打开的文件是否正确")

    # 写出整行
    def putRow(self, row, val):
        pass

    # 写出整列
    def putCol(self, col, val):
        pass

    # 写出单元格
    def putCell(self, row, col, val):
        pass

    # 全文替换
    def replace(self, raw, ret):
        pass

    # 文件保存
    # 默认保存到打开的文件打开的表中
    def save(self, path=_path, sheet=_sheet):
        pass


if __name__ == '__main__':
    # -- Xls 测试 -- #
    excel = Excel_Xls(r'C://Users//Tsos2//Desktop//raw_1.xlsx')
    # 读取整行，返回数组
    # print(excel.getRow(1))
    # 读取整列，返回数组
    # print(excel.getCol(2))
    # 读取单元格
    print(excel.getCell(1, 10))
