# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:03:38 2019

@author: HickeMJ
"""

correct_password = "python123"
name = input("Enter your name: ")
lastname = input("enter your last name: ")
password = input("enter password: ")

while correct_password != password:
    password = input("Wrong password! Enter Again: ")
    
message = "%s %s, you are logged in" % (name,lastname)

print(message)

