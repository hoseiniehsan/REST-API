#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
"""
Created on Wed Dec 11 14:05:47 2019

@author: Ehsan Hosseini

Application of REST API and MySQL DB
MySQL Used InnoDB Storage Engine
"""
# built-in modules


# app owned modules
from REST_API import RESTAPI
from db_connect import DbConnection
import pymysql.cursors




if __name__ == '__main__':
    
    url = 'http://localhost:3004'
    
    restAPI = RESTAPI(url)
    # make GET responseto get context of JSON
    keys={'k1':'name'}
    get_response = restAPI.do_get('/traffic_signs/', **keys)
    
    # insert the context to MySQL server DB: traffic_signs Table: Signs
    connection_string = {
            'host': 'localhost',
            'user': 'python',
            'password': 'Hoseini6390$',
            'db': 'traffic_signs',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor
            }
    dbConnection = DbConnection(setting=connection_string)
    # insert records of json-server response if not exists in table with 'IGNORE' option
    # MySQL Doc link: https://dev.mysql.com/doc/refman/8.0/en/insert.html
    insert_query = "INSERT IGNORE INTO traffic_signs.Signs (Name) VALUES (%s)"
    for item in get_response.json():
        values={'Name': item['name']}
        dbConnection.do_insert(insert_query, **values)
        
    # finally close the connection
    dbConnection.connection.close()
    
    
