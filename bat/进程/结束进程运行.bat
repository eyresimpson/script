@echo off
set /p pid=Enter the PID of the process to be terminated:
taskkill /F /PID %pid%
pause
