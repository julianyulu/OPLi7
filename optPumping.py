# optPumping.py --- 
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
# Last-Updated: Mon Oct  2 22:53:32 2017 (-0500)
#           By: yulu
#     Update #: 290
# 

import numpy as np


class optPumping:
    def __init__(self, Dline, excitedF, pumpPol1, pumpPol2):

        # Load D line transition database
        # ---------------------------------------------------------------------------
        if Dline == 'D1':
            if excitedF == 'F1':
                from TransitionStrength import TransStrengthD1_toF1 as TransStrength
                from TransitionStrength import DecayStrengthD1_toF1 as DecayStrength
            elif excitedF == 'F2':
                from TransitionStrength import TransStrengthD1_toF2 as TransStrength
                from TransitionStrength import DecayStrengthD1_toF2 as DecayStrength
        elif Dline == 'D2':
            from TransitionStrength import TransStrengthD2 as TransStrength
            from TransitionStrength import DecayStrengthD2 as DecayStrength
        else:
            print('Unavaliable D line transition !')

        # Initialize pumping matrix based on polarization
        # ---------------------------------------------------------------------------
        try:
            self.pumpMatrix1 = eval('TransStrength.' + pumpPol1) 
            self.pumpMatrix2 = eval('TransStrength.' + pumpPol2) 
        except AttributeError:
            print("Incorrect polorization name, please chose one of the following:\n\
            sigmaPlus, sigmaMinux, pi\n")

        # Initialize decay matrix
        # ---------------------------------------------------------------------------
        self.decayMatrix = DecayStrength 

        
        # Initialize pump beam polorization
        # ---------------------------------------------------------------------------
        self.pumpPol1 = pumpPol1 # Polorization for pumping beam F1 --> Excited states
        self.pumpPol2 = pumpPol2 # Polorization for pumping beam F2 --> Excited states
        
        # Initialize possible polarization list
        # ---------------------------------------------------------------------------
        self.pol = TransStrength.polarization

        # Initialize D line value
        # ---------------------------------------------------------------------------
        self.Dline = Dline
        
        # Initialize number of excited hyperfine magnetic substates F
        # ---------------------------------------------------------------------------
        self.numEStates = len(DecayStrength.numSubStates)

        # Initialize excited hyperfine states name
        # ---------------------------------------------------------------------------
        self.eStates = TransStrength.eStates
        
        # Initialize ground level population
        # ---------------------------------------------------------------------------
        self.pop_Ground ={
            'F1': np.ones([1,3]) * 1./8,
            'F2': np.ones([1,5]) * 1./8
            }

        # Initialize excited level population
        # ---------------------------------------------------------------------------
        self.pop_Excited = {}
        for s,n in zip(DecayStrength.eStates, DecayStrength.numSubStates):
            self.pop_Excited[s] = np.zeros([1, n])
        
        # Calculate overall factor for dipole matrix normalization
        # ---------------------------------------------------------------------------
        self.dipoleFactor = self.dipoleScaleFactor()

                
    def dipoleScaleFactor(self):
        """
        Calculate the overall scale factor which leads to:
        Gamma = sum(all transition matrix squared) * scale factor
        """
        totTransElement  = 0 
        for trans in self.decayMatrix.transition:
            for pol in self.decayMatrix.polarization:
                totTransElement = totTransElement + \
                                  eval('self.decayMatrix.' + pol + '.' + trans + '.sum()');
        from Constant import gamma 
        factor  = gamma / totTransElement
        return factor

    
    def vectorizeMatrix(self,mtx): 
        """
        Accumulate matrix columns to rows, e.g. 
        after apply to shape = (3,4) matrix, it becomes (3, 1) matrix 
        """
        return mtx.sum(axis = 1)

    
    def calGroundPop(self, popGround, popExcited, idx, I1, I2, dt):
        G1 = popGround['F1'][idx]
        G2 = popGround['F2'][idx]
        newG1 = np.zeros([1, len(G1[0])])
        newG2 = np.zeros([1, len(G2[0])])
        
        for es in self.eStates:
            newG1 += -self.vectorizeMatrix(eval("self.pumpMatrix1.F1_" + self.Dline + "_" + es)).T * G1 * I1\
                     + np.dot(popExcited[es][idx], eval("self.decayMatrix.sigmaPlus." + es + "_" + self.Dline + "_F1"))\
                     + np.dot(popExcited[es][idx], eval("self.decayMatrix.sigmaMinus." + es + "_" + self.Dline + "_F1"))\
                     + np.dot(popExcited[es][idx], eval("self.decayMatrix.pi." + es + "_" + self.Dline + "_F1"))
            newG2 += -self.vectorizeMatrix(eval("self.pumpMatrix1.F2_" + self.Dline + "_" + es)).T * G2 * I2\
                     + np.dot(popExcited[es][idx], eval("self.decayMatrix.sigmaPlus." + es + "_" + self.Dline + "_F2"))\
                     + np.dot(popExcited[es][idx], eval("self.decayMatrix.sigmaMinus." + es + "_" + self.Dline + "_F2"))\
                     + np.dot(popExcited[es][idx], eval("self.decayMatrix.pi." + es + "_" + self.Dline + "_F2"))
        newG1 = G1 + newG1 * self.dipoleFactor * dt  
        newG2 = G2 + newG2 * self.dipoleFactor * dt
        pop = {'F1': newG1,\
               'F2': newG2}
        return pop

    def calExcitedPop(self, popGround, popExcited, idx, I1, I2, dt):
        newE = {}
        for es in self.eStates: # loop thru excited states names
            newE[es] = np.zeros([1, len(popExcited[es][idx][0])])
        for p in self.pol:
            for gs,I, pumpMatrix in zip(['F1', 'F2'], [I1, I2], [self.pumpMatrix1, self.pumpMatrix2]):
                for es in self.eStates: # loop thru excited hyperfine states names 
                # 3.0 factor is to compensate repeating sum of polarization
                    newE[es] += np.dot(popGround[gs][idx], eval("pumpMatrix." + gs + "_" + self.Dline + "_" + es)) / 3.0 * I\
                            - self.vectorizeMatrix(eval("self.decayMatrix." + p + "." + es + "_" + self.Dline + "_" + gs)).T * popExcited[es][idx]
        for es in self.eStates:
            newE[es] = popExcited[es][idx] + newE[es] * self.dipoleFactor * dt
        return newE
                
    
    
    def checkUniformity(self, popGround,  popExcited):
        return popGround['F1'].sum() + popGround['F2'].sum() + sum([popExcited[str(x)].sum() for x in popExcited])
    
