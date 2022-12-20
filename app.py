# Description: This is the main file of the application. It is used to run the application.
from flask import Flask  # Import the Flask class from the flask module
from api import jwt  # Import the API object from the api folder
from datetime import timedelta
from api.userAPI import *  # Import all the routes from the userAPI
from api.listAPI import *  # Import all the routes from the listAPI
from api.cardAPI import *  # Import all the routes from the cardAPI
from api.authAPI import *  # Import all the routes from the authAPI
from flask_jwt_extended import get_jwt
from config import DevelopmentConfig  # Import the DevelopmentConfig class from the config folder


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(API)
    app.app_context().push()
    with app.app_context():
        db.create_all()
    return app


app = create_app()


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()['exp']
        now = datetime.utcnow()
        target_timestamp = datetime.timestamp(now + timedelta(seconds=app.config['JWT_REFRESH_EXPIRATION_DELTA']))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response


if __name__ == '__main__':
    app.run(debug=True)  # Run the application
