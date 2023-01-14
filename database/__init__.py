# This file is the initializing file for the database folder. It is used to initialize the database object. It is imported in the card.model.py and list.model.py files. It is also imported in the app.py file.
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime  # Import the datetime object from the datetime module.
from time import mktime as epoch  # Import the epoch function from the time module.


db = SQLAlchemy()


# The User class is a model that represents a user in the database. It has 4 fields : userID, username, email and a password hash generated by werzukrg security
class User(db.Model):
    __tablename__ = 'user'  # This name will be used to refer to the table in the database for relationships.
    userID = db.Column(db.Integer, primary_key=True)  # userID is the primary key for user table.
    username = db.Column(db.String(30), unique=True)  # username is unique
    password_hash = db.Column(db.String(
        128))  # password hash is 128 characters long because it is generated by the werkzeug security module that returns a 128 character hash
    email = db.Column(db.String(50),
                      unique=True,
                      nullable=True)  # The email is unique. It has 50 characters because it is an optimum number of characters for an email address.
    userLists = db.relationship('List',
                                backref='user')  # userLists is a relationship field that references the List class. It is used to get all the lists for a user.
    userCards = db.relationship('Card',
                                backref='user')  # userCards is a relationship field that references the Card class. It is used to get all the cards for a user.

    # The __repr__ method is used to print the object. It prints the username of the user
    def __repr__(self):
        return '<User %r>' % self.username

        # The generate_password_hash method generates a password hash from a password using the werkzeug security module.

    def generate_password_hash(self, password):
        """Generate password hash from password

        Args:
            password (string): The password to be hashed
        """
        self.password_hash = generate_password_hash(password)

    # The check password method checks if a password is correct by checking the hash. Again, this method is provided by the werkzeug security module.
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # The password property is a way to make the password field read-only. It is used like a normal field, but it actually calls the generate_password_hash method.
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    # The __init__ method is the class constructor for the User class. It takes a username and password as parameters, and sets the username and password fields.
    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.email = username + "@kanban.com"

    # This function changes the user object to json format
    def to_json(self):
        """Converts the user object to json format

        Returns:
            json: The user object in json format
        """
        json = {
            'userID': self.userID,
            'username': self.username,
            'email': self.email
        }
        lists = self.userLists
        if lists:
            json['lists'] = [l.to_json() for l in lists]
        else:
            json['lists'] = []
        return json


# The List class represents a list in the database. It has 3 fields: listID, title and userID. The userID field is a foreign key that references the userID field in the User class.
class List(db.Model):
    __tablename__ = 'list'  # This name will be used to refer to the table in the database for relationships and joins.
    listID = db.Column(db.Integer, primary_key=True)  # listID is the primary key for the list table
    title = db.Column(db.String(30))  # name is a string with a maximum of 30 characters.
    userID = db.Column(db.Integer, db.ForeignKey(
        'user.userID'))  # userID is a foreign key that references the userID field in the User class
    listCards = db.relationship('Card',
                                backref='card')  # l listCards is a relationship field that references the Card class. It is used to get all the cards for a list.

    # The __repr__ method is used to print the object. It prints the listID and name of the list.
    def __repr__(self):
        return '<listID %r name %s >' % self.listID % self.listname

    # The __init__ method is the class constructor for the List class. It takes a name and userID as parameters, and sets the name and userID fields.
    def __init__(self, name, userID):
        u = User.query.filter_by(userID=userID).first()
        if u:
            self.title = name
            self.userID = userID

    # to_json() function returns the list object in json format
    def to_json(self):
        """Converts the list object to json format
        Returns:
            json: The list object in json format
        """
        json = {
            'listID': self.listID,
            'title': self.title,
            'userID': self.userID,
        }
        cards = self.listCards
        if cards:
            json['cards'] = [c.to_json() for c in cards]
        else:
            json['cards'] = []
        return json


# The card class represents a card in the database.
class Card(db.Model):
    __tablename__ = 'card'  # This name will be used to refer to the table in the database for relationships and joins.
    cardID = db.Column(db.Integer, primary_key=True)  # cardID is the primary key for the card table
    cardName = db.Column(db.String(30))  # name is a string with a maximum of 30 characters.
    content = db.Column(db.String(1000))  # content is a string with a maximum of 1000 characters.
    creationTime = db.Column(db.DateTime)  # creationTime is a DateTime field
    lastEdited = db.Column(db.DateTime,
                           nullable=True)  # lastEdited is a DateTime field that records the last time the card was edited.
    completionDate = db.Column(db.DateTime,
                               nullable=True)  # completionDate is a DateTime field that records the date and time of completion of a task if the task is complete.
    isComplete = db.Column(
        db.Boolean, default=False)  # isComplete is a boolean field which is used to determine if the card is complete or not.
    deadline = db.Column(db.DateTime)  # deadline is a DateTime field that records the deadline of a task.
    listID = db.Column(db.Integer, db.ForeignKey(
        'list.listID'))  # listID is a foreign key that references the listID field in the List class
    userID = db.Column(db.Integer, db.ForeignKey(
        'user.userID'))  # userID is a foreign key that references the userID field in the User class

    # The __repr__ method is used to print the object. It prints the cardID and name of the card.
    def __repr__(self):
        return '<cardID %r>' % self.cardID

    # The __init__ method is the class constructor
    def __init__(self, name, listID, deadline, content=""):
        l = List.query.filter_by(listID=listID).first()
        if l:
            self.cardName = name
            self.listID = listID
            self.creationTime = datetime.now()
            self.deadline = deadline
            self.content = content
            self.isComplete = False
            self.userID = l.userID

    # The mark complete method marks a card as complete. It sets the isComplete field to True and sets the completionDate field to the current date and time.
    def markComplete(self):
        self.isComplete = True
        self.completionDate = datetime.now

    # to_json() function returns the card object in json format
    def to_json(self):
        """Converts the card object to json format
        Returns:
            json: The card object in json format
        """
        last_edit = None
        completion_date = None
        if self.lastEdited:
                last_edit: int(epoch(self.lastEdited.timetuple()))
        if self.isComplete:
            completion_date = int(epoch(self.completionDate.timetuple())*1000)
        return {
            'cardID': self.cardID,
            'cardName': self.cardName,
            'content': self.content,
            'creationTime': int(epoch(self.creationTime.timetuple())*1000),
            'lastEdited': last_edit,
            'completionDate': completion_date,
            'isComplete': self.isComplete,
            'deadline': int(epoch(self.deadline.timetuple())*1000),
            'listID': self.listID,
            'userID': self.userID
        }
