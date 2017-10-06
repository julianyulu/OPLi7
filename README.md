# Optical Pumping Simulation On Lithium7 Dline  
[![Build Status](https://travis-ci.org/SuperYuLu/OpticalPumpingLithium7Dline.svg?branch=master)](https://travis-ci.org/SuperYuLu/OpticalPumpingLithium7Dline)  
| Author | Yu Lu |
| ------:|-----: |
| Create | Oct.05 2017 |
| Institute | Univ. of Texas at Austin |  

## Introduction 
This is a repository built for simulating the hyperfine transitions under optical pumping of lithium 7 atoms, which is part of my current research. Manipulating the hyperfine states of cold atoms allows researchers to study their behavior under different interaction regimes, as well as detecting atoms in a specific state. Although the quantum transition between levels of atoms has been well studied by quantum mechanics, the accurate analytical solution of optical pumping process under certain conditions is very much rely on 2-level system model, in which the population of involved quantum states ( usually noted as ground state and excited state) is descriped by [Optical Bloch equations](https://en.wikipedia.org/wiki/Maxwell%E2%80%93Bloch_equations).   

However, apart from the ideal case of a two-level cycling transition, more general situation is that people has to deal with multi-level atoms systems, where atoms have chance to go into *dark states* and thus broke the assumptions of Optical Bloch equations. As a pratical case, alkali atoms have well documented transition strength of hyperfine (hpf) states and are widely used in cold atoms physics when combining other good properities. As in our research, *Lithium 7* atom is being used to approach super large [BEC](https://en.wikipedia.org/wiki/Bose%E2%80%93Einstein_condensate)(Bose-Einstein Condensate), well understand the behavior of Li7 atom under optical pumpuing is necessary.   

## Lithium D Line Transition  
![Lithium D line transition](https://github.com/SuperYuLu/OpticalPumpingLithium7Dline/blob/master/info/LiLevel.png)  

Above shown is the D line transitions of the two main lithium isotopes. This study will focus on the element Li7. The D1 line excited state of Li7 is not well resolved due to that fact that their seperation is much smaller than natrual linewidth, so effectively its a single level but with hiden states. In comparison, the D1 line of Li 7 excited state is well seperated and thus has to be trated individually. This simulation is to study the dynamics os population transfer of the magnetic sublevels of hpf states under different laser frequency, polarization, intensity, etc.   

