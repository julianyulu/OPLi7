# repeatPaperResult.py --- 
# 
# Filename: repeatPaperResult.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sun Oct 15 23:29:34 2017 (-0500)
# Version: 
# Last-Updated: Sun Oct 15 23:51:19 2017 (-0500)
#           By: yulu
#     Update #: 6
# 


from optPumping import optPumping
import numpy as np
import sys


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

    numSteps = int(maxSimulationTime / dt)

    
    autoStop = False
    steadyIdx = 0
    breakIdx = 0

    I10 = I1 * 10 # Convert mW/cm^2 to W/m^2
    I20 = I2 * 10 
    for i in range(numSteps):
        
        t = i * dt * 1e6
        I1 = I10 * np.exp(-2 * ((t - 20) /5)**2)
        I2 = I20 * np.exp(-2 * ((t - 20) /5)**2)
        
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


def plotPop_special( clock,  Dline, eStates, polarization1, polarization2, I1, I2, popG, popE, saveFig = True):
    """
    plot population distrubution for ground and excited states
    and specify condition in the title 
    optionally save the figure to ./img/ folder
    """
    import matplotlib.pyplot as plt
    import os
    
    excitedState = '2P3halves(unresolved)' if Dline == 'D2' else eStates[0]
    lw = 3
    
    fig = plt.figure(figsize = (15, 15), dpi = 150)
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    
    for f in ['F1', 'F2']:# Ground states
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax1.plot(clock * 1e6, [x[0][i] for x in popG[f]], "-", \
                     label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    ax1.set_title('Li7 ' +  Dline + ' transition ground(top) and excited(bottom)  hpf states population\n' \
                  + 'F1 -> ' + excitedState + ': ' + polarization1 + ' pol.  ' + str(I1) + ' mW/cm2 || ' \
                  + 'F2 -> ' + excitedState + ': ' + polarization2 + ' pol.  ' + str(I2) + ' mW/cm2', fontsize = 15)
    ax1.set_xlabel('Time [us]')
    ax1.set_ylim([0, 0.2])
    ax1.set_xlim([0, 20])
    ax1.legend(fontsize = 12)

    
    for f in list(popE.keys()):#p.eStates:
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax2.plot(clock * 1e6, [x[0][i] for x in popE[f]], "-",\
                     label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    ax2.set_xlabel('Time [us]')
    ax2.legend(fontsize = 12)

    if saveFig:
        if not os.path.isdir("./img/"):
            os.mkdir("img")
        fileName = "./img/repeatPaper.png"
        fig.savefig(fileName)
        print("[*]plots saved in " + fileName)
    plt.show()    




def main(inFile):
    """
    Run single fix parameter simultion
    simulation parameters should be specified in singleRun.in
    Usually takes about half minute, be patient
    plots will be generated by the end
    """
    
    # load input parameters 
    inputParams = readInput(inFile)
    
    clock, popG, popE, steadyIdx  = runSimu(**inputParams)
    
    params = {
        "clock": clock,
        "Dline":inputParams.get('Dline'),
        "eStates": [inputParams.get('excited_hpf_state')],
        "polarization1": inputParams.get('polarization1'),
        "polarization2": inputParams.get('polarization2'),
        "I1": inputParams.get('I1'),
        "I2": inputParams.get('I2'),
        "popG": popG,
        "popE": popE,
        "saveFig": True}

    
    if steadyIdx:
        print("\nTime for reaching steady state: {:2.2f} us\n".format(clock[steadyIdx] * 1e6))
        steadyG = {'F1': popG['F1'][steadyIdx],
                   'F2': popG['F2'][steadyIdx]}
        nicePrintStates(steadyG)
    else:
        print("\nNo steady state reached, extend the simulation time\nif you want to see it saturates\n")

    plotPop_special(**params)
    

if __name__ == '__main__':
    main(sys.stdin)
