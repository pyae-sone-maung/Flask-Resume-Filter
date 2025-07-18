import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Base configuration JWT, SECRE_KEY, etc 
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}