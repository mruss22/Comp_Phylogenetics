# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 22:48:08 2015

@author: Marisa_29
"""

"""Exercise 4
Discrete-time Markov chains
@author: jembrown
"""

"""
In this exercise, we will explore Markov chains that have discrete state spaces
and occur in discrete time steps. To set up a Markov chain, we first need to 
define the states that the chain can take over time, known as its state space.
To start, let's restrict ourselves to the case where our chain takes only two
states. We'll call them A and B."""

# Create a tuple that contains the names of the chain's states
"""A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. 
The only difference is that tuples can't be changed i.e., tuples are immutable and 
tuples use parentheses and lists use square brackets. Creating a tuple is as simple 
as putting different comma-separated values and optionally you can put these 
comma-separated values between parentheses also."""

states_tuple = ("A","B")


"""The behavior of the chain with respect to these states will be determined by 
the probabilities of taking state A or B, given that the chain is currently in 
A and B. Remember that these are called conditional probabilities (e.g., the 
probability of going to B, given that the chain is currently in state A is P(B|A).)
We record all of these probabilities in a transition matrix. Each row
of the matrix records the conditional probabilities of moving to the other
states, given that we're in the state associated with that row. In our example
row 1 will be A and row 2 will be B. So, row 1, column 1 is P(A|A); row 1, 
column 2 is P(B|A); row 2, column 1 is P(A|B); and row 2, column 2 is P(B|B). 
All of the probabilities in a ROW need to sum to 1 (i.e., the total probability
associated with all possibilities for the next step must sum to 1, conditional
on the chain's current state).
In Python, we often store matrices as "lists of lists". So, one list will be 
the container for the whole matrix and each element of that list will be 
another list corresponding to a row, like this: mat = [[r1c1,r1c2],[r2c1,r2c2]]. 
We can then access individual elements use two indices in a row. For instance,
mat[0][0] would return r1c1. Using just one index returns the whole row, like
this: mat[0] would return [r1c1,r1c2].
Define a transition matrix for your chain below. For now, keep the probabilties
moderate (between 0.2 and 0.8).
"""

# Define a transition probability matrix for the chain with states A and B
A=[0.4,0.6]
B=[0.3,0.7]
trans_matrix=[A,B]

# Try accessing a individual element or an individual row 
# Element
print trans_matrix [0] [1] 

# Row
print trans_matrix [0]
print trans_matrix [1]


"""
Now, write a function that simulates the behavior of this chain over n time
steps. To do this, you'll need to return to our earlier exercise on drawing 
values from a discrete distribution. You'll need to be able to draw a random
number between 0 and 1 (built in to scipy), then use your discrete sampling 
function to draw one of your states based on this random number.
"""

# Import scipy U(0,1) random number generator
import scipy

# Paste or import your discrete sampling function
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

# Write your Markov chain simulator below. Record the states of your chain in 
# a list. Draw a random state to initiate the chain.
#used jembrown's Markov chain simulator

matrix=[[0.5,0.5],[0.5,0.5]]
states=('a','b')
def dmcSim(n,st=states,allProbs=matrix):
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

# Run a simulation of 10 steps and print the output.

test=dmcSim(10,st=("a","b"),allProbs=matrix)
print("State A count: %d" % test.count("a"))
print("State B count: %d" % test.count("b"))
print test


# ----> Try to finish the above lines before Tues, Feb. 10th <----

# Now try running 100 simulations of 100 steps each. How often does the chain
# end in each state? How does this change as you change the transition matrix?
test2=dmcSim(100,st=("a","b"),allProbs=matrix)*100
print test2
print("State A count: %d" % test2.count("a"))
print("State B count: %d" % test2.count("b"))

'''Run 1 = State A count: 4700
State B count: 5300

Run 2 = State A count: 5200
State B count: 4800

Run 3 = State A count: 4900
State B count: 5100
'''

'''I changed the matrix to matrix=[[0.9,0.1],[0.4,0.6]] from matrix=[[0.5,0.5],[0.5,0.5]]
and state a's count increased accordingly State A count: 8600
State B count: 1400
'''

# Try defining a state space for nucleotides: A, C, G, and T. Now define a 
# transition matrix with equal probabilities of change between states.

stateSpace= ('A','C','G','T')
matrix3 = [[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25]]
test3=dmcSim(10,st=stateSpace,allProbs=matrix3)
print test3
print("State A count: %d" % test3.count("A"))
print("State C count: %d" % test3.count("C"))
print("State G count: %d" % test3.count("G"))
print("State T count: %d" % test3.count("T"))

'''output 1: 
['A', 'G', 'A', 'C', 'C', 'C', 'T', 'G', 'C', 'A']
State A count: 3
State C count: 4
State G count: 2
State T count: 1
'''

# Again, run 100 simulations of 100 steps and look at the ending states. Then
# try changing the transition matrix.
stateSpace= ('A','C','G','T')
probs = [[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25]]
test4=dmcSim(100,st=stateSpace,allProbs=probs)*100
print test4
print("State A count: %d" % test4.count("A"))
print("State C count: %d" % test4.count("C"))
print("State G count: %d" % test4.count("G"))
print("State T count: %d" % test4.count("T"))

'''output 1
State A count: 2600
State C count: 2600
State G count: 2400
State T count: 2400
'''
