#!/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys, os


class ImageProcessing:

    boxes = []
    checkers = []
    exes = []
    tetris = []
    num2im = []
    im2num = []

    def __init__(self, matrix, cmap):
        self.boxes, self.checkers = self.initialize_primitives()
        self.num2im, self.im2num = self.initialize_converters()
        self.visual_check(self.boxes)

        # Start creating shapes to detect features of
        # image inputs matrix and cmap
        self.find_face(matrix,cmap)

    def find_face(self,raw_data,cmap):

        print('Beginning Facial Analysis')
        mask = 255*np.ones(raw_data.shape)
        plt.imshow(raw_data, 'gray')
        plt.title('Attemping to find the face in this Image')
        plt.show()
        plt.title('Experimenting with diff Masks...')
        plt.imshow((raw_data + cmap)/mask)
        plt.show()


    def visual_check(self, mats):
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


class ImageMath:

    width = -1
    height = -1

    def __init__(self, matrix, file):
        """
        ImageMath takes in the image matrix, and the image file.
        It first processes the points of highest color density and
        then tries edge detection and some symmetry analysis to
        find a face.
        :param matrix:
        :param file:
        """
        print('Processing: ' + file)
        print('Dims: '+str(matrix.shape))

        self.width = matrix.shape[0]
        self.height = matrix.shape[1]

        density = self.score_image_sparsity(matrix)
        image_Proc = ImageProcessing(matrix,density)

    def score_image_sparsity(self,mat):
        """
        TODO: break the image into smaller chunks because
        right now it's too much and causing easy overflows
        :param mat:
        :return:
        """
        scoreMatrix = np.ones(mat.shape)
        maxloc = np.array([0,0])
        minloc  = np.array([0,0])
        max = 0
        min = 0
        for i in np.arange(0,self.width-1,1):
            row = []
            for j in np.arange(0,self.height-1,1):
                avg = (mat[int(i),int(j),0]/3 + mat[int(i),int(j),1]/3 + mat[int(i),int(j),2]/3)
                extr = (mat[int(i),int(j),0]/25 + mat[int(i),int(j),1]/25 + mat[int(i),int(j),2]/25)*20.0
                scoreMatrix[int(i), int(j), :] = (avg + extr*0.5)
                if avg>max:
                    max = avg
                    maxloc = np.array([int(j),int(i)])
                if avg<max:
                    min = avg
                    minloc = np.array([int(j),int(i)])
        print('Darkest Location: '+str(maxloc[0])+','+str(maxloc[1])+' is '+str(max))
        print('Brightest Location: '+str(minloc[0])+','+str(minloc[1])+' is ' + str(min))
        range = (max - min)*100/255;
        print('Contrast set to '+str(range)+'%')
        plt.imshow(scoreMatrix,)
        plt.show()
        return scoreMatrix



def usage():
    print('*----------//:INCORRECT_USAGE!:\x5C\x5C---------*')
    print('* python ImageProcessing.py -faces imgdir *')
    print('* python ImageProcessing.py -math img.ext *')
    print('*-----------------------------------------*')


def main():
    if len(sys.argv) < 3:
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
                if ind == 0:
                    faces = facelib+'/'+dir+'/'+str(folders.pop(0))
                    os.chdir(faces)
                    fnames = os.listdir(faces)
                    for fname in fnames:
                        if fname.__contains__('.jpg'):
                            print('Found Image: '+fname)
                            f = open(fname, 'rb')
                            img = plt.imread(f)
                            ImageMath(img, f)

                ind += 1
        if sys.argv[1] == '-math':
            # Folder path will have many faces
            # showing different expressions to
            # give data some variation
            path = sys.argv[2]
            os.chdir(path)
            files = os.listdir(path)
            print(str(len(files)) + ' images found for analysis.')
            # For now start with one
            f0 = files.pop(0)
            im0 = plt.imread(f0)
            ImageMath(im0, f0)


if __name__ == '__main__':
    main()