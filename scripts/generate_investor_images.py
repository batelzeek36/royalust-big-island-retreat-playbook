#!/usr/bin/env python3
"""
ROYALUST BIG ISLAND RETREAT - AI Image Generation for Investors
Generates stunning visualizations of retreat components using OpenAI DALL-E 3
and automatically integrates them into the wishlist HTML

OPTIMIZED FOR WEB PERFORMANCE:
- 1024x1024 resolution for faster loading
- Standard quality for smaller file sizes
- Auto-optimization with Pillow if available
- 50% cost reduction vs HD images
"""

import os
import json
import time
import requests
from datetime import datetime
import re

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key-here")
OPENAI_API_URL = "https://api.openai.com/v1/images/generations"

def generate_image(prompt, filename_prefix):
    """Generate image using OpenAI DALL-E 3"""
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024",  # Optimized for web - smaller file sizes, faster loading
        "quality": "standard",  # Standard quality for better performance
        "style": "natural"
    }
    
    print(f"🎨 Generating: {filename_prefix}")
    print(f"📝 Prompt: {prompt[:100]}...")
    
    try:
        response = requests.post(OPENAI_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        image_url = result['data'][0]['url']
        
        # Download the image
        img_response = requests.get(image_url)
        img_response.raise_for_status()
        
        filename = f"{filename_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        with open(filename, 'wb') as f:
            f.write(img_response.content)
        
        # Auto-optimize the image for web use
        try:
            from PIL import Image
            with Image.open(filename) as img:
                # Convert to RGB if needed and optimize
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'RGBA':
                        background.paste(img, mask=img.split()[-1])
                    else:
                        background.paste(img)
                    img = background
                
                # Save optimized version
                img.save(filename, 'PNG', optimize=True, compress_level=6)
                print(f"🔧 Optimized {filename} for web")
        except ImportError:
            print("💡 Install Pillow for automatic image optimization: pip install Pillow")
        
        print(f"✅ Saved: {filename}")
        return {
            "filename": filename,
            "url": image_url,
            "prompt": prompt,
            "status": "success"
        }
        
    except Exception as e:
        print(f"❌ Error generating {filename_prefix}: {str(e)}")
        return {
            "filename": f"{filename_prefix}_error",
            "url": None,
            "prompt": prompt,
            "status": "error",
            "error": str(e)
        }

def integrate_images_into_html(results):
    """Integrate generated images into the wishlist HTML"""
    try:
        # Read the current wishlist HTML
        with open("pages/wishlist-partial.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Create a backup
        with open("backups/wishlist-partial-full-backup.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print("🔧 Integrating images into HTML...")
        
        # Process each successful image
        for result in results:
            if result["status"] == "success" and "html_target" in result:
                image_html = f'''
                <div style="margin: 16px 0; text-align: center;">
                    <img src="{result['filename']}" alt="{result['section']} visualization" 
                         style="max-width: 100%; height: auto; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
                    <div style="font-size: 12px; color: var(--muted); margin-top: 8px; font-style: italic;">
                        AI-generated visualization of {result['section']} component
                    </div>
                </div>'''
                
                # Find the target location and insert the image
                target = result["html_target"]
                if target in html_content:
                    # Insert image after the target element
                    html_content = html_content.replace(target, target + image_html)
                    print(f"✅ Integrated {result['filename']} into {result['section']} section")
                else:
                    print(f"⚠️  Could not find target for {result['filename']}: {target}")
        
        # Write the updated HTML back to the original file
        with open("pages/wishlist-partial.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print("🎉 Updated pages/wishlist-partial.html with integrated visualizations!")
        return True
        
    except Exception as e:
        print(f"❌ Error integrating images: {str(e)}")
        return False

def main():
    print("🌺🌋 ROYALUST BIG ISLAND RETREAT - INVESTOR IMAGE GENERATION 🌋🌺")
    print("=" * 70)
    
    # Define image prompts with their corresponding HTML section mappings
    image_prompts = [
        {
            "prefix": "01_retreat_overview",
            "prompt": "Aerial view of a luxury wellness retreat on Hawaii's Big Island, featuring a stunning glass pyramid structure as the centerpiece, surrounded by lush tropical gardens with cacao groves, meditation spaces, and volcanic rock formations. Golden hour lighting with Mauna Kea in the background. Professional architectural photography style, ultra-realistic, 8K quality.",
            "html_target": "<!-- HERO IMAGE -->",
            "section": "overview"
        },

        {
            "prefix": "03_pyramid_interior_soundbath",
            "prompt": "Interior of glass pyramid sound bath studio during a ceremony, crystal singing bowls and Tibetan gongs arranged in sacred geometry, participants in meditation poses on comfortable mats, warm amber lighting creating mystical atmosphere, tropical vegetation visible through glass walls. Serene, spiritual, high-end wellness photography.",
            "html_target": '<div><strong>Capacity:</strong> treat as ceremony studio (gongs, bowls, chimes)',
            "section": "pyramid"
        },
        {
            "prefix": "04_dj_deck_music_platform",
            "prompt": "Professional outdoor DJ platform on Hawaii's Big Island, weatherproof modular design with sleek canopy, high-end sound equipment, surrounded by tropical landscaping and volcanic rock features. Directional speakers aimed at intimate gathering area, golden hour lighting, luxury event production aesthetic.",
            "html_target": '<h4>🎧🔊 Immersive Music Core</h4>',
            "section": "music"
        },
        {
            "prefix": "05_sauna_cold_plunge_therapy",
            "prompt": "Luxury heat and cold therapy area featuring beautiful wooden barrel sauna and modern cold plunge pool, set among tropical Hawaiian vegetation with volcanic rock accents. Steam rising from sauna, crystal-clear plunge water, bamboo privacy screens, resort-quality wellness facility design.",
            "html_target": '<h4>🧖‍♀️❄️ Heat/Cold Therapy Triad</h4>',
            "section": "therapy"
        },
        {
            "prefix": "06_fire_circle_gathering",
            "prompt": "Sacred fire circle gathering space on Hawaii's Big Island at dusk, natural stone seating arranged in perfect circle around contained fire pit, participants in comfortable meditation poses, tropical stars beginning to appear overhead, warm firelight illuminating faces, mystical and community-focused atmosphere.",
            "html_target": '<div><strong>Fire circle</strong> with spark screen + water bucket—story & song zone</div>',
            "section": "therapy"
        },
        {
            "prefix": "07_cacao_grove_food_forest",
            "prompt": "Thriving cacao grove and food forest on Hawaii's Big Island, mature cacao trees with pods, vanilla vines on trellises, tropical fruit trees including breadfruit and banana, herb spiral garden with medicinal plants, permaculture design principles, lush and abundant agricultural paradise.",
            "html_target": '<h4>🌿🥥 Food Forest & Medicinal Gardens</h4>',
            "section": "food-forest"
        },
        {
            "prefix": "08_hammock_grove_relaxation",
            "prompt": "Peaceful hammock grove under native Hawaiian trees, multiple comfortable hammocks and swing nets suspended between tropical hardwoods, dappled sunlight filtering through canopy, volcanic rock pathways, ultimate relaxation zone with luxury resort ambiance.",
            "html_target": '<div><strong>Hammock grove</strong> + swing nets under trees</div>',
            "section": "experience-nodes"
        },
        {
            "prefix": "09_tea_pagoda_meditation",
            "prompt": "Elegant tea pagoda meditation space, traditional Asian-inspired architecture adapted for Hawaiian setting, floor cushions arranged around low tea table, bamboo and tropical wood construction, surrounded by medicinal herb gardens, serene and contemplative atmosphere.",
            "html_target": '<div><strong>Reading/tea pagoda</strong> (non-habitable) with floor cushions, tea chest, water urn</div>',
            "section": "experience-nodes"
        },
        {
            "prefix": "10_stargaze_platform_night",
            "prompt": "Elevated stargazing platform on Hawaii's Big Island at night, comfortable reclining chairs arranged for optimal sky viewing, Milky Way visible overhead, minimal red lighting to preserve night vision, telescopes and binoculars available, romantic and awe-inspiring astronomical experience.",
            "html_target": '<div><strong>Stargaze platform:</strong> low deck with reclining camp chairs + binocular sets</div>',
            "section": "experience-nodes"
        },
        {
            "prefix": "11_labyrinth_sacred_geometry",
            "prompt": "Sacred labyrinth made from native Hawaiian lava rock, perfect spiral pattern set in tropical landscape, walking meditation path with native plants and flowers, Mount Mauna Kea visible in distance, spiritual pilgrimage destination with ancient wisdom meets modern wellness design.",
            "html_target": '<h4>🗺️🌀 Sacred Wayfinding & Quest Design</h4>',
            "section": "sacred-wayfinding"
        },
        {
            "prefix": "12_lighting_visual_magic",
            "prompt": "Magical evening lighting display throughout retreat grounds, warm amber uplights on tropical trees, subtle pixel strips along pathways, projection mapping on pyramid structure, low atmospheric haze creating beam texture, enchanting and mystical ambiance without light pollution.",
            "html_target": '<h4>🌈✨ Lighting & Visual Magic</h4>',
            "section": "lighting"
        },
        {
            "prefix": "13_outdoor_kitchen_dining",
            "prompt": "Beautiful outdoor demonstration kitchen and dining area, professional prep stations under elegant canopy, farm-to-table setup with fresh local produce displayed, tropical hardwood surfaces, stainless steel equipment, guests enjoying healthy plant-based cuisine, luxury catering aesthetic.",
            "html_target": '<h4>🧑‍🍳🌮 Food Service: Simple & Compliant</h4>',
            "section": "food-service"
        },
        {
            "prefix": "14_solar_power_sustainability",
            "prompt": "Modern solar power installation integrated seamlessly into tropical landscape, sleek solar panels positioned among native vegetation, battery storage system housed in attractive enclosure, sustainable technology meeting luxury resort standards, environmental responsibility showcase.",
            "html_target": '<h4>🔌☀️ Power & Connectivity</h4>',
            "section": "power"
        },
        {
            "prefix": "15_arrival_welcome_experience",
            "prompt": "Welcoming arrival experience at retreat entrance, beautiful natural stone pathway lined with tropical flowers, elegant signage incorporating sacred geometry, staff member offering traditional Hawaiian welcome with lei and refreshing tea, luxury hospitality meets authentic cultural respect.",
            "html_target": '<h4>🎟️📸 Guest Experience & Brand Moments</h4>',
            "section": "guest-experience"
        },
        {
            "prefix": "16_workshop_shade_structures",
            "prompt": "Elegant shade sail structures creating outdoor workshop spaces, modern tensioned fabric canopies in earth tones, comfortable seating arrangements for group activities, tropical landscaping integration, professional event space design meeting luxury wellness standards.",
            "html_target": '<div><strong>Shade sails & small canopies</strong> (< permit thresholds) for lounges & workshops</div>',
            "section": "experience-nodes"
        },
        {
            "prefix": "17_water_sanitation_facilities",
            "prompt": "Beautifully designed sanitation facilities integrated into landscape, modern composting toilets housed in attractive natural wood structures, hand-washing stations with bamboo privacy screens, tropical plantings for natural screening, luxury eco-resort bathroom facilities.",
            "html_target": '<h4>💧🚽 Water, Sanitation & Comfort</h4>',
            "section": "sanitation"
        },
        {
            "prefix": "18_complete_retreat_sunset",
            "prompt": "Complete Hawaii Big Island wellness retreat at golden hour sunset, all facilities visible in harmonious composition: glass pyramid centerpiece, DJ platform, sauna area, cacao groves, fire circle, pathways with lighting, guests enjoying various activities, luxury destination resort showcasing investment potential and visitor experience.",
            "html_target": "<!-- FINAL OVERVIEW IMAGE -->",
            "section": "complete-overview"
        }
    ]
    
    results = []
    total_images = len(image_prompts)
    
    print(f"🚀 Generating {total_images} investor-ready images...")
    print("⏳ Skipping Glass Pyramid exterior (already generated)")
    print(f"⏱️  Estimated time: {total_images * 30} seconds")
    print()
    
    for i, image_config in enumerate(image_prompts, 1):
        print(f"[{i}/{total_images}] ", end="")
        result = generate_image(image_config["prompt"], image_config["prefix"])
        results.append(result)
        
        # Rate limiting - OpenAI allows ~50 requests per minute for DALL-E 3
        if i < total_images:
            print("⏳ Waiting 2 seconds...")
            time.sleep(2)
        print()
    
    # Save results summary
    summary = {
        "generation_date": datetime.now().isoformat(),
        "total_images": total_images,
        "successful": len([r for r in results if r["status"] == "success"]),
        "failed": len([r for r in results if r["status"] == "error"]),
        "results": results
    }
    
    with open("investor_images_results.json", "w") as f:
        json.dump(summary, f, indent=2)
    
    print("=" * 70)
    print("🎉 IMAGE GENERATION COMPLETE!")
    print(f"✅ Successfully generated: {summary['successful']} images")
    if summary['failed'] > 0:
        print(f"❌ Failed: {summary['failed']} images")
    print(f"📄 Results saved to: investor_images_results.json")
    print()
    
    # Integrate images into HTML if we have successful results
    if summary['successful'] > 0:
        print("🔧 INTEGRATING IMAGES INTO WISHLIST...")
        # Add html_target info to results for integration
        for i, result in enumerate(results):
            if result["status"] == "success" and i < len(image_prompts):
                result.update(image_prompts[i])
        
        if integrate_images_into_html(results):
            print("🎯 INVESTOR PRESENTATION READY!")
            print("✅ Images generated and integrated into wishlist-with-images.html")
            print("✅ Original wishlist backed up to wishlist-partial-backup.html")
        else:
            print("⚠️  Images generated but integration failed - check files manually")
    
    print()
    print("🌟 FEATURES SHOWCASED:")
    print("• Stunning aerial overview of complete retreat")
    print("• Glass pyramid exterior and interior sound bath ceremony")
    print("• Professional DJ platform and music production setup")
    print("• Luxury sauna, cold plunge, and fire circle experiences")
    print("• Thriving cacao grove and food forest agriculture")
    print("• Peaceful relaxation areas and meditation spaces")
    print("• Sacred geometry and spiritual journey elements")
    print("• Complete infrastructure and sustainability systems")
    print()
    
    # Calculate estimated cost
    successful_images = summary['successful']
    estimated_cost = successful_images * 0.04  # $0.04 per standard DALL-E 3 image (1024x1024)
    print(f"💰 Estimated API cost: ${estimated_cost:.2f}")
    print("💡 Perfect for investor pitch decks, websites, and funding presentations!")

if __name__ == "__main__":
    main()