#!/bin/python
"""
<|AUTOMATA|>
@author TylersDurden
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys, os


class AUTOMATA:

    integers = []
    alphas = []
    Alphas = []
    bites = []

    ones = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    zeta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    diag = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    jag =  [[1, 1, 1], [1, 1, 0], [1, 0, 0]]
    invr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    st3p = [[1, 1, 0], [1, 0, 0], [0, 1, 1]]
    st0p = [[0, 0, 1], [0, 1, 1], [1, 1, 1]]
    dots = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    xros = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]

    a = [[1, 0, 1], [0, 1 ,0], [0, 1, 0]]
    b = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0, 0]]
    c = [[0, 0, 0], [0, 1, 1], [0, 0, 0]]

    def __init__(self):
        # Test simple automata of generic shapes
        # self.first_shapes = self.initializeIntegerMapping()
        # fractals = self.shapeGenerator(self.fiirst_shapes)
        # Figure out different color schemes
        self.color_spectra()

    def color_spectra(self):
        """
        Experimenting with the color schemes possible for
        graphics with different data, and layouts
        :return:
        """
        blue_leaf9 = np.array([[1,2,3],[4,5,6],[7,8,9]])
        red_leaf9 = np.array([[1,2,3],[4,5,6],[7,8,9]])
        plt.imshow(blue_leaf9,'Blues')
        plt.show()
        test_data = np.array([[4,5,3],[2,0,8],[7,1,6]])
        xlabels = ['r0','r1','r2']
        ylabels = ['c0','c1','c2']
        title = 'random'
        self.categorical_mapping(test_data,xlabels,ylabels,title, 'gray')

    @staticmethod
    def categorical_mapping(data, xlabels, ylabels, title, style):
        """
        Create a tiled plot with x and y labels, and labeled data.
        Graph is rendered with the color scheme specified with the
        style param.
        :param data:
        :param xlabels:
        :param ylabels:
        :param title:
        :param style:
        :return:
        """
        fig, ax = plt.subplots()
        im = ax.imshow(data, style)
        # Set the tick marks
        ax.set_xticks(np.arange(len(xlabels)))
        ax.set_yticks(np.arange(len(ylabels)))
        ax.set_xticklabels(xlabels)
        ax.set_yticklabels(ylabels)
        # Rotate to prevent clutter
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
        # Label each cell
        for i in range(len(ylabels)):
            for j in range(len(xlabels)):
                text = ax.text(j,i,data[i,j],ha="center",va="center",color="w")
        ax.set_title(title)
        fig.tight_layout()
        plt.show()

    def initializeIntegerMapping(self):
        eye = np.concatenate((self.ones, self.dots, self.ones), 0)
        i2i = np.concatenate((self.dots, self.ones, self.dots), 0)
        stoop = np.concatenate((self.st0p, self.st3p, self.st0p), 0)
        xros = np.concatenate((self.xros, self.dots, self.xros), 0)
        # Start using these shapes to make more complex shapes
        mess = np.concatenate((xros, stoop), 1)
        m3ss = np.concatenate((np.concatenate((xros,stoop),1),np.concatenate((xros,stoop),1)),0)
        m4ss = np.concatenate((np.concatenate((stoop,xros),1),np.concatenate((xros,stoop),1)),0)
        w1de = np.concatenate((np.concatenate((xros,stoop),0),np.concatenate((xros,stoop),0)),0)
        r0t1 = np.concatenate((np.concatenate((i2i,stoop),1),np.concatenate((stoop,xros),1)),1)
        w1de = np.concatenate((w1de, w1de), 1)
        # Now collect all the shapes made
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

        # Recursively build up the same shapes
        rand_shapes = self.shapeGenerator(shapes)
        return rand_shapes

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


class TilePuzzle:

    tiles = []
    table = [[]]

    def __init__(self, n):
        self.N = n
        # Creating an NxN Tiled puzzle game
        self.tiles = np.random.random_integers(0, self.N, self.N)
        self.table = self.make_tile_table()
        self.illustrate_tiles()

    def make_tile_table(self):
        table = [[]]


        return table

    def illustrate_tiles(self):
        xlabels = ['Col.1', 'Col.2', 'Col.3']
        ylabels = ['Row 1', 'Row 2', 'Row 3']
        title = 'Puzzle Layout'
        style = 'BrBG'
        AUTOMATA.categorical_mapping(self.table, xlabels, ylabels, title, style)


def main():
    # AUTOMATA()
    TilePuzzle(4)


if __name__ == '__main__':
    main()