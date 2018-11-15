# example-detune-scan.py ---
# 
# Filename: example.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Thu Nov 15 00:03:18 2018 (-0600)
# Version: 
# Last-Updated: Thu Nov 15 15:30:57 2018 (-0600)
#           By: yulu
#     Update #: 22
# 

import sys
import numpy as np

try:
    from opli7 import Simulator
except ModuleNotFoundError:
    sys.path.insert(0, '../')
    from opli7 import Simulator

    
if __name__ == '__main__':
    s = Simulator(config = './config.in')
    print(s)
    #[bug, has dead loop] s.scan(scanKey = 'detune2', scanValues = np.linspace(-20e6, 20e6, 5))
    s.scan(scanKey = 'detune2', scanValues = np.linspace(-20e6, 20e6, 5))
    


