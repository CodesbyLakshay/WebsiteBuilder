from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt

def role_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated_function(*args, **kwargs):
            claims = get_jwt()
            user_role = claims.get('role')
            if user_role not in roles:
                return jsonify(message="Permission denied"), 403
            return fn(*args, **kwargs)
        return decorated_function
    return wrapper
