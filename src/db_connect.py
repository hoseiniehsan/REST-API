#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:31:09 2019

@author: Ehsan Hosseini
"""

def smart_divide(func):
    print('smart_divide \n')
    def inner(a,b):
        if b != 0:
            return func(a,b)
        else:
            print('Oops, Division by Zero')
            raise ZeroDivisionError
            return False
    
    return inner;

@smart_divide
def divide(a,b):
    print('divide')
    return a/b


if __name__ == '__main__':
    '''
    division = smart_divide(divide)
    print(division(6,2))
    '''
    
    '''
    print(smart_divide(divide))
    '''
    
    
    '''
    print(divide(6,2))
    '''
    
    
    print(divide(4,0))