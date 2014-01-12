from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F,TFile,TGraphErrors, TGraph, gStyle, gPad, TMarker, TMultiGraph
from ROOT import gROOT
from array import array
import os
import ROOT as rt
import numpy as np
import matplotlib.pyplot as plt
#import os
from sys import *
#from os import *

from pylab import *
from math import *
from scipy.interpolate import interp1d
from scipy.interpolate import pchip
from scipy import interpolate

gROOT.Reset()


gStyle.SetFillColor(0)
gStyle.SetPadLeftMargin(.20)
gStyle.SetPadBottomMargin(.20)
gStyle.SetCanvasColor(10)
mg = TMultiGraph()

saves = {}


NP = 0
NP1 = 0


canvas = -1
#MAXNMC = 10000



        

def Par1(a,b,c):
    x,y,xerr,yerr=loadtxt('/Users/nifraija/Desktop/2013/recover/FRI/CenA_I/north_lobe/nlob_pp.dat',unpack=True)
    x1,y1,xerr1,yerr1=loadtxt('/Users/nifraija/Desktop/2013/recover/FRI/CenA_I/north_lobe/nlob_syn.dat',unpack=True)

    x4,y4=loadtxt('/Users/nifraija/Desktop/py/syn.dat',unpack=True)

    s = interpolate.InterpolatedUnivariateSpline(x1,y1,k=3)
    #f2 = interp1d(x4, y4, kind='nearest')
    xnew=np.linspace(6e-7, 6e-4, 100)
    ynew=s(xnew)
    #    xnew = np.linspace(min(x4), max(x4), 100) # you can change the 100 here to a smaller number if you want less 'smoothness'

    #interp = pchip(x1, y1)
    #xx = np.linspace(7e-7, 1e-3, 1001)

# Plot it all.

    
    x2=[7e-7]
    y2=[1e-13]
    
    x3=[3e10]
    y3=[1e-13]
    
    
    plt.title("Simple plot")
#adjust plot
    plt.subplots_adjust(left=0.19)


    #    plt.errorbar(x1,y1,yerr1, ls='none', color='b', marker='o', elinewidth=1)

#plot data

    plt.figure() 

#plot only errorbars
    plt.errorbar(x1, y1, yerr1, linestyle="none", marker="o", color="green", markersize=4.0, capsize=3.0, label='1')
    plt.errorbar(x, y, yerr, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=5.0, label='2')
    plt.plot(x2,y2)
    plt.plot(x3,y3)
    plt.plot(xnew, ynew, 'r')
    #plt.plot(xx, interp(xx))
    #plt.plot(x4, y4,linestyle="-")
    #    plt.plot(x4,y4,'o',xnew, f2(xnew),'--')

    plt.legend()
#labels
    plt.xlabel("this is X", size=12)
    plt.ylabel("this is Y", size=12)



    a=plt.gca() 

    #    a=plt.show()
    a.set_xscale('log') 
    a.set_yscale('log') 

    plt.ylim(1e-13,1e-10)
    plt.show()



def xx(aa,xmin, xmax):
    outspec = open("syn.dat","w")

    ax=aa
    E_c=3.48e-5
    E_m=2.3e-6
    fl=ax
    for ii in arange(-6.3, -1.0, 1.1):
        Ega0=pow(10,ii)
        Egamma=Ega0
        C1=0
        C2=0
        C3=0
        if(Egamma < E_m):
            C1=fl*pow(Egamma/E_m,4.0/3.0)
        if(E_m <= Egamma and  Egamma < E_c ):
            C2=fl*pow(Egamma/E_m,-(2.52-3.0)/2.0)
        if(Egamma >=E_c):
            C3=fl*pow(E_c/E_m,-(2.52-3.0)/2)*pow(Egamma/E_c,-(2.52-2.0)/2.0)
        C=C1+C2+C3

        outspec.write("%E %E\n" %(Ega0,C))   

    outspec.close()







