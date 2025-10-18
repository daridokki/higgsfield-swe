# higgsfield_client.py - Simplified version without external dependencies
import time
import os
import random

# Mock Config if not available
class MockConfig:
    HIGGSFIELD_BASE_URL = "https://platform.higgsfield.ai/v1"
    MODELS = {
        'text_to_image': 'nano_banana',
        'image_to_video': 'kling-2-5', 
        'text_to_video': 'kling-2-1-master-t2v'
    }
    MAX_POLLING_TIME = 300
    POLLING_INTERVAL = 5

# Use real Config if available, otherwise use MockConfig
try:
    from config import Config
except ImportError:
    print("⚠️  Using mock config")
    Config = MockConfig

class HiggsfieldClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = Config.HIGGSFIELD_BASE_URL
        self.models = Config.MODELS
        self.use_mock = os.getenv('USE_MOCK_API', 'true').lower() == 'true'
    
    def _make_request(self, endpoint, data=None, method='POST'):
        """Helper method for API requests - mock version"""
        if self.use_mock:
            return self._mock_response(endpoint)
        
        # If we need real API calls but requests is not available
        print(f"❌ Real API calls require 'requests' library")
        print(f"   Endpoint: {endpoint}")
        print(f"   Enable mock mode with: USE_MOCK_API=true")
        return self._mock_response(endpoint)
    
    def _mock_response(self, endpoint):
        """Return mock responses for testing without spending credits"""
        mock_id = f"mock_{random.randint(1000, 9999)}"
        
        # Use working sample videos for demonstration
        sample_videos = [
            "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4",
            "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
            "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
            "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
        ]
        
        # Return a random sample video
        video_url = random.choice(sample_videos)
        
        return {
            "id": mock_id,
            "jobs": [{
                "status": "completed",
                "results": {
                    "raw": {"url": video_url}
                }
            }]
        }
    
    def _poll_for_results(self, job_set_id):
        """Poll until job is completed - mock version"""
        if self.use_mock:
            # Simulate some processing time
            print(f"   ⏳ Simulating AI generation...")
            time.sleep(2)
            
            # Use working sample videos for demonstration
            sample_videos = [
                "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4",
                "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
                "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
                "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
            ]
            
            # Return a random sample video
            return random.choice(sample_videos)
            
        # Real implementation would go here
        return f"https://example.com/real-video-{job_set_id}.mp4"
    
    def text_to_image(self, prompt, aspect_ratio="16:9"):
        """Generate image from text prompt"""
        if self.use_mock:
            print(f"   🎨 Generating image: '{prompt[:50]}...'")
            time.sleep(1)
            # Return a working sample image URL
            sample_images = [
                "https://picsum.photos/800/600?random=1",
                "https://picsum.photos/800/600?random=2", 
                "https://picsum.photos/800/600?random=3"
            ]
            return random.choice(sample_images)
            
        # Real API call implementation
        params = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "input_images": []
        }
        
        data = {"params": params}
        response = self._make_request(f"generations/{self.models['text_to_image']}", data)
        job_set_id = response['id']
        
        print(f"Image generation submitted: {job_set_id}")
        return self._poll_for_results(job_set_id)
    
    def image_to_video(self, image_url, prompt, duration=4):
        """Animate image into video"""
        if self.use_mock:
            print(f"   🎥 Animating image: '{prompt[:50]}...'")
            time.sleep(2)
            # Return a working sample video URL
            sample_videos = [
                "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4",
                "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
                "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"
            ]
            return random.choice(sample_videos)
            
        # Real API call implementation
        params = {
            "prompt": prompt,
            "input_images": [image_url]
        }
        
        data = {"params": params}
        response = self._make_request(f"generations/{self.models['image_to_video']}", data)
        job_set_id = response['id']
        
        print(f"Video generation submitted: {job_set_id}")
        return self._poll_for_results(job_set_id)
    
    def text_to_video(self, prompt, duration=4):
        """Generate video directly from text (more expensive)"""
        if self.use_mock:
            print(f"   ✨ Creating special video: '{prompt[:50]}...'")
            time.sleep(3)
            # Return a working sample video URL for special moments
            sample_videos = [
                "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
                "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
                "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"
            ]
            return random.choice(sample_videos)
            
        # Real API call implementation
        params = {"prompt": prompt}
        data = {"params": params}
        
        response = self._make_request(f"generations/{self.models['text_to_video']}", data)
        job_set_id = response['id']
        
        print(f"Text-to-video generation submitted: {job_set_id}")
        return self._poll_for_results(job_set_id)

# Test the client
if __name__ == "__main__":
    print("🧪 Testing HiggsfieldClient...")
    client = HiggsfieldClient("test-key", "test-secret")
    
    # Test image generation
    image_url = client.text_to_image("cyberpunk city with neon lights")
    print(f"✅ Generated image: {image_url}")
    
    # Test video generation
    video_url = client.image_to_video(image_url, "neon lights pulsing to music")
    print(f"✅ Generated video: {video_url}")
    
    # Test direct video generation
    special_url = client.text_to_video("colorful explosion on beat drop")
    print(f"✅ Generated special video: {special_url}")