import psutil

# 获取系统内存信息
memory = psutil.virtual_memory()
print("系统内存：", memory)

# 获取系统磁盘分区信息
partitions = psutil.disk_partitions()
print("系统磁盘分区信息：", partitions)

# 获取系统 CPU 使用情况
cpu_percent = psutil.cpu_percent(interval=1)
print("系统 CPU 使用率：", cpu_percent, "%")

# 获取系统启动时间
boot_time = psutil.boot_time()
print("系统启动时间：", boot_time)

# 获取系统进程信息
processes = psutil.pids()
print("系统进程信息：", processes)
