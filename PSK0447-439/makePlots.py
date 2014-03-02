import numpy as np
import ROOT as rt

def makeFit(filePath):

    '''Read the .dat files to make the fit of the points'''
    
    global saves
    global NP1

    try:
        x1 = []
        y1 = []
        rfile = open(filePath, 'r')
        if rfile:
            for line in rfile:
                a, b = [float(t) for t in line.split()]
                x1.append(a)
                y1.append(b)
            
            ##Now we make the arrays of the points

            X = np.array(x1, float)
            Y = np.array(y1, float)

            ##Make the plots from root
            
            mg = rt.TMultiGraph()
            graph = rt.TGraph(x1.len(), X, Y)
            graph.SetMakerSize(0.7)
            graph.SetMakerStyle(4)
            graph.SetMakerColor(2)

            mg.add(graph)
            mg.GetXaxis().SetTitle('Energy (eV)')
            mg.GetYaxis().SetTitle('vFv (erg cm^{-2} s^{-1})')
            mg.SetTitle('')
            mg.draw('PSK')
    except:
        raise
        print 'Check the param of the code'


path = '/home/antonio/nissimExercises/PSK0447-439/points.dat'
makeFit(path)
