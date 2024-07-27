# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:06:40 2024

@author: student
"""

#Fibonacci series
def fibo(n):
    a=0
    b=1
    print("Fibonacci series:")
    print(a)
    print(b)
    for i in range(3,n+1):
        c = a + b
        print(c)
        a = b
        b = c

fibo(8) #print first 8 digit of fibonacci series