# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:10:34 2024

@author: student
"""

def ctof(celcius):
    fahrenheit = (9/5)*celcius+32
    return fahrenheit

def ftoc(fahrenheit):
    celcius = (fahrenheit-32)*(5/9)
    return celcius

c = float(input("Enter Celcius:"))
print("Fahrenheit is ", ctof(c))

f = float(input("Enter Fahrenheit:"))
print("Celcius is ", ftoc(f))