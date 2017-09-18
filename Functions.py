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
# Last-Updated: Sun Sep 17 23:20:36 2017 (-0500)
#           By: yulu
#     Update #: 58
# 


#from Constant import *    
#from TransitionStrength import *

class optPumping:
    groundF1Pop = [0, 0, 0]
    groundF2Pop = [0, 0, 0, 0, 0]
    excitedF0Pop = [0]
    excitedF1Pop = [0, 0, 0]
    excitedF2Pop = [0, 0, 0, 0, 0]
    excitedF3Pop = [0, 0, 0, 0, 0, 0, 0]
    
    def __init__(self, TransStrength, DecayStrength, pumpPol):

        # Initialize pump matrix 
        try:
            self.pumpMatrix = eval('TransStrength.' + pumpPol)
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
        self.dipoleFactor = dipoleFactor(self.decayMatrix)

        
    def dipoleFactor(DecayStrength): # For D2 line only at this moment
        totTransElement  = 0 # For Li D2, should be 960, use for unit test 
        for trans in DecayStrength.transition:
            for pol in DecayStrength.polarization:
                totTransElement = totTransElement + \
                                  eval('DecayStrength.' + pol + '.' + trans + '.sum()');
        from Constant import gamma 
        factor  = gamma / totTransElement
        return factor

    
    def vectorizeMatrix(mtx): # accumulate matrix columns to rows 
        return mtx.sum(axis = 1)

    def calGroundPop(self, G1,G2, E0, E1, E2, E3, E4, dt):
        minus1 = minus2 = plus1 = plus2 = 0
        for i range(0, 4):
            # pump / decay factor for ground F1 (G1) level
            minus1 += vectorizeMatrix(eval("self.pumpMatrix.F1_D2_F" + i ))
            plus1 += eval('E' + i) * eval("self.decayMatrix.sigmaPlus.F" + i + "_D2_F1")
            # pump / decay factor for ground F2 (G2) level
            minus2 += vectorizeMatrix(eval("self.pumpMatrix.F2_D2_F" + i ))
            plus2 += eval('E' + i) * eval("self.decayMatrix.sigmaPlus.F" + i + "_D2_F2")
        newG1 = G1 + (- minus1.T * G1 + plus1) * self.dipoleFactor * dt
        newG2 = G2 + (- minus2.T * G2 + plus2) * self.dipoleFactor * dt
        return (G1, G2)

    
        
        

    
        
    
