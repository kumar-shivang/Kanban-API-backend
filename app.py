from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
db = SQLAlchemy(app)


# The User class is a model that represents a user in the database. It has 4 fields : userID, username, email and a password hash generated by werzukrg security
# The __repr__ method tells Python how to print objects of this class, which is going to be useful for debugging.
class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username   

    # The generate password hash method generates a password hash from a password using the werkzeug security module.
    def generate_password_hash(self, password):
        self.password_hash = generate_password_hash(password)
    
    # The check password method checks if a password is correct by checking the hash. Again, this method is provided by the werkzeug security module.
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # The password property is a way to make the password field read-only. It is used like a normal field, but it actually calls the generate_password_hash method.
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    #The __init__ method is the class constructor for the User class. It takes a username and password as parameters, and sets the username and password fields.
    def __init__(self, username, password, email=""):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.email = email



if __name__ == '__main__':
    app.run()
