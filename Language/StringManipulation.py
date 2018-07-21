#!/bin/python
"""
STRING_MANIPULATION
@author TylersDurden
"""
import hashlib
import sys, os


class StringManipulation:

    alphas = ['a','b','c','d','e','f','g','h','i','j','k','l',
              'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Alphas = ['A','B','C','D','E','F','G','H','I','J',
              'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    holy_hex = {}

    def __init__(self):
        self.holy_hex = self.whatTheHEX()

    @staticmethod
    def whatTheHEX(self):
        """
        Hex2ascii conversion
        :return: hexdict - Dictionary converting integers to hex
        """
        hexdict = {}

        return hexdict


def main():
    test_str = input('Enter some test input: ')
    stringy = StringManipulation()
    StringManipulation.whatTheHEX(stringy)


if __name__ == '__main__':
    main()