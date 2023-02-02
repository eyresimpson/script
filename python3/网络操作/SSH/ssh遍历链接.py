import os, shutil

# 下载目录
filePath = r"/usr/local/"

# 目标目录（存放文档的目录）
targetPath = r"/usr/local/test/"

# 获取下载目录下所有文件名
pathDir = os.listdir(filePath)
# 循环每一个文件名，并对该文件名进行判断，判断是否为需要的文件
for path in pathDir:
    # 这个try主要用于捕获split的异常（其他文件可能没有分割符，无法被分割，所有可能出现数组越界）
    try:
        # 判断是否为xxx，如果是则移动到指定目录
        # split分割的是目录中的分割符，并不一定是这个，记不清了
        # split得到的数组中记得选择元素
        # 之后的每一个都可以这样做
        if path.split('_')[1].__eq__("00013330"):
            # 移动文件，第一个参数是源文件，后一个参数是目标目录
            shutil.move(filePath + "\\" + path, targetPath)

        # 判断是否为xxx，如果是则移动到指定目录
        if path.split('_')[1].__eq__("00013330"):
            # 移动文件，第一个参数是源文件，后一个参数是目标目录
            shutil.move(filePath + "\\" + path, targetPath)

        # 判断是否为xxx，如果是则移动到指定目录
        if path.split('_')[1].__eq__("00013330"):
            # 移动文件，第一个参数是源文件，后一个参数是目标目录
            shutil.move(filePath + "\\" + path, targetPath)

        # 判断是否为xxx，如果是则移动到指定目录
        if path.split('_')[1].__eq__("00013330"):
            # 移动文件，第一个参数是源文件，后一个参数是目标目录
            shutil.move(filePath + "\\" + path, targetPath)

        # 判断是否为xxx，如果是则移动到指定目录
        if path.split('_')[1].__eq__("00013330"):
            # 移动文件，第一个参数是源文件，后一个参数是目标目录
            shutil.move(filePath + "\\" + path, targetPath)
    except:
        pass
