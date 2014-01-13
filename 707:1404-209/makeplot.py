
from b import *
from math import *
import numpy as np
import matplotlib.pyplot as plt

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

    try:
        X = np.array(x1,float)
        Y1 = np.array(y1,float)
        print X#delete
        print '-----------------------------------------------------------------------------------------------------------------------'#detele
        print Y1#delete
        rw1=plt.plot(X,Y1,color="green", linewidth=1.0, linestyle="-", label="E$_\pi$")
        print 'all from plot 1'#delete

        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.xlabel(r'$\epsilon_B$', size=12)
        plt.ylabel(r'E$_\nu$ (eV)', size=12)
        plt.title('')
        plt.show()
    except ValueError:
        print 'Diferent values on the plots', sys.exc_info()[0]

        
def fEpsilon():
    x1 = []
    y1 = []
    epsilonCSC = 0.1
    epsilonASC = 0.3
    epsilonMSC = E_mssc(xiB,Lj, gammaj,dt)
    fEpsilonECSC = opt(Lj, z,gammaj, dt)*Fco(xiB,Lj, gammaj,dt,dz)

    for ii in np.arange(-1.0,3.0,0.1):
        epsilon = pow(10,ii)
        x1.append(epsilon)
        if(epsilon < epsilonASC):
            y1.append(fEpsilonECSC*pow(epsilonASC/epsilonCSC,1/3)*epsilon/epsilonASC)
        if(epsilonASC < epsilon and epsilon < epsilonCSC):
            y1.append(fEpsilonECSC*pow(epsilon/epsilon,1/3))
        if(epsilonCSC < epsilon and epsilon < epsilonMSC):
            y1.append(fEpsilonECSC*pow(epsilon/epsilonCSC,-1/2))
        if(epsilonMSC < epsilon):
            y1.append(fEpsilonECSC*pow(epsilonMSC/epsilonCSC,-1/2)*pow(epsilon/epsilonMSC,-1/2))
    try:
        X = np.array(x1,float)
        Y1 = np.array(y1,float)
        print X#delete
        print '-----------------------------------------------------------------------------------------------------------------------'#delete
        print Y1#delete
        rw1=plt.plot(X,Y1,color="green", linewidth=1.0, linestyle="-", label="E$_\pi$")
        print 'all from plot2'#delete
        
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.xlabel(r'$\epsilon_B$', size=12)
        plt.ylabel(r'E$_\nu$ (eV)', size=12)
        plt.title('')
        plt.show()
    except ValueError:
        print 'Diferent values on the plots', sys.exc_info()[0]
