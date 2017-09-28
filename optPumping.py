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
# Last-Updated: Wed Sep 27 23:50:28 2017 (-0500)
#           By: yulu
#     Update #: 231
# 


#from Constant import *    
#from TransitionStrength import *
import numpy as np 
class optPumping:
    
    
    def __init__(self, Dline,  pumpPol1, pumpPol2):
        
        if self.Dline == 'D1':
            from TransitionStrength import TransStrengthD1 as TransStrength
            from TransitionStrength import DecayStrengthD1 as DecayStrength
        elif self.Dline == 'D2':
            from TransitionStrength import TransStrengthD2 as TransStrength
            from TransitionStrength import DecayStrengthD2 as DecayStrength
        else:
            print('Unavaliable D line transition !')
        # Initialize pump matrix 
        try:
            self.pumpMatrix1 = eval('TransStrength.' + pumpPol1) # select pumping matrix based on polarization
            self.pumpMatrix2 = eval('TransStrength.' + pumpPol2) # select pumping matrix based on polarization
        except AttributeError:
            print("Incorrect polorization name, please chose one of the following:\n\
            sigmaPlus, sigmaMinux, pi\n")

        # Initialize pump beam polorization
        self.pumpPol1 = pumpPol1 # Polorization for pumping beam F1 --> Excited states
        self.pumpPol2 = pumpPol2 # Polorization for pumping beam F2 --> Excited states

        # Initialize decay matrix
        self.decayMatrix = DecayStrength # 
        
        # Initialize polarization list
        self.pol = TransStrength.polarization

        # Initialize D line
        self.Dline = Dline
        
        # Number of excited hyperfine states F
        self.numEStates = len(DecayStrength.numSubStates)

        # Excited hyperfine states name
        self.eStates = TransStrength.eStates
        
        # Transition energy levels 
        self.pumpTransLevel = TransStrength.transition
        self.decayTransLevel = DecayStrength.transition
        
        # Initialize ground level population
        self.pop_Ground ={
            'F1': np.ones([1,3]) * 3./8
            'F2': np.ones([1,5]) * 5./8
            }

        # Initialize excited level population
        self.pop_Excited = {}
        for s,n in zip(self.DecayStrength.eStates, self.DecayStrength.numSubStates):
            self.pop_Excited{s:np.zeros([1, n])}
        
        # Calculate overal factor for dipole matrix
        self.dipoleFactor = self.dipoleScaleFactor()

        # Calculate atom-light scattering rate
        
        
    def dipoleScaleFactor(self): 
        totTransElement  = 0 # For Li D2, should be 37393.75, use for unit test 
        for trans in self.decayMatrix.transition:
            for pol in self.decayMatrix.polarization:
                totTransElement = totTransElement + \
                                  eval('self.decayMatrix.' + pol + '.' + trans + '.sum()');
        from Constant import gamma 
        factor  = gamma / totTransElement
        return factor

    
    def vectorizeMatrix(self,mtx): # accumulate matrix columns to rows 
        return mtx.sum(axis = 1)

    
    def calGroundPop(self, popGround, popExcited, I1, I2, dt):
        G1 = popGround['F1']
        G2 = popGround['F2']
        newG1 = np.zeros([1, len(G1[0])])
        newG2 = np.zeros([1, len(G2[0])])
        for es in self.eStates:
            newG1 += -self.vectorizeMatrix(eval("self.pumpMatrix1.F1_D2_" + es)).T * G1 * I1\
                     + np.dot(popExcited[es], eval("self.decayMatrix.sigmaPlus." + es + "_" + self.Dline + "_F1"))\
                     + np.dot(popExcited[es], eval("self.decayMatrix.sigmaMinus." + es + "_" + self.Dline + "_F1"))\
                     + np.dot(popExcited[es], eval("self.decayMatrix.pi." + es + "_" + self.Dline + "_F1"))
            newG2 += -self.vectorizeMatrix(eval("self.pumpMatrix1.F1_D2_" + es)).T * G2 * I2\
                     + np.dot(popExcited[es], eval("self.decayMatrix.sigmaPlus." + es + "_" + self.Dline + "_F2"))\
                     + np.dot(popExcited[es], eval("self.decayMatrix.sigmaMinus." + es + "_" + self.Dline + "_F2"))\
                     + np.dot(popExcited[es], eval("self.decayMatrix.pi." + es + "_" + self.Dline + "_F2"))
            
        newG1 = G1 + newG1 * self.dipoleFactor * dt  
        newG2 = G2 + newG2 * self.dipoleFactor * dt
        return (newG1, newG2)

    def calExcitedPop(self, popGround, popExcited, I1, I2, dt):
        newE = {}
        for es in self.eStates: # loop thru excited states names
            newE[es] = np.zeros([1, len(popExcited[es])])
        for p in self.pol:
            for gs,I, pumpMatrix in zip(['F1', 'F2'], [I1, I2], [self.pumpMatrix1, self.pumpMatrix2]):
                for es in self.eStates: # loop thru excited hyperfine states names 
                # 3.0 factor is to compensate repeating sum of polarization
                newE[es] += np.dot(popGround[gs], eval("pumpMatrix." + gs + "_" + self.Dline + "_" + es)) / 3.0 * I\
                            - self.vectorizeMatrix(eval("self.decayMatrix." + p + "." + es + "_" + self.Dline + "_" + gs)).T * popExcited[es]
        for es in self.eStates:
            newE[es] = popExcited[es] + newE[es] * self.dipoleFactor * dt
        return newE
                
    
    
    def checkUniformity(self, popGround, popExcited):
        
        return popGround['F1'].sum() + popGround['F2'] + sum[popExcited[str(x)].sum() for x in popExcited]
    
