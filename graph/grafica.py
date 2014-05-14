import numpy as np
import matplotlib.pyplot as plt

def makePlot(listaDePuntos):
    plt.figure()
    for x in range(0, len(listaDePuntos)):
        try:
            Xtmp, Ytmp = np.loadtxt(listaDePuntos[x], unpack = True)
            plt.plot(Xtmp, Ytmp,'*')
            plt.savefig('graph.png')
            #a=plt.gca()
            #a.set_yscale('log')
            #a.set_xscale('log')
        except:
            print 'Hay un error, revisa:'
            raise
        
    plt.show()



        

puntos11 = ['points11-1.dat','points11-2.dat','points11-3.dat']
puntos12 = ['points12-1.dat','points12-2.dat','points12-3.dat','points12-4.dat','points12-5.dat','points12-6.dat','points12-7.dat','points12-8.dat']


makePlot(puntos11)
makePlot(puntos12)
