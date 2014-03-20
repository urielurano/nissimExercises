import numpy as np
import ROOT as rt

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
        yaba =[]
        
        x1errorV = []
        y1errorV = []
        
        path = '/home/antonio/nissimExercises/PSK0447-439/'
        i = 1;
        while(i <= len(files)):

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

            ##Make the plots from root
            
            mg = rt.TMultiGraph()
            saves = {}
            NP = 0
            NP1 = 0
            canvas = -1

            graph = rt.TGraphErrors(len(x1), X, Y)
            graph.SetMarkerSize(0.7)
            graph.SetMarkerStyle(4)
            graph.SetMarkerColor(4)

            mg.Add(graph)
            mg.Add(graph)
            mg.Draw('APE')                                                                                                                                
        saves['gr1'] = gr1
    except:
        raise
        print 'Check the param of the code'



files = ['atom.dat', 'fermi.dat', 'hess.dat', 'ned.dat', 'points.dat', 'uvot.dat', 'xrt.dat']
makeFit(files)
