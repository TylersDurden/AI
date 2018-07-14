#!/bin/python
"""
<|AUTOMATA|>
@author TylersDurden
"""
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

        shapes = []

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
        for s in shapes.__iter__():
            for sh in shapes.__iter__():
                if s.shape==sh.shape:
                    img = np.concatenate((np.concatenate((s,sh),1),np.concatenate((sh,s),1)),0)
                    Img = np.concatenate((np.concatenate((sh,s),1),np.concatenate((s,sh),1)),0)
                    plt.imshow(img,'gray')
                    #plt.show()
                    plt.imshow(Img,'gray')
                    #plt.show()
                    bigger_shapes.append(img)
                    bigger_shapes.append(Img)

        rand_shapes = self.shapeGenerator(shapes)
        fractals = self.shapeGenerator(rand_shapes)

    def shapeGenerator(self,primitives):
        shapes = []
        i = 0
        for a in primitives:
            for b in primitives:
                try:
                    i0 = np.concatenate((np.concatenate((a,b),0),np.concatenate((b,a),0)),1)
                    i1 = np.concatenate((np.concatenate((b,a),0),np.concatenate((a,b),0)),1)
                    i2 = np.concatenate((np.concatenate((a,b),1),np.concatenate((b,a),1)),0)
                    i3 = np.concatenate((np.concatenate((b,a),1),np.concatenate((a,b),1)),0)
                    # Save new shapes
                    shapes.append(i0)
                    shapes.append(i1)
                    shapes.append(i2)
                    shapes.append(i3)
                    I0 = np.concatenate((i0, i1), 1)
                    I1 = np.concatenate((i2, i3), 0)
                    plt.imshow(I0, 'gray')
                    plt.show()
                    plt.imshow(I1, 'gray')
                    plt.show()
                except ValueError:
                        i += 1 # Don't really do anything actually.
                try:
                    i4 = np.concatenate((np.concatenate((a,b),1),np.concatenate((b,a),1)),1)
                    i5 = np.concatenate((np.concatenate((b,a),1),np.concatenate((a,b),1)),0)
                    shapes.append(i4)
                    shapes.append(i5)
                    I2 = np.concatenate((i4,i5),0)
                    I3 = np.concatenate((i5,i4),1)
                    shapes.append(i4)
                    shapes.append(i5)
                    plt.imshow(I2,'gray')
                    plt.show()
                    plt.imshow(I3,'gray')
                    plt.show()
                except ValueError:
                        i += 1
            return shapes


def main():
    AUTOMATA()


if __name__ == '__main__':
    main()