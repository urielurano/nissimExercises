from math import *
from scipy.interpolate import interp1d, pchip, InterpolatedUnivariateSpline, Rbf
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

    plt.plot(X,Y,linestyle = '-')
    plt.plot(x_new,f1(x_new), linestyle = '--')
    plt.legend(['original','spline interp1d with a kind '+kind], loc='best')
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
    set1 = set(['function','epsilon','smooth'])
    set2 = set(param.keys())
    set3 = set1.intersection(set2)
    name,smth,epsi='   '
    #I'm going to call to rbf with the wanted param
    #for this I make sets with the possible call of
    #the original rbf 
    if(len(set3) > 0):
        if(set3 == set(['function','epsilon', 'smooth'])):
            rbf1 = Rbf(X,Y,function=param['function'],epsilon=param['epsilon'],smooth=param['smooth'])
            name = param['function']
            epsi = str(param['epsilon'])
            smth = str(param['smooth'])
            
        if(set3 == set(['epsilon', 'smooth'])):
            rbf1 = Rbf(X,Y,epsilon=param['epsilon'],smooth=param['smooth'])
            epsi = str(param['epsilon'])
            smth = str(param['smooth'])
                
        if(set3 == set(['function', 'smooth'])):
            rbf1 = Rbf(X,Y,function=param['function'],smooth=param['smooth'])
            name = param['function']
            smth = str(param['smooth'])
            
        if(set3 == set(['function','epsilon'])):
            rbf1 = Rbf(X,Y,function=param['function'],epsilon=param['epsilon'])
            name = param['function']
            epsi = str(param['epsilon'])
            
        if(set3 == set(['function'])):
            rbf1 = Rbf(X,Y,function=param['function'])
            name = param['function']
                
        if(set3 == set(['epsilon'])):
            rbf1 = Rbf(X,Y,epsilon=param['epsilon'])
            epsi = str(param['epsilon'])

        if(set3 == set(['smooth'])):
            rbf1 = Rbf(X,Y,smooth=param['smooth'])
            smth = str(param['smooth'])
    else:
        rbf1 = Rbf(X,Y)
    #Now im going to graph
    plt.figure()
    fi1 = rbf1(x_new)
    plt.plot(X,Y, color = 'blue', linestyle = '-')
    plt.plot(x_new, fi1, color = 'red', linestyle = '--')
    plt.legend(['original', 'Spline rbf with function='+name+' epsilon='+epsi+' with smooth='+
                smth], loc = 'best')
    plt.ylabel(r'epsilon', size = 12)
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log') 
    plt.show()


