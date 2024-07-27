# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:58:00 2024

@author: student
"""

#swaping 2 value
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

a,b = swap(5,10)
print("a is ",a," b is ",b)