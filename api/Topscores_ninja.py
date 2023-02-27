from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.leaderboard_ninja import topscore

topscores_api = Blueprint('topscores_api', __name__,
                   url_prefix='/api/topscores')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(topscores_api)

class topscoresAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210

            points = body.get('points')
            if points is None:
                return {'message': f'points are missing'}, 210

            ''' #1: Key code block, setup USER OBJECT '''
            uo = {}
            uo = topscore(name=name, 
                      points=points)

            
            ''' #2: Key Code block to add user to database '''
            # create in database
            scorenew = uo.create()
            # success returns json
            if scorenew:
                return jsonify(scorenew.read())
            # failure returns error
            return {'message': f'Processed {name}, is a format error'}, 210

    class _Read(Resource):
        def get(self):
            topscores = topscore.query.all()    # read/extract all users from database
            json_ready = {'topscores_ninja' : [topscore.read() for topscore in topscores] }
    
            # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')