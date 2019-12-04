#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 11:05:53 2019

@author: Sayed Ehsan Hosseini

REST API (Representational state transfer) is an API that uses HTTP requests 
for communication with web services.
"""

import requests
import pdb
#import AptUrl
#import dropbox
#from dropbox.exceptions import ApiError
import json
#import APIError.APIError
# from filename.py import class

# self defined classes
from APIError import APIError


pdb.set_trace()
res = requests.api.get('https://google.com')
print('response of GET requests from google.com is: {}'.format(res))
pdb.set_trace()




class RESTAPI(object):
    def __init__(self):
        print('class RESTAPI is initiated \n')
        self.header = {
                'x-rapidapi-host': "alexnormand-dino-ipsum.p.rapidapi.com",
                'x-rapidapi-key': "SIGN-UP-FOR-KEY"
                }
    
        
    def get_response(self, url):
        response = requests.api.get(url=str(url))
        self.response = response
        self.url = url
        return response

    def eval_response(self, response):
        if response:
            print('Response OK')
            print('# Response header: {}'.format(response.headers))
        else:
            print('Response Faild, status code : {}'.format(response.status_code))
        #return True
        
    def eval_resp(self, response):
        if response.status_code == 200 or 201:
            # This means something went wrong.
            return True
        else:
            raise APIError('GET /comments/ {}'.format(response.status_code))
    
    def connect_db(self):
        return Bucket(CONNSTR, password=PASSWORD)
    
    def get_items(self, place="", json_item=None):
        # The response object has a method called json. This takes the response 
        #body from the server—a sequence of bytes—and transforms it into a 
        #Python list of dictionaries
        try:
            print("place= \n", url+str(place))
            response = requests.api.get(self.url + place)
            for item in response.json():
                print('\n {} \t {}'.format(item['id'], item['shape']))
            return True
        
        except APIError as error:
            return error;
        
    
    def add_item(self, place="", shape="", postId=None, json_item=None):
        try:
            payload = {
                "shape": shape,
                "postId": postId
                }
            #json_string = self.parse_json_file(self.url+ str(place))
            #print('json_string: \n', json_string)
            #auth = ('token', 'example')
            return requests.api.post(self.url+ place, \
                                 json={
                                         'shape': shape,
                                         'postId': postId,
                                         })#, \
                                 #auth=auth)#, header=self.header)
        except APIError as error:
            return error;
        
    def do_post(self, place="", payload=""):
        try:
            return requests.api.post(self.url+ place, \
                                     json=payload
                    )
        except APIError as error:
            return error;
        
    def do_get(self, place="", **keys):
        try:
            response = requests.api.get(self.url+place)
            for item in response.json():
                print('id: {}'.format(item['id']))
                # extract json keys
                for key in sorted(keys):
                    print('\t {}'.format(item[keys[key]]))
                print('\n')
            return True
        except APIError as error:
            return error;
        
    @staticmethod
    def parse_json_file(json_file):
        with open(str(json_file)) as file_json:
            json_string = json.load(file_json)
        return json_string
    


if __name__ == '__main__':
    url = 'http://localhost:3004'
    restAPI = RESTAPI()
    res = restAPI.get_response(url=url)
    print('Http status code using response of GET requests from {} is: {}'\
          .format(url,res))
    print('response link : %s' % res.links)
    restAPI.eval_response(response=res)
    
    #db = restAPI.connect_db()
    restAPI.eval_resp(response=res)
    restAPI.get_items(place='/comments/')
    
    #add_item_resp = restAPI.add_item(place='/comments/', shape="cube", postId="2")
    payload_add_to_traffic_signs={
            'name': "green_light",
            }
    add_item_resp = restAPI.do_post(place='/traffic_signs/', payload=payload_add_to_traffic_signs)
    
    restAPI.eval_resp(add_item_resp)
    restAPI.eval_response(add_item_resp)
    restAPI.get_items(place='/comments/')
    keys = {'k1':'name'}
    restAPI.do_get(place='/traffic_signs/', **keys)
    
