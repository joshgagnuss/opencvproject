import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# cv.imshow('Blank', blank)
img = cv.imread('photos/cat1.jpg')
# cv.imshow('Cat', img)

#1 paint the image a certain colour 
blank[:] = 0,0,0
#cv.imshow('Green', blank)

#2 draw a rectangle in the image 
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
# cv.imshow('Rectangle', blank)

# 3 draw a circle in the image
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255,0,0), thickness=2)
# cv.imshow('Circle', blank)

# 4 draw a line in the image
cv.line(blank, (100,250), (blank.shape[1], blank.shape[0]), (0,0,255), thickness=2)
# cv.imshow('Line', blank)

# 5 put text on the image 
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)