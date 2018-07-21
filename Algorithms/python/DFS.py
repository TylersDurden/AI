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
        self.xdim = dims[0]
        self.ydim = dims[1]
    
    @staticmethod 
    def makeNxN(self):
        """

        """
        matrix = [[]]
        Row = []
        row = 0 
        col = 0
        last_row = False
        for point in self.rawdata:
            Row.append(point)
            col += 1
            if col == self.xdim:
                matrix[row] = Row
                row += 1
                col = 0
                for element in Row: Row.remove(element)
                continue
        np.array(matrix)


    def initialize(self, ptA, ptB):
        x0 = ptA.pop(0)
        y0 = ptA.pop()
        x1 = ptB.pop(0)
        y1 = ptB.pop()
        print(self.rawdata.pop(x0).split(' ')[y0])
        print(self.rawdata.pop(x1).split(' ')[y1])
        a = self.rawdata.pop(x0).split(' ')[y0]
        b = self.rawdata.pop(x1).split(' ')[y1]
        if (a == '0' and b == '1') or (a == '1' and b == '0'):
            print('')
        else:
            print('Start point and endpoint are both ' + a + 's. Beginning a'+
                  '[D]epth [F]irst [S]earch')


def usage():
    print('*--------<INCORRECT_USAGE>--------*')
    print('* python  -type  <data.txt>       *')
    print('*---------------------------------*')


def get_DFSearchSpace():
    """
    Let the user define the starting and stopping
    points of the Depth First Search.
    :return: Starting point ptA, and Endpoint ptB
    """
    start = input('Enter [x,y] coordinates of starting point: ')
    stop = input('Enter [x,y] coordinates of stopping point: ')
    ptA = []
    ptB = []
    for item in start:
        ptA.append(item)
    for val in stop:
        ptB.append(item)
    return ptA, ptB


def main():
    dims = []
    data = []
    if len(sys.argv) < 2:
        usage()
    else:
        if sys.argv[1] == '-matrix':
            f = open(sys.argv[2],'rb')
            data = f.readlines()
        print(str(len(data))+'x'+str(len(data[0].split(' ')))+' input matrix.')
        dims.append(len(data[0].split(' ')))    # x-length
        dims.append(len(data))      # Y-length

    # Initialize the Depth First Search Space
    dfs = DFS(data, dims)

    # Define starting point and stopping point of the search
    ptA, ptB = get_DFSearchSpace()


    dfs.initialize(ptA,ptB)


if __name__ == '__main__':
    main()
