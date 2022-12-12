# Description: This is the main file of the application. It is used to run the application.
from flask import Flask # Import the Flask class from the flask module
from database import db # Import the database object from the database folder
from api import api # Import the api object from the api folder


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)