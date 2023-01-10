# Description: This is the main file of the application. It is used to run the application.
from flask import Flask  # Import the Flask class from the flask module
from flask_cors import CORS  # Import the CORS class from the flask_cors module
import worker
from api import jwt  # Import the API object from the api folder
from api.cardAPI import *  # Import all the routes from the cardAPI
from config import DevelopmentConfig  # Import the DevelopmentConfig class from the config folder
from worker.task import say_hello

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(API)
    app.app_context().push()
    with app.app_context():
        db.create_all()
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    celery = worker.celery
    celery.Task = worker.ContextTask
    return app, celery


app, celery = create_app()

@app.route("/hello/<name>")
def hello(name):
    job = say_hello.delay(name)
    result = job.wait()
    return result, 200


if __name__ == '__main__':
    app.run(debug=True)  # Run the application
