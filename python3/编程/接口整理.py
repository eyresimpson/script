# 此脚本可以从指定文件夹中的Java源文件里整理出所有的接口数据，形成一份markdown文档
# 依赖于swagger相关注释（@api、@ApiOperation）
# 此脚本主要用于生成一份离线的文档，简单描述接口信息
import os

# 配置要扫描的路径，强烈建议直接选择ontroller文件夹，否则会执行大量无效的遍历
dir = "E:\\code\\wx-shop2.0\\dts-wx-api\\src\\main\\java\\com\\qiguliuxing\\dts\\wx"

# 生成文档的目录
target_dir = "E:\\code\\wx-shop2.0\\doc"

# 文件编码
encoding = 'utf8'


# 获取指定注解中的内容
#
def get_annotate_content():
    pass


# 在指定文件中寻找目标字符串
# 传入文件索引、要搜索的字符串
# 返回指定字符串所在行
def find_in_file(file_index):
    # print(file_index)
    return 'none'


# 判断是否为Controller接口
def is_controller(file):
    line = open(file, 'r', encoding=encoding).read().find('RestController')
    if line != -1:
        return True
    else:
        return False


# 获取Controller接口信息
# TODO:这种写法过于简单，存在非常大的隐患，需要改进识别算法
def get_controller_info(file):
    # 读取文件
    with open(file, encoding=encoding) as temp_f:
        datafile = temp_f.readlines()
        # print(target_dir + '\\' + (file.split("\\")[-1]).split('.')[0] + ".md")
    # 创建一个新文件
    with open(target_dir + '\\' + (file.split("\\")[-1]).split('.')[0] + ".md", mode='w', encoding='utf-8') as file_obj:
        api_name = ""
        api_path = ""
        func = []
        temp = ""
        line_index = 0
        for line in datafile:
            line_index += 1
            if "@Api(" in line:
                print("API 名称：", line.split("\"")[1])
                api_name = line.split("\"")[1]
            if "@RequestMapping" in line:
                print("API 路径：", line.split("\"")[1])
                api_path = line.split("\"")[1]
            if "@GetMapping" in line:
                print("Get接口地址：", line.split("\"")[1])
                func.insert(line_index.__str__() + "," + line.split("\"")[1] + ":")
                file_obj.write('## ' + line.split("\"")[1] + "\n")
            if "@PostMapping" in line:
                print("Post接口地址：", line.split("\"")[1])
                file_obj.write('## ' + line.split("\"")[1] + "\n")
            if "@ApiOperation" in line:
                print("接口描述：", line.split("\"")[1])
                file_obj.write('> ' + line.split("\"")[1] + "\n")
        file_obj.write('# ' + api_name + "\n")
        file_obj.write('API 路径：' + api_path + "\n")


# 主入口函数
if __name__ == '__main__':
    # 当前文件索引，结构为 /user.java，全路径需要在前面加上dir中的地址
    file_index = ''
    # 所有结构化的接口数据
    controller = []
    # 遍历目录中所有文件夹和文件
    # for file in dir:
    for home, dirs, files in os.walk(dir):
        print(" [INFO] 切换至 -> (" + home + ") 目录")
        # 对当前目录下所有文件进行遍历
        for file in files:
            file_index = home + '\\' + file
            print(" [INFO] 检查 -> [" + file + "]")
            # 判断该文件是否为controller接口
            if is_controller(file_index):
                # 获取Controller基础接口信息
                f_index = find_in_file(file_index)
                print(" [INFO] 当前 [" + file + "] 是controller接口")
                # 如果是Controller类，继续寻找@GetMapping/@PostMapping，并根据swagger注释编写文档
                get_controller_info(file_index)
            else:
                print(" [INFO] 当前 [" + file + "] 文件略过")
