##########################################################################
########Module that create a new file .dat with random numbers############
####and then we can write/read the file into the path of the scrip########
##########################################################################

import random
import sys
import os.path

def _fileMaker():#Here we can write a file into the path
    f = open('records.dat','w')
    f.close()

def _makeNum():#Here we make a 10000 random numbers into the file
    for x in range(1, 10000):
        _writeNum(random.random()*10)

def _writeNum(num):#Here we wrote the numbers into the file
    f = open('records.dat','a')
    f.write(str(num) + '\n')
    f.close()

def _createFile():#We make the call to make a random records file.
    _fileMaker()
    _makeNum()

def readRecord():#Here we can make a list of the records of one file
    if not os.path.exists('records.dat'):
        _createFile() #Create a new File of records in case that not exits anyone.                                                                   
    fileName = 'records.dat'
    record = open(fileName,'r')
    elements = list()
    for line in record:
        try:
            if line.find('.') == -1:
                try:#Try to convert the line in an integer number
                    elements.append(int(line))
                except:#If not an line valid, the the file .dat is not correct
                    print('Its not a valid file by the line: \n '+ line)
                    return None
            else:
                try:
                    elements.append(float(line))
                except:
                    print('Its not a valid file by the line: \n '+ line)
                    return None
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    return elements
                
