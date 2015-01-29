#*** Discrete Sampling Practice ***

"""---> Creating useful functions <---
(1) Write a function that multiplies all consecutively decreasing numbers between a maximum and 
a minimum supplied as arguments. (Like a factorial, but not necessarily going all the way to 1). 
This calculation would look like max * max-1 * max-2 * ... * min"""
from __future__ import division #imports the division module

def factorial(n,k):
    base=1
    for i in range(2,n + 1):
        base = base * i
    return base
print factorial(5,0)

"""Ex. if n is 5 then the range will return the values 2,3,4,5 one by one with each iteration,
and we multiply them with base in each iteration. """

"""Easier way would be to import the math module and use .factorial

import math
factorial=math.factorial(5)
print factorial
"""

"""(2) Using the function you wrote in (1), write a function that calculates the binomial coefficient 
(see Definition 1.4.12 in the probability reading). Actually, do this twice. 
The first time (2a) calculate all factorials fully. Now re-write the function and cancel as 
many terms as possible so you can avoid unnecessary multiplication 
(see the middle expression in Theorem 1.4.13)."""

#2a
def binCoeff(n,k):
    '''This function calculates the binomial coefficient for two integers n and k.'''
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient using the factorial formula for each element
        coeff = factorial(n,1) / (factorial(n-k,1)*factorial(k,1))
        return coeff
print binCoeff(5,2)

def binCoeff2(n,k):
    '''This function calculates the binomial coefficient for two integers n and k in a more concise way.'''
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient by cancelling out the common terms in both parts of the division
        coeff = factorial(n-k+1,n)/factorial(k,1)
        return coeff
print binCoeff2(5,2)
