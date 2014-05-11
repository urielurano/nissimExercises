import numpy as np
import matplotlib.pyplot as plt

def makePlot(listaDePuntos):
    X,Y = [],[]
    fig = plt.figure()
    for x in range(0, len(listaDePuntos)):
        try:
            Xtmp, Ytmp = np.loadtxt(listaDePuntos[x], unpack = True)
            #X.append(Xtmp)
            #Y.append(Ytmp)
            fig.add(plt.plot(Xtmp, Ytmp,'*'))
            #a=plt.gca()
            #a.set_yscale('log')
            #a.set_xscale('log')
        except:
            print x
            raise
        finally:
            print str(x) + '<- revisa el archivo ' + str(listaDePuntos[x])
        
    plt.show()



        

puntos = ['points11-2.dat','points12-1.dat','points12-3.dat','points12-5.dat','points12-7.dat','points11-1.dat','points11-3.dat','points12-2.dat','points12-4.dat','points12-6.dat','points12-8.dat']

makePlot(puntos)
    
