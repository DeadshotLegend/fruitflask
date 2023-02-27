from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.matches import Player

def comp(a):
	return a._time

# blueprint, which is registered to app in main.py
match_api = Blueprint('match_api', __name__,
                   url_prefix='/api/match')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(match_api)
class UserAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None:
                return {'message': f'Name is missing'}, 210
            # validate uid
            time = body.get('time')
            # look for password and dob
            flips = body.get('flips')

            ''' #1: Key code block, setup USER OBJECT '''
            uo = Player(name=name, time=time, flips=flips)
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'error'}, 210

    class _Read(Resource):
        def get(self):
            users = Player.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            json_ready.sort()
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')