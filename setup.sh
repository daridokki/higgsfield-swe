#!/bin/bash

echo "🚀 Setting up Music Video Generator..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.11+ first."
    echo "   On macOS: brew install python@3.11"
    echo "   On Ubuntu: sudo apt install python3 python3-pip"
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install backend dependencies
echo "📚 Installing Python dependencies..."
pip install fastapi uvicorn librosa numpy scipy sqlalchemy httpx python-multipart aiofiles python-dotenv

# Create project structure
echo "📁 Creating project structure..."
mkdir -p backend/{services,routes,models,utils}
mkdir -p frontend/{components,styles,utils,types}

# Create basic files
echo "📄 Creating configuration files..."

# Backend requirements
cat > backend/requirements.txt << 'CONFIG'
fastapi==0.104.1
uvicorn[standard]==0.24.0
librosa==0.10.1
numpy==1.24.3
scipy==1.11.4
sqlalchemy==2.0.23
httpx==0.25.2
python-multipart==0.0.6
aiofiles==23.2.1
python-dotenv==1.0.0
CONFIG

# Environment template
cat > backend/.env.example << 'CONFIG'
HIGGSFIELD_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///./music_videos.db
UPLOAD_DIR=./uploads
CONFIG

# Basic backend server
cat > backend/main.py << 'CONFIG'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Music Video Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Music Video Generator API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
CONFIG

echo "✅ Setup complete!"
echo ""
echo "🎯 Next steps:"
echo "   1. source venv/bin/activate"
echo "   2. cd backend"
echo "   3. uvicorn main:app --reload"
echo ""
echo "🚀 Your backend will be running at http://localhost:8000"
