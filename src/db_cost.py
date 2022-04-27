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
    user  = 'KevinHerrera' #se cambia
    pwd  = 'Evergreen2022' #se cambia
    driver= 'cluster0.wqyh9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
except: 
    user  = ''
    pwd  = '' 
    driver= ''


CONNECTION_STRING = f"mongodb+srv://{user}:{pwd}@{driver}"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('db-fin')