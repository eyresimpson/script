import os
import shutil


def move_files_by_extension(src_folder):
    for dirpath, dirnames, filenames in os.walk(src_folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            ext = os.path.splitext(filename)[1][1:]
            dest_folder = os.path.join(dst_folder, ext)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            shutil.move(file_path, os.path.join(dest_folder, filename))


src_folder = 'E:\\其他'
dst_folder = 'E:\\航拍'

move_files_by_extension(src_folder)
