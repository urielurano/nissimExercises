
from b import *
from math import *
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt


def fEpsilonCo():
    '''We here make the plot of the function fEpsilonCo'''
    x = []
    y = []
    epsilonPhCo = En(Ec, r_star, gammac,alphar, thetac)
    fEpsilonPhCo = fcon(Ec, r_star, gammac,alphar, thetac)

    #Here make the aranges to make the plot
    for ii in np.arange(-1.0,3.0,0.1):
        epsilon = pow(10,ii)
        x.append(epsilon)
        if epsilon < epsilonPhCo:
            y.append(fEpsilonPhCo*pow(epsilon/epsilonPhCo,2.0))
        if epsilon > epsilonPhCo:
            y.append(fEpsilonPhCo*pow(epsilon/epsilonPhCo,-1.0))
    #Now we want make the plot of the array
    try:
        X = np.array(x,float)
        Y = np.array(y,float)
        #Here we make the spline of the function
        xnew = np.linspace(10e-2,(10e2)/2,10e3) 
        f = interp1d(X, Y, kind='cubic')
        plt.plot(X,Y, color = 'blue', linestyle = '-')
        plt.plot(xnew,f(xnew), color = 'red', linestyle = '--')
        plt.legend(['original','spline cubic'], loc='best')
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.xlabel(r'$\epsilon_B$', size=12)
        plt.ylabel(r'E$_\nu$ (eV)', size=12)
        plt.title('')
        plt.show()
    except ValueError:
        print 'Please check the values of your module by this exception:'
        raise



        
def fEpsilon():
    x = []
    y = []
    epsilonCSC = 0.1 #change this value
    epsilonASC = 1e2 #change this value
    epsilonMSC = E_mssc(xiB,Lj, gammaj,dt)
    fEpsilonECSC = opt(Lj, z,gammaj, dt)*Fco(xiB,Lj, gammaj,dt,dz)

    for ii in np.arange(-1.0,3.0,0.1):
        epsilon = pow(10,ii)
        x.append(epsilon)
        if(epsilon < epsilonASC):
            y.append(fEpsilonECSC*pow(epsilonASC/epsilonCSC,1.0/3.0)*epsilon/epsilonASC)
            continue
        if(epsilonASC < epsilon and epsilon < epsilonCSC):
            y.append(fEpsilonECSC*pow(epsilon/epsilonCSC,1.0/3.0))
            continue
        if(epsilonCSC < epsilon and epsilon < epsilonMSC):
            y.append(fEpsilonECSC*pow(epsilon/epsilonCSC,-1.0/2.0))
            continue
        if(epsilonMSC < epsilon):
            y.append(fEpsilonECSC*pow(epsilonMSC/epsilonCSC,-1.0/2.0)*pow(epsilon/epsilonMSC,-1.0/2.0))
            continue
        y.append(0)

    try:
        X = np.array(x,float)
        Y = np.array(y,float)
        #Make here the spline
        x1new = np.linspace(10e-2, (10e3)/15,10e5)#check here
        x2new = np.linspace(10e-2, (10e3)/30,10e5)#check here
        x3new = np.linspace(10e-2, (10e3)/60,10e5)#check here
        x4new = np.linspace(10e-2, (10e3)/90,10e5)#check here 
        f = interp1d(X, Y, kind='cubic')
        plt.figure('graph')
        plt.subplot(411)
        plt.plot(X,Y,color = 'blue', linestyle = '-')
        plt.plot(x1new,f(x1new), color = 'red', linestyle = '--')
        plt.legend(['original','splie with a linspace from 10e-2 to 10e3/15 of 10e5' ], loc='best')
        ############################################################################
        plt.subplot(412)
        plt.plot(X,Y,color = 'blue', linestyle = '-')
        plt.plot(x2new,f(x2new), color = 'green', linestyle = '--')
        plt.legend(['original','splie with a linspace from 10e-2 to 10e3/15 of 10e5' ], loc='best')
        ############################################################################  
        plt.subplot(413)
        plt.plot(X,Y,color = 'blue', linestyle = '-')
        plt.plot(x3new,f(x3new), color = 'magenta', linestyle = '--')
        plt.legend(['original','splie with a linspace from 10e-2 to 10e3/15 of 10e5' ], loc='best')
        ############################################################################
        plt.subplot(414)
        plt.plot(X,Y,color = 'blue', linestyle = '-')
        plt.plot(x4new,f(x4new), color = 'cyan', linestyle = '--')
        plt.legend(['original','splie with a linspace from 10e-2 to 10e3/15 of 10e5' ], loc='best')
        ############################################################################  
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        plt.title('fEpsilon')
        plt.show()
    except ValueError:
        print 'Please check the values of your module by this exception:'
        raise    

#fEpsilonCo()
fEpsilon()
