@echo off
cd /d "%~dp0"

:: ── Step 1: validate CSVs and image paths ──────────────────────────────
echo.
echo Validating content...
python scripts\validate-csv.py
if errorlevel 1 (
  echo.
  echo Deploy aborted — fix the errors above first.
  pause
  exit /b 1
)

:: ── Step 2: check git identity ─────────────────────────────────────────
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

:: ── Step 3: stage + commit + push ──────────────────────────────────────
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
echo Done. Site is live on GitHub Pages in about 30 seconds.
pause
