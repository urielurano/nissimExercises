from math import *
from scipy.interpolate import interp1d, InterpolatedUnivariateSpline, Rbf,PchipInterpolator, pchip
from scipy.optimize import leastsq
import numpy as np
import matplotlib.pyplot as plt


def interp1dPlot(X, Y, x_new, **args):

    '''Make the plot of a interpolated function with interp1d'''

    set1 = set(['kind', 'wn'])
    set2 = set(args.keys())
    set3 = set1.intersection(set2)
    kind = 'with a kind '
    title = 'interp1d_spline_plot'
    if('kind' in set3):
        f1 = interp1d(X, Y, kind=args['kind'])
        kind = kind+args['kind']
    else:
        f1 = interp1d(X, Y)
    if('wn' in set3):
        if(type(args['wn']) == int):
            title = title + str(args['wn'])
            plt.figure(title)            
        else:
            print 'wn is an integer necessary'
    else:
        plt.figure(title)

    plt.plot(X,Y,linestyle = '-')
    plt.plot(x_new,f1(x_new), linestyle = '--')
    plt.legend(['original','spline interp1d '+kind], loc='best')
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')
    plt.ylabel(r'epsilon', size=12)
    plt.show()
    #Here Im going to save the file on disk if the                                                                                                
    #user want 
    if('save' in set2):
        if(type(args['save']) == bool and args['save'] ==  True):
            plt.savefig(title.strip()+'.png')
            plt.draw()
    

def UnivariateSplinePlot(X, Y, x_new, **args):
    
    '''Make the plot of a interpolated function with UnivariateSpline'''

    set1 = set(['k','wn'])
    set2 = set(args.keys())
    set3 = set1.intersection(set2)
    value = 'with k value = '
    title = 'Univariate_Spline_Plot'
    if('k' in set3):
        if(args['k']<= 5 and args['k'] >= 1 and type(args['k']) == int):
            s = InterpolatedUnivariateSpline(X,Y,k = args['k'])
            value = value+str(args['k'])
        else:
            s = InterpolatedUnivariateSpline(X,Y)
            value = '(check the value of k must be int 1<=k<=5)'
            
    else:
        s = InterpolatedUnivariateSpline(X,Y)

    if('wn' in set3):
        if(type(args['wn']) == int):
            title = title+str(args['nw'])
            plt.figure(title)
        else:
            print 'wn is an integer necessary'
    else:
        plt.figure(title)

    y_new = s(x_new)
    plt.plot(X,Y, linestyle = '-')
    plt.plot(x_new,y_new, linestyle = '--')
    plt.legend(['original','Univariate Spline '+value],loc='best')
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')
    plt.ylabel(r'epsilon', size=12)
    plt.show()
    #Here Im going to save the file on disk if the
    #user want
    if('save' in set2):
        if(type(args['save']) == bool and args['save'] ==  True):
            plt.savefig(title.strip()+'.png')
            plt.draw()



