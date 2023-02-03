import zipfile
import os


def compress_folder_to_zip(folder_path, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path)


compress_folder_to_zip('/path/to/folder', '/path/to/zip_file.zip')
