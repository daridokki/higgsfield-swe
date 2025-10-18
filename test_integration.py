#!/usr/bin/env python3
"""
Integration test script for the Music-to-Video application
Tests the connection between frontend and backend
"""

import requests
import json
import time
import os
from pathlib import Path

def test_backend_health():
    """Test if backend is running and healthy"""
    try:
        response = requests.get('http://localhost:5000/health', timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Backend health check passed")
            print(f"   Status: {data.get('status')}")
            print(f"   Message: {data.get('message')}")
            return True
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend not accessible: {e}")
        return False

def test_budget_endpoint():
    """Test budget endpoint"""
    try:
        response = requests.get('http://localhost:5000/budget', timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Budget endpoint working")
            print(f"   Used: ${data.get('used')}")
            print(f"   Remaining: ${data.get('remaining')}")
            return True
        else:
            print(f"❌ Budget endpoint failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Budget endpoint error: {e}")
        return False

def test_frontend_accessibility():
    """Test if frontend is accessible"""
    try:
        response = requests.get('http://localhost:3000', timeout=5)
        if response.status_code == 200:
            print("✅ Frontend is accessible")
            return True
        else:
            print(f"❌ Frontend not accessible: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Frontend not accessible: {e}")
        return False

def create_test_audio():
    """Create a simple test audio file"""
    # This is a placeholder - in a real test, you'd create an actual audio file
    # For now, we'll just check if the uploads directory exists
    uploads_dir = Path('backend/uploads')
    uploads_dir.mkdir(exist_ok=True)
    print("✅ Uploads directory ready")
    return True

def main():
    """Run all integration tests"""
    print("🧪 Running Music-to-Video Integration Tests")
    print("=" * 50)
    
    tests = [
        ("Backend Health Check", test_backend_health),
        ("Budget Endpoint", test_budget_endpoint),
        ("Frontend Accessibility", test_frontend_accessibility),
        ("File Upload Setup", create_test_audio),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing: {test_name}")
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to use.")
        print("\n📍 Access your application at:")
        print("   Frontend: http://localhost:3000")
        print("   Backend API: http://localhost:5000")
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        print("\n💡 Make sure both servers are running:")
        print("   Backend: python backend/app_flask.py")
        print("   Frontend: cd frontend && npm run dev")

if __name__ == '__main__':
    main()
