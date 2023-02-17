import json
import hashlib
from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import time
from flask import Blueprint, request, jsonify
import json
import requests

nutrients_api = Blueprint('nutrients_api', __name__, url_prefix='/api/nutrients')
api = Api(nutrients_api)

def nutrient(food):
	url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

	querystring = {"ingr":"apple"}

	headers = {
		"X-RapidAPI-Key": "6615470177msh2eb9d9776c82332p163317jsn65585d1a22d9",
		"X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	rj = response.json()
	print(rj["parsed"][0]["food"]["nutrients"])
 
class itemAPI:
	class _Create(Resource):
		def post(self):
			body = request.get_json()
			return nutrient(body.get("item"))

	api.add_resource(_Create, '/')