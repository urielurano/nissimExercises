from math import *
from scipy.interpolate import interp1d, pchip, InterpolatedUnivariateSpline, Rbf
import numpy as np
import matplotlib.pyplot as plt


def interp1dPlot(X, Y, x_new):

    '''Make the plot of a interpolated function with interp1d'''

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
    plt.figure()
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
    plt.show()
    
    ####################Now, all the plots in one############################
    
    plt.figure()
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
    plt.show()
    

def UnivariateSplinePlot(X, Y, x_new):
    
    '''Make the plot of a interpolated function with UnivariateSpline'''
    
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
    
    plt.figure()
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
    plt.show()
    
    #######################Now, all in one######################################
    plt.figure()
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
    plt.show()


def rbfplot(X, Y, x_new, **param):

    '''Make the plot of a interpolated function with Rbf'''

            

    plt.figure()
    #plt.subplot(231) 
    #rbf1 = Rbf(X,Y, function = 'multiquadric',epsilon = 10e-1, smooth = 10e-10)
    #rbf1 = Rbf(X,Y, function = 'multiquadric')
    rbf1 = Rbf(X,Y, function = 'multiquadric', smooth = 10e-10, epsilon = 10e-1)
    fi1 = rbf1(x_new)
    plt.plot(X,Y, color = 'blue', linestyle = '-')
    plt.plot(x_new, fi1, color = 'red', linestyle = '--')
    plt.legend(['original', 'Spline with rbf multicuadratic'], loc = 'best')
    plt.ylabel(r'epsilon', size = 12)
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log') 
    '''
    plt.figure(5)#delete this line
    #plt.subplot(232)
    rbf2 = Rbf(X,Y, function = 'inverse')
    fi2 = rbf2(x_new)
    plt.plot(X,Y, color = 'blue', linestyle = '-')
    plt.plot(x_new, fi2, color = 'green', linestyle = '--')
    plt.legend(['original', 'Spline with rbf inverse'], loc = 'best')
    #a=plt.gca()
    #a.set_yscale('log')
    #a.set_xscale('log')
    plt.ylabel(r'epsilon', size = 12)
    '''
    plt.show()


