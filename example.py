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
# Last-Updated: Thu Nov 15 00:11:13 2018 (-0600)
#           By: yulu
#     Update #: 5
# 

from opli7 import Simulator

if __name__ == '__main__':
    s = Simulator(config = './singleRun.in')
    print(s)
    s.run()


