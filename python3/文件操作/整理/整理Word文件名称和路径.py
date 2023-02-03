import os
import xlwt


def record_word_files(folder_path):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('word_files')

    row = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.doc') or file.endswith('.docx'):
                file_path = os.path.join(root, file)
                worksheet.write(row, 0, file_path)
                worksheet.write(row, 1, file)
                row += 1

    workbook.save('word_files.xls')


record_word_files('E:\\')
