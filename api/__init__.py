#This file initialize the flask api. It also contains the routes for the api.
from flask import Blueprint, jsonify # import the Blueprint class and jsonify method from the flask module
from database import db, User, List, Card # import the database object from the database folder
# from database.card_model import Card # import the Card class from the card.model file in the database/card folder
from datetime import date, timedelta # import the date and timedelta classes from the datetime module
API = Blueprint('API', __name__) # Initialize the API blueprint

@API.route('/cardID/<int:cardID>', methods=['GET']) #This route returns the card with the given cardID
def getCard(cardID):
    c = db.session.query(Card).filter(Card.cardID == cardID).first()
    return jsonify({"cardID": c.cardID, "title": c.title, "content": c.content, "deadline": c.deadline.strftime("%d-%m-%Y")}),200

@API.route('/create/card/<int:listID>/<title>/<int:deadline>', methods=['POST']) #This route creates a card with the given title and deadline in the list with the given listID
def createCard(listID, title, deadline):
    c = Card(title, " ", date.today() + timedelta(days=deadline), listID)
    db.session.add(c)
    db.session.commit()
    return jsonify({c.cardID : "Successfully created"}), 200
