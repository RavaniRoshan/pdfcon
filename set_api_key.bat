@echo off
REM API Key Setup Helper for Windows
REM This script helps you set up your Doppio API key

echo ======================================================================
echo API KEY SETUP HELPER
echo ======================================================================
echo.

REM Check if .env file already exists
if exist .env (
    echo WARNING: .env file already exists!
    echo.
    set /p "overwrite=Do you want to update it? (y/n): "
    if /i not "%overwrite%"=="y" (
        echo.
        echo Cancelled. No changes made.
        pause
        exit /b 0
    )
)

echo.
echo ======================================================================
echo GET YOUR API KEY
echo ======================================================================
echo.
echo 1. Go to: https://doppio.sh
echo 2. Sign up for a FREE account
echo 3. Copy your API key (starts with 'dp_')
echo.
echo ----------------------------------------------------------------------
echo.

set /p "api_key=Paste your API key here: "

if "%api_key%"=="" (
    echo.
    echo [ERROR] No API key provided. Setup cancelled.
    pause
    exit /b 1
)

REM Create .env file
echo # Doppio API Configuration > .env
echo # Sign up for a free API key at: https://doppio.sh >> .env
echo. >> .env
echo # Your Doppio API Key >> .env
echo DOPPIO_API_KEY=%api_key% >> .env

echo.
echo ======================================================================
echo SUCCESS!
echo ======================================================================
echo.
echo [OK] Created: .env
echo [OK] API key saved securely
echo.
echo ======================================================================
echo NEXT STEPS
echo ======================================================================
echo.
echo You're ready to generate PDFs! Try these commands:
echo.
echo   python src\generator.py           # Generate from template
echo   python example_usage.py           # Try 5 examples
echo   python batch_convert.py           # Batch convert HTML files
echo.
echo PDFs will be saved in: output\
echo.
echo Happy PDF generating!
echo ======================================================================
echo.

pause
