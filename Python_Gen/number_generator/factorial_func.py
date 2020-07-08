"""
Created on Sat Jul  4 12:47:51 2020

@author: anuj
"""

import math
from Number_validator import validate


# function to calculate factorial using the Math module of Python

def factorial_optimised(num):
    if validate(num):
        fact = int(num)
        if fact<1:
            return "Please enter a value greater than zero"
        else:
            return math.factorial(fact)
    else:
        return "User Input is invalid"

# function to calculate the factorial of a no using for loop
# def factorial(num):
#     factorial = 1
#     for i in range(1,num + 1):
#            factorial = factorial*i
#     return factorial
