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
# Last-Updated: Wed Sep 20 19:18:50 2017 (-0500)
#           By: superlu
#     Update #: 47
# 


from optPumping import optPumping
from TransitionStrength import TransStrength, DecayStrength
from Constant import dt, totalTime, pumpBeamPolarization
import numpy as np
import matplotlib.pyplot as plt

def main():
    global dt, totalTime, TransStrength, DecayStrength, pumpBeamPolarization
    p = optPumping(TransStrength, DecayStrength, pumpBeamPolarization)

    # Initialization of population array
    popG1 = []
    popG2 = []
    popE0 = []
    popE1 = []
    popE2 = []
    popE3 = []

    numSteps = int(totalTime / dt)
    for i in range(0, numSteps):
        if i == 0:
            G1 = p.groundF1Pop
            G2 = p.groundF2Pop
            E0 = p.excitedF0Pop
            E1 = p.excitedF1Pop
            E2 = p.excitedF2Pop
            E3 = p.excitedF3Pop
    
        else:
            print(popE0)
            G1, G2 = p.calGroundPop(popG1[i-1], popG2[i - 1] , popE0[i - 1], popE1[i - 1], popE2[i - 1], popE3[i - 1], dt)
            E0, E1, E2, E3 = p.calExcietedPop(popG1[i-1], popG2[i - 1] , popE0[i - 1], popE1[i - 1], popE2[i - 1], popE3[i - 1], dt)
        
        popG1.append(G1)
        popG2.append(G2)
        popE0.append(E0)
        popE1.append(E1)
        popE2.append(E2)
        popE3.append(E3)
    clock = np.linspace(0, totalTime, numSteps) * 1e9
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(clock, [x[0][0] for x in popG1], "*")
    fig.savefig("./test.png")
    plt.show()
    print("done")

if __name__ == "__main__":
    main()
    
        
        
