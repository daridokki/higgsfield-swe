#!/usr/bin/env python3
"""
Simple test to verify Higgsfield API connection
"""

import sys
import os
import json
import urllib.request
import urllib.error

# Add backend to path
sys.path.append('backend')

def test_simple_api_call():
    """Test a simple API call to Higgsfield"""
    print("🧪 Testing Simple Higgsfield API Call...")
    
    # Your credentials
    api_key = "7f3a2ee6-aeb6-4dc7-bd70-a9c01e841b0c"
    api_secret = "e5d0fdb10e97f43dfcee9031d78ec1ef28e254c20c817010c60050b67f9459eb"
    
    # Test endpoint
    url = "https://platform.higgsfield.ai/v1/text2image/soul"
    
    # Headers from documentation
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'hf-api-key': api_key,
        'hf-secret': api_secret
    }
    
    # Test data from documentation
    data = {
        "params": {
            "prompt": "cyberpunk city with neon lights, vibrant colors",
            "width_and_height": "1696x960",
            "enhance_prompt": True,
            "quality": "720p",
            "batch_size": 1
        }
    }
    
    print(f"🌐 Testing URL: {url}")
    print(f"📦 Data: {json.dumps(data, indent=2)}")
    
    try:
        # Create request
        data_json = json.dumps(data).encode('utf-8')
        req = urllib.request.Request(url, data=data_json, headers=headers, method='POST')
        
        # Make request
        print("⏳ Sending request...")
        with urllib.request.urlopen(req) as response:
            response_data = json.loads(response.read().decode('utf-8'))
            print(f"✅ SUCCESS! Response: {response_data}")
            return True
            
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"❌ HTTP Error {e.code}: {error_body}")
        print(f"   Headers: {dict(e.headers)}")
        return False
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return False

if __name__ == "__main__":
    success = test_simple_api_call()
    
    if success:
        print("\n🎉 API test PASSED!")
    else:
        print("\n❌ API test FAILED!")
        print("This will help us identify the exact issue.")
