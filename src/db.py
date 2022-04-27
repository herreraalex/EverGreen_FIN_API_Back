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
    user  = 'KevinHerrera'
    pwd  = 'Evergreen2022'
    driver= 'cluster0.wqyh9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
except: 
    user  = ''
    pwd  = '' 
    driver= ''


CONNECTION_STRING = f"mongodb+srv://{user}:{pwd}@{driver}"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('db-fin')


# Create a product in the products collection
def create_product(product_id, name, description, price,  category, date):
    
    product_doc = {"_id":product_id, "name":name, "description":description, "price":price, "category":category, "date":date}
    response = db.products.insert_one(product_doc)
    
    return response


# Given a product ID, return the product with that ID
def get_product(id):
    
    product = db.products.find({"_id": id}).limit(1)
    response = json_util.dumps(product)
    response = json.loads(response)
    
    return response


# Return alls products
def get_products():
    
    products = db.products.find()
    response = json_util.dumps(products)
    response = json.loads(response)
    
    return response


# Updates the product in the products collection
def update_product(product_id, name, description, price,  category, date):

    response = db.products.update_one(
        { "_id": product_id },
        { "$set": { "name":name, "description":description, "price":price, "category":category, "date":date } }
    )

    return response


# Gives a product ID, deletes that product 
def delete_product(id):

    response = db.products.delete_one({ "_id": id})
    
    return response
