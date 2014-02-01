from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F,TFile,TGraphErrors, TGraph, gStyle, gPad
from ROOT import gROOT
from array import array
import os
import ROOT as rt
import numpy as np
from pylab import *
from math import *
from sys import *

gROOT.Reset()

gStyle.SetFillColor(0)
gStyle.SetPadLeftMargin(.20)
gStyle.SetPadBottomMargin(.20)
gStyle.SetCanvasColor(10)
gStyle.SetOptFit(111111)

saves = {}
NP = 0
NP1 = 0
canvas = -1

##################################################################################
###################### Generating pp plot  #######################################
##################################################################################


def xx(ap,bp,xmin, xmax):
    outspec = open("npp.dat","w")
    ax=ap
    bx=bp
    for ii in arange(8.0, 10.0, 0.1):
        Ega0=pow(10,ii)
        Egamma=Ega0
        C=ax*((Ega0/1e9)**(2-bx))

        outspec.write("%E %E\n" %(Ega0,C))   

    outspec.close()



##################################################################################
###################### Making the plot on matplotlib #############################
##################################################################################




##################################################################################
###################### Fitting pp plot  ##########################################
##################################################################################

        
def make_plot():
    global saves
    global NP
 
    x = []
    y = []
    xe = []
    ye = []

    filename = "nlob_pp.dat"
    ifile = open(filename,"r")
    if ifile:
        for line in ifile:
            a,b,c,d = [float(t) for t in line.split()]
            x.append(a)
            y.append(b)
            xe.append(c)
            ye.append(d)
            NP = NP + 1
        
        X = np.array(x,float)
        XE = np.array(xe,float)
        Y = np.array(y,float)
        YE = np.array(ye,float)
        
        gr = TGraphErrors(NP,X,Y,XE,YE)
        gr.SetMarkerColor(1)
        gr.SetMarkerStyle(3)
        gr.SetMarkerSize(1)
        gr.Draw('APE')
        saves['gr'] = gr

        gPad.SetLogx()
        gPad.SetLogy()
        gPad.Update()

 
        gr.GetXaxis().SetTitle('Energy (eV)')
        gr.GetYaxis().SetTitle('vFv (erg cm^{-2} s^{-1})')
        

        gr.SetTitle('')
        fun = TF1('fun','[0]*((x/1e9)^(2-[1]))', min(x), max(x))
        gr.Fit('fun',"Q")
        fun.SetLineColor(6) 
        fun.Draw('L same')
        
        print ""  
        print("There are %d data points") %NP
        print ("P0: %2.2E +/- %2.2E") %(fun.GetParameter(0), fun.GetParError(0))
        print ('Chi square: %2.3f  NDF:%2.2f') %(fun.GetChisquare(),fun.GetNDF())
        print ("P1: %2.2f +/- %2.2f") %(fun.GetParameter(1), fun.GetParError(1))
        print ('Chi square: %2.3f  NDF:%2.2f') %(fun.GetChisquare(),fun.GetNDF())
        
        xx(fun.GetParameter(0), fun.GetParameter(1), min(x), max(x))

if __name__ == '__main__':
    make_plot()

