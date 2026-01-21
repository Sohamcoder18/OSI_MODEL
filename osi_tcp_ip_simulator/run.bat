@echo off
REM Quick Start Script for OSI vs TCP/IP Model Simulator (Windows)
REM This batch file will start the Flask application automatically

cls
echo.
echo ============================================================
echo OSI vs TCP/IP Model Visual Simulator
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [*] Checking for Flask installation...
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo [!] Flask not found, installing dependencies...
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
    echo [OK] Dependencies installed
)

echo.
echo ============================================================
echo Starting Flask Server...
echo ============================================================
echo.
echo [*] Server is starting at http://localhost:5000
echo [*] Opening browser in 2 seconds...
echo.
echo Press CTRL+C to stop the server
echo ============================================================
echo.

timeout /t 2 /nobreak >nul
start http://localhost:5000

python app.py

pause
