from flask import jsonify, request
from src.core.error_handling.exception import APIError

def register_error_handlers(app):
    @app.errorhandler(APIError)
    def handle_api_error(error):
        response = jsonify({"message": error.message})
        response.status_code = error.status_code
        app.logger.error(f"API Error: {error.message} - Status: {error.status_code}")
        return response
    
    @app.errorhandler(400)
    def bad_request_error(error):
        app.logger.warning(f"400 Bad Request: { request.url } - { error: error }")
        return jsonify({'message': 'Bad Request'}), 400
    
    @app.errorhandler(404)
    def not_found_error(error):
        app.logger.warning(f"404 Not Found: { request.url } - { error: error }")
        return jsonify({'message': 'Not Found'}), 404
    
    @app.errorhandler(401)
    def unauthorized_error(error):
        app.logger.warning(f"401 Unauthorized: { request.url } - { error: error }")
        return jsonify({'message': 'Unauthorized'}), 401
    
    @app.errorhandler(500)
    def internal_server_error(error):
        app.logger.exception("Internal Server Error")
        return jsonify({'message': 'An unexpected error occurred. Please try again later.'}), 500
    
    app.logger.info("Error handlers registered.")