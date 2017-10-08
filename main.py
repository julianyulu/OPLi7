# main.py --- 
# 
# Filename: main.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Wed Sep 20 15:34:21 2017 (-0500)
# Version: 
# Last-Updated: Sat Oct  7 21:55:13 2017 (-0500)
#           By: yulu
#     Update #: 252
# 


from optPumping import optPumping
from Constant import input
import numpy as np
from plot import plotPop

def main(Dline,
         excited_hpf_state,
         I1,
         I2,
         detune1,
         detune2,
         polorization1,
         polorization2,
         totalTime,
         dt,
         plot = True):

    p = optPumping(Dline, excited_hpf_state, polorization1, polorization2)
    I1 = I1 * 10 # Convert mW/cm^2 to W/m^2
    I2 = I2 * 10 
    # Initialization of population dictionary 
    popG = {} # Ground states population dictionary, dic of list of 2d array
    popE = {} # Excited states population dictionary, dic of list of 2d array
    numSteps = int(totalTime / dt)
    
    for i in range(0, numSteps):
        if i == 0:
            # Initial states
            popG['F1'] = [p.pop_Ground['F1']]
            popG['F2'] = [p.pop_Ground['F2']]
            for f in p.eStates:
                popE[f] = [p.pop_Excited[f]]
        else:
            newPopG = p.calGroundPop(popG, popE, i-1, I1, I2, detune1, detune2, dt)
            newPopE = p.calExcitedPop(popG, popE, i-1, I1, I2, detune1, detune2, dt)
            for f in p.eStates:
                popE[f].append(newPopE[f])
            popG['F1'].append(newPopG['F1'])
            popG['F2'].append(newPopG['F2'])
            unitCheck = p.checkUniformity(newPopG, newPopE)
            if abs( unitCheck- 1) > 0.1:
                print("Total population: ", unitCheck, " off too much, cycle: ", i)
                return 0 
    clock = np.linspace(0, totalTime, numSteps) * 1e6 # [us]

    print(
        '--------------------------------------------------\n',\
        'F = 1, m = -1, pop =', popG['F1'][-1][0][0], '\n',\
        'F = 1, m = -0, pop =', popG['F1'][-1][0][1], '\n',\
        'F = 1, m = 1, pop =', popG['F1'][-1][0][2], '\n',\
        'F = 2, m = -2, pop =', popG['F2'][-1][0][0], '\n',\
        'F = 2, m = -1, pop =', popG['F2'][-1][0][1], '\n',\
        'F = 2, m = 0, pop =', popG['F2'][-1][0][2], '\n',\
        'F = 2, m = 1, pop =', popG['F2'][-1][0][3], '\n',\
        'F = 2, m = 2, pop =', popG['F2'][-1][0][4], '\n')
        
    print("End simulation total population check: ", p.checkUniformity(popG, popE) )
    
    if plot:
        params = {
            "clock": clock,
            "Dline": Dline,
            "eStates": p.eStates,
            "polorization1": polorization1,
            "polorization2": polorization2,
            "I1": I1,
            "I2": I2,
            "popG": popG,
            "popE": popE,
            "saveFig": False
            }
        
        plotPop(**params)
       
if __name__ == "__main__":
    main(**input)
    
        
        
