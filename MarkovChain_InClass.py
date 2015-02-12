# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:22:54 2015

@author: Marisa_29
"""

#In-Class Markov Chain Exercise
#2.10.15
#@author: jembrown
"""

"Recall from your reading that any irreducible and aperiodic Markov chain has a 
stationary distribution. To convince ourselves that things will converge for 
such a chain with arbitrary transition probabilities, let's give it a try.
Work in pairs for this. It's more fun to be social."""

# Paste your Markov chain simulation function below, where the starting state
# is drawn with uniform probability from all possible states. Remember to also
# copy any import statements or other functions on which your simulator is
# dependent."""

import scipy as sp     

def discSamp(events,probs):
    """
    This function samples from a list of discrete events provided in the events
    argument, using the event probabilities provided in the probs argument. 
    These lists must:
        - Be the same length
        - Be in corresponding orders
    Also, the probabilities in probs must sum to 1.
    """
    ranNum = sp.random.random()
    cumulProbs = []
    cumulProbs.extend([probs[0]])
    for i in range(1,len(probs)):
        cumulProbs.extend([probs[i]+cumulProbs[-1]])
    for i in range(0,len(probs)):
        if ranNum < cumulProbs[i]:
           return events[i]
    return None

def dmcSim(n,st=("a","b"),allProbs=[[0.5,0.5],[0.5,0.5]]):
    """
    This function simulates the progression of a discrete-time, discrete-state
    Markov chain. It takes 3 arguments: (1) The number of steps (n), (2) the 
    state space, and (3) the transition matrix. It returns a list containing 
    the progression of states through time. This list should have length n.
    
    The chain will be initiated with a randomly drawn state.
    """
    
    # Define list to hold chain's states
    chain = []    

    # Draw a state to initiate the chain
    currState = discSamp(st,[1.0/len(st) for x in st])
    chain.extend(currState)

    # Simulate the chain over n-1 steps following the initial state
    for step in range(1,n):
        probs = allProbs[st.index(currState)] # Grabbing row associated with currState
        currState = discSamp(st,probs) # Sample new state
        chain.extend(currState)        
        
    return chain


# Define a 2x2 transition matrix. For fun, don't make all the probabilities
# equal. Also, don't use any 0s or 1s (to make sure the chain is irreducible
# and aperiodic).
matrix = [[0.8, 0.2], [0.3, 0.7]]
# Simulate a single chain for three time steps and print the states
single=dmcSim(3,st=("a","b"),allProbs=matrix)
print single
#ex. output 'b','a','a'

# Analytically calculate the progression of states for this chain.
#ex. output 'b','a','a'
state1=0.5
state2=matrix [0][0]
state3=matrix [0][0]
prog1=state1*state2*state3
print prog1

# Calculate the probability of observing the state in step 3, given the initial
# state in step 1 (i.e., as if you didn't know the state in step 2).
#ex. output 'b','?','a'
state1=0.5
state2=(matrix [0][0])+((0.5)*(matrix [0][1])*(matrix[1][0]))
state3= matrix [0][0]
prog2=state1*state2*state3
print prog2


# Now think of the chain progressing in the opposite direction. What is the
# probability of the progression through all 3 states in this direction? How
# does this compare to the original direction?
#ex. output 'b','a','a'
# reverse 'a','a','b'
state1=0.5
state2=matrix [0][0]
state3=matrix [1][1]
prog3=state1*state2*state3
print prog3

# Try the same "forward" and "reverse" calculations as above, but with this
# transition matrix:
revMat = [[0.77,0.23], [0.39,0.61]]
# and these starting frequencies for "a" and "b"
# freq(a) = 0.63   freq(b) = 0.37
trans_matrix=dmcSim(3,st=("a","b"),allProbs=revMat)
print trans_matrix
#ex. output ['a', 'a', 'b']

# What is (roughly) true about these probabilities?
state1=0.63
state2=revMat [0][0]
state3=revMat [1][1]
prog4=state1*state2*state3
print prog4

# Simulate 1,000 replicates  (or 10K if your computer is fast enough) of 25 
# steps. What are the frequencies of the 2 states across replicates through time?
trans_matrix2=dmcSim(25,st=("a","b"),allProbs=revMat)*10000
print trans_matrix2
print("State A count: %d" % trans_matrix2.count("a"))
print("State B count: %d" % trans_matrix2.count("b"))
freqA=(trans_matrix2.count("a"))/(10000*25)
print "The frequency of state a is" 
print freqA
freqB=(trans_matrix2.count("b"))/(10000*25)
print "The frequency of state b is" 
print freqB
'''ex. output
State A count: 110000
State B count: 140000
The frequency of state a is
0.44
The frequency of state b is
0.56
'''

# NOTE: Here is a function that reports the frequencies of a state through time 
# for replicate simulations. You'll need to do this several times during this exercise.

def mcStateFreqSum(sims,state="a"):
    """
    Pass this function a list of lists. Each individual list should be the
    states of a discrete-state Markov chain through time (and all the same 
    length). It will return a list containing the frequency of one state 
    ("a" by default) across all simulations through time.
    """
    freqs = []
    for i in range(len(sims[0])):  # Iterate across time steps
        stateCount = 0
        for j in range(len(sims)): # Iterate across simulations
            if sims[j][i] == state:
                stateCount += 1
        freqs.extend([float(stateCount)/float(len(sims))])
    return freqs

# Run replicate simulations 
listList = [['a','a','b'], ['a','b','b'], ['a','b','b'], ['a','a','a']]


    
# Summarize the frequency of one state through time




# What do you notice about the state frequencies through time? Try another round
# of simulations with a different transition matrix. How do the state freq.
# values change?






# Now, calculate a vector of probabilities for the focal state (e.g., 'a')
# based on the transition matrix directly (not by simulation). How do these
# values compare to the simulated frequencies?
