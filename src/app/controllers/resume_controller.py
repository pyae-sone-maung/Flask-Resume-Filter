import os
from flask import Blueprint, request, jsonify, current_app
from src.app.services.resume_service import resume_service
from src.app.dtos.base_response import success_response, fail_response

resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/resume-data', methods=['GET'])
def get_resume_data():
    try:
        resume_data = resume_service.get_porcessed_resume_data()
        print(resume_data)
        
        response_object = success_response(message=None, data=resume_data)
        return jsonify(response_object.to_dict()), 200
    except Exception as ex:
        current_app.logger.error(f"Error in get_resume_data : {ex}")
        response_object = fail_response(message=f"Error in resume-data.", error=str(ex))
        return jsonify(response_object.to_dict()), 200