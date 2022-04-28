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


# Create a client in the client collection
def create_client(client_id, name, age, cell, date):
    
    client_doc = {"_id":client_id, "name":name, "age":age, "cell":cell, "date":date}
    response = db.clients.insert_one(client_doc)
    
    return response


# Given a client ID, return the client with that ID
def get_client(id):
    
    client = db.clients.find({"_id": id}).limit(1)
    response = json_util.dumps(client)
    response = json.loads(response)
    
    return response


# Return alls clients
def get_clients():
    
    clients = db.clients.find()
    response = json_util.dumps(clients)
    response = json.loads(response)
    
    return response


# Updates the client in the clients collection
def update_client(client_id, name, age, cell, date):

    response = db.clients.update_one(
        { "_id": client_id },
        { "$set": { "name":name, "age":age, "cell":cell, "date":date } }
    )

    return response


# Gives a client ID, deletes that client 
def delete_client(id):

    response = db.clients.delete_one({ "_id": id})
    
    return response


# Create a bill in the bill collection
def create_bill(bill_id, client_id, products, value, state, date):
    
    bill_doc = {"_id":bill_id, "client_id":client_id, "products":products, "value":value, "state":state, "date":date}
    response = db.bills.insert_one(bill_doc)
    
    return response


# Given a bill_id, return the bill with those ID
def get_bill(bill_id):
    
    bill = db.bills.find({"_id": bill_id})
    response = json_util.dumps(bill)
    response = json.loads(response)
    
    return response


# Return alls bills
def get_bills():
    
    bills = db.bills.find()
    response = json_util.dumps(bills)
    response = json.loads(response)
    
    return response


# Updates the bill in the bills collection
def update_bill(bill_id, client_id, products, value, state, date):

    response = db.bills.update_one(
        {"_id": bill_id},
        { "$set": {"client_id":client_id, "products":products, "value":value, "state":state, "date":date} }
    )

    return response


# Gives a bill ID, deletes that bill 
def delete_bill(id):

    response = db.bills.delete_one({ "_id": id})
    
    return response
