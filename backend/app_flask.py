from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import uuid
import json
from werkzeug.utils import secure_filename
from music_analyzer import MusicAnalyzer
from video_generator import VideoGenerator
from credit_manager import CreditManager
from config import Config

app = Flask(__name__)
CORS(app)

# Configure upload settings
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Initialize components
music_analyzer = MusicAnalyzer()
video_generator = VideoGenerator()
credit_manager = CreditManager(Config.TOTAL_BUDGET)

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
            "GET /budget": "Check budget status"
        }
    })

@app.route('/budget', methods=['GET'])
def get_budget():
    """Get current budget status"""
    return jsonify({
        "used": round(credit_manager.used_budget, 2),
        "remaining": round(credit_manager.get_remaining_budget(), 2),
        "total": credit_manager.total_budget,
        "percentage_used": round(credit_manager.get_usage_percentage(), 1)
    })

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
        
        # Generate video
        result = video_generator.create_video_from_music(file_path)
        
        # Clean up uploaded file
        os.remove(file_path)
        
        return jsonify({
            "status": "success",
            "result": result,
            "message": f"Successfully generated {len(result['video_urls'])} video clips!"
        })
        
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
    
    print("🚀 Starting Music-to-Video Flask Server...")
    print("📍 Available Endpoints:")
    print("   GET  http://localhost:5000/health")
    print("   POST http://localhost:5000/analyze-music") 
    print("   POST http://localhost:5000/generate-video")
    print("   GET  http://localhost:5000/budget")
    print("")
    
    app.run(host='localhost', port=5000, debug=True)
