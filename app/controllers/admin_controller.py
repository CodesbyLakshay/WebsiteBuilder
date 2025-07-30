from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.admin_service import AdminService
from app.utils.decorators import role_required

bp = Blueprint('admin', __name__, url_prefix='/admin')
admin_service = AdminService()

@bp.route('/users', methods=['GET'])
@jwt_required()
@role_required('Admin')
def get_users():
    return admin_service.get_users()

@bp.route('/users/<user_id>', methods=['PUT'])
@jwt_required()
@role_required('Admin')
def update_user_role(user_id):
    data = request.get_json()
    return admin_service.update_user_role(user_id, data)

@bp.route('/roles', methods=['GET'])
@jwt_required()
@role_required('Admin')
def get_roles():
    return admin_service.get_roles()

@bp.route('/roles', methods=['POST'])
@jwt_required()
@role_required('Admin')
def create_role():
    data = request.get_json()
    return admin_service.create_role(data)
