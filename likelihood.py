
@author: Marisa_29
"""

#An Introduction to Likelihood
#@author: jembrown
"""

""
There are two primary ways to use probability models. Given what we know to be 
true about an experimental setup, we can make predictions about what we expect 
to see in an upcoming trial. For this purpose, probability functions are what 
we need. If R is the outcome of an experiment (i.e., an event) and p is a 
parameter of the probability function defined for these experimental outcomes, 
we can write these expectations or predictions as: P(R|p).
This conditional probability tells us what to expect about the outcomes of our 
experiment, given knowledge of the underlying probability model. Thus, it is a 
probability function of R given a value for p (and the model itself).
However, we might also wish to ask what we can learn about p itself, given 
outcomes of trials that have already been observed. This is the purview of the 
likelihood. Likelihoods are functions of parameters (or hypotheses, more 
generally) given some observations. The likelihood function of a parameter 
value is defined as: L(p;R) = P(R|p)
Note that this is the same probability statement we saw above. However, in this
context we are considering the outcome (R) to be fixed and we're interested in 
learning about p. Note that the likelihood is sometimes written in several 
different ways: L(p;R) or L(p) or L(p|R). P(R|p) gives a probability when R is 
discrete or a probability density when R is continuous. Since likelihoods are 
only compared for some particular R, we do not need to worry about this 
distinction. Technically speaking, likelihoods are just said to be proportional
to P(R|p), with the constant of proportionality being arbitrary.
There are some very important distinctions between likelihoods and probabilities.
First, likelihoods do NOT sum (or integrate) to 1 over all possible values of p.
Therefore, the area under a likelihood curve is not meaningful, as it is for 
probability.
It does not make sense to compare likelihoods across different R. For instance,
smaller numbers of observations generally produce higher values of P(R|p), 
because there are fewer total outcomes.
Likelihood curves provide useful information about different possible values of
p. When we are interested in comparing discrete hypotheses instead of 
continuous parameters, the likelihood ratio is often used:
L(H1;R)     P(R|H1)
-------  =  -------
L(H2;R)     P(R|H2)
Now, let's try using likelihoods to learn about unknown aspects of the process 
that's producing some data.
---> Inferring p for a binomial distribution <---
First, we'll start by trying to figure out the unknown probability of success 
associated with a Binom(5,p) random variable. If you want to try this on your 
own later, the following code will perform draws from a binomial with 5 trials.
You can simply change the associated value of p to whatever you'd like. To make
the inference blind, have a friend set this value and perform the draws from 
the Binomial for you, without revealing the value of p that they used.
"""
from __future__ import division
from scipy.stats import binom

n = 5
p = 0.5 # Change this and repeat

data = binom.rvs(n,p)

"""
For the in-class version of this exercise, I'm going to perform a manual draw 
from a binomial using colored marbles in a cup. We'll arbitrarily define dark 
marbles as successes and light marbles as failures.
Record the outcomes here:
Draw 1: Dark
Draw 2: Dark
Draw 3: Dark 
Draw 4: Dark 
Draw 5: Light
Number of 'successes': 4
Now record the observed number of succeses as in the data variable below.
"""

data =   4 # Supply observed number of successes here.
numTrials = 5

"""Since we are trying to learn about p, we define the likelihood function as;
L(p;data) = P(data|p)
If data is a binomially distributed random variable [data ~ Binom(5,p)]
P(data=k|p) = (5 choose k) * p^k * (1-p)^(n-k)
So, we need a function to calculate the binomial PMF. Luckily, you should have
just written one and posted it to GitHub for your last exercise. Copy and paste 
your binomial PMF code below. For now, I will refer to this function as binomPMF(). 
"""
def factorial(max,min):
    product=1
    for i in range(max,min-1,-1):
        product = product * i
    return product

def binCoeff3(n,k):
    '''This function calculates the binomial coefficient for two integers n and k.'''
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient by cancelling out the common terms in both parts of the division
        coeff = factorial(n,(n-k+1))/factorial(k,1)    
        return coeff

def binomPMF(k,n,p):
    """
    This function returns the probability mass of k successes for a binomial 
    distribution with n trials and a probability of success given by p.
    """
    return binCoeff3(n,k)*pow(p,k)*pow((1-p),(n-k))

"""
Now we need to calculate likelihoods for a series of different values for p to 
compare likelihoods. There are an infinite number of possible values for p, so 
let's confine ourselves to steps of 0.05 between 0 and 1.
"""
#for loops will work best throughout the excercise
# Set up a list with all relevant values of p
p_rel = []
for i in range(0,105,5):    #cannot use 0,1,0.05 the program will treat 0.05 as a float
    x=i/100.0
    p_rel.append(x)
    #The method append adds its parameter as a single element to the list, 
    #while extend gets a list and adds its content
print "\nAll relevant values of p are"
print p_rel
"""[0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 
0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]"""


# Calculate the likelihood scores for these values of p, in light of the data you've collected
L_scores=[]
for p in p_rel:
    likelihood=binomPMF(4,5,p)
    L_scores.append(likelihood)
print "\nThe likelihood scores for these values of p are"
print L_scores

""" [0.0, 2.9687500000000007e-05, 0.0004500000000000001, 0.0021515625, 0.006400000000000002, 
0.0146484375, 0.028349999999999993, 0.04877031249999999, 0.07680000000000002, 0.1127671875, 
0.15625, 0.20588906250000003, 0.2592, 0.31238593750000004, 0.36014999999999997, 0.3955078125, 
0.4096, 0.3915046875, 0.3280499999999999, 0.20362656250000014, 0.0]"""

# Find the maximum likelihood value of p (at least, the max in this set)

maxLikeli = max(L_scores)
print "\nThe maximum likelihood value of p is"
print maxLikeli
#0.4096


# What is the strength of evidence against the most extreme values of p (0 and 1)?
print "\nIn statistics to reject the null hypothesis at the 5% level, when the" 
print "p-value is less than 0.05. The event that has occurred is said to be statistically" 
print "significant at the 0.05 level. Since we know that there are at least some dark and light marbles"
print "in the cupt (due to the # of successes) it would be improbably to draw all light or dark (the extreme values of p)"


# Calculate the likelihood ratios comparing each value (in the numerator) to the max value (in the denominator)

likelihood_ratios=[]
for i in L_scores:
    ratio=i/maxLikeli
    likelihood_ratios.append(ratio)
print "\nThe likelihood that the value of p would be [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0] is (see below) in order"
print likelihood_ratios
"""[0.0, 7.247924804687501e-05, 0.0010986328125000002, 0.005252838134765624, 0.015625000000000003, 
0.035762786865234375, 0.06921386718749999, 0.1190681457519531, 0.18750000000000006, 
0.2753105163574219, 0.3814697265625, 0.5026588439941406, 0.6328124999999999, 0.7626609802246095, 
0.8792724609374999, 0.9655952453613281, 1.0, 0.9558219909667969, 0.8009033203124997, 
0.49713516235351596, 0.0]"""


"""
Now let's try this all again, but with more data. This time, we'll use 20 draws from our cup of marbles.
"""

data = 12  # Supply observed number of successes here.
numTrials = 20


# Calculate the likelihood scores for these values of p, in light of the data you've collected
L_scores2=[]
for p in p_rel:
    likelihood=binomPMF(12,20,p)
    L_scores2.append(likelihood)
print "\nThe likelihood scores for these values of p are"
print L_scores2

# Find the maximum likelihood value of p (at least, the max in this set)
maxLikeli = max(L_scores)
print "\nThe maximum likelihood value of p is"
print maxLikeli

# What is the strength of evidence against the most extreme values of p (0 and 1)?
print "\nIn statistics to reject the null hypothesis at the 5% level, when the" 
print "p-value is less than 0.05. The event that has occurred is said to be statistically" 
print "significant at the 0.05 level. Since we know that there are at least some dark and light marbles"
print "in the cupt (due to the # of successes) it would be improbably to draw all light or dark (the extreme values of p)"

# Calculate the likelihood ratios comparing each value (in the numerator) to the max value (in the denominator)
likelihood_ratios=[]
for i in L_scores:
    ratio=i/maxLikeli
    likelihood_ratios.append(ratio)
print "\nThe likelihood that the value of p would be [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0] is (see below) in order"
print likelihood_ratios

# When is the ratio small enough to reject some values of p?
print "\n the ratio is small enough to reject some values of p when the p-value is less than 0.05"
# Note: You will empirically investigate this on your own later in this exercise.
