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
# Last-Updated: Wed Oct 11 18:20:20 2017 (-0500)
#           By: superlu
#     Update #: 51
# 

##########################################################
#     Lithium Atom D Line Transition Database            #
#                                           By Yu Lu     #
#                                                        #
# Data from: "Laser cooling and Trapping"                #
# By: Harold J. Metcalf, Peter van der Straten           #
##########################################################

import numpy as np

#===========#
#  D1 Line  #
#===========#
class TransStrengthD1_toF1:
    eStates = ['F1']
    freq = 446789597 * 1e6 # [Hz]
    numSubStates = [3]    
    polarization = ['sigmaPlus', 'sigmaMinus', 'pi']
    transition = ['F1_D1_F1',
                  'F2_D1_F1',] 
    class sigmaPlus:
        pass
    class sigmaMinus:
        pass
    class pi:
        pass

class DecayStrengthD1_toF1:
    eStates = ['F1']
    freq = 446789597 * 1e6 # [Hz]
    numSubStates = [3]
    polarization = ['sigmaPlus', 'sigmaMinus', 'pi']
    transition = ['F1_D1_F1',
                  'F1_D1_F2'] 
    class sigmaPlus:
        pass
    class sigmaMinus:
        pass
    class pi:
        pass

class TransStrengthD1_toF2:
    eStates = ['F2']
    freq = 446789597 * 1e6 # [Hz]
    numSubStates = [5]    
    polarization = ['sigmaPlus', 'sigmaMinus', 'pi']
    transition = ['F1_D1_F2',
                  'F2_D1_F2',] 
    class sigmaPlus:
        pass
    class sigmaMinus:
        pass
    class pi:
        pass

class DecayStrengthD1_toF2:
    eStates = ['F2']
    freq = 446789597 * 1e6 # [Hz]
    numSubStates = [5]
    polarization = ['sigmaPlus', 'sigmaMinus', 'pi']
    transition = ['F2_D1_F1',
                  'F2_D1_F2'] 
    class sigmaPlus:
        pass
    class sigmaMinus:
        pass
    class pi:
        pass

# ==========> sigmaPlus Transitions <=========
TransStrengthD1_toF1.sigmaPlus.F1_D1_F1 = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0]
        ])
TransStrengthD1_toF1.sigmaPlus.F2_D1_F1 = np.array([
        [6, 0, 0],
        [0, 3, 0],
        [0, 0, 1],
        [0, 0, 0],
        [0, 0, 0]
        ])

TransStrengthD1_toF2.sigmaPlus.F1_D1_F2 = np.array([
        [0, 0, 1, 0, 0],
        [0, 0, 0, 3, 0],
        [0, 0, 0, 0, 6]
        ])

TransStrengthD1_toF2.sigmaPlus.F2_D1_F2 = np.array([
        [0, 2, 0, 0, 0],
        [0, 0, 3, 0, 0],
        [0, 0, 0, 3, 0],
        [0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0]
        ])

# ==========> sigmaMinus Transitions <=========
TransStrengthD1_toF1.sigmaMinus.F1_D1_F1 = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0]
        ])

TransStrengthD1_toF1.sigmaMinus.F2_D1_F1 = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [1, 0, 0],
        [0, 3, 0],
        [0, 0, 6]
        ])

TransStrengthD1_toF2.sigmaMinus.F1_D1_F2 = np.array([
        [6, 0, 0, 0, 0],
        [0, 3, 0, 0, 0],
        [0, 0, 1, 0, 0]
        ])

TransStrengthD1_toF2.sigmaMinus.F2_D1_F2 = np.array([
        [0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0],
        [0, 3, 0, 0, 0],
        [0, 0, 3, 0, 0],
        [0, 0, 0, 3, 0]
        ])

# =============> pi Transitions <=============
TransStrengthD1_toF1.pi.F1_D1_F1 = np.array([
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
        ])

TransStrengthD1_toF1.pi.F2_D1_F1 = np.array([
        [0, 0, 0],
        [3, 0, 0],
        [0, 4, 0],
        [0, 0, 3],
        [0, 0, 0]
        ])

TransStrengthD1_toF2.pi.F1_D1_F2 = np.array([
        [0, 3, 0, 0, 0],
        [0, 0, 4, 0, 0],
        [0, 0, 0, 3, 0]
        ])

TransStrengthD1_toF2.pi.F2_D1_F2 = np.array([
        [4, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 4]
        ])

# =============> Decay Matrices <=============

# Decay from F' = 1
DecayStrengthD1_toF1.sigmaMinus.F1_D1_F1 = TransStrengthD1_toF1.sigmaPlus.F1_D1_F1.T
DecayStrengthD1_toF1.sigmaMinus.F1_D1_F2 = TransStrengthD1_toF1.sigmaPlus.F2_D1_F1.T

DecayStrengthD1_toF1.sigmaPlus.F1_D1_F1 = TransStrengthD1_toF1.sigmaMinus.F1_D1_F1.T
DecayStrengthD1_toF1.sigmaPlus.F1_D1_F2 = TransStrengthD1_toF1.sigmaMinus.F2_D1_F1.T

