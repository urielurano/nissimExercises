
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


########################################################################################
##############            Fisrt Module                  ################################
########################################################################################

def sync(As,alpha, Em_s, Ec_s):

    '''Make a dat file with the fitted points '''

    outspec = open("syn.dat","w")
    Acs=As
    alp=alpha
    Ems=Em_s
    Ecs=Ec_s
    for ii in arange(-6.0, 1.5, 0.01):
        Ega0=pow(10,ii)
        Egamma=Ega0
        C1=0
        C2=0
        C3=0
        if(Egamma < Ems):
            C1=Acs*pow(Egamma/Ems,4.0/3.0)
        if(Ems <= Egamma and  Egamma < Ecs ):
            C2=Acs*pow(Egamma/Ems,-(alp-3.0)/2.0)
        if(Egamma >=Ecs):
            C3=Acs*pow(Ecs/Ems,-(alp-3.0)/2)*pow(Egamma/Ecs,-(alp-2.0)/2.0)
        C=C1+C2+C3

        outspec.write("%E %E\n" %(Ega0,C))

    outspec.close()


def comp(Ac,alpha,Em_c,Ec_c):

    '''Make a dat file with the fitted points '''

    outspec = open("comp.dat","w")
    Acc=Ac
    alp=alpha
    Emc=Em_c
    Ecc=Ec_c
    for ii in arange(4.0, 12.0, 0.01):
        Ega0=pow(10,ii)
        Egamma=Ega0
        C1=0
        C2=0
        C3=0
        if(Egamma < Emc):
            C1=Acc*pow(Egamma/Emc,4.0/3.0)
        if(Emc <= Egamma and  Egamma < Ecc ):
            C2=Acc*pow(Egamma/Emc,-(alp-3.0)/2.0)
        if(Egamma >=Ecc):
            C3=Acc*pow(Ecc/Emc,-(alp-3.0)/2)*pow(Egamma/Ecc,-(alp-2.0)/2.0)
        C=C1+C2+C3

        outspec.write("%E %E\n" %(Ega0,C))

    outspec.close()



##########################################################################################
####################### Second Module of the program #####################################
##########################################################################################

def make_SplinePlot():

    ''' Make the spline of the plot '''

    XS, YS = loadtxt('/home/antonio/nissimExercises/NGC1275/syn.dat', unpack = True)
    XC, YC = loadtxt('/home/antonio/nissimExercises/NGC1275/comp.dat', unpack = True)

    

##########################################################################################
######################## Third Module of the program #####################################
##########################################################################################


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

        fun4 = rt.TF1("fun4"," [0]*((x/[2])^(4/3)*(x>1e-6)*(x<[2])+((x/[2])**((3-[1])/2)*(x>=[2])*(x<[3])) + (([3]/[2])**((3-[1])/2))*((x/[3])**((2-[1])/2))*(x>=[3])*(x<30))",  1e-6,30)
        rt.fun4.SetParameter(1,2.5);
        rt.fun4.SetParLimits(1,2,3);
        rt.fun4.SetParameter(2,1e-4);
        rt.fun4.SetParLimits(2,1e-5,1e-3);
        rt.fun4.SetParameter(3,1);
        rt.fun4.SetParLimits(3,1e-1,5);
        rt.fun4.SetParameter(4,100);
        
        graph.Fit('fun4',"Q")                                                                                                                                                                  
        rt.fun4.Draw('L same') 

        a_s = rt.fun4.GetParameter(0)
        alfa = rt.fun4.GetParameter(1)
        em_s = rt.fun4.GetParameter(2)
        ec_s = rt.fun4.GetParameter(3)

        fun2 = rt.TF1("fun2"," [0]*((x/[1])^(4/3)*(x>1e-6)*(x<[1])+((x/[1])**((3-[3])/2)*(x>=[1])*(x<[2])) + (([2]/[1])**((3-[3])/2))*((x/[2])**((2-[3])/2))*(x>=[2]))",1e+4,1e+12)
        rt.fun2.SetParameter(0,6.32041e-07)
        rt.fun2.SetParameter(1,1e+6)
        rt.fun2.SetParLimits(1,1e+5,1e+7)
        rt.fun2.SetParameter(2,5e+7)
        rt.fun2.SetParLimits(2,1e+7,1e+9)
        rt.fun2.SetParameter(3, alfa)
        rt.fun2.SetParLimits(3,alfa, alfa)
        
        rt.fun2.SetLineColor(2)
        rt.fun2.SetLineWidth(2)
        graph.Fit('fun2',"Q")
        rt.fun2.Draw('L same')

        a_c = rt.fun2.GetParameter(0)
        em_c = rt.fun2.GetParameter(1)
        ec_c = rt.fun2.GetParameter(2)
	

	sync(a_s, alfa, em_s, ec_s)
	comp(a_c, alfa, em_c, ec_c)

        
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
    
    XS, YS = loadtxt('/home/antonio/nissimExercises/NGC1275/syn.dat', unpack = True)
    XC, YC = loadtxt('/home/antonio/nissimExercises/NGC1275/comp.dat', unpack = True)
    

    plt.figure('Experiments')
    
    plt.errorbar(X,Y, Y_arr, Y_aba, linestyle="none", marker="o", color="green", markersize=4.0, capsize=3.0, label = '1')
    plt.errorbar(X1,Y1, Y1_arr, Y1_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '2')
    plt.errorbar(X2,Y2, Y2_arr, Y2_aba, linestyle="none", marker="o", color="red", markersize=4.0, capsize=3.0, label = '3')
    plt.errorbar(X3,Y3, Y3_arr, Y3_aba, linestyle="none", marker="o", color="yellow", markersize=4.0, capsize=3.0, label = '4')
    plt.errorbar(X4,Y4, Y4_arr, Y4_aba, linestyle="none", marker="o", color="black", markersize=4.0, capsize=3.0, label = '5')
    plt.errorbar(X5,Y5, Y5_arr, Y5_aba, linestyle="none", marker="o", color="orange", markersize=4.0, capsize=3.0, label = '6')
    plt.errorbar(X6,Y6, Y6_arr, Y6_aba, linestyle="none", marker="o", color="pink", markersize=4.0, capsize=3.0, label = '7')
    plt.errorbar(X7,Y7, Y7_arr, Y7_aba, linestyle="none", marker="o", color="magenta", markersize=4.0, capsize=3.0, label = '8')
    plt.plot(XS,YS)
    plt,plot(XC,YC)

    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')

    plt.show()








files = ['FERMI.dat', 'magic.dat', 'MisuMe.dat', 'mojave.dat', 'ratan.dat', 'Swift_uvot.dat',
         'unkown.dat', 'butterfly.dat']

#makeFit(files)
#showMathPlotlib()
make_SplinePlot()
