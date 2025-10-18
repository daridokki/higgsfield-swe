#!/bin/bash

# SonicCanvas Deployment Script
echo "🚀 Starting SonicCanvas Deployment..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📝 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit: SonicCanvas Music-to-Video Generator"
fi

echo "✅ Deployment preparation complete!"
echo ""
echo "📋 Next Steps:"
echo "1. Push to GitHub: git push origin main"
echo "2. Deploy Backend to Railway"
echo "3. Deploy Frontend to Vercel"
echo "4. Update CORS settings with production URLs"
echo ""
echo "🔗 See deployment-guide.md for detailed instructions"