DecayStrengthD1_toF1.pi.F1_D1_F1 = TransStrengthD1_toF1.pi.F1_D1_F1.T
DecayStrengthD1_toF1.pi.F1_D1_F2 = TransStrengthD1_toF1.pi.F2_D1_F1.T 

# Decay from F' = 2
DecayStrengthD1_toF2.sigmaMinus.F2_D1_F1 = TransStrengthD1_toF2.sigmaPlus.F1_D1_F2.T
DecayStrengthD1_toF2.sigmaMinus.F2_D1_F2 = TransStrengthD1_toF2.sigmaPlus.F2_D1_F2.T

DecayStrengthD1_toF2.sigmaPlus.F2_D1_F1 = TransStrengthD1_toF2.sigmaMinus.F1_D1_F2.T
DecayStrengthD1_toF2.sigmaPlus.F2_D1_F2 = TransStrengthD1_toF2.sigmaMinus.F2_D1_F2.T

DecayStrengthD1_toF2.pi.F2_D1_F1 = TransStrengthD1_toF2.pi.F1_D1_F2.T
DecayStrengthD1_toF2.pi.F2_D1_F2 = TransStrengthD1_toF2.pi.F2_D1_F2.T 




#===========#
#  D2 Line  #
#===========#

class TransStrengthD2:
    eStates = ['F0', 'F1', 'F2', 'F3']
    freq = 446810184 * 1e6 #[Hz]
    numSubStates = [1, 3, 5, 7]
    polarization = ['sigmaPlus', 'sigmaMinus', 'pi']
    transition = ['F1_D2_F0', 'F1_D2_F1','F1_D2_F2', 'F1_D2_F3',
                  'F2_D2_F0', 'F2_D2_F1','F2_D2_F2', 'F2_D2_F3'] 
    class sigmaPlus:
        
        pass
    class sigmaMinus:
        pass
    class pi:
        pass

class DecayStrengthD2:
    eStates = ['F0', 'F1', 'F2', 'F3']
    freq = 446789597 * 1e6 # [Hz]
    numSubStates = [1, 3, 5, 7]
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
        


# ==========> sigmaPlus Transitions <=========
TransStrengthD2.sigmaPlus.F1_D2_F0 = np.array([[20], [0], [0]])
TransStrengthD2.sigmaPlus.F1_D2_F1 = np.array([
    [0, 25, 0],
    [0, 0, 25],
    [0, 0, 0]
    ])
TransStrengthD2.sigmaPlus.F1_D2_F2 = np.array([
    [0, 0, 5, 0, 0],
    [0, 0, 0, 15, 0],
    [0, 0, 0, 0, 30]
    ])
TransStrengthD2.sigmaPlus.F1_D2_F3 = np.zeros([3, 7])


# F2 -- D2 --> F'x 
TransStrengthD2.sigmaPlus.F2_D2_F0 = np.zeros([5, 1])
TransStrengthD2.sigmaPlus.F2_D2_F1 = np.array([
    [6, 0, 0],
    [0, 3, 0],
    [0, 0, 1],
    [0, 0, 0],
    [0, 0, 0]
    ])
TransStrengthD2.sigmaPlus.F2_D2_F2 = np.array([
    [0, 10, 0, 0, 0],
    [0, 0, 15, 0, 0],
    [0, 0, 0, 15, 0],
    [0, 0, 0, 0, 10],
    [0, 0, 0, 0, 0]
    ])
TransStrengthD2.sigmaPlus.F2_D2_F3 = np.array([
    [0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 12, 0, 0, 0],
    [0, 0, 0, 0, 24, 0, 0],
    [0, 0, 0, 0, 0, 40, 0],
    [0, 0, 0, 0, 0, 0, 60]
    ])



# ==========> sigmaMinus Transitions <=========
TransStrengthD2.sigmaMinus.F1_D2_F0 = np.array([[0], [0], [20]])
TransStrengthD2.sigmaMinus.F1_D2_F1 = np.array([
    [0, 0, 0],
    [25, 0, 0],
    [0, 25, 0]
    ])
TransStrengthD2.sigmaMinus.F1_D2_F2 = np.array([
    [30, 0, 0, 0, 0],
    [0, 15, 0, 0, 0],
    [0, 0, 5, 0, 0]
    ])
TransStrengthD2.sigmaMinus.F1_D2_F3 = np.zeros([3, 7])

# F2 -- D2 --> F'x
TransStrengthD2.sigmaMinus.F2_D2_F0 = np.zeros([5,1])
TransStrengthD2.sigmaMinus.F2_D2_F1 = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [0, 3, 0],
    [0, 0, 6]
    ])
TransStrengthD2.sigmaMinus.F2_D2_F2 = np.array([
    [0, 0, 0, 0, 0],
    [10, 0, 0, 0, 0],
    [0, 15, 0, 0, 0],
    [0, 0, 15, 0, 0],
    [0, 0, 0, 10, 0]
    ])
