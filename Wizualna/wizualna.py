import numpy as np
import skimage.io as io
import skimage
import random

SIZE_2X2_WHITE = [[[0,0,1,1],[0,0,1,1]],
                [[1,1,0,0],[1,1,0,0]],
                [[0,1,0,1],[0,1,0,1]],
                [[1,0,1,0],[1,0,1,0]],
                [[0,1,1,0],[0,1,1,0]],
                [[1,0,0,1],[1,0,0,1]]]

SIZE_2X2_BLACK = [[[1,0,0,1],[0,1,1,0]],
                [[0,1,1,0],[1,0,0,1]],
                [[0,0,1,1],[1,1,0,0]],
                [[1,1,0,0],[0,0,1,1]],
                [[0,1,0,1],[1,0,1,0]],
                [[1,0,1,0],[0,1,0,1]]]

SIZE_1X2_WHITE = [[[1,0], [1,0]],
                [[0,1], [0,1]]]

SIZE_1X2_BLACK = [[[1,0], [0,1]],
                [[0,1], [1,0]]]

def RANDOM_SIZE_2X2(isBlack):
    if isBlack:
        return SIZE_2X2_BLACK[random.randint(0, 5)]
    return SIZE_2X2_WHITE[random.randint(0, 5)]

def RANDOM_SIZE_1X2(isBlack):
    if isBlack:
        return SIZE_1X2_BLACK[random.randint(0, 1)]
    return SIZE_1X2_WHITE[random.randint(0, 1)]

def CREATE_PICTURE_2X2(inputPicture, outputPictureOne, outputPictureTwo, outputPictureThree):
    img = io.imread(inputPicture, as_gray=True)
    img = img > 0.5
    h, w = img.shape
    picture = [np.zeros((2*h, 2*w)), np.zeros((2*h, 2*w))]
    
    for r in range(h):
        for c in range(w):
            if img[r][c] == 0:
                colors = RANDOM_SIZE_2X2(True)
                for i in range(2):
                    picture[i][r*2][c*2] = colors[i][0]
                    picture[i][r*2+1][c*2] = colors[i][1]
                    picture[i][r*2][c*2+1] = colors[i][2]
                    picture[i][r*2+1][c*2+1] = colors[i][3]
                continue
            colors = RANDOM_SIZE_2X2(False)
            for i in range(2):
                picture[i][r*2][c*2] = colors[i][0]
                picture[i][r*2+1][c*2] = colors[i][1]
                picture[i][r*2][c*2+1] = colors[i][2]
                picture[i][r*2+1][c*2+1] = colors[i][3]

    picture[0] = skimage.img_as_ubyte(picture[0])
    picture[1] = skimage.img_as_ubyte(picture[1])
    io.imsave(outputPictureOne, picture[0])
    io.imsave(outputPictureTwo, picture[1])
    pictureMerge = 255 - (picture[0] + picture[1])
    io.imsave(outputPictureThree, pictureMerge)

def MERGE_PICTURE_2X2(inputPictureOne, inputPictureTwo, outputPicture):
    imgOne = io.imread(inputPictureOne, as_gray=True)
    imgTwo = io.imread(inputPictureTwo, as_gray=True)
    imgOne = imgOne > 0.5
    imgTwo = imgTwo > 0.5
    h, w = imgOne.shape
    picture = np.zeros((int(h/2), int(w/2)))

    i = 0
    for r in range(0, h, 2):
        j = 0
        for c in range(0, w, 2):
            if imgOne[r][c] == imgTwo[r][c] and imgOne[r][c+1] == imgTwo[r][c+1] and imgOne[r+1][c+1] == imgTwo[r+1][c+1] and imgOne[r+1][c] == imgTwo[r+1][c]:
                picture[i][j] = 1
                j += 1
                continue
            picture[i][j] = 0
            j += 1
        i += 1
    picture = skimage.img_as_ubyte(picture)
    io.imsave(outputPicture, picture)

