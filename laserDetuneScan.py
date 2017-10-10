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
# Last-Updated: Tue Oct 10 14:10:54 2017 (-0500)
#           By: superlu
#     Update #: 3
# 


import sys, select
import numpy as np
from functions import readInput, runSimu, findSteadyState, nicePrintStates
from plot import plotDetuneyScan

def laserDetuneScan(args = ''):
    if args:
        inputParams = readInput(args)
    else:
        inputParams = readInput("./laserDetuneScan.in")

    
