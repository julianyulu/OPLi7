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
# Version: V1.0
# Last-Updated: Fri Nov 16 00:51:57 2018 (-0600)
#           By: yulu
#     Update #: 109
# 
import matplotlib.pyplot as plt
import os


def plotPopulation( clock,  Dline, eStates, polarization1, polarization2, I1, I2, popG, popE, saveFig = True):
    """
    plot population distrubution for ground and excited states
    and specify condition in the title 
    optionally save the figure to ./img/ folder
    """
    excitedState = '2P3halves(unresolved)' if Dline == 'D2' else eStates[0]
    lw = 2
    
    fig = plt.figure(figsize = (15, 15), dpi = 150)
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    
    for f, fmt in zip(['F1', 'F2'], ['-', '--']):# Ground states
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax1.plot(clock * 1e6, [x[0][i] for x in popG[f]], fmt, \
                     label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    ax1.set_title('Li7 ' +  Dline + ' transition ground(top) and excited(bottom)  hpf states population\n' \
                  + 'F1 -> ' + excitedState + ': ' + polarization1 + ' pol.  ' + str(I1) + ' mW/cm2 || ' \
                  + 'F2 -> ' + excitedState + ': ' + polarization2 + ' pol.  ' + str(I2) + ' mW/cm2', fontsize = 15)
    ax1.set_xlabel('Time [us]')
    ax1.legend(fontsize = 10)

    
    for f in list(popE.keys()):#p.eStates:
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax2.plot(clock * 1e6, [x[0][i] for x in popE[f]], "-",\
                     label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    ax2.set_xlabel('Time [us]')
    ax2.legend(fontsize = 10)

    if saveFig:
        if not os.path.isdir("./img/"):
            os.mkdir("img")
        fileName = "./img/Dline" + "_to" + excitedState + "_" + polarization1 + "_" + polarization2 + ".png"
        fig.savefig(fileName)
        print("[*]plots saved in " + fileName)
    plt.show()    

def plotParameterScan(scanPara, scanValues, steadyPopG, steadyPopE, steadyTime, saveFig = True):
        
    lw = 2 # plot linewidth 
    fig = plt.figure(figsize = (15, 10), dpi=150)
    
    # Ground states
    ax1 = fig.add_subplot(211)
    for f in ['F1', 'F2']:
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax1.plot(scanValues, [x[0][i] for x in steadyPopG[f]], "*--", \
                     label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    ax1.legend(fontsize = 12)
    ax1.set_ylabel('Steady State Population')
    ax1.set_xlabel('%s[default unit]' %scanPara)
    ax1.set_title('Optical pumping parameter scan: %s' %scanPara)
    # # Excited states
    # print(steadyPopG)
    # ax2 = fig.add_subplot(312)
    # for f in list(steadyPopE.keys()):#p.eStates:
    #     fNum = int(f[-1])
    #     for i in range(2 * fNum + 1):
    #         ax2.plot(scanValues, [x[0][i] for x in steadyPopE[f]], "-",\
    #                  label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    # ax2.set_xlabel('laser intensity [mw/cm^2]')
    # ax2.legend(fontsize = 12)

    # Steady states time
    ax3 = fig.add_subplot(212)
    ax3.plot(scanValues, steadyTime * 1e6, '^--')
    ax1.set_xlabel('%s[default unit]' %scanPara)
    ax3.set_ylabel('Time to reach steady state [us]')

    if saveFig:
        if not os.path.isdir("./img/"):
            os.mkdir("img")
        fileName = "./img/laser_intensity_scan.png"
        fig.savefig(fileName)
        print("[*]plots saved in ",  fileName)
    
    plt.show()



    
def plotIntensityScan(laserInten, steadyPopG, steadyPopE, steadyTime, saveFig = True):
    import matplotlib.pyplot as plt
    import os
    
    lw = 2 # plot linewidth 
    fig = plt.figure(figsize = (15, 10), dpi=150)
    # Ground states
    ax1 = fig.add_subplot(211)
    for f in ['F1', 'F2']:
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax1.plot(laserInten, [x[0][i] for x in steadyPopG[f]], "*--", \
                     label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    ax1.legend(fontsize = 12)
    ax1.set_ylabel('Steady State Population')
    ax1.set_title('Optical pumping under different laser intensities')
    # # Excited states
    # print(steadyPopG)
    # ax2 = fig.add_subplot(312)
    # for f in list(steadyPopE.keys()):#p.eStates:
    #     fNum = int(f[-1])
    #     for i in range(2 * fNum + 1):
    #         ax2.plot(laserInten, [x[0][i] for x in steadyPopE[f]], "-",\
    #                  label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    # ax2.set_xlabel('laser intensity [mw/cm^2]')
    # ax2.legend(fontsize = 12)

    # Steady states time
    ax3 = fig.add_subplot(212)
    ax3.plot(laserInten, steadyTime * 1e6, '^--')
    ax3.set_xlabel('laser intensity [mw/cm^2]')
    ax3.set_ylabel('Time to reach steady state [us]')

    if saveFig:
        if not os.path.isdir("./img/"):
            os.mkdir("img")
        fileName = "./img/laser_intensity_scan.png"
        fig.savefig(fileName)
        print("[*]plots saved in ./img/" + fileName)
    
    plt.show()
    
    
def plotDetuneScan(laserDetune, steadyPopG, steadyPopE, steadyTime, saveFig = True):
    import matplotlib.pyplot as plt
    import os
    
    lw = 2 # plot linewidth 
    fig = plt.figure(figsize = (15, 10), dpi=150)

    # Ground states
    ax1 = fig.add_subplot(211)
    for f in ['F1', 'F2']:
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax1.plot(laserDetune*1e-6, [x[0][i] for x in steadyPopG[f]], "*--", \
                     label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    ax1.legend(fontsize = 12)
    ax1.set_ylabel('Steady State Population')
    ax1.set_title('Optical pumping under different laser detune')
    # # Excited states
    # print(steadyPopG)
    # ax2 = fig.add_subplot(312)
    # for f in list(steadyPopE.keys()):#p.eStates:
    #     fNum = int(f[-1])
    #     for i in range(2 * fNum + 1):
    #         ax2.plot(laserInten, [x[0][i] for x in steadyPopE[f]], "-",\
    #                  label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    # ax2.set_xlabel('laser intensity [mw/cm^2]')
    # ax2.legend(fontsize = 12)

    # Steady states time
    ax3 = fig.add_subplot(212)
    ax3.plot(laserDetune * 1e-6, steadyTime * 1e6, '^--')
    ax3.set_xlabel('laser Detune [MHz]')
    ax3.set_ylabel('Time to reach steady state [us]')

    if saveFig:
        if not os.path.isdir("./img/"):
            os.mkdir("img")
        fileName = "./img/laser_detune_scan.png"
        fig.savefig(fileName)
        print("[*]plots saved in ./img/" + fileName)
    
    plt.show()
    
def plotPop_special( clock,  Dline, eStates, polarization1, polarization2, I1, I2, popG, popE, saveFig = True):
    """
    plot population distrubution for ground and excited states
    and specify condition in the title 
    optionally save the figure to ./img/ folder
    """
    import matplotlib.pyplot as plt
    import os
    
    excitedState = '2P3halves(unresolved)' if Dline == 'D2' else eStates[0]
    lw = 3
    
    fig = plt.figure(figsize = (15, 15), dpi = 150)
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    
    for f in ['F1', 'F2']:# Ground states
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax1.plot(clock * 1e6, [x[0][i] for x in popG[f]], "-", \
                     label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    ax1.set_title('Li7 ' +  Dline + ' transition ground(top) and excited(bottom)  hpf states population\n' \
                  + 'F1 -> ' + excitedState + ': ' + polarization1 + ' pol.  ' + str(I1) + ' mW/cm2 || ' \
                  + 'F2 -> ' + excitedState + ': ' + polarization2 + ' pol.  ' + str(I2) + ' mW/cm2', fontsize = 15)
    ax1.set_xlabel('Time [us]')
    ax1.set_ylim([0, 0.2])
    ax1.set_xlim([0, 20])
    ax1.legend(fontsize = 12)

    
    for f in list(popE.keys()):#p.eStates:
        fNum = int(f[-1])
        for i in range(2 * fNum + 1):
            ax2.plot(clock * 1e6, [x[0][i] for x in popE[f]], "-",\
                     label = "F=" + str(fNum) + ", m=" + str(-fNum+ i), linewidth = lw)
    ax2.set_xlabel('Time [us]')
    ax2.legend(fontsize = 12)

    if saveFig:
        if not os.path.isdir("./img/"):
            os.mkdir("img")
        fileName = "./img/Dline" + "_to" + excitedState + "_" + polarization1 + "_" + polarization2 + ".png"
        fig.savefig(fileName)
        print("[*]plots saved in " + fileName)
    plt.show()    
