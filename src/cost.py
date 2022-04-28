
from src.db_cost import update_cost, delete_cost, get_costs, get_cost, create_cost
import json

def cost_create_cost(request):
    name = request.json['name'] 
    price = request.json['price'] 
    
    data = get_costs()
    count = len(data)
    if count == 0:  
        cost_id = "1"
    else:
        cost_id = str(int(data[count-1]["_id"]) + 1)
    
    create_cost(cost_id, name, price)
    data = get_cost(cost_id)
    message = "Cost Created"
    
    return 200, data, message


def cost_get_costs():
    message = ""
    data = get_costs()
    
    if len(data) == 0: 
        message = "No Costs"
    elif len(data) > 0:
        message = "All Costs"
    else:
        message = "Error"
    
    return 200, data, message


def cost_get_cost(id):
    message = ""
    data = get_cost(id)

    if len(data) == 0: 
        message = "Cost no exist"
    elif len(data) > 0:
        message = "Cost found"
    else:
        message = "Error"
    
    return 200, data, message


def cost_update_cost(request, id):
    name = request.json['name'] 
    price = request.json['price'] 
    
    message = ""
    data = get_cost(id)
    
    if len(data) == 0: 
        message = "Cost no exist"
    elif len(data) > 0:
        message = "Cost Updated"
        update_cost(id, name, price)
        data = get_cost(id)
    else:
        message = "Error"
    
    return 200, data, message


def cost_delete_cost(id):
    message = ""
    data = get_cost(id)
    
    if len(data) == 0: 
        message = "Cost no exist"
    elif len(data) > 0:
        message = "Cost Deleted"
        delete_cost(id)
    else:
        message = "Error"
    
    return 200, data, message