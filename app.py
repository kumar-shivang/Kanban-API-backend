# Description: This is the main file of the application. It is used to run the application.
import os
from flask import Flask  # Import the Flask class from the flask module
from database import db  # Import the database object from the database folder
from api import API, jwt  # Import the API object from the api folder
from api.userAPI import *  # Import all the routes from the userAPI
from api.listAPI import *  # Import all the routes from the listAPI
from api.cardAPI import *  # Import all the routes from the cardAPI
from api.authAPI import *  # Import all the routes from the authAPI


app = Flask(__name__)  # Initialize the flask app
current_dir = os.path.dirname(os.path.realpath(__file__))  # Get the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(current_dir, 'database.db')  # Set the database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # This is to disable the modification tracker
app.config['SECRET_KEY'] = 'secret key'  # This is the secret key for the session
app.config['JWT_SECRET'] = 'jwt secret key'  # This is the secret key for the JWT
db.init_app(app)  # Initialize the database
jwt.init_app(app)
app.register_blueprint(API)  # Register the API blueprint  # Initialize the JWTManager

if __name__ == '__main__':
    app.run(debug=True)  # Run the application
