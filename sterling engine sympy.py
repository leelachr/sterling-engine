# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:10:38 2016

@author: Leela
"""
from sympy import *

# names are prefixed by their pysical type, i.e. 
# length (len), temperature (T), pressure (P), mass (m),
# velocity (vel), acceleration (acc), volume (vol),
# molar volume (mvol), position (x) (it has the same
# units as length, but position and length are different
# properties.), time (t), area (area), density (rho)...

# units used in internal calculation are SI with 
# bar and degree C.

# ------------------------------------------------------------
# DATA DEFINITIONS
# ------------------------------------------------------------
# a System is a set of symbolic equations and knowns. 
# it must have the property that the number of symbols
# equals the number of equations plus knowns.

# a State is a dictionary with each entry matching a
# Symbol to a Position, Velocity, and Acceleration.

# a Motion is an Object:
class Motion(object): 
    def __init__(self, pos=None, vel=None, acc=None):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        
# sample data: 
sampleState = {"tennisball": Motion(1,2,0), "curlingstone": Motion(3,1,-0.5)}

# ------------------------------------------------------------
# THE ENGINE SPECS
# ------------------------------------------------------------
# universal constants:
Rgas = 8.314 # Joule/kg-K
pi = 3.1415

# initial conditions
# initial charge of moles of gas in either the left or right
# half of the engine.
molesInitHalf = 1 

xPistInit = 0.5
velPistInit = 0

# engine specs:
Thot = 80
Tcold = 5
lenEngine = 1
lenEngRadius = 0.2
lenDisp = 0.25
lenPist = 0.05
mSep = 0.2
rhoPist = 1
areaCrossSec = pi * lenEngRadius ** 2
mPiston = rhoPist * areaCrossSec * lenPist
volSep = 0.8 

V1, V2, V3, V4 = symbols("V1 V2 V3 V4")

PLeft, PRight, xDispLeft, xDispRight, xPist = \
    symbols("PLeft PRight xDispLeft xDispRight xPist")
    
V1 = areaCrossSec * (xDispLeft - 0.5 * lenDisp) #f(xDispLeft)
V2 = areaCrossSec * (xPist - 0.5 * lenPist - lenDisp) - V1 #f(xDispLeft, xPiston)
V3 = areaCrossSec * (xDispRight - 0.5 * lenDisp - lenPist - lenDisp) #f(xDispRight, xPiston)
V4 = areaCrossSec * (lenEngine - xDispRight - 0.5 * lenDisp) #f(xDispRight)
    
PLeft = molesInit * Rgas / (V1/Tcold + V2/Thot)

PRight = molesInit * Rgas / (V3/Thot + V4/Tcold)

forceFriction, forceDisplacer, forcePressures, accPiston = \
            symbols("forceFriction forceDisplacer forcePressures accPiston")

forceFriction = 0

forceDisplacer = 0

forcePressures = areaCrossSec * (PLeft - PRight)

eqPistonForceBalance = Eq(forceFriction + forceDisplacer + forcePressures \
        - mPiston * accPiston, 0)

result = solve(eqPistonForceBalance, accPiston)

# ------------------------------------------------------------
# FUNCTIONS/SOLVER
# ------------------------------------------------------------

# String Any -> Bool
# interprets second argument according to keyword argument.
def stopCriterion(keywd, value):
    if keywd == "checkAccelNearZero":
        return checkAccelNearZero(value)
    elif keywd == "checkNearWall":
        return checkNearWall(value)
    else:
        "ERROR ..."
    
# Acceleration -> Bool
def checkAccelNearZero(acc):
    epsilon = 1
    return acc <= epsilon
    
# Position -> Bool
def checkNearWall(pos):
    pass

# State Time -> State
def step(state, dt):
    newPos = state.pos + state.vel * dt + state.acc * dt ** 2
    newState = {}
    return newState

# Equation ? Time Time [String Any -> Bool] -> List-of-Posns List-of-Accelerations
# what should init be? perhaps a Dict ?? init is a list of posns and accelerations... seems like i need a data type...
# or maybe it could be an input called a System.
def integrator(eq, initConds, endTime, timeStep, stopCriterion):
    posns = init. ...
    accs = init. ...
    while stopCriterion(posns, accs) == False:
        newposns, newaccs = step(posns, accs)        
        #posns, accs = forceBalance(eq, etc)
    return newposns, newaccs
    

# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
    




