# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:44:11 2024

@author: student
"""

#find Factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
        
print(fact(5))