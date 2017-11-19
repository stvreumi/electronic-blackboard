import requests
import re
import json
from .qrcode import make_qrcode_image
from mysql import mysql,DB_Exception
from env_init import create_data_type
from server_api import *
from dataAccessObjects import *
from collections import OrderedDict
import os
import datetime

def getToken():
    token = "EAACEdEose0cBAGmx6WgZBNRRIpXQHmFUDSqHJwimcc0UPPqwemiYEeJ3AzWo88fwaY3M4bfwRiySeG0gXLaQ3NuPSEEIJ4bZAx8QxD9NgFZCFtY9cH55i7ViytnmMFHevvUmQB8J0ZBw2pZAqJXZBQ0SPgP62SBQ15t1GmIZBzb9iII4JCUDZC3kJWz98ZBBlI4IZD"
    return token

def grab_NCTUcowbei():
    #cowbei crawler
    token = getToken()
    fanpageID = "557872311000387"
    url = 'https://graph.facebook.com/v2.10/{fanpageID}/posts?access_token={token}&pretty=1&fields=message,likes,created_time,permalink_url&limit=100'

    NCTUcowbei = requests.get(url.format(fanpageID = fanpageID, token = token)).json()
    path = "static/cowbei"
    pattern_list = ["資工", "CS", "微處理機", "Dlab", "資料庫", "資料結構", "資結", "計圖", "計概", "作業", "考試"]
    if 'data' in NCTUcowbei:
        for information in NCTUcowbei['data']:
            if any (pattern in information['message'] for pattern in pattern_list):
                link = information['permalink_url']
                article = information['message']
                serial_number = make_qrcode_image(link,path)
                send_obj = save_db_data(serial_number, article, "cowbei")
                cowbei_insert_db(send_obj)

def save_db_data(serial_number, article, type_name):
    send_obj={}
    with DataTypeDao() as dataTypeDao:
        data_type = dataTypeDao.getTypeId(typeName=type_name)

    send_obj["data_type"] = data_type
    send_obj["serial_number"] = serial_number
    send_obj["article"] = article

    return send_obj

#create data_types for all websites crawler grabbed
def create_cowbei_data_types():
    create_data_type('cowbei')

def create_cowbei_table():
    try:
        fields = OrderedDict()
        fields['id'] = 'int NOT NULL unique key auto_increment'
        fields['serial_number'] = 'varchar(40) not NULL'
        fields['artical'] = 'varchar(500) not NULL'
        fields['upload_time'] = 'datetime default now()'
        fields['is_delete'] = 'bit(1) default 0'
        with DatabaseDao() as databaseDao:
            databaseDao.createTable(tableName='cowbei',fields=fields)
        return dict(result='success')
    except DB_Exception as e:
        return dict(error=e.args[1],result='fail')

# if __name__ == '__main__':
#     grab_NCTUcowbei()
