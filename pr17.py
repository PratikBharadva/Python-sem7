# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:05:47 2024

@author: student
"""

#Decimal to Binary conversion
n = int(input("Enter a number:"))
binary=""
while(n>0):
    rem = n%2
    binary = str(rem)+binary
    n=n//2
    
print(binary)