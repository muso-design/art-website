@echo off
cd /d "%~dp0"
echo Starting local server at http://localhost:8080
echo (newsletter signups are saved to subscribers.txt)
start http://localhost:8080
python scripts\dev-server.py
pause
