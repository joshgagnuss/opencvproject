import cv2 as cv
import numpy as np

img = cv.imread('photos/jomtien1.jpg')

cv.imshow('Jomtien', img)

# Translation 
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, -100)
# cv.imshow('Translated', translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    domensions = (width, height)

    return cv.warpAffine(img, rotMat, domensions)

rotated = rotate(img, 45)
# cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, 45)
# cv.imshow('Rotated_Rotated', rotated_rotated)

#Resizing 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
# cv.imshow('Resized', resized)

# FLipping
flipped = cv.flip(img, 1)
# cv.imshow('Flipped', flipped)

# Cropping 
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
