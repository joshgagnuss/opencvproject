import cv2 as cv 

img = cv.imread('photos/5people.jpg')
cv.imshow('Window', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Kevin Hart - Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
# minimum neighbours can tune it to remove false positives



print(f'Number of faces found = {len(faces)}')

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow('Detected faces', img)

cv.waitKey(0)