def rbfplot(X, Y, x_new, **args):

    '''Make the plot of a interpolated function with Rbf'''

    set1 = set(['function','epsilon','smooth','wn'])
    set2 = set(args.keys())
    set3 = (set1.intersection(set2)).difference(set(['wn']))
    name,epsi,smth='   '
    title = 'Rbf_plot'
    if(len(set3) > 0):
        if(set3 == set(['function','epsilon', 'smooth'])):
            rbf1 = Rbf(X,Y,function=args['function'],epsilon=args['epsilon'],smooth=args['smooth'])
            name = ' with a function '+args['function']
            epsi = ' with a epsilon value '+str(args['epsilon'])
            smth = ' with a smooth value '+str(args['smooth'])
            
        if(set3 == set(['epsilon', 'smooth'])):
            rbf1 = Rbf(X,Y,epsilon=args['epsilon'],smooth=args['smooth'])
            epsi = ' with a epsilon value '+str(args['epsilon'])
            smth = ' with a smooth value '+str(args['smooth'])
                
        if(set3 == set(['function', 'smooth'])):
            rbf1 = Rbf(X,Y,function=args['function'],smooth=args['smooth'])
            name = ' with a function '+args['function']
            smth = ' with a smooth value '+str(args['smooth'])
            
        if(set3 == set(['function','epsilon'])):
            rbf1 = Rbf(X,Y,function=args['function'],epsilon=args['epsilon'])
            name = ' with a function '+args['function']
            epsi = ' with a epsilon value '+str(args['epsilon'])
            
        if(set3 == set(['function'])):
            rbf1 = Rbf(X,Y,function=args['function'])
            name = ' with a function '+args['function']
                
        if(set3 == set(['epsilon'])):
            rbf1 = Rbf(X,Y,epsilon=args['epsilon'])
            epsi = ' with a epsilon value '+str(args['epsilon'])

        if(set3 == set(['smooth'])):
            rbf1 = Rbf(X,Y,smooth=args['smooth'])
            smth = ' with a smooth value '+str(args['smooth'])
    else:
        rbf1 = Rbf(X,Y)

    if('wn' in set2):
        if(type(args['wn']) == int):
	    title = title+str(args['wn'])
            plt.figure(title)
        else:
            print 'wn is an integer necessary'
    else:
        plt.figure(title)

    fi1 = rbf1(x_new)
    plt.plot(X,Y, linestyle = '-')
    plt.plot(x_new, fi1, linestyle = '--')
    plt.legend(['original', 'Spline rbf '+name+epsi+smth], loc = 'best')
    plt.ylabel(r'epsilon', size = 12)
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log') 
    plt.show()
    #Here Im going to save the file on disk if the
    #user want
    if('save' in set2):
        if(type(args['save']) == bool and args['save'] ==  True):
            plt.savefig(title.strip()+'.png')
            plt.draw()


def PchipInterpolatorPlot(X,Y,x_new, **args): #WorkInProgress

    '''Make the plot of a interpolated function with pchip interpolate'''

    set1 = set(['axis'])
    set2 = set(args.keys())
    set3 = set1.intersection(set2)
    title = 'pchip_interpolator_plot'
    axis = ' '
    if(len(set3)>0):
        if(type(args['axis']) == int):
            pcp = PchipInterpolator(X,Y,axis = args['axis'])
            axis = 'axis with value = '+ str(args['axis'])
    else:
        pcp = PchipInterpolator(X,Y) 
    if('wn' in set3):
        if(type(args['wn']) == int):
	    title = title+str(args['nw'])
            plt.figure(title)
        else:
            print 'wn is an integer necessary'
    else:
        plt.figure(title)
    plt.plot(X,Y, linestyle = '-')
    plt.plot(x_new, pcp(x_new), linestyle = '--')
    plt.legend(['original', 'Spline pchip ' + axis], loc='best')
    plt.ylabel(r'epsilon', size = 12)
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')
    plt.show()
    #Here Im going to save the file on disk if the
    #user want
    if('save' in set2):
        if(type(args['save']) == bool and args['save'] ==  True):
            plt.savefig(title.strip()+'.png')
            plt.draw()



def pchipPlot(X, Y, x_new, **args):
    title = 'pchip_plot'
    if(args.has_key('wn')):
        if(type(args['wn']) == int):
	    title = title+str(args['wn'])
            plt.figure(title)
    else:
        plt.figure(title)
    pc = pchip(X,Y)
    plt.plot(X,Y, linestyle = '-')
    plt.plot(x_new, pc(x_new), linestyle = '--')
    plt.legend(['original', 'Spline pchip '], loc='best')
    plt.ylabel(r'epsilon', size = 12)
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')
    #plt.show()
    #Here Im going to save the file on disk if the
    #user want
    if(args.has_key('save')):
        if(type(args['save']) == bool and args['save'] ==  True):
            plt.savefig(title.strip()+'.png')
            plt.draw()
            #plt.show()


