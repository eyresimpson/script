# 方法一和方法二需要的库
import os

# 方法三需要的库
# 要执行的CMD命令

cmd = 'ipconfig /all'

# 方法一：通过os.popen执行CMD命令
# 注意，有些命令可能看不到效果
system_result = os.popen(cmd)
result = system_result.read()
print(result)

# 方法二：通过os.system执行CMD命令
# 这种方式可能会出现乱码甚至获取不到返回结果的情况
# os.system(cmd)

# 方法三：通过subprocess实现
# 使用比较复杂，并可能阻塞程序
# system_result = subprocess.Popen(cmd)
