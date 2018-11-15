# example.py ---
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
# Last-Updated: Thu Nov 15 16:25:43 2018 (-0600)
#           By: yulu
#     Update #: 23
# 

import sys

try:
    from opli7 import Simulator
except ModuleNotFoundError:
    sys.path.insert(0, '../')
    from opli7 import Simulator


if __name__ == '__main__':
    try:
        s = Simulator(config = './config.in')
    except FileNotFoundError:
        s = Simulator(config = 'test/config.in')
        
    print(s)
    s.run(plot = False)


