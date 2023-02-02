@echo off
echo Enter the registry key:
set /p regkey=
reg query %regkey%
pause
