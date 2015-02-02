#*** Discrete Sampling Practice ***

"""---> Creating useful functions <---
(1) Write a function that multiplies all consecutively decreasing numbers between a maximum and 
a minimum supplied as arguments. (Like a factorial, but not necessarily going all the way to 1). 
This calculation would look like max * max-1 * max-2 * ... * min"""
from __future__ import division #imports the division module
import time

def factorial(max,min):
    product=1
    for i in range(max,min-1,-1):
        product = product * i
    return product
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
"""(3) Try calculating different binomial coefficients using both the functions 
from (2a) and (2b) for different values of n and k. Try some really big values 
there is a noticeable difference in speed between the (2a) and (2b) function. 
Which one is faster? By roughly how much?"""

#2a & 3
def binCoeff(n,k):
    '''This function calculates the binomial coefficient for two integers n and k.'''
    start = time.time()    
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient using the factorial formula for each element
        coeff = factorial(n,1) / (factorial(n-k,1)*factorial(k,1))
        end = time.time()
        elapsed = end - start        
        return coeff, elapsed
print binCoeff(500,2)

#2b & 3
def binCoeff2(n,k):
    '''This function calculates the binomial coefficient for two integers n and k in a more concise way.'''
    start = time.time()
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient by cancelling out the common terms in both parts of the division
        coeff = factorial(n,(n-k+1))/factorial(k,1)
        end = time.time()
        elapsed = end - start
        return coeff,elapsed
print binCoeff2(500,2)

def binCoeff3(n,k):
    '''This function calculates the binomial coefficient for two integers n and k in a more concise way.'''
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient by cancelling out the common terms in both parts of the division
        coeff = factorial(n,(n-k+1))/factorial(k,1)    
        return coeff
print binCoeff2(500,2)
"""Easier way would be to import the sympy module and use .binomial
import sympy
binomCoef=sympy.binomial(5, 2)
print binomCoef"""


"""(4) Use either function (2a) or (2b) to write a function that calculates the 
probability of k successes in n Bernoulli trials with probability p. This is 
called the Binomial(n,p) distribution. See Theorem 3.3.5 for the necessary equation. 
[Hint: pow(x,y) returns x^y (x raised to the power of y).]"""

def binomPMF(k,n,p):
    """
    This function returns the probability mass of k successes for a binomial 
    distribution with n trials and a probability of success given by p.
    """
    return binCoeff3(n,k)*pow(p,k)*pow((1-p),(n-k))
print binomPMF(5,10,0.5)

"""(5) Now write a function to sample from an arbitrary discrete distribution. 
This function should take two arguments. The first is a list of arbitrarily 
labeled events and the second is a list of probabilities associated with these 
events. Obviously, these two lists should be the same length."""

#function taken from jembrown 
import scipy ## Import scipy to use when drawing a random number b/t 0 and 1)    
def discSamp(events,probs):
    """
    This function samples from a list of discrete events provided in the events argument, using the event
    probabilities provided in the probs argument. These lists must:
        - Be the same length
        - Be in corresponding orders
    Also, the probabilities in probs must sum to 1.
    """
    ranNum = scipy.random.random()
    cumulProbs = []
    cumulProbs.extend([probs[0]])
    for i in range(1,len(probs)):
        cumulProbs.extend([probs[i]+cumulProbs[-1]])
    for i in range(0,len(probs)):
        if ranNum < cumulProbs[i]:
           return events[i]
    return None

"""---> Sampling sites from an alignment <---

Imagine that you have a multiple sequence alignment with two kinds of sites. 
One type of site pattern supports the monophyly of taxon A and taxon B. 
The second type supports the monophyly of taxon A and taxon C.

(6) For an alignment of 400 sites, with 200 sites of type 1 and 200 of type 2,
 sample a new alignment (a new set of site pattern counts) with replacement 
 from the original using your function from (5). Print out the counts of the 
 two types."""
 
sites = []												
 # Stores each of the 400 sites in each replicate draw.
for siteIndex in range(0,400):								
# For loop to perform 400 Bernoulli draws from the original 'alignment'.
	sites.extend([discSamp(["type1","type2"],[0.5,0.5])])     
 # Each new 'site' is added to sites
print("Type 1 count: %d" % sites.count("type1"))
print("Type 2 count: %d" % sites.count("type2"))

"""(7) Repeat (6) 100 times and store the results in a list."""

print("Sampling 100 times...")

# Importing the sys library to be able to flush output to the screen. This will ensure
#   that the progress indicator (with replicate number) shows up in real time.

import sys

counts = []													
# List to store the number of 'successes' in each replicate.
for reps in range(0,100):										
# For loop to produce 100 replicate draws.
    if reps % 10 == 0:											
    # This will be true every 10 replicates. % gives the remainder of reps/10.
        print(reps),											
        # Prints out the replicate number. Including the comma causes a space 
        #(rather than a newline) to follow the printed value.
    sys.stdout.flush()											
    # The flush() method makes sure anything waiting to be printed to the screen
    #is actually printed immediately.
    sites = []
    for siteIndex in range(0,400):
        sites.extend([discSamp(["type1","type2"],[0.5,0.5])])
    counts.extend([sites.count('type1')])						
    # Summarizing the number of successes for each replicate.

"""(8) Of those 100 trials, summarize how often you saw particular proportions 
of type 1 vs. type 2""

#(9) Calculate the probabilities of the proportions you saw in (8) using the 
binomial probability mass function (PMF) from (4)."""
freqs = []                         
 # A list to store frequencies of type 1 site proportions
uniqCounts = list(set(counts))      
# Uses set() to find the unique elements of counts, then turns it back into a list
for count in uniqCounts:            
# For each count, it adds a tuple to freqs. The first element contains the observed frequency across replicates and the 2nd element contains the exact binomial prob mass.
    freqs.extend([(float(counts.count(count))/float(100),binomPMF(count,400,0.5))])

print("Proportion, frequency")     
 # A header to label the columns that are about to be printed
for i in range(0,len(uniqCounts)):  
    print (round(float(uniqCounts[i])/400,3),freqs[i][0])

print("Proportion, Probability Mass")
for i in range(0,len(uniqCounts)):
    print (round(float(uniqCounts[i])/400,3),round(freqs[i][1],3))

#(10) Compare your results from (8) and (9).
diffs100 = []                       # List to store differences between sampled frequencies of counts and probability masses of counts
for f in freqs:
    diffs100.extend([f[0]-f[1]])    # Iteratively calculates differences b/w obs and expected and adds to the list

for i in range(0,2):                # Just printing a couple of lines to space things out
	print("")
print("Differences based on 100 resamplings...")
print("")
print " ".join('%0.4f' % diff for diff in diffs100) # Prints differences as one long line, by joining values with a space (" "). Formats floats to use 4 decimal places.

#(11) Repeat 7-10, but use 10,000 trials.
print("")
print("")
print("Sampling 10,000 times...")

counts = []
for reps in range(0,10000):
    if reps % 1000 == 0:
        print(reps),
    sys.stdout.flush()
    sites = []
    for siteIndex in range(0,400):
        sites.extend([discSamp(["type1","type2"],[0.5,0.5])])
    counts.extend([sites.count('type1')])

freqs = []
uniqCounts = list(set(counts))
for count in uniqCounts:
    freqs.extend([(float(counts.count(count))/float(10000),binomPMF(count,400,0.5))])
diffs10K = []
for f in freqs:
    diffs10K.extend([f[0]-f[1]])

for i in range(0,2):
	print("")
print("Differences based on 10,000 resamplings...")
print("")
print " ".join('%0.4f' % diff for diff in diffs10K)
