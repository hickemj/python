# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:34:34 2019

@author: micha
"""

#file = open("D:\users\hickemj\anacondaprojects\learning projects\fruits.txt", "r")
#file = open("D:/users/hickemj/anacondaprojects/learning projects/fruits.txt", "r")
#content = file.read()
#file.close
#print(content)



#myfile = open("firstfile.txt", "w")
#creates a new file and overwrites old
myfile = open("firstfile.txt", "a")
#appends to the text file


#myfile.write("Mike")
myfile.write("\nConor\nGraham\nTraci")
#write to file

myfile.close()
#close file and text will be seen in the file