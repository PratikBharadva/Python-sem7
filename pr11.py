# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:31:08 2024

@author: student
"""

#prime in given interval
def prime(start,stop):
    for i in range(start,stop):
        flag = 1
        for num in range(2,i):
            if (i%num==0):
                flag = 0
                break
        if flag == 1:
            print(i)
        else:
            flag=1

prime(4,47)