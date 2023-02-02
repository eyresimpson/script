@echo off
@REM 注意不要随便换行或格式化
for /f "tokens=2 delims=:" %%a in ( ' ipconfig ^| findstr IP ' ) do ( set ip=%%a )
echo Local IP address: %ip%
pause
