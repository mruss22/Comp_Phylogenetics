# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 00:28:12 2015

@author: Marisa_29
"""
#*** Discrete Sampling Practice ***

"""---> Creating useful functions <---
(1) Write a function that multiplies all consecutively decreasing numbers between a maximum and 
a minimum supplied as arguments. (Like a factorial, but not necessarily going all the way to 1). 
This calculation would look like max * max-1 * max-2 * ... * min"""
from __future__ import division #imports the division module
import time

def factorial(max,min):
    #factorial definition: the product of an integer and all the integers below it
    product=1
    for i in range(max,min-1,-1):
        product = product * i
    return product
print factorial(5,1)

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
"""(3) Try calculating different binomial coefficients using both the functions 
from (2a) and (2b) for different values of n and k. Try some really big values 
there is a noticeable difference in speed between the (2a) and (2b) function. 
Which one is faster? By roughly how much?"""

#2a & 3
def binom1(n,k):
    '''This function calculates the binomial coefficient for two integers n and k.'''
    start = time.time()    #will return time in seconds
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient using the factorial formula for each element
        coeff = factorial(n,1) / (factorial(n-k,1)*factorial(k,1))
        end = time.time()
        elapsed = end - start        
        return coeff, elapsed
print binom1(5000,2)

#2b & 3
def binom2(n,k):
    '''This function calculates the binomial coefficient for two integers n and k in a more concise way.'''
    start = time.time() #will return time in seconds
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient by cancelling out the common terms in both parts of the division
        coeff = factorial(n,(n-k+1))/factorial(k,1)
        end = time.time()
        elapsed = end - start
        return coeff,elapsed
print binom2(5000,2)

print 'binom2 is faster than binom1'

def binom3(n,k):
    '''This function calculates the binomial coefficient for two integers n and k in a more concise way. Without calculating 
    the return time'''
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient by cancelling out the common terms in both parts of the division
        coeff = factorial(n,(n-k+1))/factorial(k,1)    
        return coeff
print binom3(5000,2)
"""Easier way would be to import the sympy module and use .binomial
import sympy
binomCoef=sympy.binomial(5, 2)
print binom"""



"""(4) Use either function (2a) or (2b) to write a function that calculates the 
probability of k successes in n Bernoulli trials with probability p. This is 
called the Binomial(n,p) distribution. See Theorem 3.3.5 for the necessary equation. 
[Hint: pow(x,y) returns x^y (x raised to the power of y).]"""

def binomPMF(k,n,p): #binomial probability mass function 
#will use bionm3 (calculates binomial concisely without return time)
    """
    This function returns the probability mass of k successes for a binomial 
    distribution with n Bernoulli trials and a probability of success given by p.
    """
    return binom3(n,k)*pow(p,k)*pow((1-p),(n-k))
print binomPMF(5,10,0.5)

"""(5) Now write a function to sample from an arbitrary discrete distribution. 
This function should take two arguments. The first is a list of arbitrarily 
labeled events and the second is a list of probabilities associated with these 
events. Obviously, these two lists should be the same length."""

def DiscreteSamp(events,probabilities):    
    import random
    x= random.choice(events) #chooses a random number from eventlist 
    index=events.index(x)
    #this indexes the random events 
    probability=probabilities[index]
    #this is the probabilities of the events given 
    
    return "this is the event", x, "and this is the probability", probability
    
eventlist=["1","2","3","4","5"]#the lists must be the same length
problist=[.15,.45,.25,.05,.1]#events sum to 1
print DiscreteSamp(eventlist,problist)


"""---> Sampling sites from an alignment <---

Imagine that you have a multiple sequence alignment with two kinds of sites. 
One type of site pattern supports the monophyly of taxon A and taxon B. 
The second type supports the monophyly of taxon A and taxon C.

