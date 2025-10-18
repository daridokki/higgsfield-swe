import httpx
from typing import List, Dict
import asyncio

class HiggsfieldClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://cloud.higgsfield.ai/api"
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def generate_image(self, prompt: str, model: str = "nano-banana") -> str:
        """Generate image and return URL"""
        payload = {
            "prompt": prompt,
            "model": model,
            "width": 1024,
            "height": 576  # 16:9 aspect ratio for video
        }
        
        response = await self.client.post(
            f"{self.base_url}/generate/image",
            json=payload,
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        
        return response.json()['image_url']
    
    async def animate_image(self, image_url: str, prompt: str, 
                          model: str = "kling-2-5") -> str:
        """Animate image and return video URL"""
        payload = {
            "image_url": image_url,
            "prompt": prompt,
            "model": model,
            "duration": 5  # 5-second clips
        }
        
        response = await self.client.post(
            f"{self.base_url}/generate/video-from-image",
            json=payload,
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        
        return response.json()['video_url']
    
    async def generate_direct_video(self, prompt: str, 
                                  model: str = "kling-21-master-t2v") -> str:
        """Generate video directly from text (for special moments)"""
        payload = {
            "prompt": prompt,
            "model": model,
            "duration": 4
        }
        
        response = await self.client.post(
            f"{self.base_url}/generate/video-from-text", 
            json=payload,
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        
        return response.json()['video_url']