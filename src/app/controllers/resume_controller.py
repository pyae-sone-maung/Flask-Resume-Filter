from flask import Blueprint, request, jsonify, current_app

resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/resume-data', methods=['GET'])
def get_resume_data():
    return jsonify({'message': 'resume_filter success.'}), 200