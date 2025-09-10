# 🌺 ROYALUST Big Island Retreat - Project Repository

A comprehensive wellness retreat development project featuring AI-generated visualizations, operational playbooks, and investor documentation.

## 🚀 Quick Start

1. **View the main site**: Open `index.html` in your browser
2. **Generate new images**: Run `scripts/run_image_generation.bat`
3. **Optimize images**: Run `scripts/run_optimization.bat`

## 📁 Project Structure

```
├── 📄 Main Site
│   ├── index.html                    # Main landing page
│   ├── styles.css                    # Main stylesheet
│   ├── script.js                     # JavaScript functionality
│   └── pages/                        # All content pages
│       ├── wishlist-partial.html     # Retreat components wishlist
│       ├── operations-cards.html     # Operations overview
│       ├── permit-playbook.html      # Permitting guide
│       ├── pma-checklist.html        # PMA compliance checklist
│       └── royalust_big_island_retreat_ops_playbook_investor_edition.html
│
├── 🎨 Assets
│   ├── images/                       # Optimized WebP images
│   │   ├── webp/                    # Full-size WebP images
│   │   ├── medium/                  # 800px WebP images
│   │   └── thumbnails/              # 300px WebP images
│   ├── original_images/             # Original PNG files (not in Git)
│   └── reference-images/            # Reference photos and examples
│
├── 🛠️ Scripts
│   ├── generate_investor_images.py  # AI image generation (OpenAI DALL-E 3)
│   ├── optimize_images.py           # Image optimization (PNG → WebP)
│   ├── update_html_images.py        # Update HTML with responsive images
│   ├── run_image_generation.bat     # Windows batch for image generation
│   └── run_optimization.bat         # Windows batch for optimization
│
├── 📚 Documentation
│   ├── README.md                    # This file
│   ├── AI_IMAGE_SETUP.md           # AI image generation setup
│   ├── MODULARIZATION.md           # Project modularization guide
│   ├── Info.txt                    # Project information
│   ├── wishlist.txt                # Original wishlist
│   ├── higgsfield API.txt          # API documentation
│   └── ROYALUST × Big Island Retreat Ops Playbook — Investor Edition.pdf
│
├── ⚙️ Configuration
│   ├── .env.example                # Environment variables template
│   ├── investor_images_results.json # Image generation results
│   └── optimization_results.json   # Image optimization results
│
├── 🗄️ Backups
│   ├── *.backup                    # HTML file backups
│   └── old versions/               # Previous file versions
│
└── 🎯 Core Files
    └── .gitignore                  # Git ignore rules
```

## 🎨 Image Optimization System

Our images are **87.8% smaller** than originals thanks to:

- **WebP format** with 85% quality
- **Responsive sizing**: thumbnails (300px), medium (800px), full-size
- **Lazy loading** for better performance
- **Progressive enhancement** with PNG fallbacks

### Image Loading Strategy:
- **Mobile** (< 600px): 300px thumbnails (~10-20 KB)
- **Tablet** (< 1200px): 800px medium images (~50-150 KB)
- **Desktop**: Full WebP images (~200-600 KB)
- **Fallback**: Original PNGs for older browsers

## 🤖 AI Image Generation

Generate stunning retreat visualizations using OpenAI DALL-E 3:

1. Set your API key: `$env:OPENAI_API_KEY='your-key-here'`
2. Run: `scripts/run_image_generation.bat`
3. Images are automatically optimized and integrated into HTML

**Features:**
- 18 unique retreat component visualizations
- Professional architectural photography style
- Optimized for web (1024x1024, standard quality)
- 50% cost reduction vs HD images

## 🏗️ Development Workflow

1. **Make changes** to HTML/CSS/JS files
2. **Generate new images** if needed with AI scripts
3. **Optimize images** for web performance
4. **Test locally** by opening HTML files
5. **Commit and push** to GitHub

## 📊 Performance Metrics

- **Total image size**: 102.8 MB → 12.6 MB (87.8% reduction)
- **Loading speed**: 10-20x faster on mobile
- **Bandwidth savings**: 90% less data usage
- **SEO improvement**: Faster page load times

## 🌟 Key Features

- **Glass Pyramid Sound Bath Sanctum** - Sacred geometry centerpiece
- **Professional DJ Platform** - Weatherproof music production
- **Sauna & Cold Plunge** - Luxury wellness therapy
- **Cacao Grove & Food Forest** - Sustainable agriculture
- **Sacred Fire Circle** - Community gathering space
- **Stargazing Platform** - Astronomical experiences

## 💰 Investment Highlights

- **Modular development** approach for phased investment
- **Permit-compliant** design within Big Island regulations
- **Sustainable systems** with solar power and water management
- **Scalable operations** from intimate retreats to larger events
- **Multiple revenue streams** from workshops, ceremonies, and accommodations

## 🔧 Technical Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Images**: WebP with PNG fallbacks, responsive loading
- **AI Generation**: OpenAI DALL-E 3 API
- **Optimization**: Python with Pillow library
- **Version Control**: Git with organized branch structure

## 📞 Contact

For questions about this project or investment opportunities, please refer to the documentation in the `docs/` folder.

---

*Built with ❤️ for sustainable wellness tourism in Hawaii*