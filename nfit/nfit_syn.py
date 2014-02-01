from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F,TFile,TGraphErrors, TGraph, gStyle, gPad, TMarker, TMultiGraph
from ROOT import gROOT
from array import array
import os
import ROOT as rt
import numpy as np
import matplotlib.pyplot as plt
from sys import *

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
gStyle.SetFrameFillColor(0);
gStyle.SetCanvasBorderMode(0);

gStyle.SetOptFit(111111)
mg = TMultiGraph()

saves = {}
NP = 0
NP1 = 0
canvas = -1


##################################################################################
##################### Generating synchrotron plot  ###############################
##################################################################################


def xx(aa,bb, cc):
    outspec = open("nsyn.dat","w")

    ax=aa*1e-12
    E_c=bb*1e-5
    E_m=cc*1e-6
    fl=ax
    for ii in arange(-6.3, -1.0, 0.22):
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



##################################################################################
##################### Fitting synchrotron plot  ##################################
##################################################################################




def make_plot1():
    global saves    
    global NP1
 
    x1 = []
    y1 = []
    xe1 = []
    ye1 = []

    filename1 = "/home/antonio/nissimExercises/nfit/nlob_syn.dat"
    ifile = open(filename1,"r")
    if ifile:
        for line in ifile:
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
        wx=[1.64598842e-07, 1.21091811e-04]
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
        
        mg.Add(gr21)        
        mg.Add(gr1)
        mg.Draw('APE')
        saves['gr1'] = gr1

        gPad.SetLogx()
        gPad.SetLogy()
        gPad.Update()
        print min(x1), max(x1)
        mg.GetXaxis().SetTitle('Energy (eV)')
        mg.GetYaxis().SetTitle('vFv (erg cm^{-2} s^{-1})')

        mg.SetTitle('')
        fun1 = TF1('fun1','[0]*1e-12*(((x/([2]*1e-6))^(4/3)*(x>1.5e-6)*(x<([2]*1e-6)))+((x/([2]*1e-6))**((3-2.52)/2)*(x>=([2]*1e-6))*(x<[1]*1e-5)) + (([1]*10/([2]))**((3-2.52)/2)*(x/([1]*1e-5))**((2-2.52)/2))*(x>=[1]*1e-5)*(x<3e-4))', min(x1), max(x1))

        fun1.SetParameter(0,1)
        fun1.SetParLimits(0,1,1.2)
        fun1.SetParameter(1,5.7)
        fun1.SetParLimits(1,5.7,6.3)
        fun1.SetParameter(2,2.6)
        fun1.SetParLimits(2,2.6,2.63)

        gr1.Fit('fun1',"Q")
        fun1.Draw('L same')

        
        print ""  
        print("There are %d data points") %NP1
        print ("P0: %2.2E +/- %2.2E") %(fun1.GetParameter(0), fun1.GetParError(0))
        print ('Chi square: %2.3f  NDF:%2.2f') %(fun1.GetChisquare(),fun1.GetNDF())
        print ("P1: %2.2f +/- %2.2f") %(fun1.GetParameter(1), fun1.GetParError(1))
        print ('Chi square: %2.3f  NDF:%2.2f') %(fun1.GetChisquare(),fun1.GetNDF())
        print ("P2: %2.2f +/- %2.2f") %(fun1.GetParameter(2), fun1.GetParError(2))
        print ('Chi square: %2.3f  NDF:%2.2f') %(fun1.GetChisquare(),fun1.GetNDF())

        xx(fun1.GetParameter(0), fun1.GetParameter(1), fun1.GetParameter(2))

if __name__ == '__main__':
    make_plot1()
