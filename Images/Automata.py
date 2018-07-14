#!/bin/python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys, os


class AUTOMATA:

    integers = []
    alphas = []
    Alphas = []
    bites = []

    row = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    dot = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    diag= [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    bkrow=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __init__(self):
        self.initializeIntegerMapping()

    def initializeIntegerMapping(self):

        eye = np.concatenate((self.row,self.dot,self.row), 0)
        invi = np.concatenate((self.bkrow, self.diag, self.bkrow), 0)

        plt.imshow(eye, 'gray')
        plt.show()
        plt.imshow(invi, 'gray')
        plt.show()

        map = {}
        #for int in np.arange(-255,255,1):

def main():
    AUTOMATA()


if __name__ == '__main__':
    main()