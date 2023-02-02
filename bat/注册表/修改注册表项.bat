@echo off
echo Enter the registry key:
set /p regkey=
echo Enter the value name:
set /p valuename=
echo Enter the value data:
set /p valuedata=
reg add %regkey% /v %valuename% /d %valuedata% /f
pause
