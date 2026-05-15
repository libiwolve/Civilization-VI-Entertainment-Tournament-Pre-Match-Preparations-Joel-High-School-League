#!/usr/bin/env python3
import http.server
import socketserver
import socket
import os
import sys

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, format, *args):
        print(f"[{self.client_address[0]}] {args[0]} {args[1]} {args[2]}")

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print("=" * 50)
print("  Civ6 Tournament Server")
print("=" * 50)
print()
print(f"  Local:   http://localhost:{PORT}")
print(f"  Network: http://{local_ip}:{PORT}")
print()
print("  Share the network address to your group.")
print("  Press Ctrl+C to stop.")
print("=" * 50)

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Server stopped.")
