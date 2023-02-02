import os

import win32com
from self import self
from win32com.client import Dispatch

# --------------------------------------------------------
# -- 需要修改的参数
# --------------------------------------------------------
# 获取当前工作目录(仅在测试中使用，具体使用可以注释掉，并修改open_file为要打开的word文档地址即可)
path = os.getcwd() + r'/Aine.docx'
# 要打开的文件
open_file = path
# 要保存到的位置
save_file = path
# 指示系统中文档的处理工具
# 如果使用word
exec_tool = 'Word.Application'
# 如果使用wps
# exec_tool = 'wps.application'

# 指示运行的版本，如果是WPS应修改为
word = win32com.client.Dispatch(exec_tool)
# 在后台运行程序
word.Visible = 0  # 后台运行，不显示
# 运行过程不警告
word.DisplayAlerts = 0  # 不警告
# 打开word文档
doc = word.Documents.Open(open_file)


# 文档替换函数
def replace_doc(old_string, new_string):
    word.Selection.Find.ClearFormatting()
    word.Selection.Find.Replacement.ClearFormatting()
    # ------------------------------------------------------
    # 此函数设计到可能出现的各种情况，请酌情修改
    # Execute(
    #         旧字符串，表示要进行替换的字符串
    #         区分大小写：这个好理解，就是大小写对其也有影响
    #         完全匹配：也就意味着不会替换单词中部分符合的内容
    #         使用通配符
    #         同等音
    #         包括单词的所有形态
    #         倒序
    #         1（不清楚是做什么的）
    #         包含格式
    #         新的文本
    #         要替换的数量，0表示不进行替换，1表示仅替换一个
    # ------------------------------------------------------
    word.Selection.Find.Execute(old_string, False, False, False, False, False, True, 1, True, new_string, 2)


# --------------------------------------------------------
# -- 在此处添加对word文件的修改
# --------------------------------------------------------
# 把文档中的Aine字符串替换为Kine字符串
replace_doc('Aine', 'Kine')
# 把文档中的Tine字符串替换为Cine字符串
replace_doc('Tine', 'Cine')
# --------------------------------------------------------
# -- 最后操作保存
# --------------------------------------------------------
# 保存对Word文件所进行的修改
doc.SaveAs(save_file)

# 打印文件
# doc.PrintOut()

# 关闭文件
doc.Close()
# 退出word
word.Quit()
