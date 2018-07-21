#!/bin/python
"""

"""
import numpy as np
import matplotlib.pyplot as plt
import sys, os


class PuzzleBuilder:

    modes = ["maze", "jigsaw","shuffle"]
    Mode = ""

    def __init__(self, mode, dims, difficulty):
        for m in self.modes:
            if mode == m:
                self.Mode = mode
                print('Solving a '+self.Mode+' of '+str(difficulty)+'% difficulty')


def usage():
    print('')
    print('')


def menu_main():
    print('*         __________________________    \t*')
    print('*        //|/|/|PUZZLE-BUILDER|\x5c|\x5C|\x5C\x5C')
    print('*----(((|\__________________________/|)))----*')
    print('*        //|/|/|PUZZLE-BUILDER|\x5c|\x5C|\x5C\x5C')
    print('*----------------------------------*')


def main():
    menu_main()
    option = input('Enter Selection: ')


if __name__ == '__main__':
    main()