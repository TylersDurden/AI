#!/bin/python 
"""

"""
import numpy as np
import sys, os
import math


class DFS:
    
    rawdata = []
    xdim = -1
    ydim = -1
    
    def __init__(self, matrix, dims):
        self.rawdata = matrix
        self.xdim = dims(1)
        self.ydim = dims(2)
    
    @staticmethod 
    def makeNxN(self):
        
        row = 0 
        col = 0
        last_row = False
        for point in self.rawdata:
            
            col += 1
            if(col == self.xdim):
                row += 1
                col = 0


def usage():
    print('*--------<INCORRECT_USAGE>--------*')
    print('* python  <flattened matrix>      *')
    print('* flat mat format: use brackets,  *')
    print('* and make it look like:          *')
    print("*"+"\t"+str(np.array([1, 0, 0, 1, 1, 0]))+"\t\t  *")
    print('*---------------------------------*')


def main():
    if len(sys.argv) < 3:
        usage()
    else:
        print(sys.argv[2].replace('[', ''))



if __name__ == '__main__':
    main()
