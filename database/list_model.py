# This file contains the List class. It is used to represent a list in the database.
from __init__ import db # Import the database object from the __init__.py file in the database folder.


# The List class represents a list in the database. It has 3 fields: listID, title and userID. The userID field is a foreign key that references the userID field in the User class.
class List(db.Model):
    __tablename__ = 'list'  # This name will be used to refer to the table in the database for relationships and joins.
    listID = db.Column(db.Integer, primary_key=True)  # listID is the primary key for the list table
    title = db.Column(db.String(30))  # name is a string with a maximum of 30 characters.
    userID = db.Column(db.Integer, db.ForeignKey(
        'user.userID'))  # userID is a foreign key that references the userID field in the User classs 
    listCards = db.relationship('Card', backref='card') #l listCards is a relationship field that references the Card class. It is used to get all the cards for a list.
    # The __repr__ method is used to print the object. It prints the listID and name of the list.
    def __repr__(self):
        return '<listID %r name %s >' % self.listID % self.listname

    # The __init__ method is the class constructor for the List class. It takes a name and userID as parameters, and sets the name and userID fields.
    def __init__(self, name, userID):
        self.name = name
        self.userID = userID