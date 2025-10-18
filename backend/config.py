import os

class Config:
    # Higgsfield API credentials - YOU WILL NEED TO SET THESE!
    HIGGSFIELD_API_KEY = os.getenv('HIGGSFIELD_API_KEY', 'YOUR_API_KEY_HERE')
    HIGGSFIELD_API_SECRET = os.getenv('HIGGSFIELD_API_SECRET', 'YOUR_API_SECRET_HERE')
    
    # API endpoints
    HIGGSFIELD_BASE_URL = "https://platform.higgsfield.ai/v1"
    
    # Model configurations
    MODELS = {
        'text_to_image': 'nano_banana',
        'image_to_video': 'kling-2-5', 
        'text_to_video': 'kling-2-1-master-t2v'
    }
    
    # Generation settings
    MAX_POLLING_TIME = 300  # 5 minutes max wait
    POLLING_INTERVAL = 5    # Check every 5 seconds
    
    # Budget (in dollars)
    TOTAL_BUDGET = 100.00
    
    # File upload settings
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'mp3', 'wav', 'm4a', 'ogg'}