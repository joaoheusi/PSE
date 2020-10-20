import json
from pathlib import Path
import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
JSON_FILE_NAME = os.path.join(BASE_DIR,'data','history.json')

def write_json(context):
    print(BASE_DIR)
    print(JSON_FILE_NAME)
    print(context)
    file = JSON_FILE_NAME

    with open(file, 'r') as f:
        items = json.load(f)
        
        try:
            chaves = list(map(int, items.keys()))
            highest_key = int(max(chaves)) + 1
        except:
            highest_key = '1'       
        new_index = str(highest_key)
        print(type(new_index))
        print(items)

        if type(context) != None:
            with open(file,'w') as f:
                item = context
                items.update({new_index:item})
                json.dump(items,f,indent=4)

def read_json():
    file = JSON_FILE_NAME
    with open(file, 'r') as f:
        items = json.load(f)

    return items


def get_latest_status():
    file = JSON_FILE_NAME
    with open(file, 'r') as f:
        items = json.load(f)
        
        try:
            chaves = list(map(int, items.keys()))
            highest_key = int(max(chaves))
        except:
            highest_key = '1'

        last_reg = (items.get(str(highest_key)))
        try:
            last_status = last_reg.get("status")
        except:
            last_status = '1'
            write_info = {
                    "status": "Desligado",
                }
            write_json(write_info)
        
        
        if last_status == "Ligado":
            estado = {
                "button_name" : "Desligar",
                "button_class" : "btn-danger",
                "write_info" : {
                    "status": "Desligado",
                    "hora": str(datetime.now()),
                    "origem": "web" 
                }
            }
        elif last_status == "Desligado":
            print(3333333333333333333333333333333333333333333)
            estado = {
                "button_name"  : "Ligar",
                "button_class" : "btn-success",
                "write_info"   : {
                    "status": "Ligado",
                    "hora": str(datetime.now()),
                    "origem": "web" 
                }
            }
        else:
            estado = {
                "button_name"  : "Ligar",
                "button_class" : "btn-success"
            }

        return estado

        print(last_status)
