import logging
from flask import Flask, jsonify
from config import config_by_name

from src.core.logging.logging_config import setup_logging
from src.core.error_handling.handlers import register_error_handlers

from src.app.routes import register_blueprints


def create_app(confg_object):
    app = Flask(__name__)
    app.config.from_object(confg_object)
    
    setup_logging(app.logger)
    app.logger.info(f"Starting app in {confg_object.__class__.__name__} mode.")
    
    register_blueprints(app)
    
    register_error_handlers(app)
    
    @app.route('/')
    def health_check():
        return jsonify({'status': 'succss', 'message': 'API service is running!'})
    
    return app