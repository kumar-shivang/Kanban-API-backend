from . import API
from flask import request, jsonify
from database import db, User
from flask_jwt_extended import get_jwt_identity, jwt_required

@API.route('/user', methods=['GET'])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user=user.to_json()),200

@API.route('/user', methods=['POST'])
def create_user():
    req = request.get_json()
    print(req)
    if User.query.filter_by(username=req['username']).first() is None:
        user = User(username=req['username'], password=req['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    return jsonify({'error': 'User already exists'}), 401

@API.route('/user', methods=['PUT'])
@jwt_required()
def update_user():
    req = request.get_json()
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    user.username = req['newUsername']
    user.email = req['newEmail']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200

@API.route('/user', methods=['DELETE'])
@jwt_required()
def delete_user():
    user_id = get_jwt_identity()
    req = User.query.get(user_id)
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    if not user.check_password(req['password']):
        return jsonify({'error': 'Invalid password'}), 401
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200
