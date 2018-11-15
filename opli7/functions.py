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
# Last-Updated: Wed Nov 14 23:26:45 2018 (-0600)
#           By: yulu
#     Update #: 276
# 


from optPumping import OptPumping
import numpy as np

def readInput(infile):
    """
    read input from a file as a dictionary
    """
    params = {}
    # if it is a sys.stdin input 
    if str(type(infile)) == "<class '_io.TextIOWrapper'>":
        for line in infile:
            x = line.rstrip().split(':')
            try:
                params[x[0].strip()] = float(x[1].split('#')[0].strip())
            except ValueError:
                params[x[0].strip()] = x[1].split('#')[0].strip()
    # else read from a input file 
    else:
        with open(infile, 'r') as f:
            for line in f:
                x = line.rstrip().split(':')
                try:
                    params[x[0].strip()] = float(x[1].split('#')[0].strip())
                except ValueError:
                    params[x[0].strip()] = x[1].split('#')[0].strip()
    return params


def runSimu(Dline,
         excited_hpf_state,
         I1,
         I2,
         detune1,
         detune2,
         polarization1,
         polarization2,
         maxSimulationTime,
         dt):
        
    
    p = OptPumping(Dline, excited_hpf_state, polarization1, polarization2)
    I1 = I1 * 10 # Convert mW/cm^2 to W/m^2
    I2 = I2 * 10 
    # Initialization of population dictionary 
    popG = {} # Ground states population dictionary, dic of list of 2d array
    popE = {} # Excited states population dictionary, dic of list of 2d array

    numSteps = int(maxSimulationTime / dt)

    
    autoStop = True
    steadyIdx = 0
    breakIdx = 0

    for i in range(numSteps):
        
        if i == 0:
            # Initial states
            popG['F1'] = [p.pop_Ground['F1']]
            popG['F2'] = [p.pop_Ground['F2']]
            for f in p.eStates:
                popE[f] = [p.pop_Excited[f]]
            sumE = popG['F2'][0].sum()
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

            # Check if steady state reached, then auto break loop
            if autoStop and i > 10:
                if (abs(popG['F2'][i - 5] - popG['F2'][i])  <  1000 * dt).all():
                    steadyIdx = i
                    breakIdx = steadyIdx + int(5e-6 / dt)
                    autoStop = False
                else:
                    pass

            if i == breakIdx:
                print('\n[*] Steady state reached ! Auto stop ...')
                autoStop = True
                break
    clock = np.linspace(0, dt * breakIdx, breakIdx+1) if breakIdx else np.linspace(0, maxSimulationTime, numSteps) # in seconds 
    return (clock, popG, popE, steadyIdx)

def nicePrintStates(pop):
    fState = list(pop.keys())
    for f in fState:
        print("\nhpf state:", f)
        print("====================")
        for i,p in enumerate(pop[f][0]):
            mF = -int(f[-1]) + i
            print("mF = {0:1d}{1:10.4f}".format(mF, p))
        print("\n")

