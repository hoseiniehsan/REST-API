#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
"""
Created on Sun Dec  8 17:31:09 2019

@author: Ehsan Hosseini
"""

'''
Installtion:
    firstly check your pip version to upgrade:
        sudo pip install --upgrade pip
    and then run as admin:
        -H to add permission to /home/YOUR_USER/.cache/pip
        sudo -H python3 -m pip install PyMySQL
'''

# Compatibility Python 2/3 or higher

__author__ = "Author: Ehsan Hosseini"

# built-in modules
import pymysql.cursors
import json


# define classes
class DbConnection(object):
    def __init__(self):
        print('DbConnection initiated \n')
        
    def connection_to_db(self, connection_str=""):
        # Connect to the database
        connection = pymysql.connect(host=connection_str['host'],
                                     user=connection_str['user'],
                                     password=connection_str['password'],
                                     db=connection_str['db'],
                                     charset=connection_str['charset'],
                                     cursorclass=connection_str['cursorclass']
                )
        return connection
    
    def do_select(self, connection_str, sql_query):
        connection = self.connection_to_db(connection_str)
        try:
            with connection.cursor() as cursor:
                # select a record
                sql = sql_query
                cursor.execute(sql, ('1',))
                result = cursor.fetchone()
        finally:
            connection.close()
        return result
        
                


if __name__ == '__main__':
    print(__file__)
    print(__doc__)
    print(__author__)
    
    # MySQL DB for 'python'@'localhost'
    dbConnect = DbConnection()
    
    connection_string = {
            'host': 'localhost',
            'user': 'python',
            'password': 'Hoseini6390$',
            'db': 'traffic_signs',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor
            }
    
    # make a SELECT query
    sql_query = "SELECT Name FROM traffic_signs.Signs WHERE SignID=%s"
    result = dbConnect.do_select(connection_string, sql_query)
    
    print('result of sql SELECT query : %s' % result)
    
    