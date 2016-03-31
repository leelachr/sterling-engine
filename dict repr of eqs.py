# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:40:18 2016

@author: Leela
"""

import unittest
import numpy as np

# data definitions:

# an Equation is a Dictionary with Strings as keys  
# and Coefficients as entries. 
# variable prefix for this data type is eq-.

# a System is a List of Equations which satisfies
# the sytem property of equal number of equations
# and variables.

# a Coefficient is a Number.
# represents the known coefficient to a variable
# in a linear equation.

# an Index is an Integer.
# represents a column index in the matrix to
# be solved. each Variable has a unique Index.

# a Variable is a String.

eqA = {"x":1,
       "y":2,
       "z":-1,
       "sumIs":0}
eqB = {"x":1,
       "z":1,
       "sumIs":4}
eqC = {"y":1,
       "sumIs":3}

eqs = [eqA, eqB, eqC]

# Equations -> List-of-Strings 
# lists all variables, including sumIs, which
# is a special case. (it's not solved for, but
# it appears in the matrix as the right-most
# column.)
def listVars(equations):
    variables = []
    for equation in equations:
        for term in equation:
            if term == "sumIs":
                continue
            variables.append(term)
    # remove duplicates from list
    duplicatesRemoved = list(set(variables))
    # sort alphabetically
    sortedVars = sorted(duplicatesRemoved)
    # place "sumIs" at last position.
    # we want the last matrix column 
    # to be sumIs.
    sortedVars.append("sumIs")
    return sortedVars

# Equations -> Dictionary
# provides each variable with a unique Index, 
# which will be its column index in the matrix.
# keys are Indexes, values are Variables.
def indexDict(eqs):
    # List List -> Dictionary
    # returns a dictionary in which first list
    # is the keys, and second list the values.
    def dictFromTwoLists(lst1, lst2):
        return dict(zip(lst1, lst2))
    # FUNCTION BODY of indexDict
    varis = listVars(eqs)
    indexes = range(0,len(varis))
    indexDict = dictFromTwoLists(indexes, varis)
    return indexDict

# Equations -> Bool
# checks if equations obey system property
# of # eqs == # unknowns, i.e. variables.
def checkSystem(eqs):
    numEqs = len(eqs)    
    # subtract 1 because sumIs isn't an unknown.
    numUnknowns = len(listVars(eqs)) - 1 
    return numEqs == numUnknowns

# Equations -> Matrix
# creates a list of lists, converts to 
# numpy array at the very end.
def makeMatrix(eqs):
    # LOCAL VALUES AND HELPER FUNCTIONS
    indexes = indexDict(eqs)
    numCols = len(listVars(eqs))
    # Index Equation -> Coefficient
    def getCoeff(idx, eq):
        if indexes[idx] in eq:
            coeff = eq[indexes[idx]]
            return coeff
        else:
            return 0
    # Equation -> List
    def makeRow(eq):
        row = []
        [row.append(getCoeff(idx, eq)) for idx in indexes]
        return row
        
    # FUNCTION BODY of makeMatrix
    listRows = []
    [listRows.append(makeRow(eq)) for eq in eqs]
    matrix = np.array(listRows)
    return matrix    

# NumpyArray List-of-Variables -> Dictionary
# returns a dictionary in which variables are 
# the keys, and their values are the values.
def solveMatrix(matrix, variables):
    if variables[-1] == "sumIs":
        variables = variables[0:-1]
    values = np.linalg.solve(matrix[:, 0:-1], matrix[:,-1])
    resultDict = dict(zip(variables, values))
    return resultDict

# Equations -> Dictionary
def main(eqs):
    if checkSystem(eqs) == False: 
        print("""Error from function makeMatrix: The system of equations does not satisfy the condition that 
        the number of equations equals the number of variables.""")
    return solveMatrix(makeMatrix(eqs), listVars(eqs))

# -------------------------------------------------
# UNIT TESTS
# -------------------------------------------------
eqs = [eqA, eqB, eqC]
class functionTests(unittest.TestCase):
    def setUp(self):
        self.eqA = {"x":1,
                    "y":2,
                    "z":-1,
                    "sumIs":0}
        self.eqB = {"x":1,
                    "z":1,
                    "sumIs":4}
        self.eqC = {"y":1,
                    "sumIs":3}
        self.eqs = [self.eqA, self.eqB, self.eqC]
        self.vars = ["x", "y", "z", "sumIs"]
        self.indexes = {0:"x", 
                        1:"y",
                        2:"z",
                        3:"sumIs"}
        self.matrix = np.array([[1, 2, -1, 0],
                               [1, 0, 1, 4],
                               [0, 1, 0, 3]])
        self.result = {"x":-1, 
                       "y":3,
                       "z":5}
    def test_listVars(self):
        self.assertEqual(listVars(self.eqs), self.vars)
    def test_indexDict(self):
        self.assertDictEqual(indexDict(self.eqs), self.indexes)
    def test_makeMatrix(self):
        np.testing.assert_array_equal(makeMatrix(self.eqs), self.matrix)
    def test_solveMatrix(self):
        self.assertEqual(solveMatrix(self.matrix,self.vars), self.result)
unittest.main()


# ______________________________________________
# notes/todo:
# 1. for listvars:
# maybe I could use some algorithm where I 
# put new vars into a tree so I can search
# for them there.
'''# Term -> Equation Equation
# if an equation contains a term x*y
# this will return another equation which
# has each multiplicand ...
def linearizeProd(eq):
    pass

# Equation -> Equation Equation
def linearizeDiv(eq):
    pass

# Equation -> Equations
def linearizeExp(eq):
    pass
'''

# 2. the line "if indexes[idx] in eq:"
# in getCoeff is confusing because 
# indexes[idx] is actually a Variable,
# i.e. a String, but it doesn't look 
# like one.