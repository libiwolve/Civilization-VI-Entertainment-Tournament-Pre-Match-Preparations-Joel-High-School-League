#!/usr/bin/env python3
import http.server
import socketserver
import socket
import os

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, format, *args):
        print(f"[{self.client_address[0]}] {args[0]} {args[1]} {args[2]}")

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print("=" * 55)
print("  [ 文明6 . 高校娱乐赛 - 本地服务器 ]")
print("=" * 55)
print()
print(f"  本地访问:  http://localhost:{PORT}")
print(f"  局域网访问: http://{local_ip}:{PORT}")
print()
print("  把局域网地址分享到微信群,")
print("  大家就能同时看到地图图片了!")
print()
print("  按 Ctrl+C 关闭服务器")
print("=" * 55)
print()

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已关闭")
