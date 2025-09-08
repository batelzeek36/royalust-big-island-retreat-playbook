#!/usr/bin/env python3
"""
Higgsfield AI Image Generation Script for Royalust Big Island Retreat
Generates images for all major retreat components using the Soul text2image model
"""

import requests
import json
import time
import os
from typing import Dict, List, Optional

class HiggsfieldImageGenerator:
    def __init__(self, api_key: str, api_secret: str):
        self.base_url = "https://platform.higgsfield.ai"
        self.headers = {
            "Content-Type": "application/json",
            "hf-api-key": api_key,
            "hf-secret": api_secret
        }
        
    def generate_image(self, prompt: str, filename: str, 
                      width_height: str = "1024x1024", 
                      quality: str = "1080p",
                      enhance_prompt: bool = True,
                      batch_size: int = 1) -> Optional[str]:
        """Generate a single image using the Soul model"""
        
        payload = {
            "params": {
                "prompt": prompt,
                "width_and_height": width_height,
                "enhance_prompt": enhance_prompt,
                "quality": quality,
                "batch_size": batch_size
            }
        }
        
        try:
            # Submit generation request
            response = requests.post(
                f"{self.base_url}/v1/text2image/soul",
                headers=self.headers,
                json=payload
            )
            
            if response.status_code != 200:
                print(f"❌ Failed to generate {filename}: {response.status_code} - {response.text}")
                return None
                
            job_data = response.json()
            job_set_id = job_data["id"]
            print(f"🎨 Generating {filename}... (Job ID: {job_set_id})")
            
            # Poll for completion
            return self.wait_for_completion(job_set_id, filename)
            
        except Exception as e:
            print(f"❌ Error generating {filename}: {str(e)}")
            return None
    
    def wait_for_completion(self, job_set_id: str, filename: str, max_wait: int = 300) -> Optional[str]:
        """Poll job status until completion"""
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            try:
                response = requests.get(
                    f"{self.base_url}/v1/job-sets/{job_set_id}",
                    headers=self.headers
                )
                
                if response.status_code != 200:
                    print(f"❌ Failed to check status for {filename}")
                    return None
                    
                job_data = response.json()
                
                # Check if any job is finished
                for job in job_data.get("jobs", []):
                    if job["status"] == "finished" and "results" in job:
                        image_url = job["results"]["raw"]  # Get full quality image
                        print(f"✅ {filename} completed! URL: {image_url}")
                        return image_url
                    elif job["status"] == "failed":
                        print(f"❌ {filename} generation failed")
                        return None
                
                print(f"⏳ {filename} still processing...")
                time.sleep(10)  # Wait 10 seconds before next check
                
            except Exception as e:
                print(f"❌ Error checking status for {filename}: {str(e)}")
                return None
        
        print(f"⏰ {filename} timed out after {max_wait} seconds")
        return None

