# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:48:01 2020

@author: h.f.kumar.sharma
"""

def compressString(string):
    end_index = len(string)
    temp= ''
    key=[]
    value = 1
    counter = 0
    for x in string:
        counter = counter + 1
        #print("char is "+ x)
        if x == temp:
            #print("inside if "+x)
            value = value + 1 
            if(counter == end_index):
                key.append(str(value))
          
        else:
            if(value >=2):
                key.append(str(value))
                value = 1  
            temp = x
            key.append(str(temp))


    return "".join(key)


    s = 'aabbcdessefggsaaa'
    print(compressString(s))
    