# plot.py --- 
# 
# Filename: plot.py
# Description: 
#            plot the population vs time for
#            ground and excited states sublevels
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Thu Oct  5 17:52:51 2017 (-0500)
# Version: 
# Last-Updated: Sat Oct  7 22:03:41 2017 (-0500)
#           By: yulu
#     Update #: 47
# 



def plotPop( clock,  Dline, eStates, polorization1, polorization2, I1, I2, popG, popE, saveFig = True):
    import matplotlib.pyplot as plt
    import os
    
    excitedState = '2P3/2(unresolved)' if Dline == 'D2' else eStates[0]
    lw = 3
    
    fig = plt.figure(figsize = (15, 15), dpi = 150)
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    
    for f in ['F1', 'F2']:# Ground states
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax1.plot(clock, [x[0][i] for x in popG[f]], "-", \
                     label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    ax1.set_title('Li7 ' +  Dline + ' transition ground(top) and excited(bottom)  hpf states population\n' \
                  + 'F1 -> ' + excitedState + ': ' + polorization1 + ' pol.  ' + str(I1*0.1) + ' mW/cm2 || ' \
                  + 'F2 -> ' + excitedState + ': ' + polorization2 + ' pol.  ' + str(I2*0.1) + ' mW/cm2')
    ax1.set_xlabel('Time [us]')
    ax1.legend(fontsize = 8)

    
    for f in eStates:#p.eStates:
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax2.plot(clock, [x[0][i] for x in popE[f]], "-",\
                     label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    ax2.set_xlabel('Time [us]')
    ax2.legend(fontsize = 8)

    if saveFig:
        if not os.path.isdir("./img/"):
            os.mkdir("img")
        fileName = "./img/Dline" + "_to" + excitedState + "_" + polorization1 + "_" + polorization2 + ".png"
        fig.savefig(fileName)
        print("-----------------------------------------------")
        print("plots saved in ./img/" + fileName)
    plt.show()    
