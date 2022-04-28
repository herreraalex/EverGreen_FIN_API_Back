# This module contains all the database interface methods for the Evergreen system, macro process of finance 

import os
import json

from flask import Flask
from flask import jsonify
from distutils.log import error
from urllib import response
from bson import json_util
from flask_pymongo import pymongo


# Connection configuration
try:
    #user  = os.environ['user']
    #pwd  = os.environ['pwd']
    #driver = os.environ['driver']
    user  = 'JoabRomero' #se cambia
    pwd  = 'joab' #se cambia
    driver= 'cluster0.wqyh9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
except: 
    user  = ''
    pwd  = '' 
    driver= ''


CONNECTION_STRING = f"mongodb+srv://{user}:{pwd}@{driver}"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('db-fin')


# Create a cost item in the costs collection
def create_cost(cost_id, name, price):
    
    cost_doc = {"_id":cost_id, "name":name, "price":price}
    response = db.costs.insert_one(cost_doc)
    
    return response


# Given a cost ID, return the cost with that ID
def get_cost(id):
    
    cost = db.costs.find({"_id": id}).limit(1)
    response = json_util.dumps(cost)
    response = json.loads(response)
    
    return response


# Return all costs
def get_costs():
    
    cost = db.costs.find()
    response = json_util.dumps(cost)
    response = json.loads(response)
    
    return response


# Updates the cost in the costs collection
def update_cost(cost_id, name, price):

    response = db.costs.update_one(
        { "_id": cost_id },
        { "$set": { "name":name, "price":price} }
    )

    return response


# Gives a cost ID, deletes that cost 
def delete_cost(id):

    response = db.costs.delete_one({ "_id": id})
    
    return response
