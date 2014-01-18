from math import *
from scipy.interpolate import interp1d, InterpolatedUnivariateSpline, Rbf,PchipInterpolator
import numpy as np
import matplotlib.pyplot as plt


def interp1dPlot(X, Y, x_new, **args):

    '''Make the plot of a interpolated function with interp1d'''

    set1 = set(['kind'])
    set2 = set(args.keys())
    set3 = set1.intersection(set2)
    kind = 'linear'
    if(len(set3)>0):
        f1 = interp1d(X, Y, kind=args['kind'])
        kind = args['kind']
    else:
        f1 = interp1d(X, Y)
    
    plt.ion()
    plt.figure()
    plt.plot(X,Y,linestyle = '-')
    plt.plot(x_new,f1(x_new), linestyle = '--')
    plt.legend(['original','spline interp1d with a kind '+kind], loc='best')
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')
    plt.ylabel(r'epsilon', size=12)
    plt.show()
    

def UnivariateSplinePlot(X, Y, x_new, **args):
    
    '''Make the plot of a interpolated function with UnivariateSpline'''

    set1 = set(['k'])
    set2 = set(args.keys())
    set3 = set1.intersection(set2)
    value = ' '

    if(len(set3)>0):
        if(args['k']<= 5 and type(args['k']) == int):
            s = InterpolatedUnivariateSpline(X,Y,k = args['k'])
            value = str(args['k'])
        else:
            print('The value of k must be integer and minor equal than 5')
            
    else:
        s = InterpolatedUnivariateSpline(X,Y)

    y_new = s(x_new)
    plt.ion()
    plt.figure()
    plt.plot(X,Y, linestyle = '-')
    plt.plot(x_new,y_new, linestyle = '--')
    plt.legend(['original','Spline rbf with value k = '+value],loc='best')
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')
    plt.ylabel(r'epsilon', size=12)
    plt.show()


def rbfplot(X, Y, x_new, **args):

    '''Make the plot of a interpolated function with Rbf'''

    set1 = set(['function','epsilon','smooth'])
    set2 = set(args.keys())
    set3 = set1.intersection(set2)
    name,smth,epsi='   '
    if(len(set3) > 0):
        if(set3 == set(['function','epsilon', 'smooth'])):
            rbf1 = Rbf(X,Y,function=args['function'],epsilon=args['epsilon'],smooth=args['smooth'])
            name = args['function']
            epsi = str(args['epsilon'])
            smth = str(args['smooth'])
            
        if(set3 == set(['epsilon', 'smooth'])):
            rbf1 = Rbf(X,Y,epsilon=args['epsilon'],smooth=args['smooth'])
            epsi = str(args['epsilon'])
            smth = str(args['smooth'])
                
        if(set3 == set(['function', 'smooth'])):
            rbf1 = Rbf(X,Y,function=args['function'],smooth=args['smooth'])
            name = args['function']
            smth = str(args['smooth'])
            
        if(set3 == set(['function','epsilon'])):
            rbf1 = Rbf(X,Y,function=args['function'],epsilon=args['epsilon'])
            name = args['function']
            epsi = str(args['epsilon'])
            
        if(set3 == set(['function'])):
            rbf1 = Rbf(X,Y,function=args['function'])
            name = args['function']
                
        if(set3 == set(['epsilon'])):
            rbf1 = Rbf(X,Y,epsilon=args['epsilon'])
            epsi = str(args['epsilon'])

        if(set3 == set(['smooth'])):
            rbf1 = Rbf(X,Y,smooth=args['smooth'])
            smth = str(args['smooth'])
    else:
        rbf1 = Rbf(X,Y)
    
    
    plt.figure()
    fi1 = rbf1(x_new)
    plt.plot(X,Y, linestyle = '-')
    plt.plot(x_new, fi1, linestyle = '--')
    plt.legend(['original', 'Spline rbf with function='+name+' epsilon='+epsi+' with smooth='+
                smth], loc = 'best')
    plt.ylabel(r'epsilon', size = 12)
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log') 
    plt.show()

def PchipInterpolatorPlot(X,Y,x_new, **args): #WorkInProgress

    '''Make the plot of a interpolated function with UnivariateSpline'''

    set1 = set(['axis'])
    set2 = set(args.keys())
    set3 = set1.intersection(set2)
    axis = ' '
    if(len(set3)>0):
        if(type(args['axis']) == int):
            pchip = PchipInterpolator(X,Y,axis = args['axis'])
            axis = 'axis with value = '+ str(args['axis'])
    else:
        pchip = PchipInterpolator(X,Y) 

    
    plt.figure()
    plt.plot(X,Y, linestyle = '-')
    plt.plot(x_new, pchip(x_new),color = 'red', linestyle = ':')
    plt.legend(['original', 'Spline pchip ' + axis], loc='best')
    plt.ylabel(r'epsilon', size = 12)
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')
    plt.hold()
    plt.show()
