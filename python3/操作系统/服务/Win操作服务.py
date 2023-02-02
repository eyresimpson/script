import win32service
import win32serviceutil

# 指定服务名称
service_name = "wuauserv"

# 获取服务状态
status = win32serviceutil.QueryServiceStatus(service_name)[1]
print("Service Status:", status)

# 启动服务
if status == win32service.SERVICE_STOPPED:
    win32serviceutil.StartService(service_name)
    print("Service Started")

# 停止服务
elif status == win32service.SERVICE_RUNNING:
    win32serviceutil.StopService(service_name)
    print("Service Stopped")
