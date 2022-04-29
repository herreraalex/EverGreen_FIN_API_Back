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
    user  = 'ValeriaSuarez'
    pwd  = 'valeria'
    driver= 'cluster0.wqyh9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
except: 
    user  = ''
    pwd  = '' 
    driver= ''


CONNECTION_STRING = f"mongodb+srv://{user}:{pwd}@{driver}"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('db-fin')


# Create a product in the pays collection
def create_invoice(invoice_id, products_list, total_invoice, date):
    
    product_doc = {"_id":invoice_id, "products_list":products_list, "total_invoice":total_invoice, "date":date}
    response = db.pays.insert_one(product_doc)
    
    return response


# Given a invoices ID, return the invoices with that ID
def get_invoice(id):
    
    invoice = db.pays.find({"_id": id}).limit(1)
    response = json_util.dumps(invoice)
    response = json.loads(response)
    
    return response


# Return alls invoices
def get_invoices():
    
    invoices = db.pays.find()
    response = json_util.dumps(invoices)
    response = json.loads(response)
    
    return response


# Updates the invoice in the pays collection
def update_invoice_products(invoice_id, products_list, total_invoice, date):

    response = db.pays.update_one(
        { "_id": invoice_id },
        { "$set": { "products_list":products_list, "total_invoice":total_invoice, "date":date } }
    )

    return response


# Gives a product ID, deletes that product 
def delete_invoice(id):

    response = db.pays.delete_one({ "_id": id})
    
    return response

