from math import *

def convert(arrayFiles):
    x1,y1,xizq,xder,yarr,yaba = [],[],[],[],[],[]
    for x in range(0,len(arrayFiles)):
        try:
             #We now try to 
            pathFile = arrayFiles[x]
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
                

                    final_array = open('/home/antonio/Escritorio/potencias/'+pathFile,'w')

                    for elem in range(0,len(x1)):
                        final_array.write(str(pow(10,x1[elem]))+'\t')
                        final_array.write(str(pow(10,y1[elem]))+'\t')

                        if xizq[elem] != 0:
                            final_array.write(str(pow(10,xizq[elem]))+'\t')
                        else:
                            final_array.write(str(0.0)+'\t')

                        if xder[elem] != 0:
                            final_array.write(str(pow(10,xder[elem]))+'\t')
                        else:
                            final_array.write(str(0.0)+'\t')

                        if yarr[elem] != 0:
                            final_array.write(str(pow(10,yarr[elem]))+'\t')
                        else:
                            final_array.write(str(0.0)+'\t')

                        if yaba[elem] != 0:
                            final_array.write(str(pow(10,yaba[elem]))+'\t')
                        else:
                            final_array.write(str(0.0)+'\t')

                        final_array.write('\n')
                    final_array.close()
        except:
            print pathFile
            raise


puntos11 = ['points11-1.dat','points11-2.dat','points11-3.dat','points12-1.dat','points12-2.dat','points12-3.dat','points12-4.dat','points12-5.dat','points12-6.dat','points12-7.dat','points12-8.dat']

convert(puntos11)
