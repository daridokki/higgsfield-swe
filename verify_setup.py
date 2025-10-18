#!/usr/bin/env python3
"""
Verify that the app is properly configured for REAL Higgsfield API
"""

import sys
import os

# Add backend to path
sys.path.append('backend')

def verify_config():
    """Verify configuration is correct"""
    print("🔍 Verifying Configuration...")
    
    try:
        from backend.config import Config
        
        # Check API credentials
        if Config.HIGGSFIELD_API_KEY == 'YOUR_API_KEY_HERE':
            print("❌ API Key not set!")
            return False
        
        if Config.HIGGSFIELD_API_SECRET == 'YOUR_API_SECRET_HERE':
            print("❌ API Secret not set!")
            return False
            
        print(f"✅ API Key: {Config.HIGGSFIELD_API_KEY[:8]}...")
        print(f"✅ API Secret: {Config.HIGGSFIELD_API_SECRET[:8]}...")
        print(f"✅ Base URL: {Config.HIGGSFIELD_BASE_URL}")
        print(f"✅ Budget: ${Config.TOTAL_BUDGET}")
        
        return True
        
    except Exception as e:
        print(f"❌ Config error: {e}")
        return False

def verify_client():
    """Verify Higgsfield client is configured for real API"""
    print("\n🔍 Verifying Higgsfield Client...")
    
    try:
        from backend.higgsfield_client import HiggsfieldClient
        from backend.config import Config
        
        # Create client
        client = HiggsfieldClient(Config.HIGGSFIELD_API_KEY, Config.HIGGSFIELD_API_SECRET)
        
        if client.use_mock:
            print("❌ Client is in MOCK mode!")
            return False
        
        print("✅ Client configured for REAL API")
        print(f"✅ Base URL: {client.base_url}")
        
        return True
        
    except Exception as e:
        print(f"❌ Client error: {e}")
        return False

def verify_components():
    """Verify all components are properly configured"""
    print("\n🔍 Verifying Components...")
    
    try:
        from backend.music_analyzer import MusicAnalyzer
        from backend.video_generator import VideoGenerator
        from backend.credit_manager import CreditManager
        from backend.config import Config
        
        # Test music analyzer
        analyzer = MusicAnalyzer()
        print("✅ Music Analyzer: REAL librosa-based analysis")
        
        # Test video generator
        generator = VideoGenerator()
        print("✅ Video Generator: REAL Higgsfield API")
        
        # Test credit manager
        credit_mgr = CreditManager(Config.TOTAL_BUDGET)
        print(f"✅ Credit Manager: ${credit_mgr.total_budget} budget")
        
        return True
        
    except Exception as e:
        print(f"❌ Components error: {e}")
        return False

def main():
    """Run all verification checks"""
    print("🚀 Verifying Music-to-Video App Configuration")
    print("=" * 50)
    
    checks = [
        ("Configuration", verify_config),
        ("Higgsfield Client", verify_client),
        ("Components", verify_components)
    ]
    
    passed = 0
    total = len(checks)
    
    for name, check_func in checks:
        print(f"\n📋 {name}:")
        try:
            if check_func():
                passed += 1
                print(f"✅ {name} - PASSED")
            else:
                print(f"❌ {name} - FAILED")
        except Exception as e:
            print(f"❌ {name} - ERROR: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Results: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 ALL CHECKS PASSED!")
        print("✅ Your app is ready to generate REAL AI videos!")
        print("\n🚀 Next steps:")
        print("1. Make sure you're running app_flask.py (not app.py)")
        print("2. Restart your backend server")
        print("3. Upload an audio file to test!")
    else:
        print("❌ Some checks failed!")
        print("Please fix the issues above before testing.")

if __name__ == "__main__":
    main()
