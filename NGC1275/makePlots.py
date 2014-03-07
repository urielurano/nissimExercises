import numpy as np
import ROOT as rt


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
        
    except:
        raise
        print 'Check the param of the code'
        


files = ['chandra.dat', 'FERMI.dat', 'HST-optical-UV.dat', 'magic.dat', 'MisuMe.dat', 'mojave.dat', 'ratan.dat', 'swift_bat.dat', 'Swift_uvot.dat',
         'unkown.dat']

makeFit(files)
