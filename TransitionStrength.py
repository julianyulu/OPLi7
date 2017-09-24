# TransitionStrength.py --- 
# 
# Filename: TransitionStrength.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sun Sep 17 13:02:52 2017 (-0500)
# Version: 
# Last-Updated: Sun Sep 24 15:43:48 2017 (-0500)
#           By: yulu
#     Update #: 22
# 


import numpy as np

# Pumping transition 
class TransStrength:
    polarization = ['sigmaPlus', 'sigmaMinus', 'pi']
    transition = ['F1_D2_F0', 'F1_D2_F1','F1_D2_F2', 'F1_D2_F3',
                  'F2_D2_F0', 'F2_D2_F1','F2_D2_F2', 'F2_D2_F3'] 
    class sigmaPlus:
        
        pass
    class sigmaMinus:
        pass
    class pi:
        pass

# Decay transition 
class DecayStrength:
    polarization = ['sigmaPlus', 'sigmaMinus', 'pi']
    transition = ['F0_D2_F1', 'F0_D2_F2',
                  'F1_D2_F1', 'F1_D2_F2',
                  'F2_D2_F1', 'F2_D2_F2',
                  'F3_D2_F1', 'F3_D2_F2']
    class sigmaPlus:
        pass
    class sigmaMinus:
        pass
    class pi:
        pass

# ===================
# Pumping Transitions
# ===================

# SigmaPlus Transitions 
#-------------------------------------------------------------

# F1 -- D2 --> F'x
TransStrength.sigmaPlus.F1_D2_F0 = np.array([[20], [0], [0]])
TransStrength.sigmaPlus.F1_D2_F1 = np.array([
    [0, 25, 0],
    [0, 0, 25],
    [0, 0, 0]
    ])
TransStrength.sigmaPlus.F1_D2_F2 = np.array([
    [0, 0, 5, 0, 0],
    [0, 0, 0, 15, 0],
    [0, 0, 0, 0, 30]
    ])
TransStrength.sigmaPlus.F1_D2_F3 = np.zeros([3, 7])


# F2 -- D2 --> F'x 
TransStrength.sigmaPlus.F2_D2_F0 = np.zeros([5, 1])
TransStrength.sigmaPlus.F2_D2_F1 = np.array([
    [6, 0, 0],
    [0, 3, 0],
    [0, 0, 1],
    [0, 0, 0],
    [0, 0, 0]
    ])
TransStrength.sigmaPlus.F2_D2_F2 = np.array([
    [0, 10, 0, 0, 0],
    [0, 0, 15, 0, 0],
    [0, 0, 0, 15, 0],
    [0, 0, 0, 0, 10],
    [0, 0, 0, 0, 0]
    ])
TransStrength.sigmaPlus.F2_D2_F3 = np.array([
    [0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 12, 0, 0, 0],
    [0, 0, 0, 0, 24, 0, 0],
    [0, 0, 0, 0, 0, 40, 0],
    [0, 0, 0, 0, 0, 0, 60]
    ])


# SigmaMinus Transitions 
#-------------------------------------------------------------

# F1 -- D2 --> F'x 
TransStrength.sigmaMinus.F1_D2_F0 = np.array([[0], [0], [20]])
TransStrength.sigmaMinus.F1_D2_F1 = np.array([
    [0, 0, 0],
    [25, 0, 0],
    [0, 25, 0]
    ])
TransStrength.sigmaMinus.F1_D2_F2 = np.array([
    [30, 0, 0, 0, 0],
    [0, 15, 0, 0, 0],
    [0, 0, 5, 0, 0]
    ])
TransStrength.sigmaMinus.F1_D2_F3 = np.zeros([3, 7])

# F2 -- D2 --> F'x
TransStrength.sigmaMinus.F2_D2_F0 = np.zeros([5,1])
TransStrength.sigmaMinus.F2_D2_F1 = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [0, 3, 0],
    [0, 0, 6]
    ])
TransStrength.sigmaMinus.F2_D2_F2 = np.array([
    [0, 0, 0, 0, 0],
    [10, 0, 0, 0, 0],
    [0, 15, 0, 0, 0],
    [0, 0, 15, 0, 0],
    [0, 0, 0, 10, 0]
    ])
TransStrength.sigmaMinus.F2_D2_F3 = np.array([
    [60, 0, 0, 0, 0, 0, 0],
    [0, 40, 0, 0, 0, 0, 0],
    [0, 0, 24, 0, 0, 0, 0],
    [0, 0, 0, 12, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0]
    ])

# Pi Transitions 
#-------------------------------------------------------------

