@echo off
setlocal
cd /d "%~dp0"
title SUDHAAR v0.9 setup

echo.
echo  SUDHAAR v0.9 - Windows setup
echo =============================
echo.

if exist ".venv\Scripts\python.exe" goto install_deps

python --version >nul 2>&1
if not errorlevel 1 goto create_with_python

py --version >nul 2>&1
if not errorlevel 1 goto create_with_py

echo Python was not found. Install Python 3.11 or newer from https://www.python.org/downloads/windows/
echo During installation, enable Add Python to PATH, then reopen this folder and run SETUP_SUDHAAR.bat again.
pause
exit /b 1

:create_with_python
python -m venv .venv
if errorlevel 1 goto setup_failed
goto install_deps

:create_with_py
py -m venv .venv
if errorlevel 1 goto setup_failed

:install_deps
echo Installing project dependencies. This may take a few minutes.
.venv\Scripts\python.exe -m pip install --upgrade pip
if errorlevel 1 goto setup_failed
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto setup_failed

if not exist .env copy .env.example .env >nul
echo.
echo Setup completed.
echo Check .env has OLLAMA_BASE_URL=http://127.0.0.1:11434 and OLLAMA_MODEL=qwen2.5:3b.
echo Keep the Ollama Windows app running, then double-click RUN_SUDHAAR.bat.
echo.
pause
exit /b 0

:setup_failed
echo.
echo Setup failed. Read the error above and check Python/internet connectivity.
pause
exit /b 1
