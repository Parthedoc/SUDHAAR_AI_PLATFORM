@echo off
setlocal
cd /d "%~dp0"
title SUDHAAR v0.9 - Local recovery support

if not exist ".venv\Scripts\python.exe" (
  echo First run SETUP_SUDHAAR.bat to install dependencies.
  pause
  exit /b 1
)

echo Starting SUDHAAR locally...
echo Make sure the Ollama app is running and qwen2.5:3b is installed.
echo The browser usually opens at http://localhost:8501
.venv\Scripts\python.exe -m streamlit run app.py
pause