# F1 -- D2 --> F'x     
TransStrength.pi.F1_D2_F0 = np.array([[0], [20], [0]])
TransStrength.pi.F1_D2_F1 = np.array([
    [25, 0, 0],
    [0, 0, 0],
    [0, 0, 25]
    ])
TransStrength.pi.F1_D2_F2 = np.array([
    [0, 15, 0, 0, 0],
    [0, 0, 20, 0, 0],
    [0, 0, 0, 15, 0],
    ])
TransStrength.pi.F1_D2_F3 = np.zeros([3, 7])

# F2 -- D2 --> F'x
TransStrength.pi.F2_D2_F0 = np.zeros([5, 1])
TransStrength.pi.F2_D2_F1 = np.array([
    [0, 0, 0],
    [3, 0, 0],
    [0, 4, 0],
    [0, 0, 3],
    [0, 0, 0]
    ])
TransStrength.pi.F2_D2_F2 = np.array([
    [20, 0, 0, 0, 0],
    [0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0],
    [0, 0, 0, 0, 20]
    ])
TransStrength.pi.F2_D2_F3 = np.array([
    [0, 20, 0, 0, 0, 0, 0],
    [0, 0, 32, 0, 0, 0, 0],
    [0, 0, 0, 36, 0, 0, 0],
    [0, 0, 0, 0, 32, 0, 0],
    [0, 0, 0, 0, 0, 20, 0]
    ])



# ===================
# Decay Transitions
# ===================

# SigmaPlus Decay 
#-------------------------------------------------------------

# F'x -- D2 --> F1
DecayStrength.sigmaMinus.F0_D2_F1 = TransStrength.sigmaPlus.F1_D2_F0.T
DecayStrength.sigmaMinus.F1_D2_F1 = TransStrength.sigmaPlus.F1_D2_F1.T
DecayStrength.sigmaMinus.F2_D2_F1 = TransStrength.sigmaPlus.F1_D2_F2.T
DecayStrength.sigmaMinus.F3_D2_F1 = TransStrength.sigmaPlus.F1_D2_F3.T


# F'x -- D2 --> F2 
DecayStrength.sigmaMinus.F0_D2_F2 = TransStrength.sigmaPlus.F2_D2_F0.T
DecayStrength.sigmaMinus.F1_D2_F2 = TransStrength.sigmaPlus.F2_D2_F1.T
DecayStrength.sigmaMinus.F2_D2_F2 = TransStrength.sigmaPlus.F2_D2_F2.T
DecayStrength.sigmaMinus.F3_D2_F2 = TransStrength.sigmaPlus.F2_D2_F3.T


# SigmaMinus Decay 
#-------------------------------------------------------------

# F'x -- D2 --> F1
DecayStrength.sigmaPlus.F0_D2_F1 = TransStrength.sigmaMinus.F1_D2_F0.T
DecayStrength.sigmaPlus.F1_D2_F1 = TransStrength.sigmaMinus.F1_D2_F1.T
DecayStrength.sigmaPlus.F2_D2_F1 = TransStrength.sigmaMinus.F1_D2_F2.T
DecayStrength.sigmaPlus.F3_D2_F1 = TransStrength.sigmaMinus.F1_D2_F3.T

# F'x -- D2 --> F2
DecayStrength.sigmaPlus.F0_D2_F2 = TransStrength.sigmaMinus.F2_D2_F0.T
DecayStrength.sigmaPlus.F1_D2_F2 = TransStrength.sigmaMinus.F2_D2_F1.T
DecayStrength.sigmaPlus.F2_D2_F2 = TransStrength.sigmaMinus.F2_D2_F2.T
DecayStrength.sigmaPlus.F3_D2_F2 = TransStrength.sigmaMinus.F2_D2_F3.T

# Pi Decay 
#-------------------------------------------------------------

# F'x -- D2 --> F1
DecayStrength.pi.F0_D2_F1 = TransStrength.pi.F1_D2_F0.T 
DecayStrength.pi.F1_D2_F1 = TransStrength.pi.F1_D2_F1.T 
DecayStrength.pi.F2_D2_F1 = TransStrength.pi.F1_D2_F2.T 
DecayStrength.pi.F3_D2_F1 = TransStrength.pi.F1_D2_F3.T 

# F'x -- D2 --> F2
DecayStrength.pi.F0_D2_F2 = TransStrength.pi.F2_D2_F0.T
DecayStrength.pi.F1_D2_F2 = TransStrength.pi.F2_D2_F1.T
DecayStrength.pi.F2_D2_F2 = TransStrength.pi.F2_D2_F2.T
DecayStrength.pi.F3_D2_F2 = TransStrength.pi.F2_D2_F3.T

