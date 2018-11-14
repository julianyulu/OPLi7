# simulator.py --- 
# 
# Filename: simulator.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Wed Nov 14 00:34:58 2018 (-0600)
# Version: 
# Last-Updated: Wed Nov 14 00:44:12 2018 (-0600)
#           By: yulu
#     Update #: 6
# 
from .optPumping import OptPumping
import numpy as np

class Simulator:
    
    def __init__(self,
                 Dline = 'D1',
                 excited_hpf_state = 'F2',
                 I1 = 0.0,
                 I2 = 0.0,
                 detune1 = 5,
                 detune2 = 2,
                 polarization1 = 'pi',
                 polarization2 = 'pi',
                 maxSimulationTime = 500e-6,
                 dt = 10e-9):
        
        self.Dline = 'D1'
        self.excited_hpf_state = 'F2'
        self.I1 = 0.0
        self.I2 = 0.0
        self.detune1 = 5
        self.detune2 = 2
        self.polarization1 = 'pi'
        self.polarization2 = 'pi'
        self.maxSimulationTime = 500e-6
        self.dt = 10e-9

    

