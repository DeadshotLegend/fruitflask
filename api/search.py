from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import time
from flask import Blueprint, request, jsonify
import json
import requests

search_api = Blueprint('search_api', __name__,
                  url_prefix='/api/search')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(search_api)

def searchItem(item):
  result_list = []
  # JSON data:
  x = {"title": "", "ingredients": "", "instructions": ""}

  # Request
  url = "https://recipe-by-api-ninjas.p.rapidapi.com/v1/recipe"
  querystring = {"query": item}
  headers = {
      "X-RapidAPI-Key": "32d5282f94msh36a081cfb06e672p1c2a8cjsn851d00873829",
      "X-RapidAPI-Host": "recipe-by-api-ninjas.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  parse_req = response.json()
  for i in range(len(parse_req)):
      title = parse_req[i]["title"]
      ingredients = parse_req[i]["ingredients"]
      instructions = parse_req[i]["instructions"]
      # JSON data:
      x = {
          "title": title,
          "ingredients": ingredients,
          "instructions": instructions
      }
      result_list.append(x)
  return result_list



class itemAPI:
    class _Create(Resource):
        def post(self):
            body = request.get_json()
            return searchItem(body.get("item"))

    api.add_resource(_Create, '/')