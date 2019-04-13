# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:05:07 2019

@author: micha
"""

file = open("C:/users/micha/python training/fruits.txt", "r")
content = file.read()
file.close
content = content.splitlines()
#content = content

for i in content:
    print(len(i))
    #print(i)
