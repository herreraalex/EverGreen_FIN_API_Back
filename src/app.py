import json
import logging

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from datetime import datetime
from sales import sales_create_product, sales_get_products, sales_get_product, sales_update_product, sales_delete_product


app = Flask(__name__)
CORS(app)

# Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

url_base = "/eveergreen/fin"
url_products = url_base +  "/products"
url_cost = url_base + "/cost"
url_pay = url_base + "/cost"


# Funtion to create a product
@cross_origin
@app.route(url_products + "/create-product", methods=['POST'])
def api_create_product():
    try:
        code, data, message = sales_create_product(request)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get all products
@cross_origin
@app.route(url_products + "/get-products", methods=['GET'])
def api_get_products():
    try:
        code, data, message = sales_get_products()
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get a product by id
@cross_origin
@app.route(url_products + "/get-product/<id>", methods=['GET'])
def api_get_product(id):
    try:
        code, data, message = sales_get_product(id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to update a product by id
@cross_origin
@app.route(url_products + "/update-product/<id>", methods=['PUT'])
def api_update_product(id):
    try:
        code, data, message = sales_update_product(request, id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to delete a product by id
@cross_origin
@app.route(url_products + "/delete-product/<id>", methods=['DELETE'])
def api_delete_product(id):
    
    try:
        code, data, message = sales_delete_product(response, id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Function to response Api standard
def response(status_code, body, message):
    return {
            "message" : message,
            "statusCode": status_code,
            "body": body,
            "headers": {
                "content-type":"application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "isBase64Encoded": False
        }


# Function to describe an error
def log_error(e):
    logger.info(str(e))
    logger.error('Error type: ' + type(e).__name__ +', file: '+__file__ +', line: '+ str(e.__traceback__.tb_lineno))
    dict_error = {'message': str(e).replace('\'','')}
    
    return json.dumps(dict_error)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
