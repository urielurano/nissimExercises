import numpy as np
import matplotlib.pyplot as plt

def makePlot(listaDePuntos):
    plt.figure()
    colors = ['b','g','r','c','m','y','k','w']
    for x in range(0, len(listaDePuntos)):
        try:
            X, Y, Xizq, Xder, Yarr, Yaba = np.loadtxt(listaDePuntos[x], unpack = True)
            plt.errorbar(X,Y, Yarr, Yaba, linestyle="none", marker="*", markersize=4.0, capsize=3.0, label = str(x+1))
            a=plt.gca()
            a.set_yscale('log')
            a.set_xscale('log')
            plt.savefig('graph.png')
        except:
            print 'Hay un error, revisa:'
            raise
        
    plt.show()



        

puntos11 = ['points11-1.dat','points11-2.dat','points11-3.dat']
puntos12 = ['points12-1.dat','points12-2.dat','points12-3.dat','points12-4.dat','points12-5.dat','points12-6.dat','points12-7.dat','points12-8.dat']


#makePlot(puntos11)
makePlot(puntos12)
