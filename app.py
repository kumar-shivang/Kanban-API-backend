# Description: This is the main file of the application. It is used to run the application.
from flask import Flask # Import the Flask class from the flask module
from flask_cors import CORS  # Import the CORS class from the flask_cors module
import jobs
from cache import cache
from api import jwt  # Import the API object from the api folder
from api.cardAPI import *  # Import all the routes from the cardAPI
from api.userAPI import *
from api.authAPI import *
from api.listAPI import *
from api.exportAPI import *
from config import DevelopmentConfig  # Import the DevelopmentConfig class from the config folder
from mail import mail
from api import API  # Import the API object from the api folder


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    jwt.init_app(app)
    cache.init_app(app)
    mail.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.register_blueprint(API)
    app.app_context().push()
    with app.app_context():
        db.create_all()
    celery = jobs.celery
    celery.Task = jobs.ContextTask
    return app, celery


app, celery = create_app()


if __name__ == '__main__':
    app.run(debug=True)  # Run the application
