from math import *
from scipy.interpolate import interp1d, pchip, InterpolatedUnivariateSpline, Rbf
import numpy as np
import matplotlib.pyplot as plt

@staticmethod
def interp1dPlot(X, Y, Z):
    '''Make here the spline interp1d plot'''
    x_new = np.linspace(10e-2, (10e3)/15)#check here  || 10e6
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
    
@staticmethod
def UnivariateSplinePlot(X, Y)
    
