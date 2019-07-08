# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 2019

@author: Haresh
"""
## Get all the duplicates of a list
def dupsinlist(list1, val):
    pos = 0
    listval = []
    for i in x:
        temp = x.index(val, pos)
        if i == val:
            listval.append(x.index(val, pos))
        pos = pos + 1
    return listval

x = [1,2,3,4,5,6,7,8,9,10,100,101,102,100,103,105,100,108,100]
print("x has", x.count(100), "100s at ", dupsinlist(x, 100))
