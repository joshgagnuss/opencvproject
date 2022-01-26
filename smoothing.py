import cv2 as cv

img = cv.imread('photos/jomtien1.jpg')
cv.imshow('Jomtien', img)

# Smoothing and Blurring in open CV

#Averaging
average = cv.blur(img, (3,3)) # higher kerna higher blur
# cv.imshow('Averaging', average)

# Gaussian Blurring
gaussian = cv.GaussianBlur(img, (7,7), 0) 
# cv.imshow('Gaussian Blurring', gaussian)

# Median Blurring
median = cv.medianBlur(img, 7)
# cv.imshow('Median Blurring', median)

#bilateral Blurring
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Blurring', bilateral)










cv.waitKey(0)
