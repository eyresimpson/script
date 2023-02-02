from configobj import ConfigObj
config = ConfigObj("test.ini",encoding='UTF8')
config['花园路小学']['校长'] = "小许"
config.write()