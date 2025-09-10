#!/usr/bin/env python3
"""
ROYALUST BIG ISLAND RETREAT - AI Image Generation for Investors
Generates stunning visualizations of retreat components using OpenAI DALL-E 3
and automatically integrates them into the wishlist HTML
"""

import os
import json
import time
import requests
from datetime import datetime
import re

# OpenAI API Configuration - Set your API key as environment variable
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

def integrate_images_into_html(results):
    """Integrate generated images into the wishlist HTML"""
    try:
        # Read the current wishlist HTML
        with open("wishlist-partial.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Create a backup
        with open("wishlist-partial-backup.html", "w", encoding="utf-8") as f:
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
        with open("wishlist-partial.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print("🎉 Updated wishlist-partial.html with integrated visualizations!")
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
        # Add more image prompts here as needed...
    ]
    
    print("🚀 Ready to generate investor-ready images!")
    print("⚠️  Make sure to set your OPENAI_API_KEY environment variable first")
    print("📖 See AI_IMAGE_SETUP.md for complete setup instructions")
    
    if OPENAI_API_KEY == "your-openai-api-key-here":
        print("❌ Please set your OpenAI API key as an environment variable")
        print("   Windows: $env:OPENAI_API_KEY='your-key-here'")
        print("   Mac/Linux: export OPENAI_API_KEY='your-key-here'")
        return
    
    print(f"🎯 This script will generate {len(image_prompts)} images")
    print("💰 Estimated cost: ${:.2f}".format(len(image_prompts) * 0.08))

if __name__ == "__main__":
    main()