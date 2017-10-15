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
# Last-Updated: Sun Oct 15 17:20:35 2017 (-0500)
#           By: yulu
#     Update #: 215
# 


from optPumping import optPumping
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
        
    
    p = optPumping(Dline, excited_hpf_state, polarization1, polarization2)
    I1 = I1 * 10 # Convert mW/cm^2 to W/m^2
    I2 = I2 * 10 
    # Initialization of population dictionary 
    popG = {} # Ground states population dictionary, dic of list of 2d array
    popE = {} # Excited states population dictionary, dic of list of 2d array
    #numSteps = int(100e-6/dt) if autoStop else int(maxSimulationTime / dt)
    numSteps = int(maxSimulationTime / dt)

    
    autoStop = True
    breakIdx = 0
    for i in range(numSteps):
        if i == 0:
            # Initial states
            popG['F1'] = [p.pop_Ground['F1']]
            popG['F2'] = [p.pop_Ground['F2']]
            for f in p.eStates:
                popE[f] = [p.pop_Excited[f]]
            maxF1 = popG['F1'][0][0]
            minF1 = popG['F1'][0][0]
            checkKey = list(popE.keys())[-1]
            maxE = popE[checkKey]
            minE = maxE
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
            if autoStop:
                changeIndicator = False
                if (newPopE[checkKey][0] > maxE).any():
                    maxE = np.array([max(x, y) for x, y in zip(maxE, newPopE[checkKey][0])])
                    changeIndicator = True
                elif (newPopE[checkKey][0] < minE).any():
                    minE = np.array([min(x, y) for x, y in zip(minE, newPopE[checkKey][0])])
                    changeIndicator = True
                else:
                    pass
                '''
                if (newPopG['F1'][0] > maxF1).any():
                    maxF1 = np.array([max(x, y) for x,y in zip(maxF1, newPopG['F1'][0])])
                    changeIndicator = True
                if (minF1 > 1e-6).any() and (newPopG['F1'][0] < minF1).any():
                    minF1 = np.array([min(x, y) for x,y in zip(minF1, newPopG['F1'][0])])
                    changeIndicator = True
                '''
                if not changeIndicator:
                    breakIdx = i + int(5e-6 / dt)
                    autoStop = False
            ###
            '''
            if autoStop and i > 10 and (abs(np.average(popG['F2'][i-10:i-5])- np.average(popG['F2'][i-5:i])) < 1e-6).all() :
                breakIdx = i - 5 + int(5e-6 / dt) # add extral 5 us to simulate 
                autoStop = False
            '''
            ### 
            if i == breakIdx:
                print('\n[*] Steady state reached ! Auto stop ...')
                autoStop = True
                break
    clock = np.linspace(0, dt * breakIdx, breakIdx+1) if breakIdx else np.linspace(0, maxSimulationTime, numSteps) # in seconds 
    return (clock, popG, popE)


def findSteadyState(clock, popGround, popExcited):
    """
    Find the time for optical pumping to reach 
    steady states and correspongding population 
    for each ground and excited hpf states
    """

    maxF1 = popGround['F1'][0][0]
    minF1 = popGround['F1'][0][0]
    
    steadyIdx = 0
    for i in range(1, len(clock)):
        
        update = False
        if (maxF1 < popGround['F1'][i][0]).any():
            maxF1 = np.array([max(x, y) for x, y in zip(maxF1, popGround['F1'][i][0])])
            update = True
        elif (minF1 > 1e-6).any() and  (minF1 > popGround['F1'][i][0]).any():
            minF1 = np.array([min(x, y) for x,y in zip(minF1, popGround['F1'][i][0])])
            update = True
        else:
            pass
        if not update:
            steadyIdx = i
            break
    steadyG = {}
    steadyE = {}
    for key in popExcited:
        steadyE[key] = popExcited[key][steadyIdx]
    for key in popGround:
        steadyG[key] = popGround[key][steadyIdx]
        
    return clock[steadyIdx], steadyG, steadyE

def nicePrintStates(pop):
    fState = list(pop.keys())
    for f in fState:
        print("\nhpf state:", f)
        print("====================")
        for i,p in enumerate(pop[f][0]):
            mF = -int(f[-1]) + i
            print("mF = {0:1d}{1:10.4f}".format(mF, p))
        print("\n")

