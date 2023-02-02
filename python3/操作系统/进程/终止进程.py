import psutil


def kill_process(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            process.kill()
            print(f"{process_name} 进程已被终止")


process_name = "notepad.exe"  # 要操作的进程名称

kill_process(process_name)