(6) For an alignment of 400 sites, with 200 sites of type 1 and 200 of type 2,
 sample a new alignment (a new set of site pattern counts) with replacement 
 from the original using your function from (5). Print out the counts of the 
 two types."""
sites = [0,400]
for i in range(0,400):
    sites.append(DiscreteSamp(problist, eventlist)) #using DiscreteSamp from (5)
problist = [.5,.5] # 50% chance of either type 1 or type 2 
eventlist = ["a", "b"]  #type 1 and type 2
print(sites.count("a")) #counts amount of times type 1 appears
print(sites.count("b")) #counts amount of times type  appears
#argh can't get my code to work it keeps outputting 0 for both type 1 and type 2
#will need to rewrite code in (5)?



#using jembrown code (below) to complete 7-11 of excercise 
import scipy ## Import scipy to use when drawing a random number b/t 0 and 1)    
def discSamp(events,probs):
    ranNum = scipy.random.random()
    cumulProbs = []
    cumulProbs.extend([probs[0]])
    for i in range(1,len(probs)):
        cumulProbs.extend([probs[i]+cumulProbs[-1]])
    for i in range(0,len(probs)):
        if ranNum < cumulProbs[i]:
           return events[i]
    return None

sites = []												
 # Stores each of the 400 sites in each replicate draw.
for siteIndex in range(0,400):								
# For loop to perform 400 Bernoulli draws from the original 'alignment'.
	sites.extend([discSamp(["type1","type2"],[0.5,0.5])])     
 # Each new 'site' is added to sites
print("Type 1 count: %d" % sites.count("type1"))
print("Type 2 count: %d" % sites.count("type2"))
 

"""(7) Repeat (6) 100 times and store the results in a list."""
print("repat 100 times")
counts = []													
# Emplty list to store type 1 or type 2 counts
for reps in range(0,100):										
    sites = []
    for siteIndex in range(0,4000): #increased the range by 10X to sample "100" times
        sites.extend([discSamp(["type1","type2"],[0.5,0.5])])
print("Type 1 count: %d" % sites.count("type1"))
print("Type 2 count: %d" % sites.count("type2"))

"""(8) Of those 100 trials, summarize how often you saw particular proportions 
of type 1 vs. type 2""
e.g 
Type 1 count: 1987 (49.6%)
Type 2 count: 2013 (50.3%)
 
it was often close to 50% type1 and 50% type2 which makes sense because the more replicates you do the closer 
you should get to the actual probabilities

#(9) Calculate the probabilities of the proportions you saw in (8) using the 
binomial probability mass function (PMF) from (4)."""
def binom3(n,k):
    '''This function calculates the binomial coefficient for two integers n and k in a more concise way. Without calculating 
    the return time'''
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient by cancelling out the common terms in both parts of the division
        coeff = factorial(n,(n-k+1))/factorial(k,1)    
        return coeff

def binomPMF(k,n,p): #binomial probability mass function 
#will use bionm3 (calculates binomial concisely without return time)
    """
    This function returns the probability mass of k successes for a binomial 
    distribution with n Bernoulli trials and a probability of success given by p.
    """
    return binom3(n,k)*pow(p,k)*pow((1-p),(n-k))
type1PMF= binomPMF (496, 1000, .5)
print type1PMF

type2PMF= binomPMF (503, 1000, .5)
print type2PMF

"""results
type 1 0.0244313690947
type 2 0.0247754728848"""

"""print binomPMF(1987,4000,0.5)
OverflowError: integer division result too large for a float"""

#(10) Compare your results from (8) and (9).

#porportions are similar (as they should be) since they should be close to a 50/50 rati0

#(11) Repeat 7-10, but use 10,000 trials.
print("repat 10,000 times")
counts = []													
# Emplty list to store type 1 or type 2 counts
for reps in range(0,100):										
    sites = []
    for siteIndex in range(0,400000): #increased the range by 10X to sample "10,000" times
        sites.extend([discSamp(["type1","type2"],[0.5,0.5])])
print("Type 1 count: %d" % sites.count("type1"))
print("Type 2 count: %d" % sites.count("type2"))
"""results ....my computer hated that run....
type 1 199,605 (49.9%)
type 2 200,395 (50.1%)

The higher the number of reps the closer to the 50/50 value that it should be"""
