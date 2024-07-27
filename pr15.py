# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:16:39 2024

@author: student
"""

#armstrong number in an interval
import math

def armstrong(start,end):
    for n in range(start,end):        
        l = int(len(str(n)))
        arm = 0
        temp = n
        for i in range(1,l+1):
            rem = temp%10
            arm += math.pow(rem,l)
            temp = int(temp/10)
        if arm==n:
            print(n)

armstrong(1,1000)
