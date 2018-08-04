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
        # break the image up into a many cells of various shapes
        cells, rows, quarts = self.divideNanalyze(matrix)
        cell1, row1, quart1 = self.divideNanalyze(quarts.pop(1))
        cell2, row2, quart2 = self.divideNanalyze(quarts.pop(2))
        # Divide and Analyze these subdivisions as well!
        while len(quarts) > 0:
            cells, rows, quarts = self.divideNanalyze(quarts.pop(0))
            if quarts.pop().shape[0] < 16:
                break
        while len(quart1) > 0:
            cell1, row1, quart1 = self.divideNanalyze(quart1.pop(1))
            if quart1.pop().shape[0]<16:
                break
        while len(quart2) > 0:
            cell1, row1, quart2 = self.divideNanalyze(quart2.pop(2))
            if quart2.pop().shape[0] < 16:
                break

    def find_face(self, raw_data,cmap):

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
            print('loaded'+str(matrix.shape[0])+'x'+str(matrix.shape[1])+' primitive')
            # plt.show()

    def divideNanalyze(self, matrix):
        """

        :param matrix:
        :return:
        """
        qx_size = int(matrix.shape[0]/4)
        qy_size = int(matrix.shape[1]/4)
        print('Subdiving ' + str(matrix.shape[0]) + 'x' + str(matrix.shape[1]) + ' into 4 '+
              str(qx_size) + 'x' + str(qy_size) + 'pics')
        # Left colum of the 4x4 slices
        l1 = np.array(matrix[0:qx_size,0:qy_size])
        l2 = np.array(matrix[qx_size:2*qx_size,0:qy_size])
        l3 = np.array(matrix[qx_size*2:qx_size*3,0:qy_size])
        l4 = np.array(matrix[3*qx_size:4*qx_size, 0:qy_size])
        # Mid-Left column of the 4x4 slices
        ml1 = np.array(matrix[0:qx_size,qy_size:2*qy_size])
        ml2 = np.array(matrix[qx_size:2*qx_size,qy_size:2*qy_size])
        ml3 = np.array(matrix[2*qx_size:3*qx_size,qy_size:2*qy_size])
        ml4 = np.array(matrix[3*qx_size:4*qx_size,qy_size:2*qy_size])
        # Mid-Right column of the 4x4 slices
        mr1 = np.array(matrix[0:qx_size,2*qy_size:3*qy_size])
        mr2 = np.array(matrix[qx_size:2*qx_size,2*qy_size:3*qy_size])
        mr3 = np.array(matrix[2*qx_size:3*qx_size,2*qy_size:3*qy_size])
        mr4 = np.array(matrix[3*qx_size:4*qx_size,2*qy_size:3*qy_size])
        # Right column of the 4x4 slices
        r1 = np.array(matrix[0:qx_size,3*qy_size:4*qy_size])
        r2 = np.array(matrix[qx_size:2*qx_size,3*qy_size:4*qy_size])
        r3 = np.array(matrix[2*qx_size:3*qx_size,3*qy_size:4*qy_size])
        r4 = np.array(matrix[3*qx_size:4*qx_size,3*qy_size:4*qy_size])

        row1 = np.concatenate((l1,ml1,mr1,r1),1)
        row2 = np.concatenate((l2,ml2,mr2,r2),1)
        row3 = np.concatenate((l3,ml3,mr3,r3),1)
        row4 = np.concatenate((l4,ml4,mr4,r4),1)

        i0 = (np.concatenate((mr1, r1),1))
        i1 = np.concatenate((mr2,r2),1)
        i2 = np.concatenate((mr3,r3),1)
        i3 = np.concatenate((mr4,r4),1)

        q1 = np.concatenate((np.concatenate((l1,ml1),1),np.concatenate((l2,ml2),1)),0)
        q2 = np.concatenate((i0,i1),0)
        q3 = np.concatenate((np.concatenate((l3,ml3),1),np.concatenate((l4,ml4),1)),0)
        q4 = np.concatenate((i2,i3),0)
        plt.imshow(row1)
        plt.title('Top Row')
        plt.show()
        plt.imshow(row2)
        plt.title('Upper-Middle Row')
        plt.show()
        plt.imshow(row3)
        plt.title('Lower-Middle Row')
        plt.show()
        plt.imshow(row4)
        plt.title('Bottom Row')
        plt.show()

        plt.imshow(q1)
        plt.title('quarter1')
        plt.show()
        plt.imshow(q2)
        plt.title('quarter2')
        plt.show()
        plt.imshow(q3)
        plt.title('quarter3')
        plt.show()
        plt.imshow(q4)
        plt.title('quarter4')
        plt.show()

        cells = list()
        cells.append(l1)
        cells.append(l2)
        cells.append(l3)
        cells.append(l4)
        cells.append(ml1)
        cells.append(ml2)
        cells.append(ml3)
        cells.append(ml4)
        cells.append(mr1)
        cells.append(mr2)
        cells.append(mr3)
        cells.append(mr4)
        cells.append(r1)
        cells.append(r2)
        cells.append(r3)
        cells.append(r4)
        rows = list()
        rows.append(row1)
        rows.append(row2)
        rows.append(row3)
        rows.append(row4)
        quarters = list()
        quarters.append(q1)
        quarters.append(q2)
        quarters.append(q3)
        quarters.append(q4)

        return cells, rows, quarters

    def hexbin_color_heatmap(self,matrix):
        np.random.seed(19680801)
        n = 1000
        x = np.random.standard_normal(n)
        y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
        xmin = x.min()
        xmax = x.max()
        ymin = y.min()
        ymax = y.max()

        fig, ax = plt.subplots(ncols = 1, sharey=True, figsize=(7, 4))
        fig.subplots_adjust(hspace=0.5, left = 0.7, right=0.93)
        hexbn = ax.hexbin(x,y, gridsize=5, cmap='inferno')
        ax.axis([xmin, xmax, ymin, ymax])
        ax.set_title("Hexagon Binning")
        color = fig.colorbar(hexbn,ax=ax)
        color.set_label('log10(N)')


        plt.show()

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
        boxy.append(b0x3)
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
        plt.imshow(scoreMatrix)
        #plt.show()
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