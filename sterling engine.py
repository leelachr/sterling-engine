# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 23:39:18 2016

@author: Leela
"""
import numpy
import sympy

# notes/todo: 
# - make a structure out of engine specs, which can be
#   passed in to main. this makes it easier to study
#   different engine configurations. ... class Engine():
# - it's going to be a source of confusion for some 
#   eqs to go into the matrix, but some to exist as
#   a way to "unpack", like T/V = P. all eqs need to
#   go into the matrix.

# ---------------------------------------------------
# data types
# ---------------------------------------------------
# an Equation is an instance of class Equation.
# it represents a linear equation in which all terms
# have been moved to one side, and their sum is the 
# "sumIs" field of the class.
# note that equations have a name prefix of "eq".
class Equation(object):
    def __init__(self, terms=None, sumIs=None):
        self.terms = terms
        self.sumIs = sumIs

# a Term is a tuple.
# the first element is a String and represents a varible 
# name. the second element is a Number and represents
# the variable's coefficient in the linear eqution.

# a Variable is an instance of class Variable.
# note, description and units are not currently
# used and are optional. 
# name is required upon initialization.
# value can be added when known.
class Variable(object):
    def __init__(self, name=None, value=None, description=None, units=None):
        self.name = name
        self.value = value
        self.description = description
        # self.units = units 

# a System is a list of Variables.

# an Input is an list of Equations.


# ---------------------------------------------------
# constant definitions
# ---------------------------------------------------

# units: meters, kg, celcius, bar (absolute pressure).

# names are prefixed by their pysical type, i.e. 
# length (len), temperature (T), pressure (P), mass (m),
# velocity (vel), acceleration (acc), volume (vol),
# molar volume (mvol), position (pos) (it has the same
# units as length, but position and length are different
# properties.), time (t), area (area)...

# universal constants:
Rgas = 8.314 # Joule/kg-K
pi = 3.1415

# engine specs:
Thot = Variable(name="Thot", value = 80) # C
Tcold = Variable(name="Tcold", value = 5) # C
lenEngine = Variable(name="lenEngine", value = 1) # length of the engine
lenEngRadius = Variable(name="lenEngRadius", value = 0.2) # radius of the engine
lenSep = Variable(name="lenSep", value = 0.25) # length of a separator (i.e. the cork block)
lenPlunger = Variable(name="lenPlunger", value = 0.05) # length of the plunger 
mSep = Variable(name="mSep", value=0.2, description="mass of separator")
mPlunger = Variable(name="mPlunger", value=0.3, description="mass of plunger")
areaCrossSec = Variable(name="areaCrossSec", value = pi * lenEngRadius.value ** 2)
volSep = Variable(name="volSep", value=0.8, description="volume of a separator. currently, \
                                    neglect effect of center conduit.")

# declare all other variables 
Plp = Variable(name="Plp", description="pressure on left side of plunger")
Prp = Variable(name="Prp", description="pressure on right side of plunger")
accPlunger = Variable(name="accPlunger", description="acceleration of plunger")
Plw = Variable(name="Plw", description="pressure at left wall")
accSepLeft = Variable(name="accSepLeft", description="acceleration of left separator")
Prw = Variable(name="Prw", description="acceleration at right wall")
lenLeftWall = Variable(name="lenLeftWall", description="distance between left wall and separator")
posnPlunger = Variable(name="posnPlunger", description="distance from left wall to center of plunger")
lenLeftPlunger = Variable(name="lenLeftPlunger", description="...")
lenRightPlunger = Variable(name="lenRightPlunger", description="...")
Pinit = Variable(name="Pinit", description="pressure when cylinder is initially charged. \
                                same on both sides of plunger")

Plw__posSepLeft = Variable()
Plp__posPlunger = Variable()
Plp__posSepLeft = Variable()


# ---------------------------------------------------
# function definitions
# ---------------------------------------------------
# ===================================================
# package everything inside these ====== line breaks
# into a single function later. right now they're 
# separated for unit testing.
# put equations into matrix form
def makeMatrix(equations):
    pass
# checks num eqs and num unknowns.

# checks all equations if the variables have been 
# declared. prints detailed error message if not.

# List-of-Equations -> List-of-Variables
# lists all variables in a list of equations.
def listVars(equations):
    vars = []
    for equation in equations:
        for term in equation:
            vars.append(term[0])
    return vars


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

# solves matrix
def solve(matrix):
    pass

# ---------------------------------------------------
# system and model equations
# ---------------------------------------------------


# equations:
# force balance on plunger:
eqForceBalPlunger = Equation([(Plp, Rgas*areaCrossSec.value), \
                              (Prp, -Rgas*areaCrossSec.value), \
                              (accPlunger, -mPlunger.value)], \
                              0)
# force balance on left-hand separator:
eqForceBalLeftSep = Equation([(Plw, Rgas*areaCrossSec.value), \
                              (Plp, -Rgas*areaCrossSec.value), \
                              (accSepLeft, -mSep.value)], \
                              0)
# force balance on right-hand separator: 
eqForceBalRightSep = Equation([(Prp, Rgas*areaCrossSec.value), \
                               (Prw, -Rgas*areaCrossSec.value), \
                               (accSepRight, -mSep.value)], \
                               0)
# geometric legality:
eqPlungerPosn = Equation([(lenLeftWall.value, 1), \
                        (lenSep.value, 1), \
                        (lenPlunger.value, 0.5), \
                        (posnPlunger.value, -1)], \
                        0) # adds up to length on left side of plunger
eqLenEngine = Equation([(lenLeftWall.value, 1), \
                       (lenSep.value, 2), \
                       (lenLeftPlunger.value, 1), \
                       (lenRightPlunger.value, 1), \
                       (lenRightWall.value, 1), \
                       (lenEngine.value, -1)], \
                       0) # adds up to total length
# mole balance on left side:
eqMolBalLeft = Equation([(Pinit, 0.5 * (volEngine.value - volPlunger.value - 2 * volSep.value) / (Rgas * Tinit.value)), \
                        (Plw__posSepLeft, -areaCrossSec.value / (Rgas * Thot.value)), \
                        (Plw, 0.5 * areaCrossSec.value * lenSep.value / (Rgas * Thot.value)), \
                        (Plp__posPlunger, -areaCrossSec.value / (Rgas * Tcold.value)), \
                        (Plp, 0.5 * areaCrossSec.value * lenPlunger.value / (Rgas * Tcold.value)), \
                        (Plp__posSepLeft, areaCrossSec.value / (Rgas * Tcold.value)), \
                        (Plp, 0.5 * areaCrossSec.value / (Rgas * Tcold.value))], \
                        0)
# mole balance on right side:               
eqMolBalRight = Equation([(), \
                          (), \
                          ()], \
                          0)

# knowns: 
#knPinit = Equation([Pinit, 1], Pinit.value)
Pinit.value = 10


# ---------------------------------------------------
# main
# ---------------------------------------------------


