@echo off
start "" python -m http.server 5500 
start http://127.0.0.1:5500/web.html