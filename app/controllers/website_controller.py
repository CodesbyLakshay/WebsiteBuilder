from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required
from app.services.website_service import WebsiteService
from app.utils.decorators import role_required

bp = Blueprint('website', __name__)
website_service = WebsiteService()

@bp.route('/websites', methods=['GET'])
@jwt_required()
def get_websites():
    return website_service.get_websites()

@bp.route('/websites/<id>', methods=['GET'])
@jwt_required()
def get_website(id):
    return website_service.get_website(id)

@bp.route('/websites', methods=['POST'])
@jwt_required()
@role_required('Admin', 'Editor')
def create_website():
    data = request.get_json()
    return website_service.create_website(data)

@bp.route('/websites/<id>', methods=['PUT'])
@jwt_required()
@role_required('Admin', 'Editor')
def update_website(id):
    data = request.get_json()
    return website_service.update_website(id, data)

@bp.route('/websites/<id>', methods=['DELETE'])
@jwt_required()
@role_required('Admin', 'Editor')
def delete_website(id):
    return website_service.delete_website(id)

@bp.route('/preview/<id>', methods=['GET'])
def preview_website(id):
    response, status_code = website_service.get_website(id)
    if status_code == 200:
        website = response.get('website')
        if website:
            return render_template('preview.html', website=website)
    return jsonify(response), status_code
