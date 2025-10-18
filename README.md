# 🎵 SonicCanvas - Music to Video Generator

Transform your audio into mesmerizing visual experiences using AI-powered video generation.

## ✨ Features

- **Real-time Music Analysis**: Extract tempo, energy, mood, and more from your audio files
- **AI Video Generation**: Create stunning videos using Higgsfield AI APIs
- **Smart Budget Management**: Track API usage and costs
- **Modern UI**: Beautiful, responsive interface built with Next.js
- **Multiple Video Types**: Generate regular scenes and special moments

## 🚀 Quick Start

### Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.8 or higher)
- **Git**

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd higgsfield-swe
   ```

2. **Run the development setup script**
   ```bash
   python start_dev.py
   ```

   This will automatically:
   - Install all dependencies
   - Start the Flask backend server (port 5000)
   - Start the Next.js frontend server (port 3000)

3. **Open your browser**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

### Manual Setup (Alternative)

If you prefer to set up manually:

1. **Backend Setup**
   ```bash
   cd backend
   pip install -r requirements.txt
   python app_flask.py
   ```

2. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## 🔧 Configuration

### API Keys (Optional - for real video generation)

To enable real video generation (instead of mock mode):

1. Get your Higgsfield API credentials from [platform.higgsfield.ai](https://platform.higgsfield.ai)
2. Set environment variables:
   ```bash
   export HIGGSFIELD_API_KEY="your_api_key"
   export HIGGSFIELD_API_SECRET="your_api_secret"
   ```

3. Or create a `.env` file in the backend directory:
   ```
   HIGGSFIELD_API_KEY=your_api_key
   HIGGSFIELD_API_SECRET=your_api_secret
   ```

### Mock Mode (Default)

By default, the application runs in mock mode, which:
- Simulates API responses without using real credits
- Perfect for development and testing
- No API keys required

## 📁 Project Structure

```
higgsfield-swe/
├── backend/                 # Flask API server
│   ├── app_flask.py        # Main Flask application
│   ├── music_analyzer.py   # Audio analysis with librosa
│   ├── video_generator.py  # Video generation logic
│   ├── higgsfield_client.py # API client for Higgsfield
│   ├── credit_manager.py   # Budget tracking
│   └── config.py          # Configuration
├── frontend/               # Next.js React application
│   ├── app/               # Next.js app directory
│   ├── components/        # React components
│   ├── lib/              # API service layer
│   └── package.json       # Frontend dependencies
└── start_dev.py          # Development startup script
```

## 🎯 How It Works

1. **Upload Audio**: User uploads an audio file (MP3, WAV, M4A, OGG)
2. **Music Analysis**: Backend analyzes the audio using librosa to extract:
   - Tempo (BPM)
   - Energy level
   - Mood classification
   - Duration and beat count
3. **Video Planning**: System creates a video plan based on music characteristics
4. **AI Generation**: Uses Higgsfield AI to generate:
   - Images from text prompts
   - Videos from images
   - Special moments for energetic music
5. **Result Display**: Shows generated videos with download options

## 🛠️ API Endpoints

- `GET /health` - Health check
- `GET /budget` - Get budget status
- `POST /analyze-music` - Analyze uploaded audio
- `POST /generate-video` - Generate video from audio

## 💰 Budget Management

The system tracks API usage costs:
- Text-to-image: ~$0.05 per generation
- Image-to-video: ~$0.15 per generation
- Text-to-video: ~$0.25 per generation
- Default budget: $100.00

## 🔍 Development

### Backend Development
- Uses Flask with CORS enabled
- File upload handling with size limits
- Error handling and logging
- Mock mode for testing

### Frontend Development
- Next.js 14 with TypeScript
- Tailwind CSS for styling
- Real-time API integration
- Error handling and loading states

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🆘 Troubleshooting

### Common Issues

1. **Port already in use**
   - Backend: Change port in `app_flask.py`
   - Frontend: Change port in `package.json` scripts

2. **Dependencies not installing**
   - Ensure you have the correct Node.js and Python versions
   - Try clearing npm cache: `npm cache clean --force`

3. **API errors**
   - Check your internet connection
   - Verify API keys are correct
   - Check the console for detailed error messages

### Getting Help

- Check the console logs for detailed error messages
- Ensure all dependencies are installed
- Verify that both servers are running
- Check that ports 3000 and 5000 are available

---

**Happy creating! 🎨✨**