def main():
    # Get API credentials from environment variables
    api_key = os.getenv("HIGGSFIELD_API_KEY")
    api_secret = os.getenv("HIGGSFIELD_API_SECRET")
    
    if not api_key or not api_secret:
        print("❌ Please set HIGGSFIELD_API_KEY and HIGGSFIELD_API_SECRET environment variables")
        print("You can get these from the Higgsfield dashboard")
        return
    
    generator = HiggsfieldImageGenerator(api_key, api_secret)
    
    # Define all the images to generate for the retreat
    image_prompts = [
        # Core Infrastructure
        {
            "prompt": "Modern weatherproof DJ deck platform with canopy, professional sound equipment, tropical Hawaiian setting with lush greenery, golden hour lighting, cinematic quality",
            "filename": "dj_deck_platform",
            "width_height": "1920x1080"
        },
        {
            "prompt": "Stunning glass pyramid structure in Hawaiian tropical forest, sacred geometry, sound bath sanctuary, mystical ambient lighting, surrounded by native plants",
            "filename": "glass_pyramid_sanctuary",
            "width_height": "1024x1024"
        },
        {
            "prompt": "Wooden barrel sauna next to natural cold plunge pool, Big Island volcanic landscape, steam rising, tropical plants, wellness retreat atmosphere",
            "filename": "sauna_cold_plunge",
            "width_height": "1920x1080"
        },
        {
            "prompt": "Sacred fire circle with lava rock seating, spark screen, Hawaiian night sky with stars, warm firelight, ceremonial atmosphere",
            "filename": "sacred_fire_circle",
            "width_height": "1920x1080"
        },
        
        # Gardens & Food Forest
        {
            "prompt": "Lush Hawaiian food forest with breadfruit trees, banana plants, cacao grove, medicinal herbs, permaculture design, tropical paradise",
            "filename": "food_forest_garden",
            "width_height": "1920x1080"
        },
        {
            "prompt": "Spiral herb garden with medicinal plants, turmeric, ginger, moringa, Hawaiian native plants, permaculture design, morning light",
            "filename": "medicinal_herb_spiral",
            "width_height": "1024x1024"
        },
        {
            "prompt": "Cacao trees with vanilla vines growing on trellises, tropical Hawaiian setting, chocolate pods, sustainable agriculture",
            "filename": "cacao_vanilla_grove",
            "width_height": "1920x1080"
        },
        
        # Experience Zones
        {
            "prompt": "Hammock grove under tropical trees, peaceful relaxation zone, dappled sunlight, Hawaiian forest setting, zen atmosphere",
            "filename": "hammock_grove",
            "width_height": "1920x1080"
        },
        {
            "prompt": "Elegant tea pagoda with floor cushions, bamboo architecture, tropical garden views, meditation space, serene atmosphere",
            "filename": "tea_meditation_pagoda",
            "width_height": "1024x1024"
        },
        {
            "prompt": "Stargazing deck platform with reclining chairs, clear Hawaiian night sky, Milky Way visible, romantic lighting, Big Island landscape",
            "filename": "stargazing_platform",
            "width_height": "1920x1080"
        },
        {
            "prompt": "Lava rock labyrinth in Hawaiian setting, sacred geometry, spiritual pathway, native plants, mystical atmosphere",
            "filename": "lava_rock_labyrinth",
            "width_height": "1024x1024"
        },
        
        # Lighting & Ambiance
        {
            "prompt": "Ambient uplighting on tropical trees, warm amber path lights, magical evening atmosphere, Hawaiian retreat setting",
            "filename": "ambient_tree_lighting",
            "width_height": "1920x1080"
        },
        {
            "prompt": "Projection mapping on pyramid structure, ambient visual loops, mystical patterns, tropical night setting, artistic lighting",
            "filename": "pyramid_projection_mapping",
            "width_height": "1920x1080"
        },
        
        # Wellness & Ceremony
        {
            "prompt": "Sound bath ceremony inside glass pyramid, singing bowls, gongs, people in meditation, sacred atmosphere, golden light",
            "filename": "sound_bath_ceremony",
            "width_height": "1920x1080"
        },
        {
            "prompt": "Cacao ceremony setup with traditional cups, cacao beans, ceremonial altar, tropical flowers, sacred ritual atmosphere",
            "filename": "cacao_ceremony_setup",
            "width_height": "1024x1024"
        },
        {
            "prompt": "Outdoor rinse station with bamboo privacy screens, tropical shower, natural materials, Hawaiian spa atmosphere",
            "filename": "outdoor_rinse_station",
            "width_height": "1024x1024"
        },
        
        # Overall Retreat Views
        {
            "prompt": "Aerial view of complete Hawaiian retreat center, glass pyramid, gardens, platforms, tropical forest, Big Island landscape, masterplan overview",
            "filename": "retreat_aerial_overview",
            "width_height": "1920x1080"
        },
        {
            "prompt": "Welcome entrance to Hawaiian retreat, tropical landscaping, signage, path leading to pyramid, inviting atmosphere, golden hour",
            "filename": "retreat_entrance_welcome",
            "width_height": "1920x1080"
        },
        {
            "prompt": "Sunset view from retreat with Big Island landscape, volcanic mountains, tropical vegetation, peaceful evening atmosphere",
            "filename": "retreat_sunset_landscape",
            "width_height": "1920x1080"
        }
    ]
    
    print(f"🌺 Starting generation of {len(image_prompts)} images for Royalust Big Island Retreat...")
    print("=" * 80)
    
    results = []
    
    for i, image_config in enumerate(image_prompts, 1):
        print(f"\n[{i}/{len(image_prompts)}] Generating: {image_config['filename']}")
        
        url = generator.generate_image(
            prompt=image_config["prompt"],
            filename=image_config["filename"],
            width_height=image_config.get("width_height", "1024x1024"),
            quality="1080p",
            enhance_prompt=True
        )
        
        if url:
            results.append({
                "filename": image_config["filename"],
                "prompt": image_config["prompt"],
                "url": url
            })
        
        # Small delay between requests to be respectful
        time.sleep(2)
    
    # Save results to JSON file
    with open("retreat_images_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\n" + "=" * 80)
    print(f"🎉 Generation complete! {len(results)}/{len(image_prompts)} images generated successfully")
    print("📄 Results saved to: retreat_images_results.json")
    
    if results:
        print("\n✅ Successfully generated images:")
        for result in results:
            print(f"  • {result['filename']}: {result['url']}")

if __name__ == "__main__":
    main()