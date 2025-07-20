from flask import current_app
from werkzeug.utils import secure_filename

def allowed_file(filename) -> bool:
    if not filename:
        return False
    
    secured = secure_filename(filename)
    if not secured or '.' not in secured:
        return False
    
    extension = secured.split('.', 1)[1].lower()
    return extension in current_app.config['ALLOWED_EXTENSIONS']

def get_file_extension(filename)-> str | None:
    if not filename:
        return None
    secured = secure_filename(filename)
    extension = secured.split('.', 1)[1].lower()
    return extension