# Description: This is the main file of the application. It is used to run the application.
from flask import Flask
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

if __name__ == '__main__':
    app.run()