
import json

from datetime import datetime
from src.db_bill import  create_product, get_product, get_products, update_product, delete_product
from src.db_bill import create_client, get_client, get_clients, update_client, delete_client
from src.db_bill import create_bill, get_bill, get_bills, update_bill, delete_bill


def bill_create_product(request):
    name = request.json['name'] 
    description = request.json['description'] 
    price = request.json['price'] 
    category = request.json['category'] 
    date = datetime.today().strftime('%Y-%m-%d')
    
    data = get_products()
    count = len(data)
    if count == 0:  
        product_id = "1"
    else:
        product_id = str(int(data[count-1]["_id"]) + 1)
    
    create_product(product_id, name, description, price, category, date)
    data = get_product(product_id)
    message = "Product Created"
    
    return 200, data, message


def bill_get_products():
    message = ""
    data = get_products()
    
    if len(data) == 0: 
        message = "No Products"
    elif len(data) > 0:
        message = "All Products"
    else:
        message = "Error"
    
    return 200, data, message


def bill_get_product(id):
    message = ""
    data = get_product(id)

    if len(data) == 0: 
        message = "Product no exist"
    elif len(data) > 0:
        message = "Product found"
    else:
        message = "Error"
    
    return 200, data, message


def bill_update_product(request, id):
    name = request.json['name'] 
    description = request.json['description'] 
    price = request.json['price'] 
    category = request.json['category'] 
    date = datetime.today().strftime('%Y-%m-%d')
    
    message = ""
    data = get_product(id)
    
    if len(data) == 0: 
        message = "Product no exist"
    elif len(data) > 0:
        message = "Product Updated"
        update_product(id, name, description, price, category, date)
        data = get_product(id)
    else:
        message = "Error"
    
    return 200, data, message


def bill_delete_product(id):
    message = ""
    data = get_product(id)
    
    if len(data) == 0: 
        message = "Product no exist"
    elif len(data) > 0:
        message = "Product Deleted"
        delete_product(id)
    else:
        message = "Error"
    
    return 200, data, message


def bill_create_client(request):
    name = request.json['name'] 
    age = request.json['age'] 
    cell = request.json['cell'] 
    date = datetime.today().strftime('%Y-%m-%d')
    
    data = get_clients()
    count = len(data)
    if count == 0:  
        client_id = "1"
    else:
        client_id = str(int(data[count-1]["_id"]) + 1)
    
    create_client(client_id, name, age, cell, date)
    data = get_client(client_id)
    message = "Client Created"
    
    return 200, data, message


def bill_get_clients():
    message = ""
    data = get_clients()
    
    if len(data) == 0: 
        message = "No Clients"
    elif len(data) > 0:
        message = "All Clients"
    else:
        message = "Error"
    
    return 200, data, message


def bill_get_client(id):
    message = ""
    data = get_client(id)

    if len(data) == 0: 
        message = "Client no exist"
    elif len(data) > 0:
        message = "Client found"
    else:
        message = "Error"
    
    return 200, data, message


def bill_update_client(request, id):
    name = request.json['name'] 
    age = request.json['age'] 
    cell = request.json['cell'] 
    date = datetime.today().strftime('%Y-%m-%d')
    
    message = ""
    data = get_client(id)
    
    if len(data) == 0: 
        message = "Client no exist"
    elif len(data) > 0:
        message = "Client Updated"
        update_client(id, name, age, cell, date)
        data = get_client(id)
    else:
        message = "Error"
    
    return 200, data, message


def bill_delete_client(id):
    message = ""
    data = get_client(id)
    
    if len(data) == 0: 
        message = "Client no exist"
    elif len(data) > 0:
        message = "Client Deleted"
        delete_client(id)
    else:
        message = "Error"
    
    return 200, data, message


def bill_create_bill(request):
    client_id = request.json['client_id'] 
    products = request.json['products']
    value = 0
    state = request.json['state']
    date = datetime.today().strftime('%Y-%m-%d')
    
    for p in products:
        quantity = p["quantity"]
        product = get_product(p["product_id"])
        price = product[0]
        price = price["price"]
        value +=  quantity * price
    
    data = get_bills()
    count = len(data)
    if count == 0:  
        bill_id = "1"
    else:
        bill_id = str(int(data[count-1]["_id"]) + 1)
    
    create_bill(bill_id, client_id, products, value, state, date)
    data = get_bill(bill_id)
    message = "Bill Created"
    
    return 200, data, message


def bill_get_bills():
    message = ""
    data = get_bills()
    
    if len(data) == 0: 
        message = "No Bills"
    elif len(data) > 0:
        message = "All Bills"
    else:
        message = "Error"
    
    return 200, data, message


def bill_get_bill(id):
    message = ""
    data = get_bill(id)

    if len(data) == 0: 
        message = "Bill no exist"
    elif len(data) > 0:
        message = "Bill found"
    else:
        message = "Error"
    
    return 200, data, message


def bill_update_bill(request, id):
    client_id = request.json['client_id'] 
    products = request.json['products']
    value = 0
    state = request.json['state']
    date = datetime.today().strftime('%Y-%m-%d')
    
    for p in products:
        quantity = p["quantity"]
        product = get_product(p["product_id"])
        price = product[0]
        price = price["price"]
        value +=  quantity * price
    
    message = ""
    data = get_bill(id)
    
    if len(data) == 0: 
        message = "Bill no exist"
    elif len(data) > 0:
        message = "Bill Updated"
        update_bill(id, client_id, products, value, state, date)
        data = get_bill(id)
    else:
        message = "Error"
    
    return 200, data, message


def bill_delete_bill(id):
    message = ""
    data = get_bill(id)
    
    if len(data) == 0: 
        message = "Bill no exist"
    elif len(data) > 0:
        message = "Bill Deleted"
        delete_bill(id)
    else:
        message = "Error"
    
    return 200, data, message