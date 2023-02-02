import os
import shutil


def move_files_by_type(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for filename in os.listdir(src_folder):
        src_file = os.path.join(src_folder, filename)
        if os.path.isfile(src_file):
            file_type = os.path.splitext(filename)[1][1:]
            dest_type_folder = os.path.join(dest_folder, file_type)
            if not os.path.exists(dest_type_folder):
                os.makedirs(dest_type_folder)
            dest_file = os.path.join(dest_type_folder, filename)
            shutil.move(src_file, dest_file)


src_folder = 'E:\\航拍数据'
dest_folder = 'E:\\航拍'
move_files_by_type(src_folder, dest_folder)
