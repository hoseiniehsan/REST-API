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
    def __init__(self, setting):
        self.connection = self.connection_to_db(setting)
        if self.connection:
            print('DbConnection initiated and conncetion to DB is established \n')
        
    def connection_to_db(self, connection_str=""):
        # Connect to the database
        try:
            connection = pymysql.connect(host=connection_str['host'],
                                         user=connection_str['user'],
                                         password=connection_str['password'],
                                         db=connection_str['db'],
                                         charset=connection_str['charset'],
                                         cursorclass=connection_str['cursorclass']
                    )
            return connection
        except NameError as e:
            print('connection to DB failed! {}'.format(e))
            return False;
    
    
    def smart_select(func):
        def inner(sql_query, **select_condition):
            print('inner')
            return func(sql_query, **select_condition)
        
        return inner;
            
            
    
    #@smart_select
    def do_select(self, sql_query, **select_conditions):
        try:
            with self.connection.cursor() as cursor:
                # select record/s
                # Empty dictionaries evaluate to False in Python
                if bool(select_conditions) is True:
                    for condition in sorted(select_conditions):
                        #cursor.execute(sql, ('1',))
                        cursor.execute(sql_query, (select_conditions[condition],))
                        result = cursor.fetchall()
                else:
                    cursor.execute(sql_query)
                    result = cursor.fetchall()
            return result

        except NameError as e:
            print('SELECT query failed! {}'.format(e))
            return False
        '''
        else:
            return result
        finally:
            self.connection.close()
        '''
    
    
    def do_insert(self, sql_query, **values):
        try:
            # create a new record
            with self.connection.cursor() as cursor:
                for value in sorted(values):
                    cursor.execute(sql_query, (values[value],))
                
            # connection is not autocommit by default. So it must be commited 
            # to save changes.
            self.connection.commit()
            return True
        except NameError as e:
            print('INSERT query failed! {}'.format(e))
            return False
        '''
        else:
            return True
        # The code in the finally block will be executed regardless of whether 
        # an exception occurs.
        finally:
            self.connection.close()
        '''
    
        
                


if __name__ == '__main__':
    print(__file__)
    print(__doc__)
    print(__author__)
    
    # MySQL DB for 'python'@'localhost'
    
    connection_string = {
            'host': 'localhost',
            'user': 'python',
            'password': 'Hoseini6390$',
            'db': 'traffic_signs',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor
            }
    
    dbConnect = DbConnection(setting=connection_string)
    
    
    # make a SELECT query
    select_query = "SELECT Name FROM traffic_signs.Signs WHERE SignID=%s"
    select_condition={'SignID':'1'}
    result = dbConnect.do_select(select_query, **select_condition)
    
    print('result of sql quey SELECT WHERE SignID=1 : %s' % result)
    
    values = {'Name':'green_light'}
    insert_query = "INSERT INTO traffic_signs.Signs (Name) VALUES (%s)"
    #dbConnect.do_insert(insert_query, **values)
    
    
    
    select_query = "SELECT * FROM traffic_signs.Signs WHERE Name=%s"
    select_condition = {'Name':'green_light'}
    result = dbConnect.do_select(select_query, **select_condition)
    print('result of sql query SELECT WHERE Name=green_light : %s' % result)
    
    select_query = "SELECT * FROM traffic_signs.Signs"
    select_condition = {}
    result = dbConnect.do_select(select_query, **select_condition)
    print('result of sql query SELECT * : %s' % result)
    
    # finally close the connection from App to DB
    dbConnect.connection.close()
    
    