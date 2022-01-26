# split and merge color channels
import cv2 as cv
from cv2 import waitKey
import numpy as np

img = cv.imread('photos/jomtien1.jpg')
cv.imshow('Jomtien', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
# cv.imshow('Merged', merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

waitKey(0)
