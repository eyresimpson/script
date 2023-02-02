import os
import shutil
from datetime import datetime


def move_files_by_creation_time(src_folder, dst_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_ctime = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d')
            dst_path = os.path.join(dst_folder, file_ctime, file)
            if not os.path.exists(os.path.dirname(dst_path)):
                os.makedirs(os.path.dirname(dst_path))
            shutil.move(file_path, dst_path)


src_folder = 'E:\\航拍'
dst_folder = 'E:\\其他'

move_files_by_creation_time(src_folder, dst_folder)
