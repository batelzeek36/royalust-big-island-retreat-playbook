#!/usr/bin/env python3
"""
Image optimization script for faster web loading
Converts PNGs to WebP format and creates multiple sizes
"""

import os
import glob
from PIL import Image
import json

def optimize_images():
    """Process all PNG images in the current directory"""
    
    # Create output directories
    os.makedirs('images/webp', exist_ok=True)
    os.makedirs('images/thumbnails', exist_ok=True)
    os.makedirs('images/medium', exist_ok=True)
    
    # Find all PNG files
    png_files = glob.glob('*.png')
    
    if not png_files:
        print("No PNG files found in current directory")
        return
    
    results = []
    
    for png_file in png_files:
        print(f"Processing {png_file}...")
        
        try:
            # Open original image
            with Image.open(png_file) as img:
                # Get original size
                original_size = os.path.getsize(png_file)
                width, height = img.size
                
                # Convert to RGB if necessary (WebP doesn't support RGBA well)
                if img.mode in ('RGBA', 'LA'):
                    # Create white background
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'RGBA':
                        background.paste(img, mask=img.split()[-1])
                    else:
                        background.paste(img)
                    img = background
                
                # Base filename without extension
                base_name = os.path.splitext(png_file)[0]
                
                # 1. Create WebP version (same size, better compression)
                webp_path = f'images/webp/{base_name}.webp'
                img.save(webp_path, 'WebP', quality=85, optimize=True)
                webp_size = os.path.getsize(webp_path)
                
                # 2. Create thumbnail (300px width)
                thumb_width = 300
                thumb_height = int(height * (thumb_width / width))
                thumb_img = img.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)
                
                thumb_webp_path = f'images/thumbnails/{base_name}_thumb.webp'
                thumb_img.save(thumb_webp_path, 'WebP', quality=80, optimize=True)
                thumb_size = os.path.getsize(thumb_webp_path)
                
                # 3. Create medium size (800px width)
                if width > 800:
                    medium_width = 800
                    medium_height = int(height * (medium_width / width))
                    medium_img = img.resize((medium_width, medium_height), Image.Resampling.LANCZOS)
                    
                    medium_webp_path = f'images/medium/{base_name}_medium.webp'
                    medium_img.save(medium_webp_path, 'WebP', quality=85, optimize=True)
                    medium_size = os.path.getsize(medium_webp_path)
                else:
                    medium_webp_path = webp_path
                    medium_size = webp_size
                
                # Calculate savings
                savings_percent = ((original_size - webp_size) / original_size) * 100
                
                result = {
                    'original_file': png_file,
                    'original_size': original_size,
                    'original_dimensions': f"{width}x{height}",
                    'webp_file': webp_path,
                    'webp_size': webp_size,
                    'thumbnail_file': thumb_webp_path,
                    'thumbnail_size': thumb_size,
                    'medium_file': medium_webp_path,
                    'medium_size': medium_size,
                    'savings_percent': round(savings_percent, 1)
                }
                
                results.append(result)
                
                print(f"  Original: {original_size:,} bytes ({width}x{height})")
                print(f"  WebP: {webp_size:,} bytes ({savings_percent:.1f}% smaller)")
                print(f"  Thumbnail: {thumb_size:,} bytes")
                print(f"  Medium: {medium_size:,} bytes")
                print()
                
        except Exception as e:
            print(f"Error processing {png_file}: {e}")
    
    # Save results summary
    with open('optimization_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print summary
    total_original = sum(r['original_size'] for r in results)
    total_webp = sum(r['webp_size'] for r in results)
    total_savings = ((total_original - total_webp) / total_original) * 100
    
    print(f"SUMMARY:")
    print(f"Processed {len(results)} images")
    print(f"Total original size: {total_original:,} bytes")
    print(f"Total WebP size: {total_webp:,} bytes")
    print(f"Total savings: {total_savings:.1f}%")

if __name__ == "__main__":
    optimize_images()