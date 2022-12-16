from flask import Blueprint
from flask_jwt_extended import JWTManager
API = Blueprint('API', __name__)
jwt = JWTManager()


