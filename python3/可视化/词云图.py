# 绘制词云图
import os

import stylecloud

from 其他 import 随机起名

text1 = []
xxx = 500
while (True):
    xxx -= 1
    if xxx < 0:
        break
    else:
        text1.append(随机起名.getName())

stylecloud.gen_stylecloud(text=' '.join(text1),
                          collocations=False,
                          font_path=r'C:\Windows\Fonts\msyh.ttc',
                          icon_name='fas fa-play-circle',
                          size=653,
                          output_name='词云图.png')
os.system('词云图.png')
