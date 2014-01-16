from math import *
from scipy.interpolate import interp1d, pchip, InterpolatedUnivariateSpline, Rbf
import numpy as np
import matplotlib.pyplot as plt

def _fEpsilonCointerp1d(X, Y):
    '''Make the graph of the spline interp1d of fEpsilonCo'''
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
