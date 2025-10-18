import requests
import time
import os
from config import Config

class HiggsfieldClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = Config.HIGGSFIELD_BASE_URL
        self.models = Config.MODELS
        self.use_mock = os.getenv('USE_MOCK_API', 'false').lower() == 'true'
    
    def _make_request(self, endpoint, data=None, method='POST'):
        """Helper method for API requests"""
        if self.use_mock:
            return self._mock_response(endpoint)
            
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'hf-api-key': self.api_key,
            'hf-secret': self.api_secret,
            'Content-Type': 'application/json'
        }
        
        try:
            if method == 'POST':
                response = requests.post(url, json=data, headers=headers)
            else:
                response = requests.get(url, headers=headers)
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            raise
    
    def _mock_response(self, endpoint):
        """Return mock responses for testing without spending credits"""
        mock_id = f"mock_{hash(endpoint) % 10000}"
        return {
            "id": mock_id,
            "jobs": [{
                "status": "completed",
                "results": {
                    "raw": {"url": f"https://example.com/mock-{mock_id}.mp4"}
                }
            }]
        }
    
    def _poll_for_results(self, job_set_id):
        """Poll until job is completed"""
        if self.use_mock:
            return f"https://example.com/mock-video-{job_set_id}.mp4"
            
        start_time = time.time()
        
        while time.time() - start_time < Config.MAX_POLLING_TIME:
            # Check job status
            result = self._make_request(f"job-sets/{job_set_id}", method='GET')
            
            job_status = result['jobs'][0]['status']
            
            if job_status == 'completed':
                return result['jobs'][0]['results']['raw']['url']
            elif job_status == 'failed':
                raise Exception(f"Generation failed for job {job_set_id}")
            
            print(f"Waiting for generation... ({job_status})")
            time.sleep(Config.POLLING_INTERVAL)
        
        raise Exception("Generation timeout - took too long")
    
    def text_to_image(self, prompt, aspect_ratio="16:9"):
        """Generate image from text prompt"""
        if self.use_mock:
            return f"https://example.com/mock-image-{hash(prompt) % 1000}.jpg"
            
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
            return f"https://example.com/mock-video-{hash(prompt) % 1000}.mp4"
            
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
            return f"https://example.com/mock-special-{hash(prompt) % 1000}.mp4"
