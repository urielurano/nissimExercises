
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
        #Here we make the spline of the function
        x_new = np.linspace(10e-2,(10e2)/2,10e3) 
        f = interp1d(X, Y, kind='cubic')
        plt.plot(X,Y, color = 'blue', linestyle = '-')
        plt.plot(x_new,f(x_new), color = 'red', linestyle = '--')
        plt.legend(['original','spline cubic'], loc='best')
        plt.ylabel(r'epsilon', size=12)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
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
        x_new = np.linspace(10e-2, (10e3)/15)#check here  || 10e6
        '''
        #########################################################
        ################Make here the spline interp1d############
        #########################################################

        f1 = interp1d(X, Y, kind='linear')
        f2 = interp1d(X, Y, kind='nearest')
        f3 = interp1d(X, Y, kind='zero')
        f4 = interp1d(X, Y, kind='slinear')
        f5 = interp1d(X, Y, kind='quadratic')
        f6 = interp1d(X, Y, kind='cubic')
        str1 = 'spline with interp1d linear'
        str2 = 'spline with interp1d nearest'
        str3 = 'spline with interp1d zero'
        str4 = 'spline with interp1d slinear'
        str5 = 'spline with interp1d quadratic'
        str6 = 'spline with interp1d cubic'
        plt.figure(0)
        plt.subplot(231)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,f1(x_new), color = 'black', linestyle = '--')
        plt.legend(['original',str1], loc=8)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        plt.subplot(232)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,f2(x_new), color = 'green', linestyle = '--')
        plt.legend(['original',str2], loc=8)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        plt.subplot(233)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,f3(x_new), color = 'orange', linestyle = '--')
        plt.legend(['original',str3], loc=8)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        plt.subplot(234)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,f4(x_new), color = 'cyan', linestyle = '--')
        plt.legend(['original',str4], loc=8)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        plt.subplot(235)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,f5(x_new), color = 'magenta', linestyle = '--')
	a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.legend(['original',str5], loc=8)
        plt.subplot(236)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,f6(x_new), color = 'red', linestyle = '--')
        plt.legend(['original',str2], loc=8)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)

        ####################Now, all the plots in one############################
        
        plt.figure(1)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,f1(x_new), color = 'black', linestyle = '--')
        plt.plot(x_new,f2(x_new), color = 'green', linestyle = '--')
        plt.plot(x_new,f3(x_new), color = 'orange', linestyle = '--')
        plt.plot(x_new,f4(x_new), color = 'cyan', linestyle = '--')
        plt.plot(x_new,f5(x_new), color = 'magenta', linestyle = '--')
        plt.plot(x_new,f6(x_new), color = 'red', linestyle = '--')
        plt.legend(['original',str1,str2,str3,str4,str5,str6], loc='best')
        plt.xlim(0,10e2)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        
        #########################################################################
        ######Second spline, here we use the interpolated UnivariateSpline#######
        #########################################################################

        s1 = InterpolatedUnivariateSpline(X,Y,k = 1)
        y21_new = s1(x_new)
        s2 = InterpolatedUnivariateSpline(X,Y,k = 2)
        y22_new = s2(x_new)
        s3 = InterpolatedUnivariateSpline(X,Y,k = 3)
        y23_new = s3(x_new)
        s4 = InterpolatedUnivariateSpline(X,Y,k = 4)
        y24_new = s4(x_new)
        s5 = InterpolatedUnivariateSpline(X,Y,k = 5)
        y25_new = s5(x_new)
        str1 = 'Spline with UnivariateSpline with k = 1'
        str2 = 'Spline with UnivariateSpline with k = 2'
        str3 = 'Spline with UnivariateSpline with k = 3'
        str4 = 'Spline with UnivariateSpline with k = 4'
        str5 = 'Spline with UnivariateSpline with k = 5'

        plt.figure(2)
        plt.subplot(231)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,y21_new, color = 'black', linestyle = '--')
        plt.legend(['original',str1], loc=8)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        plt.subplot(232)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,y22_new, color = 'green', linestyle = '--')
        plt.legend(['original',str2], loc=8)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        plt.subplot(233)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,y23_new, color = 'orange', linestyle = '--')
        plt.legend(['original',str3], loc=8)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        plt.subplot(234)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,y24_new, color = 'cyan', linestyle = '--')
        plt.legend(['original',str4], loc=8)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        plt.subplot(235)
        plt.plot(X,Y,color = 'blue',linestyle = '-')
        plt.plot(x_new,y25_new, color = 'magenta', linestyle = '--')
        plt.legend(['original',str5], loc=8)
        a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)

        #######################Now, all in one######################################
        plt.figure(3)
        plt.plot(X,Y, color = 'blue', linestyle = '-')
        plt.plot(x_new,y21_new, color = 'black', linestyle = '--')
	plt.plot(x_new,y22_new, color = 'green', linestyle = '--')
	plt.plot(x_new,y23_new, color = 'orange', linestyle = '--')
	plt.plot(x_new,y24_new, color = 'cyan', linestyle = '--')
	plt.plot(x_new,y25_new, color = 'magenta', linestyle = '--')
        plt.legend(['original',str1,str2,str3,str4,str5], loc = 'best')
        plt.ylabel(r'epsilon', size = 12)
	a=plt.gca()
        a.set_yscale('log')
        a.set_xscale('log')
        plt.ylabel(r'epsilon', size=12)
        '''

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

#fEpsilonCo()
fEpsilon()
