# This file contains the routes for the authentication API. It is used to register and login users.
from . import API
from flask import request, jsonify
from database import User
from flask_jwt_extended import create_access_token, set_access_cookies, unset_access_cookies, jwt_required


@API.route('/auth/login', methods=['POST'])
def login():
    req = request.get_json()
    user = User.query.filter_by(username=req['username']).first()
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    if not user.check_password(req['password']):
        return jsonify({'error': 'Invalid password'}), 401
    access_token = create_access_token(identity=user.userID)
    response = jsonify({'message': 'Login successful', 'access_token': access_token})
    set_access_cookies(response, access_token)
    return response, 200

@API.route('/auth/logout', methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({'message': 'Logout successful'})
    unset_access_cookies(response)
    return response, 200
