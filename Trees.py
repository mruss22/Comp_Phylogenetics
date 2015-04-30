"""

@author: Marisa_29

Below is the beginning of a Node class definition and a simple example of how
to link nodes to form a tree. Use this as a springboard to start thinking about:
- What other attributes of a Node might we like to store?
- How do we define a Tree class? What attributes should it have?
- Can you write a function to print out a parenthetical tree string 
   (e.g., ((spA,spB),spC)) if the only argument passed to the function is a
   root node? This will require recursion.
"""

# ---> Defining Node and Tree classes <---

class Node:
    
    def __init__(self,name="",parent=None,children=None):
        self.name = name
        self.totalTreeLength = 0 # TTL couter
        self.setModels(self.root) #models go to root first
        self.alignmentMatrix = [] #empty list to hold alignmentMatrix
        self.parent = None 
        if children is None:
            self.children = []
        else:
            self.children = children
        
        
        
# ---> Creating and linking nodes <---
 
# Creating nodes to build this simple three-taxon tree: ((spA,spB),spC)
       
#  spA     spB  spC
#    \    /     /
#     \  /     /
#      \/     /
#       \    /
#        \  /
#         \/
#         |

# Define the root node to start. It currently has no parents or children.
root = Node("root") 

# Define a node for species C. It is a direct descendant of the root.
spC = Node("SpeciesC",parent=root)
root.children.append(spC)   # Adds spC as a child of the root

# Define a node for the ancestor of species A and B, descending from the root.
ancAB = Node("ancAB",parent=root)
root.children.append(ancAB)
spA = Node("SpeciesA",parent=ancAB) # Creates spA with ancAB as its parent.
spB = Node("SpeciesB",parent=ancAB) # Creates spB with ancAB as its parent.
ancAB.children.append(spA)
ancAB.children.append(spB)


print("ancAB's children: ")
for child in ancAB.children:
    print child.name
    
print("")
print("root's children: ")
for child in root.children:
    print child.name

# Play around with nodes and see if you can build more complicated trees!
ancCD = Node("ancCD",parent=root)
root.children.append(ancAB)
spC = Node("SpeciesC",parent=ancCD) # Creates spA with ancAB as its parent.
spD = Node("SpeciesD",parent=ancCD) # Creates spB with ancAB as its parent.
ancCD.children.append(spC)
ancCD.children.append(spD)

ancD = Node("ancD",parent=root)
root.children.append(ancAB)
spD1 = Node("SpeciesD1",parent=ancD) # Creates spA with ancAB as its parent.
spD2 = Node("SpeciesD2",parent=ancD) # Creates spB with ancAB as its parent.
ancD.children.append(spD1)
ancD.children.append(spD2)

print("ancCD's children: ")
for child in ancCD.children:
    print child.name

print("ancD's children: ")
for child in ancD.children:
    print child.name
    
print("")
print("root's children: ")
for child in root.children:
    print child.name

# Eventually, we will want to create a Tree class, where a parenthetical tree
# string is passed as an argument to the constructor and it automatically creates
# all the nodes and links them together. Start thinking about how to do that.


# Let's go ahead and define a Tree object that houses all these nodes and 
# organizes methods associated with them.

#import ctmc
# We'll need this later, I promise. It's always better to put import statements
# outside of class definitions. In fact, it's best to put them all at the top
# of a file. This imports the ctmc class that we previously defined.

class Tree:
    """
    Defines a class of phylogenetic tree, consisting of linked Node objects.
    """
    
    def __init__(self):
        """
        The constructor really needs to be more flexible, but for now we're 
        going to define the whole tree structure by hand. This just uses
        the same statements we used above. By next Thurs (3/19), see if you can
        write a constructor that takes a parenthetical tree as its argument and 
        builds the corresponding tree in memory. 
        """
        self.root = Node("root") 
        self.spC = Node("SpeciesC",parent=self.root)
        self.root.children.append(self.spC)
        self.ancAB = Node("ancAB",parent=self.root)
        self.root.children.append(self.ancAB)
        self.spA = Node("SpeciesA",parent=self.ancAB)
        self.spB = Node("SpeciesB",parent=self.ancAB)
        self.ancAB.children.append(self.spA)
        self.ancAB.children.append(self.spB)
        # Now, let's add branch lengths to our Node objects (remember, these fields
        # can be added arbitrarily in Python). In the future, we should probably include
        # branch lengths in the Node constructor.
        self.spA.brl = 0.1
        self.spB.brl = 0.1
        self.spC.brl = 0.2
        self.ancAB.brl = 0.1
        self.root.brl = 0
        # We're also going to add lists to each node that will hold simulated
        # sequences.
        self.spA.seq = []
        self.spB.seq = []
        self.spC.seq = []
        self.ancAB.seq = []
        self.root.seq = []
        self.setModels(self.root)

    # Write a recursive function that takes the root node as its only argument and
    # prints out all the names of the terminal nodes in the tree. Due next Tues (3/17).

