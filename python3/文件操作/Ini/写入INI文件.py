from configobj import ConfigObj
# 标记文件位置和字符类型
config = ConfigObj("test.ini",encoding='UTF8')

# 写入节点
config['花园路小学'] = {}
config['北京路小学'] = {}
config['青岛路小学'] = {}
config['济南路小学'] = {}
# 节点写入字段
config['花园路小学']['校长'] = "小明"
config['北京路小学']['校长'] = '小虎'
config['青岛路小学']['校长'] = '小花'
config['济南路小学']['校长'] = '小桃'
# 写入文件
config.write()