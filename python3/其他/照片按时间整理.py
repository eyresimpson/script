import datetime
import os
import re

import exifread


class Pic:
    # path：源路径，可以是最外层的文件夹，会自动迭代下级所有图片文件
    # target：目标路径，必须是一个空白文件夹，会自动以 XXXX年/XX月 格式创建文件夹
    # noDateExecuteType：无日期照片处理方式，default(按修改日期/创建日期处理)；other(将所有无日期的照片放在同一个文件夹里)
    # 注意，日期的判断依据是照片的日期时间来判断的，如果照片中没有相关日期信息
    @staticmethod
    def collation_by_datetime(path, target, no_date_execute_type="default"):
        imgType_list = {'jpg', 'bmp', 'png', 'jpeg', 'rgb', 'tif'}
        for root, dirs, files in os.walk(path):
            # 遍历所有文件
            for file in files:
                # 如果文件的后缀名为图片类型
                if (file.lower().endswith(
                        ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff'))):
                    try:
                        print("尝试打开 " + os.path.join(path, file))
                        # 打开文件
                        fd = open(os.path.join(path, file), 'rb')
                    except IOError:
                        print("无法打开文件，请检查文件状态是否正常！")
                        print("!------------------------> 已跳过一个无法打开的文件")
                        # return
                    # 关闭文件读取流
                    fd.close()
                    # 读取文件的EXIF信息
                    try:
                        tags = exifread.process_file(fd)
                    except:
                        tags = []
                    # 判断是否有EXIF信息（部分文件可能因为隐私等原因删除了该信息）
                    if 'EXIF DateTimeOriginal' in tags:
                        # 获取日期
                        date = str(tags['EXIF DateTimeOriginal']).split(" ")[0].split(":")
                        # 获取时间
                        time = str(tags['EXIF DateTimeOriginal']).split(" ")[1].split(":")
                        print(date[0] + "年" + date[1] + "月" + date[2] + "日 " + time[0] + "时" + time[1] + "分" + time[
                            2] + "秒")
                        # TODO:尝试复制到指定文件夹
                        # pass
                    else:
                        print("无法获取EXIF信息，尝试使用文件名中的日期进行匹配")
                        m = re.search("(\d{4}\d{1,2}\d{1,2})", file.lower())
                        try:
                            strdate = m.group(1)
                        except:
                            print("无法从文件名中获取日期...跳过")

                        print("--------------> 按文件名获取的日期为:" + strdate)
                        date = datetime.datetime.strptime(strdate, '%YYYY%mm%dd')
                        print("--------------> 按文件名获取的日期为:" + strdate)


# @staticmethod
# def getExif(path, filename):
#     old_full_file_name = os.path.join(imgpath, filename)
#     FIELD = 'EXIF DateTimeOriginal'
#     fd = open(old_full_file_name, 'rb')
#     tags = exifread.process_file(fd)
#     fd.close()
#     # 显示图片所有的exif信息
#     # print("showing res of getExif: \n")
#     # print(tags)
#     # print("\n\n\n\n");
#     if FIELD in tags:
#         print("\nstr(tags[FIELD]): %s" % (str(tags[FIELD])))  # 获取到的结果格式类似为：2018:12:07 03:10:34
#         print("\nstr(tags[FIELD]).replace(':', '').replace(' ', '_'): %s" % (
#             str(tags[FIELD]).replace(':', '').replace(' ', '_')))  # 获取结果格式类似为：20181207_031034
#         print("\nos.path.splitext(filename)[1]: %s" % (os.path.splitext(filename)[1]))  # 获取了图片的格式，结果类似为：.jpg
#         new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + os.path.splitext(filename)[1]
#         print("\nnew_name: %s" % (new_name))  # 20181207_031034.jpg
#
#         time = new_name.split(".")[0][:13]
#         new_name2 = new_name.split(".")[0][:8] + '_' + filename
#         print("\nfilename: %s" % filename)
#         print("\n%s的拍摄时间是: %s年%s月%s日%s时%s分" % (filename, time[0:4], time[4:6], time[6:8], time[9:11], time[11:13]))
#
#         # 可对图片进行重命名
#         new_full_file_name = os.path.join(imgpath, new_name2)
#         # print(old_full_file_name," ---> ", new_full_file_name)
#         # os.rename(old_full_file_name, new_full_file_name)
#     else:
#         print('No {} found'.format(FIELD), ' in: ', old_full_file_name)

if __name__ == '__main__':
    Pic.collation_by_datetime("E:\\Data\\Picture", "")
