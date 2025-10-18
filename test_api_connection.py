#!/usr/bin/env python3
"""
Test script to verify Higgsfield API connection and identify issues
"""

import sys
import os

# Add backend to path
sys.path.append('backend')

def test_api_connection():
    """Test the Higgsfield API connection"""
    print("🧪 Testing Higgsfield API Connection...")
    print("=" * 50)
    
    try:
        from backend.config import Config
        from backend.higgsfield_client import HiggsfieldClient
        
        print(f"✅ Config loaded")
        print(f"   API Key: {Config.HIGGSFIELD_API_KEY[:8]}...")
        print(f"   API Secret: {Config.HIGGSFIELD_API_SECRET[:8]}...")
        print(f"   Base URL: {Config.HIGGSFIELD_BASE_URL}")
        
        # Create client
        print("\n🔧 Creating Higgsfield client...")
        client = HiggsfieldClient(Config.HIGGSFIELD_API_KEY, Config.HIGGSFIELD_API_SECRET)
        
        if client.use_mock:
            print("❌ Client is in MOCK mode!")
            return False
        
        print("✅ Client created successfully")
        
        # Test a simple API call
        print("\n🎨 Testing image generation...")
        try:
            image_url = client.text_to_image("cyberpunk city with neon lights, vibrant colors")
            print(f"✅ Image generated successfully: {image_url[:50]}...")
            return True
        except Exception as e:
            print(f"❌ Image generation failed: {e}")
            print(f"   Error type: {type(e).__name__}")
            import traceback
            print(f"   Traceback: {traceback.format_exc()}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    success = test_api_connection()
    
    if success:
        print("\n🎉 API connection test PASSED!")
        print("✅ Your Higgsfield API is working correctly!")
    else:
        print("\n❌ API connection test FAILED!")
        print("🔍 Check the error messages above to identify the issue.")
        print("\n💡 Common issues:")
        print("   - Invalid API credentials")
        print("   - Network connectivity problems")
        print("   - API endpoint changes")
        print("   - Missing dependencies")
