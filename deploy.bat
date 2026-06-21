@echo off
setlocal
cd /d "%~dp0"

:: ── Step 1: validate CSVs and image paths ──────────────────────────────
echo.
echo Validating content...
python scripts\validate-csv.py
if errorlevel 1 goto :err_validate

:: ── Step 1b: generate responsive image variants (BRIEF §Performance) ───
echo.
echo Optimizing images...
python scripts\optimize-images.py
if errorlevel 1 goto :err_optimize

:: ── Step 1c: bake SEO / link-sharing meta from settings.csv ────────────
echo.
echo Baking SEO + link-preview tags...
python scripts\build-meta.py

:: ── Step 2: check git identity ─────────────────────────────────────────
git config user.email >nul 2>&1
if errorlevel 1 goto :err_identity

:: ── Step 3: stage + commit if there are local changes ──────────────────
git add -A
git diff --cached --quiet 2>nul
if errorlevel 1 goto :do_commit
echo No local changes to commit.
goto :push

:do_commit
set COMMIT_MSG=
set /p COMMIT_MSG=Commit message (or press Enter for default):
if "%COMMIT_MSG%"=="" set COMMIT_MSG=Update site
git commit -m "%COMMIT_MSG%"
if errorlevel 1 goto :err_commit

:: ── Step 4: push ───────────────────────────────────────────────────────
:push
git push
if errorlevel 1 goto :err_push

echo.
echo Done. Site is live on GitHub Pages in about 30 seconds.
pause
exit /b 0

:: ── Error handlers ─────────────────────────────────────────────────────
:err_validate
echo.
echo Deploy aborted — fix the CSV errors above first.
pause
exit /b 1

:err_optimize
echo.
echo Deploy aborted — image optimization failed (see the message above).
echo If Pillow is missing, install it with:  pip install Pillow
pause
exit /b 1

:err_identity
echo.
echo ERROR: Git does not know who you are. Run:
echo   git config --global user.email "your@email.com"
echo   git config --global user.name  "Your Name"
pause
exit /b 1

:err_commit
echo.
echo Commit failed unexpectedly.
pause
exit /b 1

:err_push
echo.
echo Push failed. Make sure you are signed in to GitHub.
echo Sign in by running:  gh auth login
pause
exit /b 1
