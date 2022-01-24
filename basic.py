import cv2 as cv

img = cv.imread('photos/cat1.jpg')
# cv.imshow('Cat', img)

# converting an image to greyscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blurred image
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blurred', blur)

#edge cascade
canny = cv.Canny(img, 125, 150)
# cv.imshow('Canny', canny)

#Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('Dilated', dilated)

# Eroded 
eorded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('Eroded', eorded)

# Resize the image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
# cv.imshow('Resized', resized)

# Cropping the image
cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)

cv.waitKey(0)