import numpy as np
import cv2 as cv
import imutils
import argparse

def callback(x):
    circles = cv.HoughCircles(gimg,cv.HOUGH_GRADIENT,1,dp,param2=param2, maxRadius=200)
    print(circles)
    try:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv.circle(imgn,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv.circle(imgn,(i[0],i[1]),2,(0,0,255),3)
    except:
        print("nenhum circulo encontrado")
        pass
    cv.imshow('image',imgn)
    cv.waitKey(30)

parser = argparse.ArgumentParser(description = 'Detector de círculos')

parser.add_argument('-path', action='store', dest = 'path', default='', 
                    help='path to the source image')

arguments = parser.parse_args()



cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('param2','image',200,255,callback)
cv.createTrackbar('dp','image',300,500,callback)


WIDTH = 1000
img = cv.imread(arguments.path)
imgo = imutils.resize(img, width=WIDTH)
gimg = cv.cvtColor(imgo, cv.COLOR_BGRA2GRAY)
gimg = cv.Canny(gimg,100,200)
while (True):
    imgn = imgo.copy()
    param2 = cv.getTrackbarPos('param2','image')
    dp = cv.getTrackbarPos('dp','image')
    cv.waitKey(300)

cv2.destroyAllWindows()