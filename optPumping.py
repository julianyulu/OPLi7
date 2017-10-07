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
# Last-Updated: Sat Oct  7 14:24:08 2017 (-0500)
#           By: yulu
#     Update #: 325
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

        # Initialize transition frequency
        # ---------------------------------------------------------------------------
        self.freq = TransStrength.freq

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
        print("factor : ", self.dipoleFactor)
                
    def dipoleScaleFactor(self):
        """
        Calculate the overall scale factor which leads to:
        Gamma = w^3/(3*pi*e0*hBar*c^3) * sum(all transition matrix squared) * scale factor
        Returned factor is for Metcalf yellow book, Ueg^2
        """
        from Constant import hBar, e0, gamma,c
        totTransElement  = 0 
        for trans in self.decayMatrix.transition:
            for pol in self.decayMatrix.polarization:
                totTransElement = totTransElement + \
                                  eval('self.decayMatrix.' + pol + '.' + trans + '.sum()');
        einsteinAFactor = (2 * np.pi * self.freq)**3 / (3 * np.pi * e0 * hBar * c**3)
        
        factor  = gamma / (einsteinAFactor * totTransElement)
        return factor 

    
    def reduceMatrix(self,mtx): 
        """
        Accumulate matrix columns to rows, e.g. 
        after apply to shape = (3,4) matrix, it becomes (3, 1) matrix 
        """
        return mtx.sum(axis = 1)

    def einsteinA(self, trans):
        """
        Calculate Einstein A coefficient based on Ueg^2
        """
        from Constant import hBar, e0, gamma,c
        einsteinAFactor = (2 * np.pi * self.freq)**3 / (3 * np.pi * e0 * hBar * c**3)
        return einsteinAFactor * (trans * self.dipoleFactor)

    def omega(self, trans, I):
        from Constant import h, e0, c
        Ueg = np.sqrt(trans * self.dipoleFactor)
        return Ueg * np.sqrt(2 * I /( e0 * c)) / h
            
    def calGroundPop(self, popGround, popExcited, idx, I1, I2, detune1, detune2, dt):
        G1 = popGround['F1'][idx]
        G2 = popGround['F2'][idx]
        newG1 = np.zeros([1, len(G1[0])])
        newG2 = np.zeros([1, len(G2[0])])
        from Constant import gamma
        detuneFactor1 = gamma / 2 / ((gamma / 2)**2 + detune1**2)
        detuneFactor1 = gamma / 2 / ((gamma / 2)**2 + detune2**2)
        for es in self.eStates:
            
            newG1 += -self.reduceMatrix(self.omega(eval("self.pumpMatrix1.F1_" + self.Dline + "_" + es), I1)**2/2).T * detuneFactor1 * G1 \
                     + np.dot(popExcited[es][idx],  self.einsteinA(eval("self.decayMatrix.sigmaPlus." + es + "_" + self.Dline + "_F1"))) \
                     + np.dot(popExcited[es][idx], self.einsteinA(eval("self.decayMatrix.sigmaMinus." + es + "_" + self.Dline + "_F1")))\
                     + np.dot(popExcited[es][idx], self.einsteinA(eval("self.decayMatrix.pi." + es + "_" + self.Dline + "_F1")))
            newG2 += -self.reduceMatrix(self.omega(eval("self.pumpMatrix1.F2_" + self.Dline + "_" + es), I2)**2 / 2).T * detuneFactor1 * G2 \
                     + np.dot(popExcited[es][idx], self.einsteinA(eval("self.decayMatrix.sigmaPlus." + es + "_" + self.Dline + "_F2")))\
                     + np.dot(popExcited[es][idx], self.einsteinA(eval("self.decayMatrix.sigmaMinus." + es + "_" + self.Dline + "_F2")))\
                     + np.dot(popExcited[es][idx], self.einsteinA(eval("self.decayMatrix.pi." + es + "_" + self.Dline + "_F2")))
        newG1 = G1 + newG1 * dt  
        newG2 = G2 + newG2 * dt
        pop = {'F1': newG1,\
               'F2': newG2}
        return pop

    def calExcitedPop(self, popGround, popExcited, idx, I1, I2, detune1, detune2, dt):
        from Constant import gamma
        newE = {}
        for es in self.eStates: # loop thru excited states names
            newE[es] = np.zeros([1, len(popExcited[es][idx][0])])
        for p in self.pol:
            for gs,I, detune, pumpMatrix in zip(['F1', 'F2'], [I1, I2], [detune1, detune2], [self.pumpMatrix1, self.pumpMatrix2]):
                detuneFactor = gamma / 2 / ((gamma / 2)**2 + detune**2)
                for es in self.eStates: # loop thru excited hyperfine states names 
                # 3.0 factor is to compensate repeating sum of polarization
                    newE[es] += np.dot(popGround[gs][idx], self.omega(eval("pumpMatrix." + gs + "_" + self.Dline + "_" + es), I)**2 /2 ) / 3.0 * detuneFactor\
                            - self.reduceMatrix(self.einsteinA(eval("self.decayMatrix." + p + "." + es + "_" + self.Dline + "_" + gs))).T * popExcited[es][idx]
        for es in self.eStates:
            newE[es] = popExcited[es][idx] + newE[es] * dt
        return newE
                
    
    
    def checkUniformity(self, popGround,  popExcited):
        return popGround['F1'].sum() + popGround['F2'].sum() + sum([popExcited[str(x)].sum() for x in popExcited])
    
