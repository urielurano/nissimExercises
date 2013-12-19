##################################################################
########In this module we can make a few examples of plots########
##################################################################

from creaRandom import readRecord
from PIL import Image
import matplotlib.pyplot as plt


listOfRecords = readRecord() #A list of random numbers

def plot1(): #One case of a simple plot
    plt.figure('Grafica 1')
    plt.plot(listOfRecords)
    plt.xlabel('like in the example one')
    plt.savefig('graph1.png')
    plt.show()

def plot2(): #Here we plot a random array were i = list[i]
    plt.figure('Grafica 2')
    vector = [x for x in range(len(listOfRecords))]
    plt.plot(vector,listOfRecords, 'ro')
    plt.axis([0, 50, 0, max(listOfRecords)])
    plt.xlabel('like in the example two')
    plt.savefig('graph2.png')
    plt.show()

    


plot1()
plot2()
