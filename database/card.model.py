# This file contains the Card class which represents a card in the database.
from __init__ import db  # Import the database object from the __init__.py file in the database folder.
from datetime import datetime  # Import the datetime object from the datetime module.


# The card class represents a card in the database. It has following fields: cardID, name, listID, creationTime, lastEdited, isComplete, deadline.
class Card(db.Model):
    __tablename__ = 'card'  # This name will be used to refer to the table in the database for relationships and joins.
    cardID = db.Column(db.Integer, primary_key=True)  # cardID is the primary key for the card table
    cardName = db.Column(db.String(30))  # name is a string with a maximum of 30 characters.
    listID = db.Column(db.Integer, db.ForeignKey(
        'list.listID'))  # listID is a foreign key that references the listID field in the List class
    creationTime = db.Column(db.DateTime)  # creationTime is a DateTime field
    lastEdited = db.Column(db.DateTime, nullable=True)  # lastEdited is a DateTime field that records the last time the card was edited.
    completionDate = db.Column(db.DateTime, nullable=True)  # completionDate is a DateTime field that records the date and time of completion of a task if the task is complete.
    isComplete = db.Column(
        db.Boolean)  # isComplete is a boolean field which is used to determine if the card is complete or not.
    deadline = db.Column(db.DateTime)  # deadline is a DateTime field that records the deadline of a task.
    listID = db.Column(db.Integer, db.ForeignKey('list.listID'))  # listID is a foreign key that references the listID field in the List class
    
    # The __repr__ method is used to print the object. It prints the cardID and name of the card.
    def __repr__(self):
        return '<cardID %r name %s >' % self.cardID % self.name

    # The __init__ method is the class constructor
    def __init__(self, name, listID,deadline):
        self.cardName = name
        self.listID = listID
        self.creationTime = datetime.now
        self.deadline = deadline
        self.isComplete = False

    # The markcomplete method marks a card as complete. It sets the isComplete field to True and sets the completionDate field to the current date and time.
    def markComplete(self):
        self.isComplete = True
        self.completionDate = datetime.now