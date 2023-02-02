import xlrd
import xlwt
from xlutils.copy import copy




# 打开想要更改的excel文件
old_excel = xlrd.open_workbook('fileName.xls', formatting_info=True)
# 将操作文件对象拷贝，变成可写的workbook对象
new_excel = copy(old_excel)
# 获得第一个sheet的对象
ws = new_excel.get_sheet(0)
# 写入数据
ws.write(0, 0, '第一行，第一列')
ws.write(0, 1, '第一行，第二列')
ws.write(0, 2, '第一行，第三列')
ws.write(1, 0, '第二行，第一列')
ws.write(1, 1, '第二行，第二列')
ws.write(1, 2, '第二行，第三列')
# 另存为excel文件，并将文件命名
new_excel.save('new_fileName.xls')
