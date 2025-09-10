@echo off
echo.
echo 🌺🌋 ROYALUST BIG ISLAND RETREAT - AI IMAGE GENERATION 🌋🌺
echo.
echo This script will generate AI images for all retreat components using OpenAI DALL-E 3
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
pip install requests Pillow

echo.
echo 🔑 OPENAI API SETUP
echo.
echo You need your OpenAI API key:
echo 1. Go to https://platform.openai.com/api-keys
echo 2. Create a new API key
echo 3. Copy the key (starts with sk-)
echo.

set /p API_KEY="Enter your OpenAI API Key: "

if "%API_KEY%"=="" (
    echo ❌ OpenAI API Key is required
    pause
    exit /b 1
)

echo.
echo 🚀 Starting image generation...
echo This will generate 18 high-quality images optimized for web
echo Each image costs ~$0.04 (total ~$0.72)
echo Each image takes 10-20 seconds to generate
echo Total estimated time: 5-10 minutes
echo.

REM Set environment variable and run the script
set OPENAI_API_KEY=%API_KEY%

python scripts/generate_investor_images.py

echo.
echo 🎉 Image generation complete!
echo Check config/investor_images_results.json for results
echo.
pause