from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

bp = Blueprint('auth', __name__)
auth_service = AuthService()

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    return auth_service.signup(data)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return auth_service.login(data)
