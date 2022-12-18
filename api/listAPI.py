#This file contains routes for the list API.
from database import db, List, User
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import API


@API.route('/list', methods=['GET'])
@jwt_required(locations=['json'])
def get_list():
    req = request.get_json()
    user_id = get_jwt_identity()
    l = List.query.filter_by(listID=req['listID']).first()
    if l is None:
        return jsonify({'error': 'List not found'}), 404
    elif l.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    else:
        return l.to_json(), 200


@API.route('/list', methods=['POST'])
@jwt_required(locations=['json'])
def create_list():
    req = request.get_json()
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    lists = user.userLists
    if req['title'] not in lists: 
        l = List(req['title'], user_id)
        db.session.add(l)
        db.session.commit()
        return jsonify({'message': 'List created successfully'}), 201
    return jsonify({'error': 'List already exists'}), 400


@API.route('/list', methods=['PUT'])
@jwt_required(locations=['json'])
def update_list():
    req = request.get_json()
    user_id = get_jwt_identity()
    l = List.query.filter_by(listID=req['listID']).first()
    if l is None:
        return jsonify({'error': 'List not found'}), 404
    if l.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    l.title = req['title']
    db.session.commit()
    return jsonify({'message': 'List updated successfully'}), 200


@API.route('/list', methods=['DELETE'])
@jwt_required(locations=['json'])
def delete_list():
    req = request.get_json()
    user_id = get_jwt_identity()
    l = List.query.filter_by(listID=req['listID']).first()
    if l is None:
        return jsonify({'error': 'List not found'}), 404
    if l.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    db.session.delete(l)
    db.session.commit()
    return jsonify({'message': 'List deleted successfully'}), 200
