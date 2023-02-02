import os
from PIL import Image


def convert_to_jpg(dir_path):
    for filename in os.listdir(dir_path):
        if filename.endswith(".png"):
            img = Image.open(os.path.join(dir_path, filename))
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            img.save(os.path.join(dir_path, new_filename), "JPEG")


dir_path = "/path/to/directory"
convert_to_jpg(dir_path)
