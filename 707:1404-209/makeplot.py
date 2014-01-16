
from b import *
from math import *
from scipy.interpolate import interp1d, pchip, InterpolatedUnivariateSpline, Rbf
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
        _fEpsilonCointerp1d(X, Y)
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
        
        
        
        #################################################################
        ######################third spline, rbf##########################
        #################################################################

        ######################In subplots################################
        plt.figure(4)
        #plt.subplot(231) 
        rbf1 = Rbf(X,Y, function = 'multiquadric',epsilon = 10e-1, smooth = 10e-10)
        fi1 = rbf1(x_new)
        plt.plot(X,Y, color = 'blue', linestyle = '-')
        plt.plot(x_new, fi1, color = 'red', linestyle = '--')
        plt.legend(['original', 'Spline with rbf multicuadratic'], loc = 'best')
        plt.xlim(0,200)
        plt.ylim(-250,300)
        #a=plt.gca()
        #a.set_yscale('log')
        #a.set_xscale('log')
        #plt.ylabel(r'epsilon', size = 12)
        '''
        plt.figure(5)#delete this line
        #plt.subplot(232)
        rbf2 = Rbf(X,Y, function = 'inverse')
        fi2 = rbf2(x_new)
        plt.plot(X,Y, color = 'blue', linestyle = '-')
        plt.plot(x_new, fi2, color = 'green', linestyle = '--')
        plt.legend(['original', 'Spline with rbf inverse'], loc = 'best')
        plt.xlim(0,200)
        plt.ylim(-250,300)
        #a=plt.gca()
        #a.set_yscale('log')
        #a.set_xscale('log')
        plt.ylabel(r'epsilon', size = 12)
        '''
        plt.show()
    except ValueError:
        print 'Please check the values of your module by this exception:'
        raise    

fEpsilonCo()
#fEpsilon()
