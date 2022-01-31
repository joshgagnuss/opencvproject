import cv2 as cv

img = cv.imread('photos/jomtien1.jpg')
# cv.imshow('Jomtien', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Jomtien', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Threshold Inverse', thresh_inv)

#Adaptive Threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13, 3)
cv.imshow('Adaptive Threshold', adaptive_thresh)


cv.waitKey(0)