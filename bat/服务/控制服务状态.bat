@echo off

@REM 要求用户输入服务名称，并启动此服务

echo Enter the service name:
set /p servicename=
net start %servicename%
echo The service %servicename% has been started.
pause
net stop %servicename%
echo The service %servicename% has been stopped.
pause
