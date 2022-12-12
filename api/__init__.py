#This file initialize the flask api. It also contains the routes for the api.
from flask_api import FlaskAPI # import the Flask API from the flask_api module
from database import db # import the database object from the database folder
from database.card_model import Card # import the Card class from the card.model file in the database/card folder
api = FlaskAPI() #Initialize the flask api

@api.route('/cardID/<int:cardID>', methods=['GET']) #This route returns the card with the given cardID
def getCard(cardID):
    return db.session.query(Card).filter(Card.cardID == cardID).first()

    