
from b import *
from math import *
import numpy as np
import matplotlib.pyplot as plt

def fEpsilonCo():
    x = []
    y = []
    epsilonPhCo = En(Ec, r_star, gammac,alphar, thetac)
    fEpsilonPhCo = fcon(Ec, r_star, gammac,alphar, thetac)


    for ii in np.arange(-1.0,3.0,0.1):
        epsilon = pow(10,ii)
        x.append(epsilon)
        if epsilon < epsilonPhCo:
            y.append(fEpsilonPhCo*pow(epsilon/epsilonPhCo,2.0))
        if epsilon > epsilonPhCo:
            y.append(fEpsilonPhCo*pow(epsilon/epsilonPhCo,-1.0))

    try:
        X = np.array(x,float)
        Y = np.array(y,float)
        rw1=plt.plot(X,Y1,color="green", linewidth=1.0, linestyle="-", label="E$_\pi$")
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.xlabel(r'$\epsilon_B$', size=12)
        plt.ylabel(r'E$_\nu$ (eV)', size=12)
        plt.title('')
        plt.show()
    except ValueError:
        print 'Diferent values on the plots'

        
def fEpsilon():
    x = []
    y = []
    epsilonCSC = 0.1 #change this value to the trust
    epsilonASC = 1e4 #change this value to the trust
    epsilonMSC = E_mssc(xiB,Lj, gammaj,dt)
    fEpsilonECSC = opt(Lj, z,gammaj, dt)*Fco(xiB,Lj, gammaj,dt,dz)

    for ii in np.arange(-1.0,3.0,0.1):
        epsilon = pow(10,ii)
        x.append(epsilon)
        if(epsilon < epsilonASC):
            y.append(fEpsilonECSC*pow(epsilonASC/epsilonCSC,1.0/3.0)*epsilon/epsilonASC)
            break
        if(epsilonASC < epsilon and epsilon < epsilonCSC):
            y.append(fEpsilonECSC*pow(epsilon/epsilonCSC,1.0/3.0))
            break
        if(epsilonCSC < epsilon and epsilon < epsilonMSC):
            y.append(fEpsilonECSC*pow(epsilon/epsilonCSC,-1.0/2.0))
            break
        if(epsilonMSC < epsilon):
            y.append(fEpsilonECSC*pow(epsilonMSC/epsilonCSC,-1.0/2.0)*pow(epsilon/epsilonMSC,-1.0/2.0))
            break
        y.append(0)

    try:
        X = np.array(x,float)
        Y = np.array(y,float)
        rw1=plt.plot(X,Y,color="green", linewidth=1.0, linestyle="-", label="E$_\pi$")
        
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.xlabel(r'$\epsilon_B$', size=12)
        plt.ylabel(r'E$_\nu$ (eV)', size=12)
        plt.title('')
        plt.show()
    except ValueError:
        print 'Diferents values of the dimentions of x and y'
        raise    

fEpsilon()
