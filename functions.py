# functions.py --- 
# 
# Filename: functions.py
# Description: 
#            Functions for post-simulation analysis
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Mon Oct  9 10:16:45 2017 (-0500)
# Version: 
# Last-Updated: Mon Oct  9 13:56:48 2017 (-0500)
#           By: superlu
#     Update #: 56
# 


from optPumping import optPumping
from Constant import input
import numpy as np

def runSimu(Dline,
         excited_hpf_state,
         I1,
         I2,
         detune1,
         detune2,
         polorization1,
         polorization2,
         totalTime,
         dt):
        

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
    clock = np.linspace(0, totalTime, numSteps) # in seconds 
    return (clock, popG, popE)


def findSteadyState(clock, popGround, popExcited):
    """
    Find the time for optical pumping to reach 
    steady states and correspongding population 
    for each ground and excited hpf states
    """

    try:
        states = popExcited['F1']
    except KeyError:
        states = popExcited['F2']

    states = popGround['F2']
    steadyIdx = 0
    for i in range(len(clock)):
        
        if i <10:
            pass
        else:
            if (abs(np.average(states[i-5:i]) - np.average(states[i:i+5])) < 1e-6).all():
               steadyIdx = i
               break
           
    steadyG = {}
    steadyE = {}
    for key in popExcited:
        steadyE[key] = popExcited[key][steadyIdx]
    for key in popGround:
        steadyG[key] = popGround[key][steadyIdx]
        
    return clock[steadyIdx], steadyG, steadyE

    
