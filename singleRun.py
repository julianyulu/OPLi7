# sigleRun.py --- 
# 
# Filename: sigleRun.py
# Description:
#          Run a sigle simulation and plot
#        population distribution 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Mon Oct  9 10:28:14 2017 (-0500)
# Version: 
# Last-Updated: Mon Oct  9 13:59:42 2017 (-0500)
#           By: superlu
#     Update #: 20
# 



from plot import plotPop
from functions import *
from Constant import input 

def main():
    clock, popG, popE = runSimu(**input)
    params = {
        "clock": clock,
        "Dline":input.get('Dline'),
        "eStates": [input.get('excited_hpf_state')],
        "polorization1": input.get('polorization1'),
        "polorization2": input.get('polorization2'),
        "I1": input.get('I1'),
        "I2": input.get('I2'),
        "popG": popG,
        "popE": popE,
        "saveFig": False
            }

    t, steadyG, steadE = findSteadyState(clock, popG, popE)
    if t == 0:
        print("No steady state reached, extend the simulation time")
    else:
        print("Time for reaching steady state: {:2.2f} us".format(t * 1e6))
        #nicePrintStates(steady, steadyE)

    plotPop(**params)
    
  
    

if __name__ == '__main__':
    main()
