# laserIntensityScan.py --- 
# 
# Filename: laserIntensityScan.py
# Description: 
#           Scan the laser intensity and compare
#       population and time take to reach steady
#       states
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Mon Oct  9 23:00:53 2017 (-0500)
# Version: 
# Last-Updated: Tue Oct 10 00:20:12 2017 (-0500)
#           By: yulu
#     Update #: 22
# 


import sys, select
import numpy as np
from functions import readInput, runSimu, findSteadyState, nicePrintStates
from plot import plotIntensityScan

def main(args = ''):
    
    if args:
        inputParams = readInput(args)
    else:
        inputParams = readInput("./laserIntensityScan.in")

    startI = inputParams.get('startI')
    endI = inputParams.get('endI')
    dI = inputParams.get('dI')
    scanLaserId = inputParams.get('scanLaserId')
    
    laserInten = np.linspace(startI, endI, int((endI - startI) / dI))
        
    for i,I in enumerate(laserInten):
        clock, popG, popE = runSimu(
            Dline = inputParams['Dline'],
            excited_hpf_state = inputParams['excited_hpf_state'],
            I1 = I if scanLaserId == 'I1' else inputParams['I1'],
            I2 = I if scanLaserId == 'I2' else inputParams['I2'],
            detune1 = inputParams['detune1'],
            detune2 = inputParams['detune2'],
            polorization1 = inputParams['polorization1'],
            polorization2 = inputParams['polorization2'],
            maxSimulationTime = inputParams['maxSimulationTime'],
            dt = inputParams['dt']
            )

        if i == 0:
            steadyPopG = {'F1': [popG['F1'][-1]],
                          'F2': [popG['F2'][-1]]}
            steadyPopE = {}
            for key in popE.keys():
                steadyPopE[key] = [popE[key]]
            steadyTime = [clock[-1]]
        else:
            steadyPopG['F1'].append(popG['F1'][-1])
            steadyPopG['F2'].append(popG['F2'][-1])
            for key in popE.keys():
                steadyPopE[key].append(popE[key])
            steadyTime.append(clock[-1])

    steadyTime = np.array(steadyTime)
    plotIntensityScan(laserInten, steadyPopG, steadyPopE, steadyTime)


if __name__ == '__main__':
    infile, _, _ = select.select([sys.stdin], [], [], 3)
    if infile:
        main(sys.stdin)
    else:
        main()
