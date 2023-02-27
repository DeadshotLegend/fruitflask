""" database dependencies to support sqliteDB examples """
# from random import randrange
# from datetime import date
# import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class topscore(db.Model):
    __tablename__ = 'topscores'  # table name is plural, class name is singular

    # Define the heal schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=True, nullable=False)
    _points = db.Column(db.String(255), unique=False, nullable=False)


    # constructor of a heal object, initializes the instance variables within object (self)
    def __init__(self, name, points):
        self._name = name
        self._points = points

       # ---------------------------name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    # ----------------------------points
    @property
    def points(self):
        return self._points
    @points.setter
    def points(self, points):
        self._points = points
    
    # -------------------------output
    @property
    def dictionary(self):
        dict = {
            "name" : self.name,
            "points" : self.points
        }
        return dict
        
    def __str__(self):
        return json.dumps(self.dictionary())
    def __repr__(self):
        return f'Food(name={self._name}, points={self._points})'

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from heal(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to heals table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary

    def read(self):
        return {
            "id": self.id,
            "name" : self.name,
            "points" : self.points
        }

    # CRUD update: updates
    # returns self
    def update(self, name="", points=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(points) > 0:
            self.restaurant = points
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """


# Builds working data for testing
def inittopscores():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        u1 = topscore(name='Name', points='0')
        u2 = topscore(name='CoolerName', points='0')

        scores = [u1, u2]

        """Builds sample table"""
        for h in scores:
            try:
                h.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {topscore.id}")
            