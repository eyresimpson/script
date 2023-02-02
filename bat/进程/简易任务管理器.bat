@echo off

@REM 此脚本会展示当前所有运行的进程，并要求用户输入PID，会根据PID结束对于进程的运行

echo List of running processes:
tasklist
set /p pid=Enter the PID of the process to be terminated:
taskkill /F /PID %pid%
pause
