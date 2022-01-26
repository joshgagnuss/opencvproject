#switching between color spaces 
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/jomtien1.jpg')
cv.imshow('Jomtien', img)

# plt.imshow(img)
# plt.show() 


# BGR to Greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# BGR to RGB 
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)

plt.imshow(rgb)
# plt.show()

#BGR to LAB
# lab = cv.cvtColor(img, cv.COlOR_BGR2LAB) # not working 
# cv.imshow('LAB', lab)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV_BGR', hsv_bgr)


cv.waitKey(0)