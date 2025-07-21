class APIError(Exception):
    def __init__(self, message, status_code=500, error=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error = error if error is not None else []
        

class BadRequestError(APIError):
    status_code = 400
    
class UnauthorizedError(APIError):
    status_code = 401
    
class NotFoundError(APIError):
    status_code = 404
    
class InternalServerError(APIError):
    status_code = 500