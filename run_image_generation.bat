@echo off
echo.
echo 🌺🌋 ROYALUST BIG ISLAND RETREAT - IMAGE GENERATION 🌋🌺
echo.
echo This script will generate AI images for all retreat components using Higgsfield API
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

REM Install required packages
echo 📦 Installing required Python packages...
pip install requests

echo.
echo 🔑 API CREDENTIALS SETUP
echo.
echo You need to get your API credentials from Higgsfield dashboard:
echo 1. Go to https://platform.higgsfield.ai
echo 2. Sign up/login and go to Quickstart section
echo 3. Copy your API Key and Secret
echo.

set /p API_KEY="Enter your Higgsfield API Key: "
set /p API_SECRET="Enter your Higgsfield API Secret: "

if "%API_KEY%"=="" (
    echo ❌ API Key is required
    pause
    exit /b 1
)

if "%API_SECRET%"=="" (
    echo ❌ API Secret is required
    pause
    exit /b 1
)

echo.
echo 🚀 Starting image generation...
echo This will generate 18 high-quality images for your retreat
echo Each image takes 30-60 seconds to generate
echo Total estimated time: 15-20 minutes
echo.

REM Set environment variables and run the script
set HIGGSFIELD_API_KEY=%API_KEY%
set HIGGSFIELD_API_SECRET=%API_SECRET%

python generate_retreat_images.py

echo.
echo 🎉 Image generation complete!
echo Check the retreat_images_results.json file for all image URLs
echo.
pause