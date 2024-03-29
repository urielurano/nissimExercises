from b import *
from math import *
from makesplineplots import *
import numpy as np
	
def fEpsilonCo():
    '''We here make the plot of the function fEpsilonCo'''
    x = []
    y = []
    epsilonPhCo = En(Ec, r_star, gammac,alphar, thetac)
    fEpsilonPhCo = fcon(Ec, r_star, gammac,alphar, thetac)

    #Here make the aranges to make the plot
    for ii in np.arange(-1.0,3.0,0.2150):
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

        #########Call the plots here###########################
        '''
	x_new = np.linspace(10e-2, 20, 1000)
        interp1dPlot(X, Y, x_new, kind='quadratic', save = True)
        x_new = np.linspace(10e-2,20,100) 
        PchipInterpolatorPlot(X,Y,x_new, save = True)
       
        x_new = np.linspace(10e-2,20,100)
        rbfplot(X, Y, x_new, function='thin_plate', save = True)
        '''
        x_new = np.linspace(10e-2,1000,10000)
        UnivariateSplinePlot(X, Y, x_new, k = 2, save = True)
        '''
        x_new = np.linspace(10e-2,60,500)
        pchipPlot(X, Y, x_new, save = True)
        '''
        
        

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

    for ii in np.arange(-1.0,3.0,0.3):
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

	#CALL HERE THE PLOTS
        '''
        x_new = np.linspace(10e-2,100,100)
        PchipInterpolatorPlot(X,Y,x_new, save = True)
        x_new = np.linspace(10e-2,100,100)
        rbfplot(X, Y, x_new, function='quintic', save = True)
        x_new = np.linspace(10e-2,100,100) 
        UnivariateSplinePlot(X, Y, x_new, k = 4, save = True)
        '''
        x_new = np.linspace(10e-2,100,100)
        pchipPlot(X, Y, x_new, save = True)
        



    except ValueError:
        print 'Please check the values of your module by this exception:'
        raise    

if __name__ == '__main__':
    fEpsilonCo()
    #fEpsilon()
