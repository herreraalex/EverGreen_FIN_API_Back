
import json

from datetime import datetime
from src.db_pay import  create_invoice, get_invoice, get_invoices, update_invoice_products, delete_invoice


def pay_create_invoice(request):
    products_list = request.json['products_list'] 
    total_invoice = request.json['total_invoice'] 
    date = datetime.today().strftime('%Y-%m-%d')
    
    data = get_invoices()
    count = len(data)
    if count == 0:  
        invoice_id = "1"
    else:
        invoice_id = str(int(data[count-1]["_id"]) + 1)
    
    create_invoice(invoice_id, products_list, total_invoice, date)
    data = get_invoice(invoice_id)
    message = "Product Created"
    
    return 200, data, message


def pay_get_invoices():
    message = ""
    data = get_invoices()
    
    if len(data) == 0: 
        message = "No Invoices"
    elif len(data) > 0:
        message = "All Invoices"
    else:
        message = "Error"
    
    return 200, data, message


def pay_update_invoice_products(request, id):
    products_list = request.json['products_list'] 
    total_invoice = request.json['total_invoice'] 
    date = datetime.today().strftime('%Y-%m-%d')
    
    message = ""
    data = get_invoice(id)
    
    if len(data) == 0: 
        message = "Product no exist"
    elif len(data) > 0:
        message = "Product Updated"
        update_invoice_products(id, products_list, total_invoice, date)
        data = get_invoice(id)
    else:
        message = "Error"
    
    return 200, data, message


def pay_delete_invoice(id):
    message = ""
    data = get_invoice(id)
    
    if len(data) == 0: 
        message = "Product no exist"
    elif len(data) > 0:
        message = "Product Deleted"
        delete_invoice(id)
    else:
        message = "Error"
    
    return 200, data, message