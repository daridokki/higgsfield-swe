# higgsfield_client.py - Real Higgsfield API client
import time
import os
import json
import urllib.request
import urllib.parse
import urllib.error

class HiggsfieldClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        # FIXED: Use correct base URLs from documentation
        self.base_url_v1 = "https://platform.higgsfield.ai/v1"  # For v1 endpoints
        self.base_url = "https://platform.higgsfield.ai"        # For non-v1 endpoints
        # FORCE REAL API - NO MOCK MODE
        self.use_mock = False
        
        # Verify we have real credentials
        if api_key == 'YOUR_API_KEY_HERE' or api_secret == 'YOUR_API_SECRET_HERE':
            raise Exception("❌ API credentials not properly configured!")
        
        print("✅ Using REAL Higgsfield API with provided credentials")
        print(f"   API Key: {api_key[:8]}...")
        print(f"   API Secret: {api_secret[:8]}...")
    
    def _make_request(self, endpoint, data=None, method='POST'):
        """Make HTTP request to Higgsfield API"""
        # REAL API ONLY - NO MOCK MODE
        
        url = f"{self.base_url}/{endpoint}"
        print(f"   🌐 Making API request to: {url}")
        print(f"   📝 Method: {method}")
        print(f"   🔑 API Key: {self.api_key[:8]}...")
        
        # Prepare headers - correct format from documentation + anti-bot measures
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'hf-api-key': self.api_key,
            'hf-secret': self.api_secret,
            'Referer': 'https://cloud.higgsfield.ai',
            'Origin': 'https://cloud.higgsfield.ai'
        }
        
        # Prepare data
        if data:
            data_json = json.dumps(data).encode('utf-8')
            print(f"   📦 Data: {json.dumps(data, indent=2)}")
        else:
            data_json = None
        
        try:
            # Create request
            req = urllib.request.Request(url, data=data_json, headers=headers, method=method)
            
            # Add minimal delay to avoid rate limiting
            import time
            time.sleep(1)  # 1 second delay for speed
            
            # Make request
            print(f"   ⏳ Sending request...")
            with urllib.request.urlopen(req) as response:
                response_data = json.loads(response.read().decode('utf-8'))
                print(f"   ✅ Response received: {response_data}")
                return response_data
                
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            print(f"❌ API Error {e.code}: {error_body}")
            print(f"   Headers: {dict(e.headers)}")
            raise Exception(f"API request failed: {e.code} - {error_body}")
        except Exception as e:
            print(f"❌ Request failed: {e}")
            print(f"   Error type: {type(e).__name__}")
            raise Exception(f"Request failed: {e}")
    
    def _make_request_with_base_url(self, endpoint, data=None, base_url=None, method='POST'):
        """Make HTTP request with custom base URL"""
        if base_url is None:
            base_url = self.base_url
            
        url = f"{base_url}/{endpoint}"
        print(f"   🌐 Making API request to: {url}")
        print(f"   📝 Method: {method}")
        print(f"   🔑 API Key: {self.api_key[:8]}...")
        
        # Prepare headers - correct format from documentation + anti-bot measures
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'hf-api-key': self.api_key,
            'hf-secret': self.api_secret,
            'Referer': 'https://cloud.higgsfield.ai',
            'Origin': 'https://cloud.higgsfield.ai'
        }
        
        # Prepare data
        if data:
            data_json = json.dumps(data).encode('utf-8')
            print(f"   📦 Data: {json.dumps(data, indent=2)}")
        else:
            data_json = None
        
        try:
            # Create request
            req = urllib.request.Request(url, data=data_json, headers=headers, method=method)
            
            # Add minimal delay to avoid rate limiting
            import time
            time.sleep(1)  # 1 second delay for speed
            
            # Make request
            print(f"   ⏳ Sending request...")
            with urllib.request.urlopen(req) as response:
                response_data = json.loads(response.read().decode('utf-8'))
                print(f"   ✅ Response received: {response_data}")
                return response_data
                
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            print(f"❌ API Error {e.code}: {error_body}")
            print(f"   Headers: {dict(e.headers)}")
            raise Exception(f"API request failed: {e.code} - {error_body}")
        except Exception as e:
            print(f"❌ Request failed: {e}")
            print(f"   Error type: {type(e).__name__}")
            raise Exception(f"Request failed: {e}")
    
    # Mock methods removed - REAL API ONLY
    
    def _poll_for_results(self, job_set_id):
        """Poll until job is completed"""
        # REAL API ONLY - NO MOCK MODE
        
        # Real polling implementation - balanced for speed and reliability
        max_attempts = 40  # 2 minutes max for reliable results
        for attempt in range(max_attempts):
            try:
                print(f"   🔍 Checking job status (attempt {attempt + 1}/{max_attempts})...")
                
                # Try a completely different approach - maybe we need to use a different base URL
                # or maybe the polling endpoint is completely different
                
                # FIXED: Use the correct polling endpoint from documentation
                # The correct endpoint is: GET /v1/job-sets/{job_set_id}
                polling_attempts = [
                    (f"v1/job-sets/{job_set_id}", self.base_url),  # Correct endpoint!
                ]
                
                response = None
                for endpoint, base_url in polling_attempts:
                    try:
                        print(f"   🔍 Trying: {base_url}/{endpoint}")
                        response = self._make_request_with_base_url(endpoint, method='GET', base_url=base_url)
                        print(f"   ✅ Success with: {base_url}/{endpoint}")
                        break
                    except Exception as e:
                        if "404" in str(e) or "unidentified route" in str(e):
                            print(f"   ❌ 404 for {base_url}/{endpoint}")
                            continue
                        else:
                            print(f"   ❌ Error for {base_url}/{endpoint}: {e}")
                            continue
                
                if response is None:
                    print(f"   ⏳ All polling attempts failed, waiting... ({attempt + 1}/{max_attempts})")
                    time.sleep(2)  # Fastest retry
                    continue
                
                
                print(f"   📊 Polling response: {response}")
                
                if response.get('jobs') and len(response['jobs']) > 0:
                    job = response['jobs'][0]
                    status = job.get('status')
                    print(f"   🔍 Job status: {status}")
                    
                    if status == 'completed':
                        # FIXED: Use correct result format from documentation
                        results = job.get('results', {})
                        video_url = None
                        
                        # Check the correct result format: results.raw.url
                        if results and 'raw' in results and 'url' in results['raw']:
                            video_url = results['raw']['url']
                            print(f"   ✅ Found video URL: {video_url}")
                            return video_url
                        else:
                            print(f"   ⚠️ No video URL found in results: {results}")
                            raise Exception("Completed job has no video URL")
                    elif status == 'failed':
                        error_message = job.get('error', 'Unknown API error')
                        raise Exception(f"Higgsfield API job failed: {error_message}")
                    elif status in ['pending', 'running', 'queued', 'in_progress']:
                        print(f"   ⏳ Waiting for completion... ({attempt + 1}/{max_attempts})")
                        time.sleep(2)  # Fastest polling for speed
                    else:
                        print(f"   ⚠️ Unknown job status: {status}")
                        time.sleep(5)
                else:
                    print(f"   ⚠️ No jobs found in response")
                    time.sleep(2)  # Fastest retry
                
            except Exception as e:
                print(f"   ❌ Polling error: {e}")
                time.sleep(3)  # Faster retry
        
        print("   ⏰ Generation timed out - this may be due to high API load")
        print("   💡 Tip: Try again in a few minutes or with a shorter audio file")
        raise Exception("Generation timed out - API may be experiencing high load")
    
    def text_to_image(self, prompt, aspect_ratio="16:9"):
        """Generate image from text prompt using Nano Banana model"""
        # REAL API ONLY - NO MOCK MODE
        
        print(f"   🎨 Generating image: '{prompt[:50]}...'")
        
        # FIXED: Use correct endpoint and parameters from documentation
        endpoint = "v1/text2image/nano-banana"
        base_url = self.base_url  # Use non-v1 base URL since endpoint already has v1
        
        data = {
            "params": {
                "prompt": prompt,
                "aspect_ratio": aspect_ratio,
                "input_images": []
            }
        }
        
        print(f"   🔄 Using correct endpoint: {endpoint}")
        print(f"   📦 Data: {json.dumps(data, indent=2)}")
        
        response = self._make_request_with_base_url(endpoint, data, base_url)
        job_set_id = response['id']
        print(f"   📝 Image generation submitted: {job_set_id}")
        return self._poll_for_results(job_set_id)
    
    def image_to_video(self, image_url, prompt, duration=5):
        """Animate image into video using Kling 2.5 Turbo model"""
        # REAL API ONLY - NO MOCK MODE
        
        print(f"   🎥 Animating image: '{prompt[:50]}...'")
        
        # FIXED: Use correct Kling 2.5 Turbo endpoint from documentation
        endpoint = "generate/kling-2-5"
        base_url = self.base_url  # Use non-v1 base URL
        
        data = {
            "params": {
                "model": "kling-v2-5-turbo",
                "duration": duration,
                "enhance_prompt": True,
                "input_image": {
                    "type": "image_url",
                    "image_url": image_url
                },
                "prompt": prompt
            }
        }
        
        print(f"   🔄 Using Kling 2.5 Turbo endpoint: {endpoint}")
        response = self._make_request_with_base_url(endpoint, data, base_url)
        job_set_id = response['id']
        print(f"   📝 Video generation submitted: {job_set_id}")
        return self._poll_for_results(job_set_id)
    
    def text_to_video(self, prompt, duration=6):
        """Generate video directly from text using Minimax T2V model"""
        # REAL API ONLY - NO MOCK MODE
        
        print(f"   ✨ Creating special video: '{prompt[:50]}...'")
        
        # FIXED: Use correct Minimax T2V endpoint from documentation
        endpoint = "generate/minimax-t2v"
        base_url = self.base_url  # Use non-v1 base URL
        
        data = {
            "params": {
                "duration": duration,
                "resolution": "768",
                "enable_prompt_optimizier": True,
                "prompt": prompt
            }
        }
        
        print(f"   🔄 Using Minimax T2V endpoint: {endpoint}")
        response = self._make_request_with_base_url(endpoint, data, base_url)
        job_set_id = response['id']
        
        print(f"   📝 Text-to-video generation submitted: {job_set_id}")
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