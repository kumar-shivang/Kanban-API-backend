#This file contains routes for the list API.
from database import db, List, User
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import API


@API.route('/list', methods=['GET'])
@jwt_required()
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
@jwt_required()
def create_list():
    req = request.get_json()
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    lists = user.userLists
    list_names = [l.title for l in lists]
    if req['title'] not in list_names:
        l = List(req['title'], user_id)
        db.session.add(l)
        db.session.commit()
        return jsonify({'message': 'List created successfully', 'list':l.to_json()}), 201
    return jsonify({'error': 'List already exists'}), 400


@API.route('/list', methods=['PUT'])
@jwt_required()
def update_list():
    req = request.get_json()
    print(req)
    user_id = get_jwt_identity()
    print(user_id)
    l = List.query.get(req['listID'])
    if l is None:
        return jsonify({'error': 'List not found'}), 404
    if l.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    lists = List.query.filter_by(userID=user_id).all()
    list_names = [list.title for list in lists]
    print(list_names)
    if req['new_title'] not in list_names:
        l.title = req['new_title']
        db.session.commit()
        print("ok")
        return jsonify({'message': 'List updated successfully'}), 200
    else:
        print("not ok")
        return jsonify({'error': 'List with same title already exists'}), 400


@API.route('/list', methods=['DELETE'])
@jwt_required()
def delete_list():
    print(request.headers)
    req = request.get_json()
    print(req)
    user_id = get_jwt_identity()
    l = List.query.filter_by(listID=req['listID']).first()
    if l is None:
        return jsonify({'error': 'List not found'}), 404
    if l.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    for card in l.listCards:
        db.session.delete(card)
    db.session.delete(l)
    db.session.commit()
    return jsonify({'message': 'List deleted successfully'}), 200

@API.route('/list/movecards', methods=['PATCH'])
@jwt_required()
def move_cards():
    req = request.get_json()
    user_id = get_jwt_identity()
    l = List.query.get(req['listID'])
    l2 = List.query.get(req['newListID'])
    if l is None:
        return jsonify({'error': 'List not found'}), 404
    if l2 is None:
        return jsonify({'error': 'Target list not found'}), 404
    if l.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    for card in l.listCards:
        card.listID = req['newListID']
    db.session.commit()
    return jsonify({'message': 'Cards moved successfully'}), 200
