
import json

from datetime import datetime
from db import  create_product, get_product, get_products, update_product, delete_product


def sales_create_product(request):
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


def sales_get_products():
    message = ""
    data = get_products()
        
    if len(data) == 0: 
        message = "No Products"
    elif len(data) > 0:
        message = "All Products"
    else:
        message = "Error"
    
    return 200, data, message


def sales_get_product(id):
    message = ""
    data = get_product(id)
    
    if len(data) == 0: 
        message = "Product no exist"
    elif len(data) > 0:
        message = "Product found"
    else:
        message = "Error"
    
    return 200, data, message


def sales_update_product(request, id):
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


def sales_delete_product(id):
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