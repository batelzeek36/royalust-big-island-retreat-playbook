# AI Image Generation Setup

## Prerequisites
- OpenAI API account with DALL-E 3 access
- Python 3.7+ with `requests` library

## Setup Instructions

1. **Get OpenAI API Key**
   - Go to https://platform.openai.com
   - Create account and get API key
   - Ensure you have credits for DALL-E 3 usage

2. **Set Environment Variable**
   ```bash
   # Windows (PowerShell)
   $env:OPENAI_API_KEY="your-actual-api-key-here"
   
   # Windows (CMD)
   set OPENAI_API_KEY=your-actual-api-key-here
   
   # Mac/Linux
   export OPENAI_API_KEY="your-actual-api-key-here"
   ```

3. **Or Create .env File**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your key
   OPENAI_API_KEY=your-actual-api-key-here
   ```

## Usage

### Test Single Image
```bash
python test_single_image.py
```

### Generate All Images
```bash
python generate_investor_images.py
```

## Cost Estimate
- Single test image: ~$0.08
- Complete image suite (17 images): ~$1.36
- High-resolution (1792x1024) DALL-E 3 images

## Generated Images
The script creates stunning visualizations for:
- Aerial retreat overview
- Glass pyramid exterior & interior
- DJ platform and music setup
- Sauna, cold plunge, fire circle
- Cacao grove and food forest
- Relaxation areas and meditation spaces
- Sacred geometry and wayfinding
- Infrastructure and facilities

All images are automatically integrated into the wishlist HTML with professional styling.