#!/usr/bin/env python3
"""
ROYALUST BIG ISLAND RETREAT - AI Image Generation for Investors
Generates stunning visualizations of retreat components using OpenAI DALL-E 3
"""

import os
import json
import time
import requests
from datetime import datetime

# OpenAI API Configuration
OPENAI_API_KEY = "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"
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
        "size": "1792x1024",  # Landscape format perfect for presentations
        "quality": "hd",
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

def main():
    print("🌺🌋 ROYALUST BIG ISLAND RETREAT - INVESTOR IMAGE GENERATION 🌋🌺")
    print("=" * 70)
    
    # Define image prompts for key retreat components
    image_prompts = [
        {
            "prefix": "01_retreat_overview",
            "prompt": "Aerial view of a luxury wellness retreat on Hawaii's Big Island, featuring a stunning glass pyramid structure as the centerpiece, surrounded by lush tropical gardens with cacao groves, meditation spaces, and volcanic rock formations. Golden hour lighting with Mauna Kea in the background. Professional architectural photography style, ultra-realistic, 8K quality."
        },
        {
            "prefix": "02_glass_pyramid_exterior",
            "prompt": "Magnificent glass pyramid sound bath sanctuary on Hawaii's Big Island, geometric crystal structure gleaming in tropical sunlight, surrounded by native Hawaiian plants and volcanic rock landscaping. Sacred geometry meets modern architecture, with warm ambient lighting beginning to glow from within. Cinematic composition, luxury resort photography style."
        },
        {
            "prefix": "03_pyramid_interior_soundbath",
            "prompt": "Interior of glass pyramid sound bath studio during a ceremony, crystal singing bowls and Tibetan gongs arranged in sacred geometry, participants in meditation poses on comfortable mats, warm amber lighting creating mystical atmosphere, tropical vegetation visible through glass walls. Serene, spiritual, high-end wellness photography."
        },
        {
            "prefix": "04_dj_deck_music_platform",
            "prompt": "Professional outdoor DJ platform on Hawaii's Big Island, weatherproof modular design with sleek canopy, high-end sound equipment, surrounded by tropical landscaping and volcanic rock features. Directional speakers aimed at intimate gathering area, golden hour lighting, luxury event production aesthetic."
        },
        {
            "prefix": "05_sauna_cold_plunge_therapy",
            "prompt": "Luxury heat and cold therapy area featuring beautiful wooden barrel sauna and modern cold plunge pool, set among tropical Hawaiian vegetation with volcanic rock accents. Steam rising from sauna, crystal-clear plunge water, bamboo privacy screens, resort-quality wellness facility design."
        },
        {
            "prefix": "06_fire_circle_gathering",
            "prompt": "Sacred fire circle gathering space on Hawaii's Big Island at dusk, natural stone seating arranged in perfect circle around contained fire pit, participants in comfortable meditation poses, tropical stars beginning to appear overhead, warm firelight illuminating faces, mystical and community-focused atmosphere."
        },
        {
            "prefix": "07_cacao_grove_food_forest",
            "prompt": "Thriving cacao grove and food forest on Hawaii's Big Island, mature cacao trees with pods, vanilla vines on trellises, tropical fruit trees including breadfruit and banana, herb spiral garden with medicinal plants, permaculture design principles, lush and abundant agricultural paradise."
        },
        {
            "prefix": "08_hammock_grove_relaxation",
            "prompt": "Peaceful hammock grove under native Hawaiian trees, multiple comfortable hammocks and swing nets suspended between tropical hardwoods, dappled sunlight filtering through canopy, volcanic rock pathways, ultimate relaxation zone with luxury resort ambiance."
        },
        {
            "prefix": "09_tea_pagoda_meditation",
            "prompt": "Elegant tea pagoda meditation space, traditional Asian-inspired architecture adapted for Hawaiian setting, floor cushions arranged around low tea table, bamboo and tropical wood construction, surrounded by medicinal herb gardens, serene and contemplative atmosphere."
        },
        {
            "prefix": "10_stargaze_platform_night",
            "prompt": "Elevated stargazing platform on Hawaii's Big Island at night, comfortable reclining chairs arranged for optimal sky viewing, Milky Way visible overhead, minimal red lighting to preserve night vision, telescopes and binoculars available, romantic and awe-inspiring astronomical experience."
        },
        {
            "prefix": "11_labyrinth_sacred_geometry",
            "prompt": "Sacred labyrinth made from native Hawaiian lava rock, perfect spiral pattern set in tropical landscape, walking meditation path with native plants and flowers, Mount Mauna Kea visible in distance, spiritual pilgrimage destination with ancient wisdom meets modern wellness design."
        },
        {
            "prefix": "12_lighting_visual_magic",
            "prompt": "Magical evening lighting display throughout retreat grounds, warm amber uplights on tropical trees, subtle pixel strips along pathways, projection mapping on pyramid structure, low atmospheric haze creating beam texture, enchanting and mystical ambiance without light pollution."
        },
        {
            "prefix": "13_outdoor_kitchen_dining",
            "prompt": "Beautiful outdoor demonstration kitchen and dining area, professional prep stations under elegant canopy, farm-to-table setup with fresh local produce displayed, tropical hardwood surfaces, stainless steel equipment, guests enjoying healthy plant-based cuisine, luxury catering aesthetic."
        },
        {
            "prefix": "14_solar_power_sustainability",
            "prompt": "Modern solar power installation integrated seamlessly into tropical landscape, sleek solar panels positioned among native vegetation, battery storage system housed in attractive enclosure, sustainable technology meeting luxury resort standards, environmental responsibility showcase."
        },
        {
            "prefix": "15_arrival_welcome_experience",
            "prompt": "Welcoming arrival experience at retreat entrance, beautiful natural stone pathway lined with tropical flowers, elegant signage incorporating sacred geometry, staff member offering traditional Hawaiian welcome with lei and refreshing tea, luxury hospitality meets authentic cultural respect."
        },
        {
            "prefix": "16_workshop_shade_structures",
            "prompt": "Elegant shade sail structures creating outdoor workshop spaces, modern tensioned fabric canopies in earth tones, comfortable seating arrangements for group activities, tropical landscaping integration, professional event space design meeting luxury wellness standards."
        },
        {
            "prefix": "17_water_sanitation_facilities",
            "prompt": "Beautifully designed sanitation facilities integrated into landscape, modern composting toilets housed in attractive natural wood structures, hand-washing stations with bamboo privacy screens, tropical plantings for natural screening, luxury eco-resort bathroom facilities."
        },
        {
            "prefix": "18_complete_retreat_sunset",
            "prompt": "Complete Hawaii Big Island wellness retreat at golden hour sunset, all facilities visible in harmonious composition: glass pyramid centerpiece, DJ platform, sauna area, cacao groves, fire circle, pathways with lighting, guests enjoying various activities, luxury destination resort showcasing investment potential and visitor experience."
        }
    ]
    
    results = []
    total_images = len(image_prompts)
    
    print(f"🚀 Generating {total_images} investor-ready images...")
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
    print("🎯 INVESTOR PRESENTATION READY!")
    print("These high-quality images showcase your retreat's full potential")
    print("Perfect for pitch decks, websites, and investor meetings")
    print()
    
    # Calculate estimated cost
    successful_images = summary['successful']
    estimated_cost = successful_images * 0.08  # $0.08 per HD DALL-E 3 image
    print(f"💰 Estimated API cost: ${estimated_cost:.2f}")

if __name__ == "__main__":
    main()