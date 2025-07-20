import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Base configuration JWT, SECRE_KEY, etc 
    
    # File Upload Settings
    UPLOAD_FOLDER = os.path.join("src", "assets", "uploads")
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'docx', 'xlsx'}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 16 MB limit for uploads

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}