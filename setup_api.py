#!/usr/bin/env python3
"""
Setup script for Higgsfield API credentials
"""

import os
import sys

def create_env_file():
    """Create .env file with API credentials"""
    env_content = """# Higgsfield API Credentials
# Replace these with your actual API credentials from Higgsfield
HIGGSFIELD_API_KEY=YOUR_API_KEY_HERE
HIGGSFIELD_API_SECRET=YOUR_API_SECRET_HERE

# Set to false to use real API (requires valid credentials)
USE_MOCK_API=true

# Budget settings
TOTAL_BUDGET=100.00
"""
    
    env_path = "backend/.env"
    
    if os.path.exists(env_path):
        print(f"⚠️  {env_path} already exists")
        response = input("Do you want to overwrite it? (y/N): ")
        if response.lower() != 'y':
            print("Keeping existing .env file")
            return
    
    with open(env_path, 'w') as f:
        f.write(env_content)
    
    print(f"✅ Created {env_path}")
    print("📝 Please edit the file and add your real API credentials")

def main():
    print("🚀 Setting up Higgsfield API credentials...")
    print()
    
    # Check if we're in the right directory
    if not os.path.exists("backend"):
        print("❌ Please run this script from the project root directory")
        sys.exit(1)
    
    # Create .env file
    create_env_file()
    
    print()
    print("🔧 Next steps:")
    print("1. Get your API credentials from https://cloud.higgsfield.ai/")
    print("2. Edit backend/.env and replace YOUR_API_KEY_HERE and YOUR_API_SECRET_HERE")
    print("3. Set USE_MOCK_API=false to use real API")
    print("4. Restart your backend server")
    print()
    print("💡 For testing, you can keep USE_MOCK_API=true to use sample videos")
    print("   (This won't spend your credits but will show Big Buck Bunny videos)")

if __name__ == "__main__":
    main()
