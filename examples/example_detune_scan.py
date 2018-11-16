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
# Last-Updated: Fri Nov 16 00:12:07 2018 (-0600)
#           By: yulu
#     Update #: 25
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
    print("Model Parameters:")
    print(s)
    s.scan(scanKey = 'detune2', scanValues = np.linspace(-5e6, 5e6, 6))
    


