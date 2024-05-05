import cv2 as cv
import numpy as np

img = cv.imread('../resources/iloveimg-resized/beautiful-sunset.jpg')

# Showing Images
cv.imshow('Original Image', img)


# Default called trackbar function
def traceTrackbars(x):
    print(x)

# Create trackbars
cv.namedWindow('Color Detector')


# Closing windows
cv.waitKey(0)
cv.destroyAllWindows()
