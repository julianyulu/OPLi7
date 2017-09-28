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
# Last-Updated: Thu Sep 28 18:50:32 2017 (-0500)
#           By: superlu
#     Update #: 188
# 


from optPumping import optPumping
#from TransitionStrength import TransStrength, DecayStrength
from Constant import dt, totalTime, polorization1, polorization2, I1, I2, Dline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from cycler import cycler

def main():
    global dt, totalTime, polorization1, polorization2, I1, I2
    p = optPumping(Dline,polorization1, polorization2)

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
            newPopG = p.calGroundPop(popG, popE, i-1, I1, I2, dt)
            newPopE = p.calExcitedPop(popG, popE, i-1, I1, I2, dt)
            for f in p.eStates:
                popE[f].append(newPopE[f])
            popG['F1'].append(newPopG['F1'])
            popG['F2'].append(newPopG['F2'])

            unitCheck = p.checkUniformity(newPopG, newPopE)
            if abs( unitCheck- 1) > 0.1:
                print("Total population: ", unitCheck, " off too much")
                return 0 
    clock = np.linspace(0, totalTime, numSteps) * 1e9

    
    #matplotlib.rcParams.update({
    #    'lines.markersize': 5
    #    })

    print(
        'F = 1, m = -1, pop =', popG['F1'][-1][0][0], '\n',\
        'F = 1, m = -0, pop =', popG['F1'][-1][0][1], '\n',\
        'F = 1, m = 1, pop =', popG['F1'][-1][0][2], '\n',\
        'F = 2, m = -2, pop =', popG['F2'][-1][0][0], '\n',\
        'F = 2, m = -1, pop =', popG['F2'][-1][0][1], '\n',\
        'F = 2, m = 0, pop =', popG['F2'][-1][0][2], '\n',\
        'F = 2, m = 1, pop =', popG['F2'][-1][0][3], '\n',\
        'F = 2, m = 2, pop =', popG['F2'][-1][0][4], '\n')
    print("Total population: ", p.checkUniformity(G1,G2,E0, E1, E2, E3) )
    lw = 3
    fig1 = plt.figure(1)
    ax1 = fig1.add_subplot(111)
    ax1.plot(clock, [x[0][0] for x in popG['F1']], "-", label = 'F = 1, m = -1', linewidth = lw)
    ax1.plot(clock, [x[0][1] for x in popG['F1']], "-", label = 'F = 1, m = 0', linewidth = lw)
    ax1.plot(clock, [x[0][2] for x in popG['F1']], "-", label = 'F = 1, m = 1', linewidth = lw)
    ax1.plot(clock, [x[0][0] for x in popG['F2']], "-", label = 'F = 2, m = -2', linewidth = lw)
    ax1.plot(clock, [x[0][1] for x in popG['F2']], "-", label = 'F = 2, m = -1', linewidth = lw)
    ax1.plot(clock, [x[0][2] for x in popG['F2']], "-", label = 'F = 2, m = 0', linewidth = lw)
    ax1.plot(clock, [x[0][3] for x in popG['F2']], "-", label = 'F = 2, m = 1', linewidth = lw)
    ax1.plot(clock, [x[0][4] for x in popG['F2']], "-", label = 'F = 2, m = 2', linewidth = lw)
    ax1.legend()
    

    
    fig2 = plt.figure(2)
    ax2 = fig2.add_subplot(111)
    #cm2 = plt.get_cmap('magma', linewidth = lw)
    #ax2.set_prop_cycle(cycler('color', [cm2(1. * i / 16) for i in range(16)]))
    for f in p.eStates:
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax2.plot(clock, [x[0][i] for x in popE[f]], "-", label = "F=" + str(fNum) + ", m=" + -fNum+ i, linewidth = lw)

    ax2.legend()
    
    #fig.savefig("./test.png")
    plt.show()
    #matplotlib.rcdefaults()
    print("done")

if __name__ == "__main__":
    main()
    
        
        
