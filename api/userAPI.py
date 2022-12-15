from . import API
from flask import request, jsonify
from database import db, User

@API.route('/user', methods=['GET'])
def get_user():
    req = request.get_json()
    print(req)
    user = User.query.filter_by(userID=req['userID']).first()
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    if not user.check_password(req['password']):
        return jsonify({'message': 'Invalid password'}), 401
    return user.to_json(), 200
