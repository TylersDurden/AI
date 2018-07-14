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

    ones = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    zeta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    diag = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    invr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    st3p = [[1, 1, 0], [1, 0, 0], [0, 1, 1]]
    st0p = [[0, 0, 1], [0, 1, 1], [1, 1, 1]]
    dots = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    xros = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]

    a = [[1, 0, 1], [0, 1 ,0], [0, 1, 0]]
    b = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0, 0]]
    c = [[0, 0, 0], [0, 1, 1], [0, 0, 0]]

    def __init__(self):
        self.initializeIntegerMapping()

    def initializeIntegerMapping(self):
        eye = np.concatenate((self.ones, self.dots, self.ones), 0)
        i2i = np.concatenate((self.dots, self.ones, self.dots), 0)
        stoop = np.concatenate((self.st0p, self.st3p, self.st0p), 0)
        xros = np.concatenate((self.xros, self.dots, self.xros), 0)


        mess = np.concatenate((xros, stoop), 1)
        m3ss = np.concatenate((np.concatenate((xros,stoop),1),np.concatenate((xros,stoop),1)),0)
        m4ss = np.concatenate((np.concatenate((stoop,xros),1),np.concatenate((xros,stoop),1)),0)
        w1de = np.concatenate((np.concatenate((xros,stoop),0),np.concatenate((xros,stoop),0)),0)
        r0t1 = np.concatenate((np.concatenate((i2i,stoop),1),np.concatenate((stoop,xros),1)),1)
        w1de = np.concatenate((w1de, w1de), 1)

        shapes = list()
        shapes.append(eye)
        shapes.append(i2i)
        shapes.append(stoop)
        shapes.append(xros)
        shapes.append(mess)
        shapes.append(m3ss)
        shapes.append(m4ss)
        shapes.append(w1de)
        shapes.append(r0t1)
        #shapes.append(w33d)

        #plt.imshow(eye, 'gray')
        #plt.show()
        #plt.imshow(i2i, 'gray')
        #plt.title('i2i')
        #plt.show()
        #plt.imshow(stoop, 'gray')
        #plt.show()
        #plt.title('st00p')
        #plt.imshow(xros,'gray')
        #plt.show()
        #plt.title('xros')
        #plt.imshow(mess,'gray')
        #plt.show()
        #plt.title('messy')
        plt.imshow(m3ss,'gray')
        plt.title('m3ss')
        plt.plot()
        #plt.show()

        plt.imshow(m4ss,'gray')
        plt.title('m4ss')
        #plt.show()

        plt.imshow(r0t1,'gray')
        plt.title('rotated ?')
        #plt.show()

        plt.imshow(w1de,'gray')
        #plt.show()

        plt.imshow(self.a,'gray')
        #plt.show()

        bigger_shapes = []
        for s in shapes:
          for sh in shapes:
              if s.shape==sh.shape:
                img = np.concatenate((np.concatenate((s,sh),1),np.concatenate((sh,s),1)),0)
                Img = np.concatenate((np.concatenate((sh,s),1),np.concatenate((s,sh),1)),0)
                plt.imshow(img,'gray')
                plt.show()
                plt.imshow(Img,'gray')
                plt.show()
                bigger_shapes.append(img)
                bigger_shapes.append(Img)

def main():
    AUTOMATA()


if __name__ == '__main__':
    main()