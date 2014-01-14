
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
<<<<<<< HEAD
        rw1=plt.plot(X,Y,color="green", linewidth=1.0, linestyle="-", label="E$_\pi$")
=======
        #Here we make the spline of the function
        Y1 = interp1d(X, Y, kind='cubic')
        plt.plot(X,Y, '-',X,Y1(X),'--')
        plt.legend(['original','spline cubic'], loc='best')
>>>>>>> issue1
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.xlabel(r'$\epsilon_B$', size=12)
        plt.ylabel(r'E$_\nu$ (eV)', size=12)
        plt.title('')
        plt.show()
    except ValueError:
<<<<<<< HEAD
        print 'Exception making the plot'
        raise

    #Here we make the spline of the function
    try:
        f = interp1d(X, Y)
=======
        print 'Please check the values of your module by this exception:'
        raise

>>>>>>> issue1


        
def fEpsilon():
    x = []
    y = []
    epsilonCSC = 0.1 #change this value
<<<<<<< HEAD
    epsilonASC = 1e4 #change this value
=======
    epsilonASC = 1e2 #change this value
>>>>>>> issue1
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
        x1new = np.linspace(10e-2, (10e3)/15)#check here
        x2new = np.linspace(10e-2, (10e3)/30)#check here
        x3new = np.linspace(10e-2, (10e3)/60)#check here
        x4new = np.linspace(10e-2, (10e3)/90)#check here 
        f = interp1d(X, Y, kind='cubic')
        plt.plot(X,Y,color = 'blue', linestyle = '-')
        plt.plot(x1new,f(x1new), color = 'red', linestyle = '--')
        plt.plot(x2new,f(x2new), color = 'green', linestyle = '--')
        plt.plot(x3new,f(x3new), color = 'magenta', linestyle = '--')
        plt.plot(x4new,f(x4new), color = 'black', linestyle = '--')
        str0 = 'original'
        str1 = 'spline cubic with a maximum (10e3)/15'
        str2 = 'spline cubic with a maximum (10e3)/30'
        str3 = 'spline cubic with a maximun (10e3)/60'
        str4 = 'spline cubic with a maximun (10e3)/90'
        plt.legend([str0, str1, str2, str3, str4], loc='best')
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        plt.title('fEpsilon')
        plt.show()
    except ValueError:
        print 'Please check the values of your module by this exception:'
        raise    

<<<<<<< HEAD

fEpsilonCo()
#fEpsilon()
=======
#fEpsilonCo()
fEpsilon()
>>>>>>> issue1
