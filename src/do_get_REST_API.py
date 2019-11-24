#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 11:05:53 2019

@author: ehsan
"""

import requests
import pdb


res = requests.api.get('https://scotch.io')
print('response of GET requests from scotch.io is: {}'.format(res))
pdb.set_trace()



class RESTAPI(object):
    def __init__(self):
        print('class RESTAPI is initiated \n')
        
    def get_response(self, url):
        response = requests.api.get(url=str(url))
        return response

    def eval_response(self, response):
        if response:
            print('Response OK')
            print('# Response header: .{}'.format(response.headers))
        else:
            print('Response Faild, status code : {}'.format(response.status_code))


if __name__ == '__main__':
    url = 'http://127.0.0.1/index.html'
    restAPI = RESTAPI()
    res = restAPI.get_response(url=url)
    print('Http status code using response of GET requests from {} is: {}'\
          .format(url,res))
    print('response link : %s' % res.links)
    restAPI.eval_response(response=res)
