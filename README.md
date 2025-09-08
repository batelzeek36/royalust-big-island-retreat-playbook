# 🌺🌋 Royalust Big Island Retreat - AI Image Generation

Generate stunning AI images for all components of your Hawaiian retreat using the Higgsfield API.

## 🎯 What This Does

This tool automatically generates **18 high-quality AI images** covering every major element of your Big Island retreat:

- **Core Infrastructure**: DJ platform, glass pyramid sanctuary, sauna/cold plunge
- **Gardens & Food Forest**: Cacao groves, medicinal herb spirals, permaculture designs  
- **Experience Zones**: Hammock groves, tea pagodas, stargazing platforms
- **Sacred Spaces**: Fire circles, labyrinths, ceremony setups
- **Ambiance**: Lighting designs, projection mapping, sunset views
- **Overview Shots**: Aerial views, entrance, landscape vistas

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ installed
- Higgsfield API account (free signup at [platform.higgsfield.ai](https://platform.higgsfield.ai))

### Step 1: Get API Credentials
1. Visit [https://platform.higgsfield.ai](https://platform.higgsfield.ai)
2. Sign up or log in to your account
3. Go to the **Quickstart** section in your dashboard
4. Copy your **API Key** and **API Secret** (⚠️ shown only once - save them!)

### Step 2: Run the Generator

**Windows:**
```cmd
run_image_generation.bat
```

**Mac/Linux:**
```bash
# Install dependencies
pip install requests

# Set your credentials
export HIGGSFIELD_API_KEY="your-api-key-here"
export HIGGSFIELD_API_SECRET="your-api-secret-here"

# Run the generator
python generate_retreat_images.py
```

### Step 3: Get Your Images
- Generation takes **15-20 minutes** total (18 images × ~1 min each)
- Progress updates show in real-time
- All image URLs saved to `retreat_images_results.json`
- Images are hosted by Higgsfield for 30 days

## 📁 Generated Images

| Category | Images | Format |
|----------|--------|--------|
| **Infrastructure** | DJ deck, pyramid, sauna/plunge, fire circle | 1920×1080 |
| **Gardens** | Food forest, herb spiral, cacao grove | 1920×1080 |
| **Experience** | Hammocks, tea pagoda, stargazing deck | 1920×1080 |
| **Sacred** | Labyrinth, ceremonies, sound baths | 1024×1024 |
| **Ambiance** | Lighting, projections, landscapes | 1920×1080 |
| **Overview** | Aerial view, entrance, sunset | 1920×1080 |

## 💰 Cost Estimate

- **Higgsfield Pricing**: ~$1 USD = 16 credits
- **Per Image Cost**: ~2-4 credits (1080p quality)
- **Total Cost**: ~$3-5 USD for all 18 images

## 🔧 Advanced Usage

### Custom Image Generation
Edit `generate_retreat_images.py` to modify prompts or add new images:

```python
{
    "prompt": "Your custom prompt here, Hawaiian tropical setting, cinematic quality",
    "filename": "custom_image_name",
    "width_height": "1920x1080"  # or "1024x1024"
}
```

### Batch Sizes
Generate multiple variations by changing `batch_size`:
```python
batch_size=3  # Generates 3 variations per prompt
```

### Quality Settings
- `"720p"` - Faster, lower cost
- `"1080p"` - Higher quality (recommended)

## 📊 Results Format

The `retreat_images_results.json` file contains:
```json
[
  {
    "filename": "glass_pyramid_sanctuary",
    "prompt": "Stunning glass pyramid structure in Hawaiian tropical forest...",
    "url": "https://higgsfield-generated-image-url.com/image.jpg"
  }
]
```

## 🛠️ Troubleshooting

### Common Issues

**"API Key Invalid"**
- Double-check your credentials from the Higgsfield dashboard
- Make sure you're using the API key, not your login password

**"Generation Failed"**
- Check your account credit balance
- Some prompts may be filtered for content policy
- Try running again - temporary API issues can occur

**"Python Not Found"**
- Install Python from [python.org](https://python.org)
- Make sure Python is added to your system PATH

**"Timeout Errors"**
- Images can take 30-90 seconds each to generate
- Script waits up to 5 minutes per image
- Check your internet connection

### Rate Limits
- First 1,000 generations: max 2 concurrent jobs
- Script includes automatic delays between requests
- If you hit limits, wait a few minutes and resume

## 📝 File Structure

```
├── generate_retreat_images.py    # Main generation script
├── run_image_generation.bat      # Windows launcher
├── README.md                     # This file
├── wishlist.txt                  # Original retreat blueprint
├── higgsfield API.txt           # API documentation
└── retreat_images_results.json  # Generated image URLs (created after run)
```

## 🎨 Using Your Images

Once generated, you can:
- Download images directly from the URLs
- Use in presentations, websites, marketing materials
- Share with investors, partners, or team members
- Create mood boards and design references

**Note**: Images are hosted by Higgsfield for 30 days. Download and save locally for permanent storage.

## 🆘 Support

- **Higgsfield API Issues**: Check [platform.higgsfield.ai](https://platform.higgsfield.ai) status
- **Script Issues**: Review error messages and check troubleshooting section
- **Custom Modifications**: Edit the prompts array in `generate_retreat_images.py`

## 📄 License

This tool is for generating images for the Royalust Big Island Retreat project. Generated images follow Higgsfield's terms of service.

---

**Ready to visualize your retreat? Run the generator and bring your vision to life! 🌺**