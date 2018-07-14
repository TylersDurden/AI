#!/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys, os
from PIL import Image
import exifread


class ImageProcessing:

    boxes = []
    checkers = []
    exes = []
    tetris = []
    num2im = []
    im2num = []

    def __init__(self):
        self.boxes, self.checkers = self.initialize_primitives()
        self.num2im, self.im2num = self.initialize_converters()
        self.visual_check(self.boxes)

    def visual_check(self,mats):
        for matrix in mats:
            plt.imshow(matrix,'gray')
            #plt.show()

    def initialize_primitives(self):
        boxy = []
        b0x0 = np.array([[0,0,0],[0,1,0],[0,0,0]])
        b0x1 = np.array([[1,1,1],[1,0,1],[1,1,1]])
        b0x2 = np.array([[0,1,1],[0,0,1],[1,1,1]])
        b0x3 = np.array([[1,1,0],[1,1,0],[0,0,0]])
        chkr = []
        chk0 = np.array([[1,0,1], [0,0,0], [1,0,1]])
        chk1 = np.array([[0,1,0], [1,1,1], [0,1,0]])
        chk2 = np.array([[1,1,0], [0,0,1], [1,1,0]])
        chk3 = np.array([[1,0,1], [0,1,0], [1,0,1]])
        chk4 = np.array([[0,1,0], [1,0,1], [0,1,0]])
        boxy.append(b0x0)
        boxy.append(b0x1)
        boxy.append(b0x2)
        chkr.append(chk0)
        chkr.append(chk1)
        chkr.append(chk2)
        chkr.append(chk3)
        chkr.append(chk4)
        # Now do the X-shaped elements


        return boxy, chkr

    def initialize_converters(self):
        n2i = []
        i2n = []

        return n2i, i2n



class ImageCounter:

    def __init__(self,matrix):
        density = self.score_image_sparsity(matrix)


    def score_image_sparsity(self,mat):
        scoreMatrix = [[]]

        return scoreMatrix


def usage():
    print('*----------//:INCORRECT_USAGE!:\x5C\x5C---------*')
    print('* python ImageProcessing.py -faces imgdir *')
    print('* python ImageProcessing.py -math img.ext *')
    print('*-----------------------------------------*')


def main():
    if(len(sys.argv) < 3):
        usage()
    else:
        if sys.argv[1] == '-faces':
            facelib = sys.path.pop(0)+'/'+sys.argv[2]
            dirs = os.listdir(facelib)
            ind = 0
            for dir in dirs:
                os.chdir(facelib+'/'+dir)
                print('Folder '+'\x09'+str(facelib+'/'+dir))
                folders = os.listdir(facelib+'/'+dir)
                if(ind == 0):
                    faces = facelib+'/'+dir+'/'+str(folders.pop(0))
                    os.chdir(faces)
                    fnames = os.listdir(faces)
                    for fname in fnames:
                        if fname.__contains__('.jpg'):
                            print('Found Image: '+fname)
                            f = open(fname,'rb')
                            img = plt.imread(f)
                            ImageCounter(img)

                ind += 1


        ImageProcessing()


if __name__ == '__main__':
    main()