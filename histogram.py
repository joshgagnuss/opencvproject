import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/jomtien1.jpg')
# cv.imshow('Jomtien', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Jomtien', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('circle', circle)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

# greyscale histogram
grey_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title('Histogram Greyscale')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(grey_hist)
plt.xlim([0, 256])
plt.show()

# Colour Histogram
plt.figure() 
plt.title('Histogram Color')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)