def CREATE_PICTURE_1X2(inputPicture, outputPictureOne, outputPictureTwo, outputPictureThree):
    img = io.imread(inputPicture, as_gray=True)
    img = img > 0.5
    h, w = img.shape
    picture = [np.zeros((h, 2*w)), np.zeros((h, 2*w))]

    for r in range(h):
        for c in range(w):
            if img[r][c] == 0:
                colors = RANDOM_SIZE_1X2(True)
                for i in range(2):
                    picture[i][r][c*2] = colors[i][0]
                    picture[i][r][c*2+1] = colors[i][1]
                continue
            colors = RANDOM_SIZE_1X2(False)
            for i in range(2):
                picture[i][r][c*2] = colors[i][0]
                picture[i][r][c*2+1] = colors[i][1]

    picture[0] = skimage.img_as_ubyte(picture[0])
    picture[1] = skimage.img_as_ubyte(picture[1])
    io.imsave(outputPictureOne, picture[0])
    io.imsave(outputPictureTwo, picture[1])
    pictureMerge = 255 - (picture[0] + picture[1])
    io.imsave(outputPictureThree, pictureMerge)

def MERGE_PICTURE_1X2(inputPictureOne, inputPictureTwo, outputPicture):
    imgOne = io.imread(inputPictureOne, as_gray=True)
    imgTwo = io.imread(inputPictureTwo, as_gray=True)
    imgOne = imgOne > 0.5
    imgTwo = imgTwo > 0.5
    h, w = imgOne.shape
    picture = np.zeros((h, int(w/2)))

    for r in range(h):
        i = 0
        for c in range(0, w, 2):
            if imgOne[r][c] == imgTwo[r][c] and imgOne[r][c+1] == imgTwo[r][c+1]:
                picture[r][i] = 1
                i += 1
                continue
            picture[r][i] = 0
            i += 1
    picture = skimage.img_as_ubyte(picture)
    io.imsave(outputPicture, picture)

if __name__=='__main__':

    CREATE_PICTURE_1X2(rf"files\1x2\1\picture.png", rf"files\1x2\1\picture1.png", rf"files\1x2\1\picture2.png", rf"files\1x2\1\picture3.png")
    MERGE_PICTURE_1X2(rf"files\1x2\1\picture1.png", rf"files\1x2\1\picture2.png", rf"files\1x2\1\pictureOut.png")

    CREATE_PICTURE_1X2(rf"files\1x2\2\picture.png", rf"files\1x2\2\picture1.png", rf"files\1x2\2\picture2.png", rf"files\1x2\2\picture3.png")
    MERGE_PICTURE_1X2(rf"files\1x2\2\picture1.png", rf"files\1x2\2\picture2.png", rf"files\1x2\2\pictureOut.png")

    CREATE_PICTURE_1X2(rf"files\1x2\3\picture.png", rf"files\1x2\3\picture1.png", rf"files\1x2\3\picture2.png", rf"files\1x2\3\picture3.png")
    MERGE_PICTURE_1X2(rf"files\1x2\3\picture1.png", rf"files\1x2\3\picture2.png", rf"files\1x2\3\pictureOut.png")

    CREATE_PICTURE_2X2(rf"files\2x2\1\picture.png", rf"files\2x2\1\picture1.png", rf"files\2x2\1\picture2.png", rf"files\2x2\1\picture3.png")
    MERGE_PICTURE_2X2(rf"files\2x2\1\picture1.png", rf"files\2x2\1\picture2.png", rf"files\2x2\1\pictureOut.png")

    CREATE_PICTURE_2X2(rf"files\2x2\2\picture.png", rf"files\2x2\2\picture1.png", rf"files\2x2\2\picture2.png", rf"files\2x2\2\picture3.png")
    MERGE_PICTURE_2X2(rf"files\2x2\2\picture1.png", rf"files\2x2\2\picture2.png", rf"files\2x2\2\pictureOut.png")