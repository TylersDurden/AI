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
    valid_path = False

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
        y0 = ptA.pop()
        x0 = ptA.pop()
        y1 = ptB.pop()
        x1 = ptB.pop()
        xi = ""
        yi = ""
        xf = ""
        yf = ""

        if xi == 0:
            xi = "0"
        else:
            xi = str(x0)
        if yi == 0:
            yi = "0"
        else:
            yi = str(y0)
        if xf == 0:
            xf = "0"
        else:
            xf = str(x1)
        if yf == 0:
            yf = "0"
        else:
            yf = str(y1)
        a = self.rawdata.pop(x0).split(' ')[y0]
        b = self.rawdata.pop(x1).split(' ')[y1]



        if b == '1' and a == '1':
            print(a+'->'+b)
            print('Start point and endpoint are both ' + a + 's. Beginning a' +
                  '[D]epth [F]irst [S]earch from:')
            print('['+xi+','+yi+']->['+xf+','+yf+']')
            self.valid_path = True
        else:
            print a+'->'+b+' is invalid!'


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
        ptB.append(val)
    pta = [ptA.__getitem__(0), ptA.__getitem__(1)]
    ptb = [ptB.__getitem__(0), ptB.__getitem__(1)]
    return pta, ptb


def main():
    dims = []
    data = []
    if len(sys.argv) < 3:
        usage()
    else:
        if sys.argv[1] == '-matrix':
            f = open(sys.argv[2], 'rb')
            data = f.readlines()
        print(str(len(data))+'x'+str(len(data[0].split(' ')))+' input matrix.')
        dims.append(len(data[0].split(' ')))    # x-length
        dims.append(len(data))      # Y-length

        # Initialize the Depth First Search Space
        dfs = DFS(data, dims)

        # Define starting point and stopping point of the search
        ptA, ptB = get_DFSearchSpace()

        # Determine if endpoints are valid (must be equal)
        dfs.initialize(ptA, ptB)


if __name__ == '__main__':
    main()
