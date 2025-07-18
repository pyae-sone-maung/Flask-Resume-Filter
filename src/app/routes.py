from src.app.controllers.resume_controller import resume_bp

def register_blueprints(app):
    app.register_blueprint(resume_bp, url_prefix='/api/resume')