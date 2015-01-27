#*** Discrete Sampling Practice ***

"""---> Creating useful functions <---
(1) Write a function that multiplies all consecutively decreasing numbers between a maximum and 
a minimum supplied as arguments. (Like a factorial, but not necessarily going all the way to 1). 
This calculation would look like max * max-1 * max-2 * ... * min"""

def factorial(n):
    base=1
    for i in range(2,n + 1):
        base = base * i
    return base
print factorial(5)

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
