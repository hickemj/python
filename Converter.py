# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 16:43:50 2019

@author: micha
"""

def string_length(mystring):
    return len(mystring)

print(string_length("hello"))





def converter(c):
    f = c * 9/5 + 32
    return f 

    
def string_length(mystring):

    if type(mystring) == int:
        return"sorry, integers don't have length"
    elif type(mystring) == float:
        return"sorry, floats don't have length"
    else:
        return len(mystring)

    