import numpy as np
import cv2 as cv
import imutils
import argparse

def callback(x):
    
    circles = cv.HoughCircles(gimg,cv.HOUGH_GRADIENT,dp = dp/10,minDist=100,param1=param1,param2=param2)
    canny = cv.Canny(gimg,50,200)
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
    grey_3_channel = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
    numpy_horizontal_concat = np.concatenate((imgn, grey_3_channel), axis=1) 
    cv.imshow('image',numpy_horizontal_concat)
    
    cv.waitKey(30)


parser = argparse.ArgumentParser(description = 'Detector de círculos')

parser.add_argument('-i', "--image", required = True, action='store', dest = 'path', default='', 
                        help='path to the source image')
arguments = parser.parse_args()

img = cv.imread(arguments.path)
gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
kernel = np.ones((5,5),np.uint8)

#Threshold is util to find black wheels
#gray = cv.threshold(gray,50,255,cv.THRESH_BINARY_INV)[1]
gimg = cv.morphologyEx(gray, cv.MORPH_OPEN, kernel)
cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('param1','image',90,100,callback)
cv.createTrackbar('param2','image',100,255,callback)
cv.createTrackbar('dp','image',5,25,callback)

while (True):
    imgn = img.copy()
    param1 = cv.getTrackbarPos('param1','image')
    param2 = cv.getTrackbarPos('param2','image')
    dp = cv.getTrackbarPos('dp','image')
    cv.waitKey(300)

cv2.destroyAllWindows()