def make_plot1():
    global saves
    
    global NP1
 

    #global MAXNMC

    x1 = []
    y1 = []
    xe1 = []
    ye1 = []

    filename1 = "/Users/nifraija/Desktop/2013/recover/FRI/CenA_I/north_lobe/nlob_syn.dat"
    ifile = open(filename1,"r")
    if ifile:
        for line in ifile:
            #print line
            a1,b1,c1,d1 = [float(t) for t in line.split()]
            x1.append(a1)
            y1.append(b1)
            xe1.append(c1)
            ye1.append(d1)
            NP1 = NP1 + 1

        
        X1 = np.array(x1,float)
        XE1 = np.array(xe1,float)
        Y1 = np.array(y1,float)
        YE1 = np.array(ye1,float)

        gr1 = TGraphErrors(NP1,X1,Y1,XE1,YE1)
        gr1.SetMarkerSize(0.7)
        gr1.SetMarkerStyle(4)
        gr1.SetMarkerColor(4)


        n1=2
        wx=[5.64598842e-07, 2.21091811e-04]
        wy=[1.64598842e-13, 1.21091811e-11]
        wex=[0,0]
        wey=[0,0]
        Wx = np.array(wx,float)
        Wy = np.array(wy,float)
        Wex = np.array(wex,float)
        Wey = np.array(wey,float)

        gr21= TGraphErrors(n1,Wx,Wy,Wex,Wey)
        gr21.SetMarkerColor()
        gr21.SetMarkerStyle(8)
        gr21.SetMarkerSize(0.0001)  
        gr21.SetLineColor(3)
        #gPad.SetLogy();  
        #gPad.SetLogx();
        #gr21.SetFillColor(2) 


        

        mg.Add(gr21)        
        mg.Add(gr1)
        mg.Draw('APE')
        saves['gr1'] = gr1

        gPad.SetLogx()
        gPad.SetLogy()
        gPad.Update()

        #mg.GetXaxis().CenterTitle(1)
        #mg.Getyaxis().CenterTitle(1)

        mg.GetXaxis().SetTitle('Energy (eV)')
        mg.GetYaxis().SetTitle('vFv (erg cm^{-2} s^{-1})')
        #print min(x1), max(x1) 

        mg.SetTitle('')
        fun1 = TF1('fun1','[0]*(((x/2.3e-6)^(4/3)*(x>1e-6)*(x<2.3e-6))+((x/2.3e-6)**((3-2.52)/2)*(x>=2.3e-6)*(x<3.48e-5)) + ((3.48e-5/2.3e-6)**((3-2.52)/2)*(x/3.48e-5)**((2-2.52)/2))*(x>=3.48e-5)*(x<1e-4))', min(x1), max(x1))
        gr1.Fit('fun1',"Q")
        #mg.SetLineColor(6) 
        fun1.Draw('L same')


        #[0]*(((x/3.6e-6)^(4/3)*(x>1e-6)*(x<3.6e-6))+((x/3.6e-6)**((3-2.52)/2)*(x>=3.6e-6)*(x<3.48e-5)) + ((3.48e-5/3.6e-6)**((3-2.52)/2)*(x/3.48e-5)**((2-2.52)/2))*(x>=3.48e-5)*(x<1e-4))

        
        print ""  
        print("There are %d data points") %NP1
        print ("P0: %2.2E +/- %2.2E") %(fun1.GetParameter(0), fun1.GetParError(0))
        print ('Chi square: %2.3f  NDF:%2.2f') %(fun1.GetChisquare(),fun1.GetNDF())
        #print ("P1: %2.2f +/- %2.2f") %(fun1.GetParameter(1), fun1.GetParError(1))
        #print ('Chi square: %2.3f  NDF:%2.2f') %(fun1.GetChisquare(),fun1.GetNDF())

        xx(fun1.GetParameter(0), min(x1), max(x1))
        Par1(fun1.GetParameter(0), min(x1), max(x1))

        #Par(fun.GetParameter(0), fun.GetParameter(1), min(x), max(x))

if __name__ == '__main__':
    make_plot1()



#plt.xticks([1e-6,0,1e4,1e11])

#configure  Y axes
#plt.ylim(1e-14,1e-9)
#plt.yticks([1e-14, 3e-9, 5e-7, 7e-9])


#title
#plt.plot(x, y, linestyle="dashed", marker="o", color="green")
