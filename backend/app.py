from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import uuid
from video_generator import VideoGenerator
from config import Config

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Initialize our video generator
video_gen = VideoGenerator()

# Create upload folder
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy", 
        "message": "Music-to-Video Server is running!",
        "endpoints": {
            "POST /analyze-music": "Analyze music without generating video",
            "POST /generate-video": "Full music-to-video generation", 
            "GET /budget": "Check budget status"
        }
    })

@app.route('/analyze-music', methods=['POST'])
def analyze_music():
    """Analyze music without generating video"""
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    if not allowed_file(audio_file.filename):
        return jsonify({"error": "File type not allowed. Use MP3, WAV, M4A, or OGG"}), 400
    
    # Save uploaded file temporarily
    file_path = os.path.join(Config.UPLOAD_FOLDER, f"{uuid.uuid4()}_{audio_file.filename}")
    audio_file.save(file_path)
    
    try:
        # Analyze music only
        analysis = video_gen.music_analyzer.analyze_music(file_path)
        
        # Clean up
        os.remove(file_path)
        
        return jsonify({
            "status": "success",
            "analysis": analysis,
            "message": "Music analysis completed!"
        })
        
    except Exception as e:
        # Clean up on error too
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"error": str(e)}), 500

@app.route('/generate-video', methods=['POST'])
def generate_video():
    """Full music-to-video generation"""
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    if not allowed_file(audio_file.filename):
        return jsonify({"error": "File type not allowed. Use MP3, WAV, M4A, or OGG"}), 400
    
    # Save uploaded file temporarily
    file_path = os.path.join(Config.UPLOAD_FOLDER, f"{uuid.uuid4()}_{audio_file.filename}")
    audio_file.save(file_path)
    
    try:
        # Generate complete video
        result = video_gen.create_video_from_music(file_path)
        
        # Clean up
        os.remove(file_path)
        
        return jsonify({
            "status": "success", 
            "result": result,
            "message": f"Successfully generated {len(result['video_urls'])} video clips!"
        })
        
    except Exception as e:
        # Clean up on error
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"error": str(e)}), 500

@app.route('/budget', methods=['GET'])
def get_budget():
    """Get current budget status"""
    return jsonify({
        "used": round(video_gen.credit_manager.used_budget, 2),
        "remaining": round(video_gen.credit_manager.get_remaining_budget(), 2),
        "total": video_gen.credit_manager.total_budget,
        "percentage_used": round(video_gen.credit_manager.get_usage_percentage(), 1)
    })

if __name__ == '__main__':
    print("🚀 Starting Music-to-Video Server...")
    print("📍 Available Endpoints:")
    print("   GET  http://localhost:5000/health")
    print("   POST http://localhost:5000/analyze-music") 
    print("   POST http://localhost:5000/generate-video")
    print("   GET  http://localhost:5000/budget")
    print("")
    print("💡 Tip: Use USE_MOCK_API=true for testing without spending credits")
    print("")
    
    app.run(debug=True, host='0.0.0.0', port=5000)