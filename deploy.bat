@echo off
cd /d "%~dp0"

:: Check git identity is configured
git config user.email >nul 2>&1
if errorlevel 1 (
  echo.
  echo ERROR: Git does not know who you are.
  echo Run these two commands in a terminal, then try again:
  echo.
  echo   git config --global user.email "your@email.com"
  echo   git config --global user.name "Your Name"
  echo.
  pause
  exit /b 1
)

git add -A

set /p msg=Commit message (or press Enter for default):
if "%msg%"=="" set msg=Update site

git commit -m "%msg%"
if errorlevel 1 (
  echo.
  echo Nothing to commit - no changes detected.
  pause
  exit /b 0
)

git push
if errorlevel 1 (
  echo.
  echo Push failed. Make sure you are signed in to GitHub.
  echo Sign in by running:  gh auth login
  pause
  exit /b 1
)

echo.
echo Done. Site is live on GitHub.
pause
