#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:22:26 2019

@author: Sayed Ehsan Hosseini
link:
    https://stackoverflow.com/questions/30970905/python-conditional-exception-messages
"""
class APIError(Exception):
    """An API Error Exception"""
    def __init__(self, status):
        self.status = status
        
    def __str__(self):
        return "APIError: status={}".format(self.status)
    
