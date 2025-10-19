from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import uuid
import json
from werkzeug.utils import secure_filename
from music_analyzer import MusicAnalyzer
from video_generator import VideoGenerator
from config import Config

app = Flask(__name__)

# Configure CORS for production
allowed_origins = [
    'http://localhost:3000', 
    'http://127.0.0.1:3000',
    # Vercel frontend domains (both old and new)
    'https://vision-of-sound-8wx4495w6-daridokkis-projects.vercel.app',
    'https://vision-of-sound.vercel.app',
    # Allow all Vercel domains for now
    'https://*.vercel.app'
]

# Allow all origins in development, specific origins in production
if os.environ.get('ENVIRONMENT') == 'production':
    CORS(app, origins=['*'])  # Temporarily allow all origins
else:
    CORS(app, origins=['*'])

# Configure upload settings
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Initialize components
print("🚀 Initializing Music-to-Video Generator with REAL Higgsfield API...")
print(f"   API Key: {Config.HIGGSFIELD_API_KEY[:8]}...")
print(f"   API Secret: {Config.HIGGSFIELD_API_SECRET[:8]}...")

music_analyzer = MusicAnalyzer()
video_generator = VideoGenerator()

# Global progress tracking
current_progress = {
    'step': '',
    'progress': 0,
    'current_step': 0,
    'total_steps': 6,
    'is_complete': False
}

print("✅ All components initialized with REAL API!")

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "Music-to-Video Server is running!",
        "endpoints": {
            "POST /analyze-music": "Analyze music without generating video",
            "POST /generate-video": "Full music-to-video generation",
            "GET /progress": "Get generation progress"
        }
    })


@app.route('/progress', methods=['GET'])
def get_progress():
    """Get current generation progress"""
    return jsonify(current_progress)

@app.route('/analyze-music', methods=['POST'])
def analyze_music():
    """Analyze uploaded music file"""
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file type"}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)
        
        # Analyze music
        analysis = music_analyzer.analyze_music(file_path)
        
        # Clean up uploaded file
        os.remove(file_path)
        
        return jsonify({
            "status": "success",
            "analysis": analysis,
            "message": "Music analysis completed!"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate-video', methods=['POST'])
def generate_video():
    """Generate video from uploaded music file"""
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file type"}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)
        
        # Generate video using REAL Higgsfield API
        print("🎬 Starting video generation with REAL Higgsfield API...")
        print(f"   File: {file_path}")
        print(f"   File exists: {os.path.exists(file_path)}")
        
        try:
            # Reset progress
            current_progress.update({
                'step': 'Starting generation...',
                'progress': 0,
                'current_step': 0,
                'total_steps': 6,
                'is_complete': False
            })
            
            def progress_callback(progress_data):
                global current_progress
                current_progress.update(progress_data)
                print(f"📊 Progress: {progress_data['step']} ({progress_data['progress']}%)")
            
            result = video_generator.create_video_from_music(file_path, progress_callback)
            
            # Mark as complete
            current_progress.update({
                'step': 'Generation complete!',
                'progress': 100,
                'is_complete': True
            })
            
            print("✅ Video generation completed!")
            print(f"   Generated {len(result['video_urls'])} videos")
            
            # DEBUG: Print video URLs
            for i, video in enumerate(result['video_urls']):
                print(f"   Video {i+1}: {video['url'][:50]}...")
                print(f"   Type: {video['type']}")
                print(f"   Description: {video.get('description', 'N/A')[:50]}...")
            
            # Clean up uploaded file
            os.remove(file_path)
            
            return jsonify({
                "status": "success",
                "result": result,
                "message": f"Successfully generated {len(result['video_urls'])} video clips!"
            })
            
        except Exception as e:
            print(f"❌ Video generation failed: {e}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            
            # Clean up uploaded file
            if os.path.exists(file_path):
                os.remove(file_path)
            
            return jsonify({
                "status": "error",
                "error": str(e),
                "message": "Video generation failed. Check server logs for details."
            }), 500
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(413)
def too_large(e):
    return jsonify({"error": "File too large. Maximum size is 50MB."}), 413

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Create upload folder
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
    
    # Get port from environment (for production deployment)
    port = int(os.environ.get('PORT', 8000))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    print("🚀 Starting Music-to-Video Flask Server...")
    print("📍 Available Endpoints:")
    print(f"   GET  http://{host}:{port}/health")
    print(f"   POST http://{host}:{port}/analyze-music") 
    print(f"   POST http://{host}:{port}/generate-video")
    print("")
    
    app.run(host=host, port=port, debug=debug)
