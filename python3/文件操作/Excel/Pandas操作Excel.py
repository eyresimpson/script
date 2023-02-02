import pandas


class P_Excel:

    # ------------------------------------------------------
    # 构造
    def __init__(self, path):
        self.Sheet = pandas.read_excel(path, sheet_name=None, header=None)
        self.__path = path

    # ------------------------------------------------------
    # 集中定义
    # 打开Excel的路径
    __path = ''
    # 本地表格字典
    Sheet = None

    # ------------------------------------------------------
    # 对数据进行读写

    # 读取整行
    # 返回一个list集合
    def getRow(self, row, sheet='Sheet1'):
        return self.Sheet[sheet].iloc[row].tolist()

    # 读取整列
    def getCol(self, col, sheet='Sheet1'):
        return self.Sheet[sheet][col].tolist()

    # 读取单元格
    # 必须传入行列值，且必须为整数，默认读取Sheet1
    # 如果要读取其他表，请为sheet指定新值
    def getCell(self, row, col, sheet='Sheet1'):
        return self.Sheet[sheet].iat[row, col]

    # 读取部分块数据
    # 指定行列值
    def getBlock(self, row_s, row_e, col_s, col_e, sheet='Sheet1'):
        return self.Sheet[sheet].iloc[row_s:row_e, col_s:col_e]

    # 在控制台打印读取到的表格
    def print(self):
        print(self.Sheet)

    # ------------------------------------------------------
    # 获取表格信息
    # ------------------------------------------------------
    # 对数据进行分析

    # 填充NaN数据
    def cleanNan(self, sheet="Sheet1", val=''):
        self.Sheet[sheet] = self.Sheet[sheet].fillna(value=val)

    # 对整表中符合条件的数据进行替换
    def replaceSheet(self, raw, ret, sheet='Sheet1'):
        self.Sheet[sheet].replace(raw, str(ret), inplace=True)

    # ------------------------------------------------------
    # Excel外部操作
    # 将文件保存到指定的地址
    # 如果想要保存到表里，必须执行此函数，否则修改仅发生在内存中
    # 注意，Pandas不能保存样式，也就是说源表格的样式都会丢失...
    # 正常还是当做读取和分析来用吧，写出还是用其他库的实现吧
    def save(self, sheet='Sheet1'):
        self.Sheet[sheet].to_excel(self.__path, index=False, index_label=False, header=False, engine='xlsxwriter')

    # 表复制（源,目标）
    def copy(self, raw, ret):
        pass

    # 关闭Excel应用程序
    @staticmethod
    def close(Type='Excel_Pandas'):
        pass


if __name__ == '__main__':
    # -- Pandas 测试 -- #
    excel = P_Excel(r'C://Users//Tsos2//Desktop//raw_1.xlsx')
    # excel.print()
    # excel.cleanNan(val='测试')
    # excel.print()
    # print(excel.getRow(3))
    # print(excel.getCol(2))
    # print(excel.getCell(0, 0))
    # print(excel.getBlock(1, 6, 0, 1))
    # excel.replaceSheet('青岛', '莱西')
    # excel.print()
    # excel.save()
