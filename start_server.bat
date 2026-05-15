@echo off
chcp 65001 >nul
title WenMing6 Tournament Server
cd /d "%~dp0"
echo ========================================
echo   Civilization VI Tournament Server
echo ========================================
echo.
echo  Your LAN address (share to WeChat group):
echo.
ipconfig | findstr /i "IPv4"
echo.
echo  Example: http://192.168.x.x:8080
echo.
echo  Press Ctrl+C to stop server
echo ========================================
echo.
python -m http.server 8080
pause
