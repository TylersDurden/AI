#!/bin/python 
"""

"""
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
                
    