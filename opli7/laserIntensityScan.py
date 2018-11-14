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
# Last-Updated: Sun Oct 15 22:24:09 2017 (-0500)
#           By: yulu
#     Update #: 34
# 
import sys
import numpy as np
from functions import readInput, runSimu, nicePrintStates
from plot import plotIntensityScan

def main(inFile):
    """
    Simulate specified optical pumping process under different
    laser intensity. 
    Plot the steady state population and time to reach steady
    state for different laser intensity.
    Input parameters should be specified in laserIntensityScan.in
    """
    
    # load input parameters 
    
    inputParams = readInput(inFile)
    
    startI = inputParams.get('startI')
    endI = inputParams.get('endI')
    dI = inputParams.get('dI')
    scanLaserId = inputParams.get('scanLaserId')
    
    laserInten = np.linspace(startI, endI, int((endI - startI) / dI))
        
    for i,I in enumerate(laserInten):
        clock, popG, popE, steadyIdx = runSimu(
            Dline = inputParams['Dline'],
            excited_hpf_state = inputParams['excited_hpf_state'],
            I1 = I if scanLaserId == 'I1' else inputParams['I1'],
            I2 = I if scanLaserId == 'I2' else inputParams['I2'],
            detune1 = inputParams['detune1'],
            detune2 = inputParams['detune2'],
            polarization1 = inputParams['polarization1'],
            polarization2 = inputParams['polarization2'],
            maxSimulationTime = inputParams['maxSimulationTime'],
            dt = inputParams['dt']
            )

        if i == 0:
            steadyPopG = {'F1': [popG['F1'][steadyIdx]],
                          'F2': [popG['F2'][steadyIdx]]}
            steadyPopE = {}
            for key in popE.keys():
                steadyPopE[key] = [popE[key]]
            steadyTime = [clock[steadyIdx]]
        else:
            steadyPopG['F1'].append(popG['F1'][steadyIdx])
            steadyPopG['F2'].append(popG['F2'][steadyIdx])
            for key in popE.keys():
                steadyPopE[key].append(popE[key][steadyIdx])
            steadyTime.append(clock[steadyIdx])

    steadyTime = np.array(steadyTime)
    plotIntensityScan(laserInten, steadyPopG, steadyPopE, steadyTime)


if __name__ == '__main__':
    main(sys.stdin)