def printNames(self,node):
        """
        A method of a Tree object that will print out the names of its terminal nodes.
        """
        terminal_node=[]
        if len(node.children) == 0:
            for child in node.children:
                print node.name
                if len(child.children) >0:
                    terminal_node.append(self.printNames(child))
                else:
                    terminal_node.append(child.name)
                    print child.name

 
    # Write a recursive function to calculate the total tree length (the sum of
    # all the branch lengths). Again, the root node of a tree should be the only 
    # argument the first time this function is called. Due next Tues (3/17).
def treeLength(self,node):
        """
        A method to calculate and return total tree length.
        """
totalTreeLength = 0
if len(node.children) > 0:
    for child in node.children        
        self.totalTreeLength += node.br1
"""the statement x += y is equivalent to x = operator.iadd(x, y). 
    Another way to put it is to say that z = operator.iadd(x, y) is equivalent 
    to the compound statement z = x; z += y"""
else: 
    self.totalTreeLength = node.brl + totalbrl
return 
    self.totalTreeLength

    # Write a recursive function that takes the root node as one of its arguments
    # and prints out a parenthetical (Newick) tree string. Due next Tues (3/17).
    
    def newick(self,node):
        """
        A method of a Tree object that will print out the Tree as a 
        parenthetical string (Newick format).
        """
#code influenced from http://stackoverflow.com/questions/11195374/python-for-loop-iteration
# newick ex. (A,(B,C),D);
newickString = "(" # the start of the string
        
        if len(node.children) == 0: # Is the node terminal/at the tip
            return node.name + ":" + str(node.brl)# returns name : branch length
            
        else:
            for child in node.children: 
                newickString += self.newick(child) # runs the function for all the children
                if node.children[-1] == child: # is the previous node a child
                    pass 
                else:
                    newickString += "," # adds a comma to separate sister clades
            if node.brl == 0: # checks if the node is the root
                newickString += ")" 
            else:
                newickString += ")"+ ":" + str(node.brl) # otherwise, adds the brl for the ancestor
            
        return newickString.replace(",(","(") # removes the errant comma before non-sister clades

    # Now, let's write a recursive function to simulate sequence evolution along a
    # tree. This amounts to simply simulating evolution along each branch 
    # from the root towards the tips. We'll need to use our ctmc class for setting the 
    # conditions of our simulation, which is why we imported it above our tree 
    # class definition. In this case, we've stored the definition of our ctmc 
    # class in a separate file (ctmc.py) to keep our tree code compact.
    # Now, let's add a ctmc object to each internal node in our tree (except the
    # root). Again, it would be best to add the ctmcs as part of the Node
    # constructor, if we know that we'll be simulating data.
    
    # Try to get this simulator and associated functions working by next Thurs. (3/19)    
    
    def setModels(self,node):
        """
        This method of a Tree object defines a ctmc object associated with all
        nodes that have a branch length (i.e., all but the root).
        """
#imported ctmc above

    def simulate(self,node):
        """
        This method simulates evolution along the branches of a tree, taking
        the root node as its initial argument.
        """
          if node.children == []:
			pass #the pass statement does nothing 
		else:
			for child in node.children:
				child.sequence = [ctmc.ContMarkov(time = child.brl).simulation(seq=node.sequence)]
				self.simulate(child)   
    def printSeqs(self,node):
        """
        This method prints out the names of the tips and their associated
        sequences as an alignment (matrix).
        """
        if len(node.children) > 0: #does node have any children
            for child in node.children:
                self.printseqs(child)
        else: 
            self.alignmentMatrix.append(node.name)
            self.alignmentMatrix.append(node.seq)
        return self.alignmentMatrix
   
   print (node.name)
		for child in node.children:
			self.printSeqs(child)
