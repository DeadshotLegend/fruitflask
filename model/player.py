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
    
    # output content using str(object) in human readable form, uses getter
    def __str__(self):
        return f'name: "{self.name}", id: "{self.uid}", psw: "{self.password}"'

    # output command to recreate the object, uses attribute directly
    def __repr__(self):
        return f'Person(name={self._name}, uid={self._uid}, password={self._password})'
    
    def __dir__(self):
        return ["name", "uid"]