# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:23:24 2019

@author: HickeMJ
"""


myfile = open("firstfile.txt", "a+")
#Read and write to the text file w a+
#This will go to the end of the file for appending

#myfile.write("Mike")
myfile.write("\nDave\nBen\nBailey")
#write to file

myfile.close()
#close file and text will be seen in the file

myfile = open("firstfile.txt", "a+")

myfile.read()   

myfile.seek(0)
#to find the start of the file
