from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models.user import User

class AuthService:
    def signup(self, data):
        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        user = User(email=data['email'], password=hashed_password, role='Viewer')
        user.save()
        return {'message': 'User created successfully'}, 201

    def login(self, data):
        user_data = User.find_by_email(data['email'])
        if user_data and check_password_hash(user_data['password'], data['password']):
            access_token = create_access_token(
                identity=user_data['email'],
                additional_claims={'role': user_data['role']}
            )
            return {'access_token': access_token}, 200
        return {'message': 'Invalid credentials'}, 401
