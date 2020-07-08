# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 21:29:06 2020

@author: anuj
"""
from Number_validator import ackvalidate

# Create a function to calculate the Ackermann value based on the algoritham
def ackermann(m, n):
    if ackvalidate(m, n):
        m1 = int(m)
        n1 = int(n)
        if m1 < 0 or n1 < 0:
            return "User input cannot be less than zero"
        if m1 == 0:
            return n1 + 1
        elif n1 == 0:
            return ackermann(m1 - 1, 1)
        else:
            return ackermann(m1 - 1, ackermann(m1, n1 - 1))
