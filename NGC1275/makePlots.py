#import numpy as np
#import ROOT as rt
#import matplotlib.pyplot as plt
#import sys, os
#from sys import *
#from os import *

from array import array
import os
import ROOT as rt
import numpy as np
import matplotlib.pyplot as plt
from sys import *
from pylab import *
from math import *
from makesplineplots import *






rt.gROOT.Reset()

rt.gStyle.SetFillColor(0)
rt.gStyle.SetPadLeftMargin(.20)
rt.gStyle.SetPadBottomMargin(.20)
rt.gStyle.SetCanvasColor(10)
rt.gStyle.SetFrameFillColor(0);
rt.gStyle.SetCanvasBorderMode(0);

rt.gStyle.SetOptFit(111111)
mg = rt.TMultiGraph()

saves = {}
NP = 0
NP1 = 0
canvas = -1

def makeFit(files):

    '''Read the .dat files to make the fit of the points'''
    
    global saves
    global NP1

    try:
        x1 = []
        y1 = []
        xizq = []
        xder = []
        yarr = []
        yaba = []
        mt = []
        separados = []
        
        path = '/home/antonio/nissimExercises/NGC1275/c_NGC1275/'
        i = 0;
        while(i < len(files)):
            pathFile = path + files[i]
            rfile = open(pathFile, 'r')
            if rfile:
                for line in rfile:
                    a, b, c, d, e, f = [float(t) for t in line.split()]
                    x1.append(a)
                    y1.append(b)
                    xizq.append(c)
                    xder.append(d)
                    yarr.append(e)
                    yaba.append(f)
            i = i+1
        ##Now we make the arrays of the points
        X = np.array(x1, float)
        Y = np.array(y1, float)
        Xizq = np.array(xizq, float)
        Xder = np.array(xder, float)
        Yarr = np.array(yarr, float)
        Yaba = np.array(yaba, float)
        
        ##Make the plots from root
        
        graph = rt.TGraphErrors(len(x1), X, Y, Xizq, Yarr)
        graph.SetMarkerSize(0.7)
        graph.SetMarkerStyle(4)
        graph.SetMarkerColor(4)
        
        mg.Add(graph)
        mg.Draw('APE')                                                                                                 
        saves['graph'] = graph
        rt.gPad.SetLogx()
        rt.gPad.SetLogy()
        rt.gPad.Update()

        mg.GetXaxis().SetTitle('Energy (eV)')
        mg.GetYaxis().SetTitle('vFv (erg cm^{-2} s^{-1})')

        fun1 = rt.TF1('fun1','[0]*1e-12*(((x/([2]*1e-6))^(4/3)*(x>1.5e-6)*(x<([2]*1e-6)))+((x/([2]*1e-6))**((3-2.52)/2)*(x>=([2]*1e-6))*(x<[1]*1e-5)) + (([1]*10/([2]))**((3-2.52)/2)*(x/([1]*1e-5))**((2-2.52)/2))*(x>=[1]*1e-5)*(x<3e-4))', min(x1), max(x1))
        
        
        rt.fun1.SetParameter(0,1)
        rt.fun1.SetParLimits(0,1,1.2)
        rt.fun1.SetParameter(1,5.7)
        rt.fun1.SetParLimits(1,5.7,6.3)
        rt.fun1.SetParameter(2,2.6)
        rt.fun1.SetParLimits(2,2.6,2.63)
        
        rt.fun1.SetLineColor(2)
        rt.fun1.SetLineWidth(2)
        graph.Fit('fun1',"Q")
        rt.fun1.Draw('L same')

        
    except:
        raise
        print 'Check the param of the code'
        

def showMathPlotlib():
    ''' Make the plot on matplotlib  '''

    X,Y, X_izq, X_der, Y_arr, Y_aba = loadtxt('/home/antonio/nissimExercises/NGC1275/c_NGC1275/FERMI.dat', unpack = True)
    X1,Y1, X1_izq, X1_der, Y1_arr, Y1_aba = loadtxt('/home/antonio/nissimExercises/NGC1275/c_NGC1275/magic.dat', unpack = True)
    X2,Y2, X2_izq, X2_der, Y2_arr, Y2_aba = loadtxt('/home/antonio/nissimExercises/NGC1275/c_NGC1275/MisuMe.dat', unpack = True)
    X3,Y3, X3_izq, X3_der, Y3_arr, Y3_aba = loadtxt('/home/antonio/nissimExercises/NGC1275/c_NGC1275/mojave.dat', unpack = True)
    X4,Y4, X4_izq, X4_der, Y4_arr, Y4_aba = loadtxt('/home/antonio/nissimExercises/NGC1275/c_NGC1275/ratan.dat', unpack = True)
    X5,Y5, X5_izq, X5_der, Y5_arr, Y5_aba = loadtxt('/home/antonio/nissimExercises/NGC1275/c_NGC1275/Swift_uvot.dat', unpack = True)
    X6,Y6, X6_izq, X6_der, Y6_arr, Y6_aba= loadtxt('/home/antonio/nissimExercises/NGC1275/c_NGC1275/unkown.dat', unpack = True)
    X7,Y7, X7_izq, X7_der, Y7_arr, Y7_aba= loadtxt('/home/antonio/nissimExercises/NGC1275/c_NGC1275/butterfly.dat', unpack = True)
    

    plt.figure('Experiments')
    
    plt.errorbar(X,Y, Y_arr, Y_aba, linestyle="none", marker="o", color="green", markersize=4.0, capsize=3.0, label = '1')
    plt.errorbar(X1,Y1, Y1_arr, Y1_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '2')
    plt.errorbar(X2,Y2, Y2_arr, Y2_aba, linestyle="none", marker="o", color="red", markersize=4.0, capsize=3.0, label = '3')
    plt.errorbar(X3,Y3, Y3_arr, Y3_aba, linestyle="none", marker="o", color="yellow", markersize=4.0, capsize=3.0, label = '4')
    plt.errorbar(X4,Y4, Y4_arr, Y4_aba, linestyle="none", marker="o", color="black", markersize=4.0, capsize=3.0, label = '5')
    plt.errorbar(X5,Y5, Y5_arr, Y5_aba, linestyle="none", marker="o", color="orange", markersize=4.0, capsize=3.0, label = '6')
    plt.errorbar(X6,Y6, Y6_arr, Y6_aba, linestyle="none", marker="o", color="pink", markersize=4.0, capsize=3.0, label = '7')
    plt.errorbar(X7,Y7, Y7_arr, Y7_aba, linestyle="none", marker="o", color="magenta", markersize=4.0, capsize=3.0, label = '8')

    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')

    plt.show()








files = ['FERMI.dat', 'magic.dat', 'MisuMe.dat', 'mojave.dat', 'ratan.dat', 'Swift_uvot.dat',
         'unkown.dat']

makeFit(files)
#showMathPlotlib()
