# This file contains routes for the card API.
from database import db, List, Card
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import API
from datetime import datetime


@API.route('/card', methods=['GET'])
@jwt_required()
def get_card():
    req = request.get_json()
    user_id = get_jwt_identity()
    card = Card.query.filter_by(cardID=req['cardID']).first()
    if card is None:
        return jsonify({'error': 'Card not found'}), 404
    if card.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    return card.to_json(), 200


@API.route('/card', methods=['POST'])
@jwt_required()
def create_card():
    req = request.get_json()
    print(req)
    user_id = get_jwt_identity()
    epoch_seconds = req['deadline']
    deadline = datetime.fromtimestamp(epoch_seconds)
    l = List.query.get(req['listID'])
    if l is None:
        return jsonify({'error': 'List not found'}), 404
    if l.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    card = Card(req['title'], listID=req['listID'], deadline=deadline, content=req['content'])
    db.session.add(card)
    db.session.commit()
    return jsonify({'message': 'Card created successfully', 'card':card.to_json()}), 201


@API.route('/card', methods=['PUT'])
@jwt_required()
def update_card():
    req = request.get_json()
    user_id = get_jwt_identity()
    card = Card.query.get(req['cardID'])
    timestamp = req['new_deadline']
    deadline = datetime.fromtimestamp(timestamp)
    if card is None:
        return jsonify({'error': 'Card not found'}), 404
    if card.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    card.title = req['new_title']
    card.deadline = deadline
    card.content = req['new_content']
    db.session.commit()
    return jsonify({'message': 'Card updated successfully','card':card.to_json()}), 200

@API.route('/card', methods=['DELETE'])
@jwt_required()
def delete_card():
    req = request.get_json()
    user_id = get_jwt_identity()
    card = Card.query.filter_by(cardID=req['cardID']).first()
    if card is None:
        return jsonify({'error': 'Card not found'}), 404
    if card.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    db.session.delete(card)
    db.session.commit()
    return jsonify({'message': 'Card deleted successfully'}), 200

@API.route('/card/move', methods=['PATCH'])
@jwt_required()
def move_card():
    req = request.get_json()
    user_id = get_jwt_identity()
    card = Card.query.get(req['cardID'])
    l = List.query.get(req['new_listID'])
    if card is None:
        return jsonify({'error': 'Card not found'}), 404
    if card.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    if l is None:
        return jsonify({'error': 'List not found'}), 409
    if l.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    card.listID = req['new_listID']
    card.lastEdited = datetime.now()
    db.session.commit()
    return jsonify({'message': 'Card moved successfully', 'card':card.to_json()}), 200

@API.route('/card/markComplete', methods=['PATCH'])
@jwt_required()
def mark_card_complete():
    req = request.get_json()
    user_id = get_jwt_identity()
    card = Card.query.get(req['cardID'])
    if card is None:
        return jsonify({'error': 'Card not found'}), 404
    if card.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    if card.isComplete:
        return jsonify({'error': 'Card already marked as complete'}), 409
    card.isComplete = True
    card.completionDate = datetime.now()
    db.session.commit()
    return jsonify({'message': 'Card marked as complete successfully', 'card':card.to_json()}), 200

@API.route('/card/markIncomplete', methods=['PATCH'])
@jwt_required()
def mark_card_incomplete():
    req = request.get_json()
    user_id = get_jwt_identity()
    card = Card.query.filter_by(cardID=req['cardID']).first()
    if card is None:
        return jsonify({'error': 'Card not found'}), 404
    if card.userID != user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    card.isComplete = False
    card.completionDate = None
    db.session.commit()
    return jsonify({'message': 'Card marked incomplete successfully', "card":card.to_json()}), 200
    