#This file initialize the flask api. It also contains the routes for the api.
from flask import Blueprint, jsonify, make_response # import the Blueprint class and jsonify method from the flask module
from database import db, User, List, Card # import the database object from the database folder
# from database.card_model import Card # import the Card class from the card.model file in the database/card folder
from datetime import date, timedelta # import the date and timedelta classes from the datetime module

API = Blueprint('API', __name__) # Initialize the API blueprint


'''
This part of the code is used to create the routes for CRUD operations of the User model.
'''

# This route is used to return all the users in the database
@API.route('/user', methods=['GET'])
# @token_required
def get_all_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['id'] = user.userID
        user_data['username'] = user.username
        user_data['email'] = user.email
        output.append(user_data)
    return jsonify({'users': output})



# This route is used to return a user with a specific id
@API.route('/user/<user_id>', methods=['GET'])
# @token_required
def get_user(user_id):
    user = User.query.filter_by(userID=user_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})

    return jsonify(user.to_json())


# This route is used to create a new user with a specific username and password
@API.route('/user/<username>/<password>', methods=['POST'])
def create_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'Username already exists!'})
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!', 'userID': new_user.userID, })

# This route is used to add an email to a user with a specific id
@API.route('/user/email/<int:user_id>/<email>', methods=['PUT'])
# @token_required
def add_email(user_id, email):
    user = User.query.filter_by(userID=user_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})
    user.email = email
    db.session.commit()
    return jsonify({'message': 'Email added to user!'})


# This route is used to delete a user with a specific id
@API.route('/user/<int:user_id>', methods=['DELETE'])
# @token_required
def delete_user(user_id):
    user = User.query.filter_by(userID=user_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'The user has been deleted!'})


'''
This part of the code is used to create the routes for CRUD operations of the List model.
'''

# This route is used to create a new list with a specific name and user id
@API.route('/list/<name>/<int:user_id>', methods=['POST'])
# @token_required
def create_list(name, user_id):
    user = User.query.filter_by(userID=user_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})
    new_list = List(name=name, user=user)
    db.session.add(new_list)
    db.session.commit()
    return jsonify({'message': 'New list created!', 'listID': new_list.listID })


# This route is used to return all the lists in the database that belongs to a specific user
@API.route('/list/<int:user_id>', methods=['GET'])
# @token_required
def get_all_lists(user_id):
    user = User.query.filter_by(userID=user_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})
    lists = List.query.filter_by(user=user).all()
    output = []
    for list in lists:
        output.append(list.to_json())
    return jsonify({'lists': output})

