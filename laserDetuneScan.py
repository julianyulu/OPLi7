# laserDetuneScan.py --- 
# 
# Filename: laserDetuneScan.py
# Description: 
#            Simulate optical pumping under
#         different laser detune, analyze the
#         steady states population and time
#         takes to reach steady states.
#
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Tue Oct 10 11:29:11 2017 (-0500)
# Version: 
# Last-Updated: Tue Oct 10 22:25:09 2017 (-0500)
#           By: yulu
#     Update #: 8
# 


import numpy as np
from functions import readInput, runSimu, findSteadyState, nicePrintStates
from plot import plotDetuneScan

def main():
    """
    Simulate specified optical pumping process under different
    laser frequency detune. 
    Plot the steady state population and time to reach steady
    state for different detune frequency.
    Input parameters should be specified in laserDetuneScan.in
    """
            
    # load input parameters 
    try:
        inputParams = readInput("./laserDetuneScan.in")
    except FileNotFoundError:
        print("No file 'laserDetuneScan.in' avaliable in ./")
        raise FileNotFoundError
    
    startD = inputParams.get('startDetune')
    endD = inputParams.get('endDetune')
    dD = inputParams.get('dDetune')
    scanLaserId = inputParams.get('scanLaserId')
    
    laserDetune = np.linspace(startD, endD, int((endD - startD) / dD))
        
    for i,D in enumerate(laserDetune):
        clock, popG, popE = runSimu(
            Dline = inputParams['Dline'],
            excited_hpf_state = inputParams['excited_hpf_state'],
            I1 = inputParams['I1'],
            I2 = inputParams['I2'],
            detune1 = D if scanLaserId == 'I1' else inputParams['detune1'],
            detune2 = D if scanLaserId == 'I2' else inputParams['detune2'],
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
    plotDetuneScan(laserDetune, steadyPopG, steadyPopE, steadyTime)
    
if __name__ == '__main__':
    main()