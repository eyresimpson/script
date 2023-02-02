import psutil

# 获取所有进程信息
process_list = psutil.process_iter()

# 遍历进程列表，输出每个进程的详细信息
for process in process_list:
    process_info = process.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_info'])
    print(process_info)
