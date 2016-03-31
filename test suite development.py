import unittest

class Variable(object):
    def __init__(self, name=None, value=None, description=None, units=None):
        self.name = name
        self.val = value
        self.description = description

class Equation(object):
    def __init__(self, terms=None, sumIs=None):
        self.terms = terms
        self.sumIs = sumIs
        
x = Variable(name="x")
y = Variable(name="y", value=1)
z = Variable(name="z")

eqA = Equation([(x, -1), \
                (y, -2), \
                (z, 1)], \
                0)
eqB = Equation([(x, -1), \
                (z, -1)], \
                4)
                
myInput = [eqA, eqB]
                
# ---------------------------------------------------
# function definitions
# ---------------------------------------------------
# ===================================================
# package everything inside these ====== line breaks
# into a single function later. right now they're 
# separated for unit testing.

# List-of-Equations -> List-of-Variables
# lists all variables in a list of equations.
# returns list which is sorted alphabetically.
def listVars(equations):
    variables = []
    for equation in equations:
        for term in equation.terms:
            if term[0].name == None:
                continue
            variables.append(term[0].name)
    # remove duplicates from list
    noDuplicates = list(set(variables))
    # sort alphabetically
    sortedVars = sorted(noDuplicates)
    return sortedVars

# List-of-Equations List-of-Variables -> Matrix
# put equations into matrix form
def makeMatrix(equations, variables):
    # count equations
    len(equations)
    
    

# checks num eqs and num unknowns.

# checks all equations if the variables have been 
# declared. prints detailed error message if not.


# List-of-Variables -> Matrix
# makes a matrix with as many columns as there
# are unique variables & as many rows as there
# are equations.
def initMatrix(lstVars):
    size = len(lstVars)
        
    # appends two matrices.
    
# gets size of a system (i.e. num elem in set)

# checks that all variables in all equations have 
# been initialized with a name.
# ====================================================

print(listVars(myInput))
