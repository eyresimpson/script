import os
import zipfile

# 要解压的文件
file = r'D:/test.zip'
# 要解压到的目录
target = r'F:/'

if not os.path.exists(target):
    os.mkdir(target)

with zipfile.ZipFile(file) as zf:
    zf.extractall(target)
# import os.path
# import zipfile
#
# # 要解压的文件
# file = r'D:/test.zip'
# # 要解压到的目录
# target = r'F:/'
#
# if not os.path.exists(target): os.mkdir(target)
# zip = zipfile.ZipFile(file)
# for name in zip.namelist():
#     name = name.replace('\\', '/')
#     if name.endswith('/'):
#         os.mkdir(os.path.join(target, name))
#     else:
#         ext_filename = os.path.join(target, name)
#         ext_dir = os.path.dirname(ext_filename)
#         if not os.path.exists(ext_dir): os.mkdir(ext_dir)
#         outfile = open(ext_filename, 'wb')
#         outfile.write(zip.read(name))
#         outfile.close()
#
