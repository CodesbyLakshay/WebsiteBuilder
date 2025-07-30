from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from app.config import Config

mongo = PyMongo()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    jwt.init_app(app)

    from app.controllers.auth_controller import bp as auth_bp
    from app.controllers.website_controller import bp as website_bp
    from app.controllers.admin_controller import bp as admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(website_bp)
    app.register_blueprint(admin_bp)

    return app
