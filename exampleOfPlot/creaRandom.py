##########################################################################
########Module that create a new file .dat with random numbers############
##########################################################################

import random

def fileMaker():
    f = open('records.dat','w')
    f.close()

def makeNum():
    for x in range(1, 10000):
        writeNum(random.random()*100)

def writeNum(num):
    f = open('records.dat','a')
    f.write(str(num) + '\n')
    f.close()

fileMaker()
makeNum()
