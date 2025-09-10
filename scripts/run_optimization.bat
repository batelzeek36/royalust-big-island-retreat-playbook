@echo off
echo Installing required Python packages...
pip install Pillow

echo.
echo Starting image optimization...
python scripts/optimize_images.py

echo.
echo Optimization complete! Check the images/ folder for results.
pause