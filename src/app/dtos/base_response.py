import json

class ApiResponse:
    def __init__(self, status, message=None, data=None, error=None):
        self.status = status
        self.message = message
        self.data = data
        self.error = error

    def to_dict(self):
        response = {
            "status": self.status,
            "message": self.message,
            "data": self.data,
            "error": self.error
        }
        return {key: value for key, value in response.items() if value is not None}
        
def success_response(message, data):
    return ApiResponse(status="success", message=message, data=data)

def fail_response(message, error):
    return ApiResponse(status="error", message=message, error=error)