# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:11:51 2024

@author: student
"""

#largest among three number
ip1 = int(input("Enter a first number:"))
ip2 = int(input("Enter a second number:"))
ip3 = int(input("Enter a third number:"))

print("first is greater" if ip1 > ip2 and ip1 > ip3 else "second is greater" if ip1 > ip2 and ip1 > ip3 else "third is greater")

'''if (ip1>ip2 and ip1>ip3):
    print(ip1," is greater")
elif(ip2>ip1 and ip2>ip3):
    print(ip2," is greater")
else:
    print(ip3," is greater")
    '''