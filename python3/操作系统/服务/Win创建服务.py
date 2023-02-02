import win32service
import win32serviceutil
import win32api
import win32con
import os


class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MyService"
    _svc_display_name_ = "My Service Display Name"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)


if __name__ == '__main__':
    win32api.SetConsoleCtrlHandler(lambda x: True, True)
    win32serviceutil.HandleCommandLine(MyService)


# 安装服务的命令行命令：
# python myservice.py install

# 启动服务的命令行命令：
# python myservice.py start

# 停止服务的命令行命令：
# python myservice.py stop

# 删除服务的命令行命令：
# python myservice.py remove