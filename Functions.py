# Functions.py --- 
# 
# Filename: Functions.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sun Sep 17 16:36:41 2017 (-0500)
# Version: 
# Last-Updated: Tue Sep 19 18:36:44 2017 (-0500)
#           By: superlu
#     Update #: 109
# 


#from Constant import *    
#from TransitionStrength import *
import numpy as np 
class optPumping:
    groundF1Pop = np.array([0, 0, 0])
    groundF2Pop = np.array([0, 0, 0, 0, 0])
    excitedF0Pop = np.array([0])
    excitedF1Pop = np.array([0, 0, 0])
    excitedF2Pop = np.array([0, 0, 0, 0, 0])
    excitedF3Pop = np.array([0, 0, 0, 0, 0, 0, 0])
    
    def __init__(self, TransStrength, DecayStrength, pumpPol):

        # Initialize pump matrix 
        try:
            self.pumpMatrix = eval('TransStrength.' + pumpPol) # select pumping matrix based on polarization
        except AttributeError:
            print("Incorrect polorization name, please chose one of the following:\n\
            sigmaPlus; sigmaMinux, pi\n")

        # Initialize decay matrix
        self.decayMatrix = DecayStrength
        
        # Initialize polarization list
        self.pol = TransStrength.polarization
                
        # Transition energy levels 
        self.pumpTransLevel = TransStrength.transition
        self.decayTransLevel = DecayStrength.transition
        
        # Initialize ground level population
        l1 = len(self.groundF1Pop)
        l2 = len(self.groundF2Pop)
        for i in range(l1):
            self.groundF1Pop[i] = 0.5 / l1
        for i in range(l2):
            self.groundF2Pop[i] = 0.5 / l2

        # Calculate overal factor for dipole matrix
        self.dipoleFactor = self.dipoleScaleFactor()

        
    def dipoleScaleFactor(self): # For D2 line only at this moment
        totTransElement  = 0 # For Li D2, should be 960, use for unit test 
        for trans in self.decayMatrix.transition:
            for pol in self.decayMatrix.polarization:
                totTransElement = totTransElement + \
                                  eval('self.decayMatrix.' + pol + '.' + trans + '.sum()');
        from Constant import gamma 
        factor  = gamma / totTransElement
        return factor

    
    def vectorizeMatrix(self,mtx): # accumulate matrix columns to rows 
        return mtx.sum(axis = 1)

    def calGroundPop(self, G1,G2, E0, E1, E2, E3, dt):
        newG1 = G1
        newG2 = G2 
        for i in range(0, 4):
            newG1 += - np.dot(self.vectorizeMatrix(eval("self.pumpMatrix.F1_D2_F" + str(i))).T,  G1)
                     #+ np.dot(eval('E' + str(i)), eval("self.decayMatrix.sigmaPlus.F" + str(i)+ "_D2_F1"))\
                     #+ np.dot(eval('E' + str(i)), eval("self.decayMatrix.sigmaMinus.F" + str(i)+ "_D2_F1"))\
                     #+ np.dot(eval('E' + str(i)), eval("self.decayMatrix.pi.F" + str(i)+ "_D2_F1"))
            print(newG1)
            newG2 += - self.vectorizeMatrix(eval("self.pumpMatrix.F2_D2_F" + str(i))).T * G2\
                     + eval('E' + str(i)) * eval("self.decayMatrix.sigmaPlus.F" + str(i)+ "_D2_F2")\
                     + eval('E' + str(i)) * eval("self.decayMatrix.sigmaMinus.F" + str(i)+ "_D2_F2")\
                     + eval('E' + str(i)) * eval("self.decayMatrix.pi.F" + str(i)+ "_D2_F2")
        
        newG1 = newG1 * self.dipoleFactor * dt
        newG2 = newG2 * self.dipoleFactor * dt
        return (G1, G2)

    def calExcietedPop(self, G1, G2, E0, E1, E2, E3, dt):
        newE0 = newE1 = newE2 = newE3 = newE4 = 0
        
        for p in self.pol: # Loop thru polarization
            for g in range(1, 3): # Loop thru ground state
                 # pump from ground states to E0 -  decay to ground states from E0
                newE0  += eval("G" + str(g)) * eval("self.pumpMatrix." + p + ".F" + str(g) + "_D2_F0")\
                          - self.vectorizeMatrix(eval("self.decayMatrix." + p + ".F0_D2_F" + str(g))).T * E0 
                newE1  += eval("G" + str(g)) * eval("self.pumpMatrix." + p + ".F" + str(g) + "_D2_F1")\
                          - self.vectorizeMatrix(eval("self.decayMatrix." + p + ".F1_D2_F" + str(g))).T * E1 
                newE2  += eval("G" + str(g)) * eval("self.pumpMatrix." + p + ".F" + str(g) + "_D2_F2")\
                          - self.vectorizeMatrix(eval("self.decayMatrix." + p + ".F2_D2_F" + str(g))).T * E2
                newE3  += eval("G" + str(g)) * eval("self.pumpMatrix." + p + ".F" + str(g) + "_D2_F3")\
                          - self.vectorizeMatrix(eval("self.decayMatrix." + p + ".F3_D2_F" + str(g))).T * E3
        newE0 = E0 + newE0 * self.dipoleFactor * dt
        newE1 = E1 + newE1 * self.dipoleFactor * dt
        newE2 = E2 + newE2 * self.dipoleFactor * dt
        newE3 = E3 + newE3 * self.dipoleFactor * dt
        return(newE0, newE1, newE2, newE3)
    
    
        
        

    
        
    
