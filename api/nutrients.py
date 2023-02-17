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

	querystring = {"ingr":food}

	headers = {
		"X-RapidAPI-Key": "6615470177msh2eb9d9776c82332p163317jsn65585d1a22d9",
		"X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	rj = response.json()
	rj["parsed"][0]["food"]["nutrients"]
	text=""
	for nut in ['ENERC_KCAL','PROCNT', 'FAT', 'CHOCDF', 'FIBTG']:
		if nut == "ENERC_KCAL":
			text+="Calories: " + ["parsed"][0]["food"]["nutrients"][nut] + "kcal\n"
		if nut == "PROCNT":
			text+="Proteins: " + ["parsed"][0]["food"]["nutrients"][nut] + "g\n"
		if nut == "FAT":
			text+="fats: " + ["parsed"][0]["food"]["nutrients"][nut] + "g\n"
		if nut == "CHOCDF":
			text+="Carbonhydrates: " + ["parsed"][0]["food"]["nutrients"][nut] + "g\n"
		if nut == "FIBTG":
			text+="Fibers: " + ["parsed"][0]["food"]["nutrients"][nut] + "g"
		
	ans={"text":text}
	return ans
 
class itemAPI:
	class _Create(Resource):
		def post(self):
			body = request.get_json()
			return nutrient(body.get("item"))

	api.add_resource(_Create, '/')