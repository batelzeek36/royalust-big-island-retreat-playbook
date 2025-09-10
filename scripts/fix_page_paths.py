#!/usr/bin/env python3
"""
Fix relative paths in HTML files moved to pages/ folder
"""

import os
import glob
import re

def fix_paths_in_file(file_path):
    """Fix relative paths in a single HTML file"""
    print(f"Fixing paths in {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix image paths - add ../ prefix
    content = re.sub(r'srcset="images/', r'srcset="../images/', content)
    content = re.sub(r'src="images/', r'src="../images/', content)
    content = re.sub(r'src="original_images/', r'src="../original_images/', content)
    
    # Fix any CSS/JS paths if they exist
    content = re.sub(r'href="styles\.css"', r'href="../styles.css"', content)
    content = re.sub(r'src="script\.js"', r'src="../script.js"', content)
    
    # Write back the fixed content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Fixed {file_path}")

def main():
    """Fix paths in all HTML files in pages/ folder"""
    print("🔧 Fixing relative paths in pages/ folder...")
    
    # Find all HTML files in pages folder
    html_files = glob.glob('pages/*.html')
    
    if not html_files:
        print("No HTML files found in pages/ folder")
        return
    
    print(f"Found {len(html_files)} HTML files to fix:")
    for html_file in html_files:
        print(f"  {html_file}")
    
    print()
    
    for html_file in html_files:
        try:
            fix_paths_in_file(html_file)
        except Exception as e:
            print(f"❌ Error fixing {html_file}: {e}")
    
    print("\n🎉 Path fixing complete!")

if __name__ == "__main__":
    main()