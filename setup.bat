@echo off
REM HTML to PDF Generator - Windows Setup Script
REM This script sets up the project environment on Windows

echo ============================================================
echo HTML to PDF Generator - Setup
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version
echo.

REM Check if pip is available
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not available
    echo Please reinstall Python with pip included
    pause
    exit /b 1
)

echo [OK] pip is available
echo.

REM Install dependencies
echo Installing dependencies...
echo ============================================================
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [OK] Dependencies installed successfully
echo.

REM Check if .env file exists
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env >nul 2>&1
    echo.
    echo [IMPORTANT] Please edit .env file and add your Doppio API key
    echo 1. Open .env file in a text editor
    echo 2. Replace "your_api_key_here" with your actual API key
    echo 3. Get a free API key at: https://doppio.sh
    echo.
) else (
    echo [OK] .env file already exists
    echo.
)

REM Ensure output directory exists
if not exist output (
    mkdir output
    echo [OK] Created output directory
) else (
    echo [OK] output directory exists
)
echo.

echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo Next steps:
echo 1. Edit .env file and add your DOPPIO_API_KEY
echo    Get a free key at: https://doppio.sh
echo.
echo 2. Run the generator:
echo    python src\generator.py
echo.
echo 3. Check examples:
echo    python example_usage.py
echo.
echo 4. Batch convert all HTML files:
echo    python batch_convert.py
echo.
echo Generated PDFs will be saved in the "output" folder
echo ============================================================
echo.

pause
