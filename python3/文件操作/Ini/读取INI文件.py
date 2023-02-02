from configobj import ConfigObj
# 标记文件位置和字符类型
config = ConfigObj("test.ini",encoding='UTF8')

# 读取section中的所有值
print(config['花园路小学'])
# 读取section中的某一个指定值
print(config['花园路小学']['校长'])
