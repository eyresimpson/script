import os
import time
from PIL import Image

path = '/path/to/images'  # specify the directory path of images

for filename in os.listdir(path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        image = Image.open(os.path.join(path, filename))
        try:
            exif_data = image._getexif()
            date_time = exif_data[36867]
            new_name = time.strptime(date_time, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m')
            os.rename(os.path.join(path, filename), os.path.join(path, new_name + '.jpg'))
        except:
            print('Error renaming image:', filename)
