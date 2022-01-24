import cv2 as cv

# img = cv.imread('photos/cat1.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)

def rescaleFrame(frame, scale=.75):
    #works for images, video & live video 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # only works for live video
    capture.set(3,width)
    capture.set(4,height)

#Reading Videos 

capture = cv.VideoCapture('videos/test.mkv')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    # cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()