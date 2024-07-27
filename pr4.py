# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:37:07 2024

@author: student
"""

import math
#Quadratic Equation
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

temp = (b*b)-(4*a*c)

if temp < 0 :
    print("No root possible")
else:
    eq = (-b + math.sqrt(temp))/2*a
    print("roots :",eq)
    eq = (-b - math.sqrt(temp))/2*a
    print("roots :",eq)
    