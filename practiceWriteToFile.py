# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:34:07 2019

@author: HickeMJ
"""

#myfile = open("practicefile.txt", "w")
#myfile.write("1\n2\n3")
#myfile.close()
#close file and text will be seen in the file

#OR

numbers = [5,6,7]
file = open("mynumbers.txt", "w")
for i in numbers:
    file.write(str(i) + "\n")
file.close()


