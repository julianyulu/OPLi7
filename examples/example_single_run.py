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
# Last-Updated: Thu Nov 15 16:32:53 2018 (-0600)
#           By: yulu
#     Update #: 28
#


import sys
import os

pkgPath = os.path.dirname(os.path.realpath(__file__ + '/../'))


try:
    from opli7 import Simulator
except ModuleNotFoundError:
    sys.path.insert(0, pkgPath)
    from opli7 import Simulator


if __name__ == '__main__':
    """
    test single run 
    currently this script can only be run 
    under /example folder.
    """
    s = Simulator(config = os.path.join(pkgPath, 'examples/config.in'))
    print(s)
    s.run()


