import json
import logging

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from datetime import datetime
from src.bill import bill_create_product, bill_get_products, bill_get_product, bill_update_product, bill_delete_product
from src.bill import bill_create_client, bill_get_clients, bill_get_client, bill_update_client, bill_delete_client
from src.bill import bill_create_bill, bill_get_bill, bill_get_bills, bill_update_bill, bill_delete_bill
from src.cost import cost_create_cost, cost_get_costs, cost_get_cost, cost_update_cost, cost_delete_cost


app = Flask(__name__)
CORS(app)

# Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

url_base = "/eveergreen/fin"
url_products = url_base +  "/products"
url_clients = url_base + "/clients"
url_bills = url_base + "/bills"
url_cost = url_base + "/cost"
url_pay = url_base + "/cost"


# Funtion to create a product
@cross_origin
@app.route(url_products + "/create-product", methods=['POST'])
def api_create_product():
    try:
        code, data, message = bill_create_product(request)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get all products
@cross_origin
@app.route(url_products + "/get-products", methods=['GET'])
def api_get_products():
    try:
        code, data, message = bill_get_products()
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get a product by id
@cross_origin
@app.route(url_products + "/get-product/<id>", methods=['GET'])
def api_get_product(id):
    try:
        code, data, message = bill_get_product(id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to update a product by id
@cross_origin
@app.route(url_products + "/update-product/<id>", methods=['PUT'])
def api_update_product(id):
    try:
        code, data, message = bill_update_product(request, id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to delete a product by id
@cross_origin
@app.route(url_products + "/delete-product/<id>", methods=['DELETE'])
def api_delete_product(id):
    
    try:
        code, data, message = bill_delete_product(id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to create a client
@cross_origin
@app.route(url_clients + "/create-client", methods=['POST'])
def api_create_client():
    try:
        code, data, message = bill_create_client(request)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get all clients
@cross_origin
@app.route(url_clients + "/get-clients", methods=['GET'])
def api_get_clients():
    try:
        code, data, message = bill_get_clients()
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get a client by id
@cross_origin
@app.route(url_clients + "/get-client/<id>", methods=['GET'])
def api_get_client(id):
    try:
        code, data, message = bill_get_client(id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to update a client by id
@cross_origin
@app.route(url_clients + "/update-client/<id>", methods=['PUT'])
def api_update_client(id):
    try:
        code, data, message = bill_update_client(request, id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to delete a client by id
@cross_origin
@app.route(url_clients + "/delete-client/<id>", methods=['DELETE'])
def api_delete_client(id):
    
    try:
        code, data, message = bill_delete_client(id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to create a bill
@cross_origin
@app.route(url_bills + "/create-bill", methods=['POST'])
def api_create_bill():
    try:
        code, data, message = bill_create_bill(request)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get all bills
@cross_origin
@app.route(url_bills + "/get-bills", methods=['GET'])
def api_get_bills():
    try:
        code, data, message = bill_get_bills()
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get a bill by id
@cross_origin
@app.route(url_bills + "/get-bill/<id>", methods=['GET'])
def api_get_bill(id):
    try:
        code, data, message = bill_get_bill(id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to update a bill by id
@cross_origin
@app.route(url_bills + "/update-bill/<id>", methods=['PUT'])
def api_update_bill(id):
    try:
        code, data, message = bill_update_bill(request, id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to delete a bill by id
@cross_origin
@app.route(url_bills + "/delete-bill/<id>", methods=['DELETE'])
def api_delete_bill(id):
    
    try:
        code, data, message = bill_delete_bill(id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


#Costs section-----------------------------
# Funtion to create a product
@cross_origin
@app.route(url_cost + "/create-cost", methods=['POST'])
def api_create_cost():
    try:
        code, data, message = cost_create_cost(request)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get all costs
@cross_origin
@app.route(url_cost + "/get-costs", methods=['GET'])
def api_get_costs():
    try:
        code, data, message = cost_get_costs()
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get a cost by id
@cross_origin
@app.route(url_cost + "/get-cost/<id>", methods=['GET'])
def api_get_cost(id):
    try:
        code, data, message = cost_get_cost(id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to update a cost by id
@cross_origin
@app.route(url_cost + "/update-cost/<id>", methods=['PUT'])
def api_update_cost(id):
    try:
        code, data, message = cost_update_cost(request, id)
        return response(code, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to delete a cost by id
@cross_origin
@app.route(url_cost + "/delete-cost/<id>", methods=['DELETE'])
def api_delete_cost(id):
    
    try:
        code, data, message = cost_delete_cost(id)
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
    #app.run(port=8000, debug=True)
    app.run()
