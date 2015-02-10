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
import numpy

def MarkovChain(matrix,length):
    Mchain=[] #make an emtpy list
    number=numpy.random.random(1)
    states_tuple=("A","B")
    if  number<matrix[0][0]: #individal element
        state=states_tuple[0] #individal row
    else: 
        state=states_tuple[1]
    Mchain.append(state)
    if length ==1:
        return Mchain 
    else:
        for state in MarkovChain(matrix,(length-1)): 
            if state=="A": 
                number=numpy.random.random(1)
                if number<=matrix[0][0]:
                    state=="A"
                else:
                    state=="B"
            elif state=="B":
                number=numpy.random.random(1)
                if number<=matrix[1][1]:
                    state=="B"
                else:
                    state=="A"
            Mchain.append(state)     
        return Mchain



# Run a simulation of 10 steps and print the output.

test=MarkovChain(matrix,10)

print test


# ----> Try to finish the above lines before Tues, Feb. 10th <----

# Now try running 100 simulations of 100 steps each. How often does the chain
# end in each state? How does this change as you change the transition matrix?




# Try defining a state space for nucleotides: A, C, G, and T. Now define a 
# transition matrix with equal probabilities of change between states.



         
# Again, run 100 simulations of 100 steps and look at the ending states. Then
# try changing the transition matrix.
