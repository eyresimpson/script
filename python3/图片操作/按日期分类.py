import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

"""
该脚本使用 os.listdir 函数扫描指定目录中的文件，并使用 os.path.join 函数获取文件的完整路径。
如果文件是图片，则使用 Pillow 库的 Image.open 函数打开该图片，并使用 img._getexif 函数获取其 EXIF 数据。
如果图片包含拍摄时间信息（通过标记 36867 指示），则使用 datetime.strptime 函数解析该时间，并使用 os.makedirs 函数创建以年份命名的文件夹。
最后，使用 os.rename 函数将该图片移动到对应的文件夹中。
"""


def sort_images(dir_path):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    exif_data = {TAGS.get(key, key): value for key, value in img._getexif().items()}
                    if 36867 in exif_data:
                        date = exif_data[36867]
                        date = datetime.strptime(date, "%Y:%m:%d %H:%M:%S")
                        year = str(date.year)
                        year_dir = os.path.join(dir_path, year)
                        if not os.path.exists(year_dir):
                            os.makedirs(year_dir)
                        new_file_path = os.path.join(year_dir, filename)
                        os.rename(file_path, new_file_path)
            except:
                pass


dir_path = "/path/to/directory"
sort_images(dir_path)
