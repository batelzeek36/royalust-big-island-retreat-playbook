#!/usr/bin/env python3
"""
ROYALUST BIG ISLAND RETREAT - Single Image Test
Tests generating one AI image and placing it in the wishlist HTML
"""

import os
import json
import requests
from datetime import datetime

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key-here")
OPENAI_API_URL = "https://api.openai.com/v1/images/generations"

def generate_test_image():
    """Generate a single test image using OpenAI DALL-E 3"""
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Test with the glass pyramid exterior - visually striking and easy to verify
    test_prompt = "Magnificent glass pyramid sound bath sanctuary on Hawaii's Big Island, geometric crystal structure gleaming in tropical sunlight, surrounded by native Hawaiian plants and volcanic rock landscaping. Sacred geometry meets modern architecture, with warm ambient lighting beginning to glow from within. Cinematic composition, luxury resort photography style."
    
    payload = {
        "model": "dall-e-3",
        "prompt": test_prompt,
        "n": 1,
        "size": "1792x1024",  # Landscape format
        "quality": "hd",
        "style": "natural"
    }
    
    print("🎨 Generating test image: Glass Pyramid Exterior")
    print(f"📝 Prompt: {test_prompt[:80]}...")
    
    try:
        response = requests.post(OPENAI_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        image_url = result['data'][0]['url']
        
        # Download the image
        img_response = requests.get(image_url)
        img_response.raise_for_status()
        
        filename = f"test_pyramid_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        with open(filename, 'wb') as f:
            f.write(img_response.content)
        
        print(f"✅ Image saved: {filename}")
        return {
            "filename": filename,
            "url": image_url,
            "prompt": test_prompt,
            "status": "success"
        }
        
    except Exception as e:
        print(f"❌ Error generating image: {str(e)}")
        return {
            "filename": None,
            "url": None,
            "prompt": test_prompt,
            "status": "error",
            "error": str(e)
        }

def integrate_test_image(image_result):
    """Integrate the test image into the wishlist HTML"""
    if image_result["status"] != "success":
        print("❌ Cannot integrate - image generation failed")
        return False
    
    try:
        # Read the current wishlist HTML
        with open("wishlist-partial.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Create a backup
        with open("wishlist-partial-test-backup.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print("🔧 Integrating test image into HTML...")
        
        # Target location for glass pyramid section
        target = '<h4>🔺🔔 Glass Pyramid Sound Bath Sanctum</h4>'
        
        # Create the image HTML
        image_html = f'''
                <div style="margin: 16px 0; text-align: center;">
                    <img src="{image_result['filename']}" alt="Glass Pyramid Sound Bath Sanctum visualization" 
                         style="max-width: 100%; height: auto; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
                    <div style="font-size: 12px; color: var(--muted); margin-top: 8px; font-style: italic;">
                        AI-generated visualization of Glass Pyramid Sound Bath Sanctum
                    </div>
                </div>'''
        
        # Find the target and insert the image
        if target in html_content:
            html_content = html_content.replace(target, target + image_html)
            print(f"✅ Found target location and integrated image")
        else:
            print(f"❌ Could not find target: {target}")
            return False
        
        # Write the test HTML
        with open("wishlist-test-with-image.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print("🎉 Created wishlist-test-with-image.html!")
        return True
        
    except Exception as e:
        print(f"❌ Error integrating image: {str(e)}")
        return False

def main():
    print("🌺🌋 ROYALUST - SINGLE IMAGE TEST 🌋🌺")
    print("=" * 50)
    print("Testing AI image generation and HTML integration")
    print("This will generate 1 image and place it in the Glass Pyramid section")
    print()
    
    # Generate test image
    print("🚀 Step 1: Generating test image...")
    image_result = generate_test_image()
    
    if image_result["status"] == "success":
        print(f"✅ Image generation successful!")
        print(f"📁 File: {image_result['filename']}")
        
        # Test HTML integration
        print()
        print("🚀 Step 2: Testing HTML integration...")
        if integrate_test_image(image_result):
            print("✅ HTML integration successful!")
            print()
            print("🎯 TEST RESULTS:")
            print("✅ AI image generation: WORKING")
            print("✅ File download: WORKING") 
            print("✅ HTML integration: WORKING")
            print()
            print("📄 Files created:")
            print(f"  • {image_result['filename']} (generated image)")
            print("  • wishlist-test-with-image.html (HTML with image)")
            print("  • wishlist-partial-test-backup.html (backup)")
            print()
            print("🎉 Ready to run the full batch generation!")
            print("💰 Test cost: ~$0.08")
        else:
            print("❌ HTML integration failed")
    else:
        print("❌ Image generation failed")
        print(f"Error: {image_result.get('error', 'Unknown error')}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()