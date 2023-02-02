import win32service
import win32serviceutil
import win32api

services = win32serviceutil.EnumServices()

for service in services:
    name, display_name, status = service
    print("Service Name:", name)
    print("Display Name:", display_name)
    print("Status:", status)
    print("\n")
