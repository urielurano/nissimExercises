
from b import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

def fEpsilonCo():
    x1 = []
    y1 = []
    epsilonPhCo = En(Ec, r_star, gammac,alphar, thetac)
    fEpsilonPhCo = fcon(Ec, r_star, gammac,alphar, thetac)


    for ii in np.arange(-1.0,3.0,0.1):
        epsilon = pow(10,ii)
        x1.append(epsilon)
        if epsilon < epsilonPhCo:
            y1.append(fEpsilonPhCo*pow(epsilon/epsilonPhCo,2.0))
        if epsilon > epsilonPhCo:
            y1.append(fEpsilonPhCo*pow(epsilon/epsilonPhCo,-1.0))
    X = np.array(x1,float)
    Y1 = np.array(y1,float)
    rw1=plt.plot(X,Y1,color="green", linewidth=1.0, linestyle="-", label="E$_\pi$")

    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')
    plt.xlabel(r'$\epsilon_B$', size=12)
    plt.ylabel(r'E$_\nu$ (eV)', size=12)
    plt.title('')
    plt.show()

def fEpsilon():
    x1 = []
    y1 = []
    epsilonCSC = 0
    epsilonASC = 0
    epsilonMSC = E_mssc(xiB,Lj, gammaj,dt)

    for ii in np.arange(-1.0,3.0,0.1):
        epsilon = pow(10,ii)
        x1.append(epsilon)
        if(epsilon < epsilonASC):
            y1.append(pow(epsilonASC/epsilonCSC,1/3)*epsilon/epsilonASC))
        if(epsilonASC < epsilon and epsilon < epsilonCSC):
            y1.append(pow(epsilon/epsilon))
