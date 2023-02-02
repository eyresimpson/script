from docx import Document


cp = 'xx公司'
yn1 = '□'
yn2 = '🗹'
year = '2020'
month = '7'
day = '12'
bank = 'asd'
n_year = '2020'
n_month = '7'
n_day = '29'


replace_dict = {
    "(1)": cp,
    "(2)": yn1,
    "(3)": yn2,
    "(4)": year,
    "(5)": month,
    "(6)": day,
    "(7)": bank,
    "(8)": n_year,
    "(9)": n_month,
    "(10)": n_day
}

def check_and_change(document, replace_dict):
    """
    遍历word中的所有 paragraphs，在每一段中发现含有key 的内容，就替换为 value 。
    （key 和 value 都是replace_dict中的键值对。）
    """
    for para in document.paragraphs:
        for i in range(len(para.runs)):
            for key, value in replace_dict.items():
                if key in para.runs[i].text:
                    print(key + "-->" + value)
                    para.runs[i].text = para.runs[i].text.replace(key, value)
    return document


document = Document(r'D:\\xxx.docx')
document = check_and_change(document, replace_dict)
document.save("D://ccc.docx")
# document.PrintOut()
