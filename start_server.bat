@echo off
title 文明6 选人工具 - 服务器
cd /d "%~dp0"
echo ========================================
echo   文明6 . 高校娱乐赛 - 本地服务器
echo ========================================
echo.
echo 你的局域网地址（分享给微信群）：
echo.
ipconfig | findstr /i "IPv4"
echo.
echo 示例访问地址：http://你的IP:8080
echo.
echo 按 Ctrl+C 关闭服务器
echo ========================================
echo.
python -m http.server 8080
pause