TransStrengthD2.sigmaMinus.F2_D2_F3 = np.array([
    [60, 0, 0, 0, 0, 0, 0],
    [0, 40, 0, 0, 0, 0, 0],
    [0, 0, 24, 0, 0, 0, 0],
    [0, 0, 0, 12, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0]
    ])


# =============> pi Transitions <=============
TransStrengthD2.pi.F1_D2_F0 = np.array([[0], [20], [0]])
TransStrengthD2.pi.F1_D2_F1 = np.array([
    [25, 0, 0],
    [0, 0, 0],
    [0, 0, 25]
    ])
TransStrengthD2.pi.F1_D2_F2 = np.array([
    [0, 15, 0, 0, 0],
    [0, 0, 20, 0, 0],
    [0, 0, 0, 15, 0],
    ])
TransStrengthD2.pi.F1_D2_F3 = np.zeros([3, 7])

TransStrengthD2.pi.F2_D2_F0 = np.zeros([5, 1])
TransStrengthD2.pi.F2_D2_F1 = np.array([
    [0, 0, 0],
    [3, 0, 0],
    [0, 4, 0],
    [0, 0, 3],
    [0, 0, 0]
    ])
TransStrengthD2.pi.F2_D2_F2 = np.array([
    [20, 0, 0, 0, 0],
    [0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0],
    [0, 0, 0, 0, 20]
    ])
TransStrengthD2.pi.F2_D2_F3 = np.array([
    [0, 20, 0, 0, 0, 0, 0],
    [0, 0, 32, 0, 0, 0, 0],
    [0, 0, 0, 36, 0, 0, 0],
    [0, 0, 0, 0, 32, 0, 0],
    [0, 0, 0, 0, 0, 20, 0]
    ])

# =============> Decay Matrices <=============

DecayStrengthD2.sigmaMinus.F0_D2_F1 = TransStrengthD2.sigmaPlus.F1_D2_F0.T
DecayStrengthD2.sigmaMinus.F1_D2_F1 = TransStrengthD2.sigmaPlus.F1_D2_F1.T
DecayStrengthD2.sigmaMinus.F2_D2_F1 = TransStrengthD2.sigmaPlus.F1_D2_F2.T
DecayStrengthD2.sigmaMinus.F3_D2_F1 = TransStrengthD2.sigmaPlus.F1_D2_F3.T


DecayStrengthD2.sigmaMinus.F0_D2_F2 = TransStrengthD2.sigmaPlus.F2_D2_F0.T
DecayStrengthD2.sigmaMinus.F1_D2_F2 = TransStrengthD2.sigmaPlus.F2_D2_F1.T
DecayStrengthD2.sigmaMinus.F2_D2_F2 = TransStrengthD2.sigmaPlus.F2_D2_F2.T
DecayStrengthD2.sigmaMinus.F3_D2_F2 = TransStrengthD2.sigmaPlus.F2_D2_F3.T

DecayStrengthD2.sigmaPlus.F0_D2_F1 = TransStrengthD2.sigmaMinus.F1_D2_F0.T
DecayStrengthD2.sigmaPlus.F1_D2_F1 = TransStrengthD2.sigmaMinus.F1_D2_F1.T
DecayStrengthD2.sigmaPlus.F2_D2_F1 = TransStrengthD2.sigmaMinus.F1_D2_F2.T
DecayStrengthD2.sigmaPlus.F3_D2_F1 = TransStrengthD2.sigmaMinus.F1_D2_F3.T

DecayStrengthD2.sigmaPlus.F0_D2_F2 = TransStrengthD2.sigmaMinus.F2_D2_F0.T
DecayStrengthD2.sigmaPlus.F1_D2_F2 = TransStrengthD2.sigmaMinus.F2_D2_F1.T
DecayStrengthD2.sigmaPlus.F2_D2_F2 = TransStrengthD2.sigmaMinus.F2_D2_F2.T
DecayStrengthD2.sigmaPlus.F3_D2_F2 = TransStrengthD2.sigmaMinus.F2_D2_F3.T

DecayStrengthD2.pi.F0_D2_F1 = TransStrengthD2.pi.F1_D2_F0.T 
DecayStrengthD2.pi.F1_D2_F1 = TransStrengthD2.pi.F1_D2_F1.T 
DecayStrengthD2.pi.F2_D2_F1 = TransStrengthD2.pi.F1_D2_F2.T 
DecayStrengthD2.pi.F3_D2_F1 = TransStrengthD2.pi.F1_D2_F3.T 

DecayStrengthD2.pi.F0_D2_F2 = TransStrengthD2.pi.F2_D2_F0.T
DecayStrengthD2.pi.F1_D2_F2 = TransStrengthD2.pi.F2_D2_F1.T
DecayStrengthD2.pi.F2_D2_F2 = TransStrengthD2.pi.F2_D2_F2.T
DecayStrengthD2.pi.F3_D2_F2 = TransStrengthD2.pi.F2_D2_F3.T

