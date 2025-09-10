#!/usr/bin/env python3
"""
Update HTML files to use optimized WebP images with fallbacks
"""

import re
import os
import glob

def create_responsive_img_tag(png_filename):
    """Create a responsive image tag with WebP and PNG fallbacks"""
    base_name = os.path.splitext(png_filename)[0]
    
    return f'''<picture>
    <source srcset="images/thumbnails/{base_name}_thumb.webp" media="(max-width: 600px)" type="image/webp">
    <source srcset="images/medium/{base_name}_medium.webp" media="(max-width: 1200px)" type="image/webp">
    <source srcset="images/webp/{base_name}.webp" type="image/webp">
    <source srcset="images/thumbnails/{base_name}_thumb.webp" media="(max-width: 600px)">
    <source srcset="images/medium/{base_name}_medium.webp" media="(max-width: 1200px)">
    <img src="{png_filename}" alt="" loading="lazy" style="width: 100%; height: auto;">
</picture>'''

def update_html_file(html_file):
    """Update a single HTML file to use optimized images"""
    print(f"Updating {html_file}...")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all img tags with PNG sources
    img_pattern = r'<img[^>]*src=["\']([^"\']*\.png)["\'][^>]*>'
    
    def replace_img(match):
        full_tag = match.group(0)
        png_src = match.group(1)
        
        # Extract other attributes
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', full_tag)
        alt_text = alt_match.group(1) if alt_match else ""
        
        style_match = re.search(r'style=["\']([^"\']*)["\']', full_tag)
        style_attr = style_match.group(1) if style_match else "width: 100%; height: auto;"
        
        class_match = re.search(r'class=["\']([^"\']*)["\']', full_tag)
        class_attr = f' class="{class_match.group(1)}"' if class_match else ""
        
        # Get just the filename
        png_filename = os.path.basename(png_src)
        base_name = os.path.splitext(png_filename)[0]
        
        return f'''<picture{class_attr}>
    <source srcset="images/thumbnails/{base_name}_thumb.webp" media="(max-width: 600px)" type="image/webp">
    <source srcset="images/medium/{base_name}_medium.webp" media="(max-width: 1200px)" type="image/webp">
    <source srcset="images/webp/{base_name}.webp" type="image/webp">
    <img src="{png_src}" alt="{alt_text}" loading="lazy" style="{style_attr}">
</picture>'''
    
    # Replace all img tags
    updated_content = re.sub(img_pattern, replace_img, content)
    
    # Create backup
    backup_file = f"{html_file}.backup"
    if not os.path.exists(backup_file):
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Created backup: {backup_file}")
    
    # Write updated content
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"  Updated {html_file}")

def main():
    """Update all HTML files in the current directory"""
    html_files = glob.glob('*.html')
    
    if not html_files:
        print("No HTML files found")
        return
    
    print(f"Found {len(html_files)} HTML files to update:")
    for html_file in html_files:
        print(f"  {html_file}")
    
    print()
    
    for html_file in html_files:
        try:
            update_html_file(html_file)
        except Exception as e:
            print(f"Error updating {html_file}: {e}")
    
    print("\nHTML update complete!")
    print("Your original files are backed up with .backup extension")

if __name__ == "__main__":
    main()