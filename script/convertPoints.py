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
            print x1[elem],pow(10,x1[elem])
            print pathFile
            raise


files = ['atom.dat', 'fermi.dat', 'hess.dat', 'ned.dat', 'uvot.dat', 'xrt.dat']

convert(files)
