from Tkinter import *

def window():

    root = Tk()  
    
    frame = Frame(root)  
    frame.pack()  
    
    label = Label(frame, text="Hola, por favor selecciona los archivos de los experimentos")  
    c1 = Checkbutton(frame, text="Synchrotron")  
    c2 = Checkbutton(frame, text="Inverse Compton")  
    entry = Entry(frame)  
    button = Button(frame, text="Aceptar")  
    
    label.pack()  
    c1.pack()  
    c2.pack()
    entry.pack()  
    button.pack()  
  
    root.mainloop()  


def makeArray(filesArray):

    '''This script take all the files .dat and make only one of all points'''

    x1,y1,xizq,xder,yarr,yaba=[],[],[],[],[],[]

    #walk along the array of file paths
    for x in range(0,len(filesArray)):
        try:
            #We now try to 
            pathFile = filesArray[x]
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
                

            final_array = open('puntos_experimentos.dat','w')

            for elem in range(0,len(x1)):
                final_array.write(str(x1[elem])+'\t')
                final_array.write(str(y1[elem])+'\t')
                final_array.write(str(xizq[elem])+'\t')
                final_array.write(str(xder[elem])+'\t')
                final_array.write(str(yarr[elem])+'\t')
                final_array.write(str(yaba[elem])+'\t')
                final_array.write('\n')
            final_array.close()
        except:
            print "Revisa la ruta de tus archivos"

listaDeArchivos = ['archivo1.dat','archivo2.dat','archivoN.dat' ]



window()
