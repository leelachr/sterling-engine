# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 02:30:14 2016

@author: Leela
"""
import numpy as np

#def fun(lstEqs, lstVars):
    # equation 1xn Matrix -> 1xn Matrix
    myRow = np.zeros((1, len(lstVars)))
    fillRow = lambda equation: map(lambda term: myRow[indexFromName(term[0].name)] = term[1], equation.terms)
    
    # List List -> 1xn Matrix
    map(lambda eq: ... eq ... lstVars, lstEqs) 

# equation terms have a name. 
# turn the name into an index using 
# its position in an alphabetically
# sorted list.
def indexFromName(string, sortedListVars):
    pass

myMat = np.zeros((2, 3))
#myMat.setfield(42, (1, 1))
print(myMat)
