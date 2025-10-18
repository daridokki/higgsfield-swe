import os

class Config:
    # Higgsfield API credentials - REAL CREDENTIALS SET!
    HIGGSFIELD_API_KEY = os.getenv('HIGGSFIELD_API_KEY', '7f3a2ee6-aeb6-4dc7-bd70-a9c01e841b0c')
    HIGGSFIELD_API_SECRET = os.getenv('HIGGSFIELD_API_SECRET', 'e5d0fdb10e97f43dfcee9031d78ec1ef28e254c20c817010c60050b67f9459eb')
    
    # API endpoints - correct base URL from documentation
    HIGGSFIELD_BASE_URL = "https://platform.higgsfield.ai/v1"
    
    # Model configurations - BEST models for music-to-video project
    # FIXED: Using correct model names from documentation
    MODELS = {
        'text_to_image': 'nano-banana',        # Nano Banana - Text to Image
        'image_to_video': 'kling-2-5',         # Kling 2.5 Turbo - Image to Video  
        'text_to_video': 'minimax-t2v'        # Minimax T2V - Text to Video
    }
    
    # Generation settings
    MAX_POLLING_TIME = 300  # 5 minutes max wait
    POLLING_INTERVAL = 5    # Check every 5 seconds
    
    # Budget (in dollars)
    TOTAL_BUDGET = 100.00
    
    # File upload settings
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'mp3', 'wav', 'm4a', 'ogg'}