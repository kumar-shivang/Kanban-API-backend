# Description: This is the main file of the application. It is used to run the application.
from flask import Flask  # Import the Flask class from the flask module
# from flask_cors import CORS  # Import the CORS class from the flask_cors module
from database import db  # Import the database object from the database folder
from api import API  # Import the API object from the api folder
from api.userAPI import *  # Import all the routes from the userAPI


app = Flask(__name__)  # Initialize the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'  # This is the path to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # This is to disable the modification tracker
app.config['SECRET_KEY'] = 'secret key'  # This is the secret key for the session
with app.app_context():
    db.init_app(app)  # Initialize the database
    db.create_all()  # Create the database
app.register_blueprint(API)  # Register the API blueprint


if __name__ == '__main__':
    app.run(debug=True)  # Run the application
