# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 16:43:50 2019

@author: micha
"""

temps = [10, -20, 100]


def converter(c):
    f = c * 9/5 + 32
    return f 
for temps in temps:
    print(converter(temps))