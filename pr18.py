# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:09:51 2024

@author: student
"""

#Factors of numbers
n = int(input("Enter a number:"))

print("Factors:")
for i in range(1,n+1):
    if n%i == 0:
        print(i)