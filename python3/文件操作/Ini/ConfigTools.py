# 对常见的配置文件的操作封装
# @Author Tine Aine
# @Version 1.0.0
# TODO: 重要的功能通过到C++库实现
# 主操作器类
from configobj import ConfigObj


class ConfigureOperation:
    # ---------------------------
    # 操作器
    # ---------------------------
    # windows ini 配置文件操作器
    iniOperation = None

    # 初始化操作器主类
    def __init__(self):
        pass

    # 获取ini配置操作器
    def ConfigureOperation(self):
        self.iniOperation = self.IniOperation()
        return self.iniOperation

    class IniOperation:
        config = None

        def __init__(self,filename,encoding='UTF8'):
            self.config = ConfigObj(filename, encoding)

        # 读取配置文件
        def readConfig(self, filename, encoding='UTF8'):
            return self.config

        # 写出配置文件
        def writeConfigSection(self, filename, section, encoding='UTF8'):
            config = ConfigObj(filename, encoding)

