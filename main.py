# Description: This is the main file of the application. It is used to run the application.
from flask import Flask # Import the Flask class from the flask module
from database import db # Import the database object from the database folder
from api import api # Import the api object from the api folder


app = Flask(__name__) #Initialize the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #This is the path to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #This is to disable the modification tracker
app.config['SECRET_KEY'] = 'screat key' #This is the secret key for the session
db.init_app(app) #Initialize the database
api.init_app(app) #Initialize the api

if __name__ == '__main__':
    app.run()