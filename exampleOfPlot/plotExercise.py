##################################################################
########In this module we can make a few examples of plots########
##################################################################

from creaRandom import readRecord
import matplotlib.pyplot as plt
from math import *

listOfRecords = readRecord() #A list of random numbers
array = sorted(listOfRecords)#Make a sort of the records                                                                                          
vector = [x for x in range(len(listOfRecords))] #Make a vector




def _powerOfAList(list, num):#Make the n-power of the elements of a list of numbers
    power = []
    for x in range(len(list)):
        try:
            power.append(pow(list[x], num))
        except:
            print 'Invalid list'
    return power

def _function1():
    finalArray = []
    for x in array:                                                                                             
        finalArray.append(cos(x)*pi*1/180)
    return finalArray

def _function2():
    finalArray = []
    for x in array:
        finalArray.append(sin(x)*pi*1/180)
    return finalArray

def plot1(): #One case of a simple plot
    plt.figure('Plot 1')
    plt.plot(listOfRecords)
    plt.title('graph 1')
    plt.grid(True)
    plt.savefig('graph1.png')
    plt.show()

def plot2(): #Here we plot a random array were i = list[i]
    plt.figure('Plot 2')
    plt.plot(vector,listOfRecords, 'ro')
    plt.axis([0, 50, 0, max(listOfRecords)])
    plt.title('graph 2')
    plt.grid(True)
    plt.savefig('graph2.png')
    plt.show()

def plot3():#Anoter example of a plot, different functions on the same plane
    plt.figure('Plot 3')
    array2 = _powerOfAList(array,2)
    array3 = _powerOfAList(array,1/2)
    plt.plot(array, array, 'bs', array2, array2, 'g^',array3, array3, 'r^')
    plt.axis([0, 10, 0, max(listOfRecords)])
    plt.title('graph 2')
    plt.grid(True)
    plt.savefig('graph3.png')
    plt.show()


def plot4():#Put a two plots in a same window
    array1 = _function1()
    array2 = _function2()
    plt.figure('Plot 4')
    plt.subplot(211)
    plt.plot(array, array1, 'bo')
    plt.grid(True)
    plt.subplot(212)
    plt.plot(array, array2, 'ro')
    plt.title('graph 4')
    plt.grid(True)
    plt.savefig('graph4.png')
    plt.show()



plot1()
plot2()
plot3()
plot4()
