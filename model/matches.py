""" database dependencies to support sqliteDB examples """
# from random import randrange
# from datetime import date
# import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class food(db.Model):
    __tablename__ = 'foods'  # table name is plural, class name is singular

    # Define the heal schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=True, nullable=False)
    _points = db.Column(db.String(255), unique=False, nullable=False)
    _image = db.Column(db.String(255), unique=True, nullable=False)


    # constructor of a heal object, initializes the instance variables within object (self)
    def __init__(self, name, points, image):
        self._name = name
        self._points = points
        self._image = image

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
    # --------------------------image
    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, image):
        self._image = image
    
    # -------------------------output
    @property
    def dictionary(self):
        dict = {
            "name" : self.name,
            "points" : self.points,
            "image" : self.image
        }
        return dict
        
    def __str__(self):
        return json.dumps(self.dictionary())
    def __repr__(self):
        return f'Food(name={self._name}, points={self._points}, image={self._image})'

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
            "points" : self.points,
            "image" : self.image
        }

    # CRUD update: updates
    # returns self
    def update(self, name="", points="", image=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(points) > 0:
            self.restaurant = points
        if len(image) > 0:
            self.protein = image
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
def initfooditem():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        u1 = food(name='Burger', points='10', image='https://png.pngtree.com/png-vector/20190130/ourlarge/pngtree-cute-minimalist-creative-cartoon-hamburger-png-image_611163.jpg')
        u2 = food(name= 'Fries', points='20', image='https://thumbs.dreamstime.com/b/french-fries-cartoon-clipart-red-paper-box-carton-121897301.jpg')

        fooditems = [u1, u2]

        """Builds sample table"""
        for h in fooditems:
            try:
                h.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {food.id}")

import json

# Define a User Class/Template
# -- A User represents the data we want to manage
class Player:    
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, time, flips):
        self._name = name    # variables with self prefix become part of the object, 
        self._time = time
        self._flips = flips

    # a name getter method, extracts name from object
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name
    
    # a getter method, extracts email from object
    @property
    def time(self):
        return self._time
    
    # a setter function, allows name to be updated after initial object creation
    @time.setter
    def time(self, time):
        self._time = time
    
    @property
    def flips(self):
        return self._flips

    @flips.setter
    def flips(self, flips):
        self._password = flips
    
    def __str__(self):
        return json.dumps(self.dictionary())
    def __repr__(self):
        return f'Food(name={self._name}, points={self._points}, image={self._image})'
    
    def __dir__(self):
        return {"name":self._name, "time":self._time, "flips":self._flips}
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
            "name" : self._name,
            "points" : self._time,
            "image" : self._flips
        }

    # CRUD update: updates
    # returns self
    def update(self, name="", time="", flips=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(time) > 0:
            self._time = time
        if len(flips) > 0:
            self._flips = flips
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

def initfooditem():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        u1 = Player(name='god', time='0.01', flips='8')

        fooditems = [u1]

        """Builds sample table"""
        for h in fooditems:
            try:
                h.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {food.id}")